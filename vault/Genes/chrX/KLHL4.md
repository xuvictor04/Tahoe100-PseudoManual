---
symbol: "KLHL4"
type: "gene"
col: 2232
ensembl_id: "ENSG00000102271"
name: "kelch like family member 4"
location: "Xq21.31"
module: 25
arm: "-"
pooled_cpm: 28.22
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# KLHL4

*kelch like family member 4* — Xq21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.41× (z +6.3, q 2e-07, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (J82 5.27×; ⚠ toxic; transcription drop); [[Ponatinib (drug)]] 5 µM in 1 line (J82 4.85×).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.807× (z -9.4, q 3e-18, down in 35 of 48 measured lines) ⚠ position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.122×, MIA PaCa-2 0.176×, LoVo 0.239×, NCI-H2030 0.278×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.0756×, A-172 0.170×; ⚠ transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.230×; ⚠ cell-cycle shift, explains ~81% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R12A]] (+0.56, fdr 1e-05), [[MSX2]] (+0.55, fdr 1e-05), [[SUMO4]] (+0.53, fdr 2e-05); moves opposite to [[PTPN18]] (-0.57, fdr 3e-05), [[C1orf198]] (-0.56, fdr 1e-05), [[ALG6]] (-0.54, fdr 4e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2232.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (J82 5.27×; ⚠ toxic; transcription drop); [[Ponatinib (drug)]] 5 µM in 1 line (J82 4.85×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.3 | 2e-07 | 30/48 (LOX-IMVI, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2232.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (LOX-IMVI 0.122×, MIA PaCa-2 0.176×, LoVo 0.239×, NCI-H2030 0.278×; ⚠ toxic; transcription drop); [[Docetaxel (drug)]] 0.05 µM in 2 lines (MIA PaCa-2 0.0756×, A-172 0.170×; ⚠ transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.230×; ⚠ cell-cycle shift, explains ~81% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.807×** | -9.4 | 3e-18 | 35/48 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.741×** | -3.9 | 0.022 | 14/48 (A-427, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.743×** | -3.9 | 0.022 | 21/45 (MIA PaCa-2, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.746×** | -3.7 | 0.036 | 14/31 (LOX-IMVI, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.832×** | -3.4 | 0.086 | 14/48 (NCI-H1792, HS-578T, …) | top dose only | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2232. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 15.9 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +8.7) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 4.85× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0756× (z -14.6) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 25.5 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.170× (z -9.8) ⚠ transcription drop |
| [[KATO III (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.180× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -9.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 67.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.3) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H2030 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.278× (z -8.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2232), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R12A]] | +0.56 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MSX2]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[SUMO4]] | +0.53 | +0.46 / +0.47 | both halves | 2e-05 |  |
| [[PAFAH1B1]] | +0.52 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[CSNK1A1]] | +0.51 | +0.52 / +0.43 | both halves | 3e-05 |  |
| [[GPATCH8]] | +0.51 | +0.56 / +0.43 | both halves | 3e-05 |  |
| [[ARID5B]] | +0.50 | +0.48 / +0.44 | both halves | 3e-05 |  |
| [[PALLD]] | +0.49 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[SSH2]] | +0.49 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[BASP1]] | +0.49 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[SPOP]] | +0.49 | +0.44 / +0.44 | both halves | 3e-05 | same gene group |
| [[ZNF75A]] | +0.48 | +0.49 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPN18]] | -0.57 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[C1orf198]] | -0.56 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[ALG6]] | -0.54 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[RFT1]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FAM136A]] | -0.53 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[DLST]] | -0.52 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[DAZAP1]] | -0.52 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[CERS2]] | -0.52 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[ABCB10]] | -0.52 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[NAE1]] | -0.51 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[DPAGT1]] | -0.51 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[AKT1]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.377). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.0, -26.8); signed map (-5.1, 10.5). **Vector** length 77.3, 14.6% of its response variance represented; |z| ≥ 3 in 678 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.9 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | +3.4 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Afatinib (drug)]] 0.05 µM |  | +1.8 | +2.3 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | +1.8 | +1.5 |
| fall | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | -3.1 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.7 | -9.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -2.5 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.1 | -1.3 |
|  | [[Lopinavir (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.3 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.31 — chrX:87,517,409-87,670,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1687, DKELCHL, KHL4 |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Matched by | ensembl_id |

UniProt [Q9C0H6](https://www.uniprot.org/uniprotkb/Q9C0H6) carries no function annotation.

**Summary**, from NCBI Gene [56062](https://www.ncbi.nlm.nih.gov/gene/56062):

> This gene encodes a member of the kelch family of proteins, which are characterized by kelch repeat motifs and a POZ/BTB protein-binding domain. It is thought that kelch repeats are actin binding domains. However, the specific function of this protein has not been determined. Alternative splicing of this gene results in two transcript variants encoding different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6355) · Entrez [56062](https://www.ncbi.nlm.nih.gov/gene/56062) · UniProt [Q9C0H6](https://www.uniprot.org/uniprotkb/Q9C0H6) · Ensembl [ENSG00000102271](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102271)

## Data

Gene col 2232: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2232); `tables/drug_effects.parquet` (6 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2232, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2232]; `tensor/DDL_lfc|DDL_z.npy` [2232]; `embed/gene_vectors.npy` [2232]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2232 or target_col == 2232). Every well: [[KLHL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
