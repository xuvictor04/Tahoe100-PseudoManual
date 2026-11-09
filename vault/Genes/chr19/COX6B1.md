---
symbol: "COX6B1"
type: "gene"
col: 4729
ensembl_id: "ENSG00000126267"
name: "cytochrome c oxidase subunit 6B1"
location: "19q13.12"
module: 48
arm: "+"
pooled_cpm: 54.73
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# COX6B1

*cytochrome c oxidase subunit 6B1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.78× (z +7.3, q 1e-10, up in 47 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.62× (z +3.8, q 0.019, up in 40 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 5.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.235×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 25 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA1]] (+0.87, fdr 7e-06), [[ATP5MK]] (+0.87, fdr 7e-06), [[UQCRB]] (+0.87, fdr 7e-06, ⚠ UQCRB in the vector space only through flagged drug-doses), [[ROMO1]] (+0.86, fdr 7e-06); moves opposite to [[LIN7C]] (-0.71, fdr 1e-05), [[ZNF460]] (-0.71, fdr 1e-05), [[TEX261]] (-0.69, fdr 3e-05).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A-427 5.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.78×** | +7.3 | 1e-10 | 47/47 (A-427, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.94×** | +5.7 | 3e-06 | 33/39 (A549, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.14×** | +3.9 | 0.019 | 37/44 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.019 | 40/48 (A549, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.7 | 0.027 | 40/46 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.83×** | +3.4 | 0.073 | 36/47 (PANC-1, SW480, …) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.81×** | +3.3 | 0.078 | 38/46 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4729.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.235×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | 0.665× | -3.2 | 0.31 | 27/48 (C-33 A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.542× | -3.1 | 0.31 | 44/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.549× | -3.0 | 0.31 | 43/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4729. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 67.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.10× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | — |
| [[C-33 A (line)]] | alt | 48.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -8.9) |
| [[A-172 (line)]] | wt | 53.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 67.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 50.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 86.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 57.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4729), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 25 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA1]] | +0.87 | +0.82 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 979 |
| [[ATP5MK]] | +0.87 | +0.76 / +0.89 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport |
| [[UQCRB]] ⚠ | +0.87 | +0.83 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ROMO1]] | +0.86 | +0.78 / +0.88 | both halves | 7e-06 | STRING 682 |
| [[COX6C]] | +0.85 | +0.79 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[ATP5ME]] | +0.85 | +0.79 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 759 |
| [[COX7C]] | +0.84 | +0.76 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[COX4I1]] ⚠ | +0.84 | +0.78 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[ATP5PD]] | +0.84 | +0.62 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 879 |
| [[RPS19]] | +0.84 | +0.78 / +0.83 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.84 | +0.77 / +0.89 | both halves | 7e-06 | pathway: Aerobic respiration and respiratory electron transport; STRING 412 |
| [[UQCRQ]] ⚠ | +0.84 | +0.68 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999; ⚠ in the vector space only through flagged drug-doses |
| [[NDUFA4]] | +0.83 | +0.74 / +0.86 | both halves | 7e-06 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[TOMM7]] | +0.82 | +0.76 / +0.83 | both halves | 7e-06 | STRING 412 |
| [[UBL5]] | +0.82 | +0.71 / +0.87 | both halves | 7e-06 | STRING 477 |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.71 | -0.49 / -0.75 | both halves | 1e-05 |  |
| [[ZNF460]] | -0.71 | -0.53 / -0.72 | both halves | 1e-05 |  |
| [[TEX261]] | -0.69 | -0.46 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.900). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-45.9, -22.4); signed map (-34.7, 9.1). **Vector** length 64.1, 28.7% of its response variance represented; |z| ≥ 3 in 439 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Formation of ATP by chemiosmotic coupling* (reactome, mean cos +0.79 to 7); *Complex I biogenesis* (reactome, mean cos +0.68 to 9); *Cristae formation* (reactome, mean cos +0.79 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | +2.3 | +3.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.1 | +3.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.7 | -0.5 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.5 | +3.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -5.4 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -5.1 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | +0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | +0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome c oxidase subunit 6B1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:35,648,323-35,658,782 (+) |
| Ensembl biotype | protein_coding |
| Also known as | COXG; previously COX6B |
| Gene groups (HGNC) | Mitochondrial complex IV: cytochrome c oxidase subunits |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 9 pathways, smallest: Complex IV assembly; Cytoprotection by HMOX1; TP53 Regulates Metabolic Genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P14854](https://www.uniprot.org/uniprotkb/P14854) (Cytochrome c oxidase subunit 6B1):

> Component of the cytochrome c oxidase, the last enzyme in the mitochondrial electron transport chain which drives oxidative phosphorylation. The respiratory chain contains 3 multisubunit complexes succinate dehydrogenase (complex II, CII), ubiquinol-cytochrome c oxidoreductase (cytochrome b-c1 complex, complex III, CIII) and cytochrome c oxidase (complex IV, CIV), that cooperate to transfer electrons derived from NADH and succinate to molecular oxygen, creating an electrochemical gradient over …

**Summary**, from NCBI Gene [1340](https://www.ncbi.nlm.nih.gov/gene/1340):

> Cytochrome c oxidase (COX), the terminal enzyme of the mitochondrial respiratory chain, catalyzes the electron transfer from reduced cytochrome c to oxygen. It is a heteromeric complex consisting of 3 catalytic subunits encoded by mitochondrial genes and multiple structural subunits encoded by nuclear genes. The mitochondrially-encoded subunits function in electron transfer, and the nuclear-encoded subunits may be involved in the regulation and assembly of the complex. This nuclear gene encodes …

**Accessions** — [HGNC:2280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2280) · Entrez [1340](https://www.ncbi.nlm.nih.gov/gene/1340) · UniProt [P14854](https://www.uniprot.org/uniprotkb/P14854) · Ensembl [ENSG00000126267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126267)

## Data

Gene col 4729: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4729); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4729, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4729]; `tensor/DDL_lfc|DDL_z.npy` [4729]; `embed/gene_vectors.npy` [4729]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4729 or target_col == 4729). Every well: [[COX6B1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX6B1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
