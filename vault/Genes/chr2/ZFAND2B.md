---
symbol: "ZFAND2B"
type: "gene"
col: 8172
ensembl_id: "ENSG00000158552"
name: "zinc finger AN1-type containing 2B"
location: "2q35"
module: 24
arm: "+"
pooled_cpm: 7.14
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 3
n_dd_up_clean: 1
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ZFAND2B

*zinc finger AN1-type containing 2B* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +5.3, q 3e-05, up in 23 of 41 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.34×; ⚠ cell-cycle shift, explains ~74% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.345× (z -4.2, q 0.017, down in 25 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTIF3]] (+0.73, fdr 7e-06), [[INAFM1]] (+0.72, fdr 7e-06), [[FBXW5]] (+0.72, fdr 7e-06); moves opposite to [[TMX1]] (-0.74, fdr 7e-06), [[NUP155]] (-0.72, fdr 7e-06), [[EFTUD2]] (-0.69, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8172.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 4.34×; ⚠ cell-cycle shift, explains ~74% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.3 | 3e-05 | 23/41 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.65×** | +5.3 | 3e-05 | 22/40 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +4.9 | 2e-04 | 5/12 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.80×** | +4.4 | 0.002 | 17/32 (KATO III, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.1 | 0.004 | 13/33 (PANC-1, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.96× | +3.2 | 0.12 | 6/34 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.93× | +3.2 | 0.13 | 15/37 (SW480, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~58% of this change | 1.50× | +3.0 | 0.18 | 14/38 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.345×** | -4.2 | 0.017 | 25/44 (Panc 03.27, NCI-H2347, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.390×** | -3.7 | 0.046 | 23/41 (RPMI-7951, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.708×** | -3.7 | 0.046 | 21/46 (CFPAC-1, NCI-H2347, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.96 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +9.4) ⚠ cell-cycle shift, explains ~74% of this change | — |
| [[A-172 (line)]] | wt | 7.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.17 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.44 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 6 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTIF3]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[INAFM1]] | +0.72 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[FBXW5]] | +0.72 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.72 | +0.67 / +0.66 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG32]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[RCE1]] | +0.71 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[SNHG7]] | +0.70 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[LIN7B]] | +0.70 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[PMM1]] | +0.70 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.69 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[GGNBP2]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NKAP]] | +0.68 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[UBE2B]] | +0.68 | +0.69 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMX1]] | -0.74 | -0.65 / -0.75 | both halves | 7e-06 |  |
| [[NUP155]] | -0.72 | -0.65 / -0.75 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.69 | -0.61 / -0.76 | both halves | 7e-06 |  |
| [[VMA21]] | -0.69 | -0.54 / -0.71 | both halves | 1e-05 |  |
| [[TMX3]] | -0.69 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.68 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[EIF2S1]] | -0.66 | -0.57 / -0.70 | both halves | 1e-05 |  |
| [[IPO5]] | -0.66 | -0.55 / -0.70 | both halves | 1e-05 |  |
| [[XRCC5]] | -0.65 | -0.55 / -0.68 | both halves | 1e-05 |  |
| [[XRCC6]] | -0.65 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.64 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[DARS2]] | -0.64 | -0.41 / -0.73 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.3, -14.8); signed map (-16.1, -1.6). **Vector** length 65.4, 13.3% of its response variance represented; |z| ≥ 3 in 550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +5.1 | +5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +1.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.9 | +2.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.8 | +2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -2.6 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.2 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.7 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.4 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger AN1-type containing 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,195,237-219,209,651 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIRAPL |
| Gene groups (HGNC) | Zinc fingers AN1-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV99](https://www.uniprot.org/uniprotkb/Q8WV99) (AN1-type zinc finger protein 2B):

> Plays a role in protein homeostasis by regulating both the translocation and the ubiquitin-mediated proteasomal degradation of nascent proteins at the endoplasmic reticulum. It is involved in the regulation of signal-mediated translocation of proteins into the endoplasmic reticulum. It also plays a role in the ubiquitin-mediated proteasomal degradation of proteins for which signal-mediated translocation to the endoplasmic reticulum has failed. May therefore function in the endoplasmic reticulum …

**Summary**, from NCBI Gene [130617](https://www.ncbi.nlm.nih.gov/gene/130617):

> This gene encodes a protein containing AN1-type zinc-fingers and ubiquitin-interacting motifs. The encoded protein likely associates with the proteosome to stimulate the degradation of toxic or misfolded proteins. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:25206](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25206) · Entrez [130617](https://www.ncbi.nlm.nih.gov/gene/130617) · UniProt [Q8WV99](https://www.uniprot.org/uniprotkb/Q8WV99) · Ensembl [ENSG00000158552](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158552)

## Data

Gene col 8172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8172); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8172]; `tensor/DDL_lfc|DDL_z.npy` [8172]; `embed/gene_vectors.npy` [8172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8172 or target_col == 8172). Every well: [[ZFAND2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
