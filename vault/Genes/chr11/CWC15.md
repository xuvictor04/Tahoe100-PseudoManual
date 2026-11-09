---
symbol: "CWC15"
type: "gene"
col: 7428
ensembl_id: "ENSG00000150316"
name: "CWC15 spliceosome associated protein"
location: "11q21"
module: 220
arm: "+"
pooled_cpm: 53.93
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/220"]
generated_by: "tahoemap"
---

# CWC15

*CWC15 spliceosome associated protein* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.78× (z +6.2, q 4e-07, up in 42 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[DT-061 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0703×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR83OS]] (+0.77, fdr 7e-06, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[SECISBP2L]] (+0.77, fdr 7e-06), [[CIR1]] (+0.75, fdr 7e-06), [[METTL14]] (+0.72, fdr 7e-06); moves opposite to [[NUP188]] (-0.73, fdr 7e-06), [[ELK4]] (-0.68, fdr 7e-06), [[PSME3]] (-0.65, fdr 7e-06).
> It is in [[Module 220]], a single-armed module (Respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7428.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.78×** | +6.2 | 4e-07 | 42/49 (LoVo, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +5.0 | 2e-04 | 40/47 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.60×** | +4.2 | 0.004 | 30/49 (PANC-1, A549, …) | two highest doses | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +3.9 | 0.013 | 28/48 (LS 180, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | 1.43× | +3.2 | 0.14 | 27/48 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | 1.41× | +3.0 | 0.23 | 21/40 (A-427, PANC-1, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7428.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[DT-061 (drug)]] 0.05 µM in 1 line (NCI-H661 0.0703×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.884× | -3.5 | 0.22 | 1/49 (COLO 205) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7428. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 51.7 | 0 | 1 | — | [[DT-061 (drug)]] 0.05 µM 0.0703× (z -8.6) |
| [[A-172 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 42.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 68.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 56.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 44.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 46.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 43.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 43.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 50.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 68.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7428), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR83OS]] ⚠ | +0.77 | +0.66 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SECISBP2L]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[CIR1]] | +0.75 | +0.74 / +0.74 | both halves | 7e-06 | STRING 861 |
| [[METTL14]] | +0.72 | +0.72 / +0.64 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[MRPL22]] | +0.71 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MPHOSPH8]] | +0.71 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.71 | +0.61 / +0.74 | both halves | 7e-06 |  |
| [[EAPP]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[SYF2]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 998 |
| [[IGBP1]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.70 | +0.64 / +0.76 | both halves | 7e-06 |  |
| [[SCNM1]] | +0.70 | +0.68 / +0.73 | both halves | 7e-06 | STRING 818 |
| [[ASB7]] | +0.70 | +0.59 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.73 | -0.63 / -0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[ELK4]] | -0.68 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[PSME3]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.62 | -0.38 / -0.71 | both halves | 6e-05 |  |
| [[HNRNPAB]] | -0.61 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[THOC6]] | -0.61 | -0.48 / -0.66 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[VMA21]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 220]] — Respiratory electron transport; 11 genes; every member is in the + arm (projection on the module's main direction 0.725). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.9, -10.9); signed map (-14.9, -5.6). **Vector** length 85.3, 30.2% of its response variance represented; |z| ≥ 3 in 343 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.6 | +6.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.9 | +3.9 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +0.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.6 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | -0.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.3 | +0.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.7 | -0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.7 | -2.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | CWC15 spliceosome associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,962,620-94,973,586 (-) |
| Ensembl biotype | protein_coding |
| Also known as | C11orf5, HSPC148, Cwf15, AD002 |
| Gene groups (HGNC) | NineTeen complex; NTC associated proteins; Spliceosomal C complex |
| Reactome | 7 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Dengue Virus-Host Interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P013](https://www.uniprot.org/uniprotkb/Q9P013) (Spliceosome-associated protein CWC15 homolog):

> Involved in pre-mRNA splicing as component of the spliceosome. Component of the PRP19-CDC5L complex that forms an integral part of the spliceosome and is required for activating pre-mRNA splicing. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [51503](https://www.ncbi.nlm.nih.gov/gene/51503):

> Predicted to enable RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nuclear speck. Part of U2-type catalytic step 2 spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26939) · Entrez [51503](https://www.ncbi.nlm.nih.gov/gene/51503) · UniProt [Q9P013](https://www.uniprot.org/uniprotkb/Q9P013) · Ensembl [ENSG00000150316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150316)

## Data

Gene col 7428: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7428); `tables/drug_effects.parquet` (7 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7428, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7428]; `tensor/DDL_lfc|DDL_z.npy` [7428]; `embed/gene_vectors.npy` [7428]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7428 or target_col == 7428). Every well: [[CWC15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CWC15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
