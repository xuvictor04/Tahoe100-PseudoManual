---
symbol: "C11orf1"
type: "gene"
col: 6055
ensembl_id: "ENSG00000137720"
name: "cilia and flagella associated protein 68"
location: "11q23.1"
module: 24
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 2
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# C11orf1

*cilia and flagella associated protein 68* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.50× (z +8.9, q 2e-16, up in 22 of 23 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.63× (z +4.9, q 1e-04, up in 19 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 9.37×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.567× (z -4.0, q 0.032, down in 22 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A-427 0.0415×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0628×); [[Methotrexate (drug)]] 0.05 µM in 1 line (A549 0.0743×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf56]] (+0.72, fdr 7e-06), [[PIGP]] (+0.72, fdr 7e-06), [[CLN8-AS1]] (+0.71, fdr 1e-05); moves opposite to [[PRPS2]] (-0.55, fdr 2e-05), [[RRM2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6055.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 9.37×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.50×** | +8.9 | 2e-16 | 22/23 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +8.1 | 1e-13 | 11/11 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +7.5 | 9e-12 | 7/7 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.63×** | +4.9 | 1e-04 | 19/45 (CFPAC-1, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~25% of this change | **1.68×** | +3.7 | 0.022 | 11/25 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.022 | 16/45 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 2.12× | +3.1 | 0.18 | 4/19 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6055.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (A-427 0.0415×); [[HI-TOPK-032 (drug)]] 0.05 µM in 1 line (NCI-H1792 0.0628×); [[Methotrexate (drug)]] 0.05 µM in 1 line (A549 0.0743×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.567×** | -4.0 | 0.032 | 22/46 (SNU-1, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.629× | -3.0 | 0.66 | 3/46 (HEC-1-A, BT-474, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 3.52 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0415× (z -9.5) |
| [[A549 (line)]] | wt | 4.44 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0743× (z -8.5) |
| [[LoVo (line)]] | wt | 5.35 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.37× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 4.19 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0628× (z -8.7) |
| [[A-172 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.98 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf56]] | +0.72 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[PIGP]] | +0.72 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.71 | +0.53 / +0.77 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.68 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[RFXANK]] | +0.65 | +0.40 / +0.71 | both halves | 5e-05 |  |
| [[YBEY]] | +0.63 | +0.37 / +0.73 | both halves | 9e-05 |  |
| [[CHCHD5]] | +0.63 | +0.34 / +0.70 | both halves | 1e-04 |  |
| [[PTRHD1]] ⚠ | +0.63 | +0.33 / +0.70 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[HSBP1L1]] | +0.63 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[AKAP1-DT]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[FMC1]] | +0.62 | +0.48 / +0.71 | both halves | 2e-05 |  |
| [[GPBP1]] | +0.62 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[DNAJC30]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRPS2]] | -0.55 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[RRM2]] | -0.54 | -0.59 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.2, -16.4); signed map (-9.3, 0.9). **Vector** length 43.9, 5.72% of its response variance represented; |z| ≥ 3 in 679 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.7 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | +0.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +8.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -1.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.6 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.1 | -3.0 |
|  | [[Tirabrutinib (drug)]] 0.05 µM |  | -1.1 | -2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | cilia and flagella associated protein 68 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:111,878,935-111,885,975 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23499; previously C11orf1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5F2](https://www.uniprot.org/uniprotkb/Q9H5F2) (Cilia- and flagella-associated protein 68):

> Microtubule inner protein (MIP) part of the dynein-decorated doublet microtubules (DMTs) in cilia axoneme, which is required for motile cilia beating.

**Summary**, from NCBI Gene [64776](https://www.ncbi.nlm.nih.gov/gene/64776):

> Predicted to be involved in flagellated sperm motility. Located in axoneme and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1163) · Entrez [64776](https://www.ncbi.nlm.nih.gov/gene/64776) · UniProt [Q9H5F2](https://www.uniprot.org/uniprotkb/Q9H5F2) · Ensembl [ENSG00000137720](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137720)

## Data

Gene col 6055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6055); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6055]; `tensor/DDL_lfc|DDL_z.npy` [6055]; `embed/gene_vectors.npy` [6055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6055 or target_col == 6055). Every well: [[C11orf1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C11orf1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
