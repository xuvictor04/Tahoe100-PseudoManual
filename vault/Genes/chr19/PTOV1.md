---
symbol: "PTOV1"
type: "gene"
col: 2530
ensembl_id: "ENSG00000104960"
name: "PTOV1 extended AT-hook containing adaptor protein"
location: "19q13.33"
module: 3
arm: "+"
pooled_cpm: 30.79
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 4
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PTOV1

*PTOV1 extended AT-hook containing adaptor protein* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.14× (z +8.2, q 1e-13, up in 39 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.00× (z +4.2, q 0.003, up in 35 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.584× (z -8.3, q 9e-14, down in 42 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.343×, LoVo 0.409×, NCI-H460 0.426×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0635×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.179×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.141×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH7]] (+0.77, fdr 7e-06), [[DHPS]] (+0.74, fdr 7e-06), [[UNC45A]] (+0.69, fdr 7e-06); moves opposite to [[PDAP1]] (-0.63, fdr 2e-05), [[EIF4G1]] (-0.62, fdr 1e-05), [[TRMT5]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2530.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.14×** | +8.2 | 1e-13 | 39/43 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +6.6 | 1e-08 | 29/36 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.53×** | +4.6 | 1e-03 | 35/46 (CFPAC-1, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.00×** | +4.2 | 0.003 | 35/46 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.84×** | +3.7 | 0.022 | 30/48 (SW480, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.54×** | +3.4 | 0.057 | 22/40 (A549, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.72×** | +3.3 | 0.065 | 22/48 (NCI-H460, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +3.3 | 0.065 | 1/48 (NCI-H23) | inconsistent across doses | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.3 | 0.065 | 23/46 (SHP-77, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.32× | +3.0 | 0.14 | 20/47 (NCI-H23, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2530.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (NCI-H23 0.343×, LoVo 0.409×, NCI-H460 0.426×); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (AN3 CA 0.0635×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.179×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SNU-1 0.141×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.584×** | -8.3 | 9e-14 | 42/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -5.5 | 1e-05 | 34/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | 0.723× | -3.4 | 0.14 | 25/48 (AN3 CA, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2530. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 27.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.325× (z -9.7) |
| [[AN3 CA (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0635× (z -12.6) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 61.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +9.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 32.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 25.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 18.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -8.7) |
| [[SNU-1 (line)]] | wt | 31.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.141× (z -9.8) |
| [[A-172 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 35.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2530), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH7]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[DHPS]] | +0.74 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[UNC45A]] | +0.69 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[RPS11]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[MARK4]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[MXD4]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | same gene group |
| [[RAB40C]] | +0.64 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[NDUFS7]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[ADIPOR1]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CBFA2T2]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[LMBR1L]] | +0.63 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[TMEM219]] | +0.63 | +0.61 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDAP1]] | -0.63 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[TRMT5]] | -0.59 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[NOP14]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[MAK16]] | -0.58 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[TFAM]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[DCLRE1A]] | -0.57 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[GUF1]] | -0.57 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[PPIL1]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ZNF816]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.56 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[GPATCH4]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-15.0, -18.8); signed map (-27.5, 5.6). **Vector** length 64.3, 15.5% of its response variance represented; |z| ≥ 3 in 486 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.5 | +4.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.4 | +3.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.8 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.3 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.7 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.4 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | PTOV1 extended AT-hook containing adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,850,735-49,860,744 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YD1](https://www.uniprot.org/uniprotkb/Q86YD1) (Prostate tumor-overexpressed gene 1 protein):

> May activate transcription. Required for nuclear translocation of FLOT1. Promotes cell proliferation.

**Summary**, from NCBI Gene [53635](https://www.ncbi.nlm.nih.gov/gene/53635):

> This gene encodes a protein that was found to be overexpressed in prostate adenocarcinomas. The encoded protein was found to interact with the lipid raft protein flotillin-1 and shuttle it from the cytoplasm to the nucleus in a cell cycle dependent manner. Alternative splicing of this gene results in multiple transcript variants. [provided by RefSeq, Feb 2015]

**Accessions** — [HGNC:9632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9632) · Entrez [53635](https://www.ncbi.nlm.nih.gov/gene/53635) · UniProt [Q86YD1](https://www.uniprot.org/uniprotkb/Q86YD1) · Ensembl [ENSG00000104960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000104960)

## Data

Gene col 2530: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2530); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2530, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2530]; `tensor/DDL_lfc|DDL_z.npy` [2530]; `embed/gene_vectors.npy` [2530]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2530 or target_col == 2530). Every well: [[PTOV1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTOV1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
