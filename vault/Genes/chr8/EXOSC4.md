---
symbol: "EXOSC4"
type: "gene"
col: 10969
ensembl_id: "ENSG00000178896"
name: "exosome component 4"
location: "8q24.3"
module: 7
arm: "+"
pooled_cpm: 4.44
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EXOSC4

*exosome component 4* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.27× (z +5.3, q 5e-05, up in 27 of 45 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.11× (z +4.8, q 3e-04, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.517× (z -3.8, q 0.071, down in 13 of 46 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM: 0.570× (z -3.7, q 0.071, down in 20 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sulfisoxazole (drug)]] 5 µM in 1 line (SHP-77 0.202×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.187×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MRPL36]] (+0.80, fdr 7e-06), [[EMC6]] (+0.79, fdr 7e-06), [[MRPS12]] (+0.77, fdr 1e-05); moves opposite to [[DPY19L4]] (-0.62, fdr 6e-05), [[HACD2]] (-0.61, fdr 5e-05), [[HP1BP3]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **2.27×** | +5.3 | 5e-05 | 27/45 (LOX-IMVI, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.42×** | +5.2 | 5e-05 | 21/25 (NCI-H2030, SHP-77, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.11×** | +4.8 | 3e-04 | 25/44 (AsPC-1, SW480, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **2.06×** | +4.6 | 5e-04 | 12/26 (AsPC-1, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.66×** | +4.6 | 5e-04 | 20/38 (A549, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.94×** | +4.2 | 0.002 | 20/46 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change | **1.85×** | +4.0 | 0.006 | 20/36 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.78×** | +3.7 | 0.015 | 16/45 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.6 | 0.024 | 16/45 (HT-29, HOP62, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.81×** | +3.5 | 0.027 | 2/6 (SW1417, A498) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.66×** | +3.2 | 0.059 | 14/45 (LOX-IMVI, NCI-H1792, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.69×** | +3.1 | 0.092 | 14/43 (NCI-H1792, HEC-1-A, …) | rises with dose | composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10969.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Sulfisoxazole (drug)]] 5 µM in 1 line (SHP-77 0.202×); [[Homoharringtonine (drug)]] 5 µM in 1 line (RKO 0.187×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.517×** | -3.8 | 0.071 | 13/46 (MIA PaCa-2, A-427, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | **0.570×** | -3.7 | 0.071 | 20/45 (LoVo, NCI-H2030, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.72 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 5 µM 0.202× (z -9.6) |
| [[A-172 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.19 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 8 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL36]] | +0.80 | +0.62 / +0.85 | both halves | 7e-06 | STRING 403 |
| [[EMC6]] | +0.79 | +0.58 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[MRPS12]] | +0.77 | +0.53 / +0.79 | both halves | 1e-05 | STRING 567 |
| [[NCBP2AS2]] | +0.75 | +0.53 / +0.78 | both halves | 1e-05 |  |
| [[ZNF593]] | +0.74 | +0.54 / +0.78 | both halves | 1e-05 | STRING 558 |
| [[C16orf91]] | +0.74 | +0.52 / +0.75 | both halves | 1e-05 |  |
| [[OXLD1]] | +0.73 | +0.44 / +0.82 | both halves | 3e-05 |  |
| [[TRMT10C]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 | pathway: rRNA processing |
| [[YRDC]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[BLOC1S4]] | +0.69 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[POP7]] | +0.69 | +0.38 / +0.75 | both halves | 7e-05 |  |
| [[THAP7]] | +0.67 | +0.51 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPY19L4]] | -0.62 | -0.39 / -0.65 | both halves | 6e-05 |  |
| [[HACD2]] | -0.61 | -0.39 / -0.63 | both halves | 5e-05 |  |
| [[HP1BP3]] | -0.60 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[PRCP]] | -0.58 | -0.56 / -0.51 | both halves | 1e-05 | STRING 427 |
| [[DHFR]] | -0.57 | -0.18 / -0.68 | ⚠ one half (not replicated) | 9e-04 |  |
| [[TMEM237]] | -0.56 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[SEPTIN2]] | -0.55 | -0.52 / -0.64 | both halves | 1e-05 |  |
| [[PCBP2]] | -0.55 | -0.31 / -0.58 | both halves | 2e-04 |  |
| [[LAMP2]] | -0.55 | -0.37 / -0.67 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.490). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-44.0, -11.1); signed map (-12.0, -7.9). **Vector** length 50.9, 8.40% of its response variance represented; |z| ≥ 3 in 596 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +5.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.6 | +2.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.0 | +1.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.7 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | exosome component 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,078,648-144,080,648 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRrp41p, FLJ20591, Rrp41p, RRP41, RRP41A, Ski6p, SKI6, p12A |
| Gene groups (HGNC) | Exosome complex; MicroRNA protein coding host genes |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE |
| Reactome | 20 pathways, smallest: mRNA decay by 3' to 5' exoribonuclease; Butyrate Response Factor 1 (BRF1) binds and destabilizes mRNA; KSRP (KHSRP) binds and destabilizes mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NPD3](https://www.uniprot.org/uniprotkb/Q9NPD3) (Exosome complex component RRP41):

> Non-catalytic component of the RNA exosome complex which has 3'->5' exoribonuclease activity and participates in a multitude of cellular RNA processing and degradation events. In the nucleus, the RNA exosome complex is involved in proper maturation of stable RNA species such as rRNA, snRNA and snoRNA, in the elimination of RNA processing by-products and non-coding 'pervasive' transcripts, such as antisense RNA species and promoter-upstream transcripts (PROMPTs), and of mRNAs with processing …

**Summary**, from NCBI Gene [54512](https://www.ncbi.nlm.nih.gov/gene/54512):

> Enables mRNA 3'-UTR AU-rich region binding activity. Involved in several processes, including DNA deamination; maturation of 5.8S rRNA; and nuclear-transcribed mRNA catabolic process. Acts upstream of or within defense response to virus. Located in cytosol; euchromatin; and nuclear lumen. Part of exosome (RNase complex). [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18189) · Entrez [54512](https://www.ncbi.nlm.nih.gov/gene/54512) · UniProt [Q9NPD3](https://www.uniprot.org/uniprotkb/Q9NPD3) · Ensembl [ENSG00000178896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178896)

## Data

Gene col 10969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10969); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10969]; `tensor/DDL_lfc|DDL_z.npy` [10969]; `embed/gene_vectors.npy` [10969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10969 or target_col == 10969). Every well: [[EXOSC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOSC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
