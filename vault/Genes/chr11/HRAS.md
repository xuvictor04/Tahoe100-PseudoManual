---
symbol: "HRAS"
type: "gene"
col: 10523
ensembl_id: "ENSG00000174775"
name: "HRas proto-oncogene, GTPase"
location: "11p15.5"
module: 24
arm: "+"
pooled_cpm: 8.48
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# HRAS

*HRas proto-oncogene, GTPase* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.80× (z +10.5, q 5e-23, up in 26 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.70× (z +4.2, q 0.005, up in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.79×, SW480 5.42×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 4.37×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0699×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSNA1]] (+0.64, fdr 3e-05), [[FBXW5]] (+0.63, fdr 2e-05), [[RFNG]] (+0.61, fdr 8e-05); moves opposite to [[ILF3]] (-0.51, fdr 1e-04), [[SRP9]] (-0.50, fdr 4e-05), [[HNRNPA2B1]] (-0.50, fdr 2e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10523.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (PANC-1 4.79×, SW480 5.42×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 4.37×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.80×** | +10.5 | 5e-23 | 26/28 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.21×** | +8.8 | 4e-16 | 16/16 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +4.6 | 9e-04 | 18/22 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +4.2 | 0.005 | 19/46 (LS 180, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.66×** | +3.8 | 0.015 | 17/35 (A549, PANC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~39% of this change | **1.62×** | +3.8 | 0.015 | 20/35 (A-172, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +3.3 | 0.079 | 14/35 (LoVo, A498, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.51×** | +3.2 | 0.085 | 16/46 (PANC-1, LS 180, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 1.72× | +3.0 | 0.15 | 7/43 (LS 180, Hs 766T, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cepharanthine (drug)]] 0.5 µM in 1 line (NCI-H1792 0.0699×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10523. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.79× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 4.56 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0699× (z -8.9) |
| [[SW480 (line)]] | alt | 8.04 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.42× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.73 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.24 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.78 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.39 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10523), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 10 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSNA1]] | +0.64 | +0.43 / +0.73 | both halves | 3e-05 |  |
| [[FBXW5]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[RFNG]] | +0.61 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[MEX3D]] | +0.61 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[CDC34]] | +0.60 | +0.51 / +0.59 | both halves | 1e-05 | pathway: C-type lectin receptors (CLRs) |
| [[ARL8A]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[HECTD4]] | +0.59 | +0.43 / +0.57 | both halves | 4e-05 |  |
| [[C1orf35]] | +0.58 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PSMD9]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ENKD1]] | +0.57 | +0.39 / +0.56 | both halves | 5e-05 |  |
| [[CNIH4]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SAC3D1]] | +0.57 | +0.43 / +0.56 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ILF3]] | -0.51 | -0.36 / -0.51 | both halves | 1e-04 |  |
| [[SRP9]] | -0.50 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[HNRNPA2B1]] | -0.50 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ZNF300]] | -0.48 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[SRSF1]] | -0.48 | -0.26 / -0.52 | both halves | 3e-04 |  |
| [[XRCC5]] | -0.48 | -0.33 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.575). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.0, -15.5); signed map (-24.0, 5.2). **Vector** length 52.9, 8.69% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +10.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.8 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +0.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.6 | +4.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.3 | +0.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.2 | +0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | HRas proto-oncogene, GTPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:532,242-537,321 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HRAS1 |
| Gene groups (HGNC) | RAS type GTPase family |
| Hallmark sets | PEROXISOME, PI3K_AKT_MTOR_SIGNALING, APICAL_JUNCTION, P53_PATHWAY |
| Reactome | 138 pathways, smallest: RAS GTPase cycle mutants; Signaling by RAS GAP mutants; Signaling by RAS GTPase mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P01112](https://www.uniprot.org/uniprotkb/P01112) (GTPase HRas):

> Signal transducer in the Ras-MAPK signaling pathway that regulates cell proliferation and survival. Ras proteins bind GDP/GTP and possess intrinsic GTPase activity. Recognized by LZTR1 that mediates its ubiquitination by a BCR (BTB-CUL3-RBX1) E3 ubiquitin-protein ligase complex.

**Summary**, from NCBI Gene [3265](https://www.ncbi.nlm.nih.gov/gene/3265):

> This gene belongs to the Ras oncogene family, whose members are related to the transforming genes of mammalian sarcoma retroviruses. The products encoded by these genes function in signal transduction pathways. These proteins can bind GTP and GDP, and they have intrinsic GTPase activity. This protein undergoes a continuous cycle of de- and re-palmitoylation, which regulates its rapid exchange between the plasma membrane and the Golgi apparatus. Mutations in this gene cause Costello syndrome, a …

**Accessions** — [HGNC:5173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5173) · Entrez [3265](https://www.ncbi.nlm.nih.gov/gene/3265) · UniProt [P01112](https://www.uniprot.org/uniprotkb/P01112) · Ensembl [ENSG00000174775](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174775)

## Data

Gene col 10523: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10523); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10523, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10523]; `tensor/DDL_lfc|DDL_z.npy` [10523]; `embed/gene_vectors.npy` [10523]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10523 or target_col == 10523). Every well: [[HRAS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HRAS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
