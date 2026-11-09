---
symbol: "OXLD1"
type: "gene"
col: 12835
ensembl_id: "ENSG00000204237"
name: "oxidoreductase like domain containing 1"
location: "17q25.3"
module: 11
arm: "+"
pooled_cpm: 4.11
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# OXLD1

*oxidoreductase like domain containing 1* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +6.2, q 3e-07, up in 28 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.511× (z -4.6, q 0.003, down in 24 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SCAND1]] (+0.76, fdr 1e-05), [[NCBP2AS2]] (+0.75, fdr 1e-05), [[C1orf122]] (+0.73, fdr 3e-05); moves opposite to [[HDLBP]] (-0.56, fdr 1e-04), [[DHFR]] (-0.54, fdr 0.002, ⚠ one half only (not replicated)).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +6.2 | 3e-07 | 28/37 (CFPAC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +6.1 | 3e-07 | 19/23 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.41×** | +5.8 | 1e-06 | 3/6 (NCI-H2347, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **2.00×** | +4.7 | 3e-04 | 8/21 (SW480, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +4.1 | 0.004 | 18/32 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.0 | 0.007 | 11/22 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **1.70×** | +3.4 | 0.062 | 2/7 (HS-578T, NCI-H2347) | all doses, stronger at high dose | composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.61×** | +3.2 | 0.083 | 12/37 (SNU-423, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.511×** | -4.6 | 0.003 | 24/44 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.680×** | -3.7 | 0.051 | 20/38 (SHP-77, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.585×** | -3.6 | 0.051 | 16/47 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.614× | -3.3 | 0.13 | 9/47 (NCI-H1792, NCI-H2030, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.623× | -3.2 | 0.15 | 16/40 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.630× | -3.1 | 0.16 | 14/43 (HS-578T, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 13 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAND1]] | +0.76 | +0.52 / +0.80 | both halves | 1e-05 |  |
| [[NCBP2AS2]] | +0.75 | +0.53 / +0.80 | both halves | 1e-05 |  |
| [[C1orf122]] | +0.73 | +0.44 / +0.76 | both halves | 3e-05 |  |
| [[EXOSC4]] | +0.73 | +0.44 / +0.82 | both halves | 3e-05 |  |
| [[ZNF593]] | +0.72 | +0.47 / +0.81 | both halves | 2e-05 |  |
| [[EMC6]] | +0.72 | +0.34 / +0.84 | both halves | 1e-04 |  |
| [[MRPL36]] | +0.70 | +0.46 / +0.79 | both halves | 3e-05 |  |
| [[RDH14]] | +0.70 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[BLOC1S4]] | +0.69 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[MRPS12]] | +0.67 | +0.28 / +0.76 | both halves | 3e-04 |  |
| [[ENDOG]] | +0.66 | +0.33 / +0.74 | both halves | 1e-04 |  |
| [[MRPL20-AS1]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDLBP]] | -0.56 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[DHFR]] | -0.54 | -0.12 / -0.71 | ⚠ one half (not replicated) | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2]] | C | EID2 activity raises OXLD1's level | lines that do not express EID2 (3) vs lines expressing it (47) | 1.90× lower at baseline in the lines without EID2 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, ITPR2-AS1, ENSG00000261341; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.539). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-43.6, -11.2); signed map (-11.5, -7.3). **Vector** length 44.9, 6.15% of its response variance represented; |z| ≥ 3 in 688 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +6.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +4.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +1.6 | +4.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.2 | +2.6 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | -2.1 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -2.1 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | -1.7 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -3.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | oxidoreductase like domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:81,665,036-81,666,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC104712; previously C17orf90 |
| Matched by | ensembl_id |

UniProt [Q5BKU9](https://www.uniprot.org/uniprotkb/Q5BKU9) carries no function annotation.

**Summary**, from NCBI Gene [339229](https://www.ncbi.nlm.nih.gov/gene/339229):

> Located in mitochondrion. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27901) · Entrez [339229](https://www.ncbi.nlm.nih.gov/gene/339229) · UniProt [Q5BKU9](https://www.uniprot.org/uniprotkb/Q5BKU9) · Ensembl [ENSG00000204237](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204237)

## Data

Gene col 12835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12835); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12835]; `tensor/DDL_lfc|DDL_z.npy` [12835]; `embed/gene_vectors.npy` [12835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12835 or target_col == 12835). Every well: [[OXLD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXLD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
