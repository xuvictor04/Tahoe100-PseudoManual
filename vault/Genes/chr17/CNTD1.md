---
symbol: "CNTD1"
type: "gene"
col: 10730
ensembl_id: "ENSG00000176563"
name: "cyclin N-terminal domain containing 1"
location: "17q21.2-q21.31"
module: 21
arm: "+"
pooled_cpm: 2.97
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CNTD1

*cyclin N-terminal domain containing 1* — 17q21.2-q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.53× (z +9.7, q 1e-19, up in 33 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.05 µM in 1 line (NCI-H460 0.0854×); [[Adenosine (drug)]] 0.05 µM in 1 line (J82 0.0472×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAF1-AS1]] (+0.73, fdr 7e-06), [[ASB14]] (+0.69, fdr 7e-06), [[SPATC1]] (+0.69, fdr 7e-06); moves opposite to [[ACTR5]] (-0.55, fdr 6e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.53×** | +9.7 | 1e-19 | 33/34 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.69×** | +9.7 | 1e-19 | 12/14 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.82×** | +7.4 | 3e-11 | 3/4 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.94×** | +6.9 | 7e-10 | 19/37 (HS-578T, C32, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +5.4 | 1e-05 | 17/47 (A498, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +5.1 | 3e-05 | 1/5 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.92×** | +4.8 | 1e-04 | 18/43 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.74×** | +4.1 | 0.003 | 4/18 (BT-474, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.6 | 0.022 | 7/19 (LOX-IMVI, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.4 | 0.031 | 11/45 (A-172, SW1417, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.59×** | +3.4 | 0.031 | 8/44 (HOP62, LS 180, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.05 µM in 1 line (NCI-H460 0.0854×); [[Adenosine (drug)]] 0.05 µM in 1 line (J82 0.0472×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 2.48 | 0 | 1 | — | [[Adenosine (drug)]] 0.05 µM 0.0472× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 2.26 | 0 | 1 | — | [[Thymol (drug)]] 0.05 µM 0.0854× (z -8.8) |
| [[A-172 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAF1-AS1]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[ASB14]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.69 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[LINC02307]] | +0.68 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PLA2G12B]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DENND6A-AS1]] | +0.67 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[DDX19A-DT]] | +0.66 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[FAM184B]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[LINC01618]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[IL12RB2]] | +0.65 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[LINC02951]] | +0.64 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTR5]] | -0.55 | -0.56 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.9, 25.1); signed map (30.8, 5.7). **Vector** length 43.2, 4.91% of its response variance represented; |z| ≥ 3 in 873 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +4.6 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +9.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +1.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +1.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.2 | -0.8 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin N-terminal domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2-q21.31 — chr17:42,798,800-42,811,587 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ40137; previously CNTD |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N815](https://www.uniprot.org/uniprotkb/Q8N815) (Cyclin N-terminal domain-containing protein 1):

> Plays a role in the different steps of crossover formation during meiotic recombination. Participates in the crossover differentiation step of crossover-specific recombination intermediates through its interaction with PRR19. In addition, stimulates crossover formation through the interactions with RFC3 and RFC4 and simultaneously regulates cell-cycle progression through interactions with CDC34 and subsequent ubiquitination of WEE1. May also participates in an active deselection process that …

**Summary**, from NCBI Gene [124817](https://www.ncbi.nlm.nih.gov/gene/124817):

> Predicted to be involved in reciprocal meiotic recombination and regulation of meiotic cell cycle. Predicted to act upstream of or within spermatogenesis. Predicted to be located in chromosome. Predicted to be active in site of double-strand break. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26847](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26847) · Entrez [124817](https://www.ncbi.nlm.nih.gov/gene/124817) · UniProt [Q8N815](https://www.uniprot.org/uniprotkb/Q8N815) · Ensembl [ENSG00000176563](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176563)

## Data

Gene col 10730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10730); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10730]; `tensor/DDL_lfc|DDL_z.npy` [10730]; `embed/gene_vectors.npy` [10730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10730 or target_col == 10730). Every well: [[CNTD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNTD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
