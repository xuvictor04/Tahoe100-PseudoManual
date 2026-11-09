---
symbol: "RBMX2"
type: "gene"
col: 5582
ensembl_id: "ENSG00000134597"
name: "RNA binding motif protein X-linked 2"
location: "Xq26.1"
module: 12
arm: "+"
pooled_cpm: 32.59
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# RBMX2

*RNA binding motif protein X-linked 2* — Xq26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 1.64× (z +4.3, q 0.009, up in 36 of 48 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.54× (z +3.9, q 0.023, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.640× (z -4.0, q 0.029, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.145×; ⚠ transcription drop; cell-cycle shift, explains ~40% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C18orf21]] (+0.82, fdr 7e-06), [[NKAP]] (+0.81, fdr 7e-06), [[SMIM26]] (+0.79, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[RP9]] (+0.78, fdr 7e-06); moves opposite to [[EIF5A]] (-0.71, fdr 7e-06), [[PPIA]] (-0.70, fdr 1e-05), [[MOB1A]] (-0.68, fdr 9e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF570]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.64×** | +4.3 | 0.009 | 36/48 (SW480, A-427, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.023 | 36/48 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.49×** | +3.6 | 0.061 | 26/46 (RPMI-7951, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.4 | 0.098 | 24/45 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **1.44×** | +3.3 | 0.098 | 24/44 (A-172, A549, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.44×** | +3.3 | 0.098 | 26/47 (NCI-H1573, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5582.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (H4 0.145×; ⚠ transcription drop; cell-cycle shift, explains ~40% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -4.0 | 0.029 | 32/48 (J82, SW 1088, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 0.746× | -3.5 | 0.11 | 28/48 (SK-MEL-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.684× | -3.4 | 0.11 | 25/48 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 26.1 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.145× (z -8.7) ⚠ transcription drop; cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 35.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 37.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 60.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C18orf21]] | +0.82 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[NKAP]] | +0.81 | +0.83 / +0.80 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 768 |
| [[SMIM26]] ⚠ | +0.79 | +0.73 / +0.82 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RP9]] | +0.78 | +0.73 / +0.75 | both halves | 7e-06 | STRING 426 |
| [[FRA10AC1]] | +0.77 | +0.76 / +0.75 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.76 | +0.83 / +0.79 | both halves | 7e-06 |  |
| [[NOL7]] ⚠ | +0.76 | +0.64 / +0.78 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[MPHOSPH10]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[MTIF3]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[NEMF]] | +0.74 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[LEO1]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[SNHG11]] | +0.73 | +0.63 / +0.79 | both halves | 7e-06 |  |
| [[PUS3]] | +0.73 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF5A]] | -0.71 | -0.68 / -0.63 | both halves | 7e-06 |  |
| [[PPIA]] | -0.70 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[MOB1A]] | -0.68 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[FKBP1A]] | -0.68 | -0.68 / -0.71 | both halves | 7e-06 |  |
| [[PRPS2]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[SUMO3]] | -0.65 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[TXNDC5]] | -0.65 | -0.58 / -0.74 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.65 | -0.61 / -0.68 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 426 |
| [[RBBP7]] | -0.65 | -0.66 / -0.63 | both halves | 7e-06 |  |
| [[DHFR]] | -0.65 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[VMA21]] | -0.64 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[CTSZ]] | -0.64 | -0.54 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF570]] | B | ZNF570 activity lowers RBMX2's level | lines that do not express ZNF570 (15) vs lines expressing it (35) | 1.01× higher at baseline in the lines without ZNF570 | 0.097 | ⚠ within organs, on part of the lines; also absent: ZNF569, PEG10, DNAAF9 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.876). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-38.0, -9.8); signed map (-16.0, -8.3). **Vector** length 84.3, 24.7% of its response variance represented; |z| ≥ 3 in 442 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.9 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.5 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | -0.2 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.3 | +1.6 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.8 | -0.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.2 | -3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -5.5 | +3.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.4 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | +0.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.6 | -2.1 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | RNA binding motif protein X-linked 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq26.1 — chrX:130,401,987-130,413,656 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-79, Snu17 |
| Gene groups (HGNC) | RNA binding motif containing |
| Reactome | 4 pathways, smallest: mRNA Splicing - Major Pathway; mRNA Splicing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y388](https://www.uniprot.org/uniprotkb/Q9Y388) (RNA-binding motif protein, X-linked 2):

> Involved in pre-mRNA splicing as component of the activated spliceosome. As a component of the minor spliceosome, involved in the splicing of U12-type introns in pre-mRNAs (Probable).

**Summary**, from NCBI Gene [51634](https://www.ncbi.nlm.nih.gov/gene/51634):

> Enables RNA binding activity. Involved in mRNA splicing, via spliceosome. Located in nuclear membrane and nucleolus. Part of U2-type precatalytic spliceosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24282](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24282) · Entrez [51634](https://www.ncbi.nlm.nih.gov/gene/51634) · UniProt [Q9Y388](https://www.uniprot.org/uniprotkb/Q9Y388) · Ensembl [ENSG00000134597](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134597)

## Data

Gene col 5582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5582); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5582]; `tensor/DDL_lfc|DDL_z.npy` [5582]; `embed/gene_vectors.npy` [5582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5582 or target_col == 5582). Every well: [[RBMX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RBMX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
