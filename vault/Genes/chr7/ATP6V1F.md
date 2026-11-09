---
symbol: "ATP6V1F"
type: "gene"
col: 4888
ensembl_id: "ENSG00000128524"
name: "ATPase H+ transporting V1 subunit F"
location: "7q32.1"
module: 24
arm: "+"
pooled_cpm: 22.79
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ATP6V1F

*ATPase H+ transporting V1 subunit F* — 7q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +6.2, q 4e-07, up in 40 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +4.1, q 0.005, up in 29 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Asciminib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0362×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP6V0B]] (+0.72, fdr 1e-05), [[CIAO2B]] (+0.69, fdr 3e-05), [[TRAPPC5]] (+0.69, fdr 7e-06); moves opposite to [[SYNCRIP]] (-0.64, fdr 1e-05), [[HNRNPA3]] (-0.62, fdr 1e-05), [[SRSF1]] (-0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4888.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.71×** | +6.2 | 4e-07 | 40/44 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.28×** | +5.4 | 2e-05 | 30/33 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.9 | 2e-04 | 35/44 (COLO 205, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.93×** | +4.7 | 4e-04 | 38/48 (HOP62, PANC-1, …) | two highest doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.89×** | +4.2 | 0.003 | 34/39 (A-172, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.1 | 0.005 | 29/46 (A549, HT-29, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.72×** | +3.5 | 0.030 | 29/48 (NCI-H23, SK-MEL-2, …) | rises with dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.64×** | +3.5 | 0.030 | 25/44 (C32, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.57×** | +3.2 | 0.084 | 26/48 (SW 900, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.56×** | +3.2 | 0.086 | 26/48 (HOP62, PANC-1, …) | two highest doses | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.094 | 27/47 (LS 180, A498, …) | two highest doses | cell-cycle shift (explains ~22% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Asciminib (drug)]] 0.5 µM in 1 line (AN3 CA 0.0362×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.43 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4888. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 33.4 | 0 | 1 | — | [[Asciminib (drug)]] 0.5 µM 0.0362× (z -11.7) |
| [[A-172 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 39.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 20.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4888), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 18 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0B]] | +0.72 | +0.55 / +0.78 | both halves | 1e-05 | same gene group; pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION; STRING 999 |
| [[CIAO2B]] | +0.69 | +0.45 / +0.76 | both halves | 3e-05 |  |
| [[TRAPPC5]] | +0.69 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[RNASEK]] | +0.67 | +0.66 / +0.69 | both halves | 7e-06 | STRING 996 |
| [[RNF181]] | +0.66 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[FAU]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 | pathway: Cellular response to starvation |
| [[RANGRF]] | +0.66 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[MIEN1]] | +0.65 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[RPS15]] ⚠ | +0.65 | +0.56 / +0.65 | both halves | 1e-05 | pathway: Cellular response to starvation; ⚠ in the vector space only through flagged drug-doses |
| [[POLR2J]] ⚠ | +0.64 | +0.49 / +0.71 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LAGE3]] | +0.63 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[C19orf53]] | +0.62 | +0.37 / +0.72 | both halves | 8e-05 |  |
| [[TRAPPC2B]] | +0.61 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[DCXR]] | +0.61 | +0.51 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SYNCRIP]] | -0.64 | -0.49 / -0.66 | both halves | 1e-05 |  |
| [[HNRNPA3]] | -0.62 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[SRSF1]] | -0.62 | -0.40 / -0.68 | both halves | 5e-05 |  |
| [[LMNB2]] | -0.61 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[HNRNPM]] | -0.60 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[HNRNPA2B1]] | -0.59 | -0.35 / -0.61 | both halves | 1e-04 |  |
| [[HNRNPD]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[EWSR1]] | -0.57 | -0.36 / -0.62 | both halves | 1e-04 |  |
| [[RBBP7]] | -0.57 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[FOXM1]] | -0.56 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[TFDP1]] | -0.56 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[LAS1L]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.4, -24.0); signed map (-29.8, 9.3). **Vector** length 60.0, 15.9% of its response variance represented; |z| ≥ 3 in 491 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.9 | +1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.2 | +3.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.9 | +1.3 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | +1.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | +1.4 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.4 | +1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.3 | +0.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +2.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | -3.3 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -2.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -2.2 | +6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.9 | +1.0 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -1.7 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.3 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q32.1 — chr7:128,862,856-128,865,847 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ATP6S14, VATF, Vma7 |
| Gene groups (HGNC) | V-type ATPase subunits |
| Hallmark sets | UV_RESPONSE_UP, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 16 pathways, smallest: Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy; Insulin receptor recycling; ROS and RNS production in phagocytes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16864](https://www.uniprot.org/uniprotkb/Q16864) (V-type proton ATPase subunit F):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it promotes acidification of the extracellular environment (By similarity). The V-ATPase complex also acts as an activator for mTORC1 on …

**Summary**, from NCBI Gene [9296](https://www.ncbi.nlm.nih.gov/gene/9296):

> This gene encodes a component of vacuolar ATPase (V-ATPase), a multisubunit enzyme that mediates acidification of eukaryotic intracellular organelles. V-ATPase dependent organelle acidification is necessary for such intracellular processes as protein sorting, zymogen activation, receptor-mediated endocytosis, and synaptic vesicle proton gradient generation. V-ATPase is composed of a cytosolic V1 domain and a transmembrane V0 domain. The V1 domain consists of three A and three B subunits, two G …

**Accessions** — [HGNC:16832](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16832) · Entrez [9296](https://www.ncbi.nlm.nih.gov/gene/9296) · UniProt [Q16864](https://www.uniprot.org/uniprotkb/Q16864) · Ensembl [ENSG00000128524](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128524)

## Data

Gene col 4888: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4888); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4888, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4888]; `tensor/DDL_lfc|DDL_z.npy` [4888]; `embed/gene_vectors.npy` [4888]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4888 or target_col == 4888). Every well: [[ATP6V1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
