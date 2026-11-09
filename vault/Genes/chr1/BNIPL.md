---
symbol: "BNIPL"
type: "gene"
col: 8642
ensembl_id: "ENSG00000163141"
name: "BCL2 interacting protein like"
location: "1q21.3"
module: 37
arm: "+"
pooled_cpm: 3.84
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 8
n_dd_up_clean: 6
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# BNIPL

*BCL2 interacting protein like* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +6.8, q 5e-09, up in 18 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.502× (z -6.3, q 1e-07, down in 23 of 41 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.546× (z -5.8, q 2e-06, down in 19 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB12]] (+0.75, fdr 7e-06), [[TNXB]] (+0.74, fdr 7e-06), [[ECT2L]] (+0.73, fdr 7e-06); moves opposite to [[TTPAL]] (-0.58, fdr 4e-05), [[UROS]] (-0.54, fdr 1e-04), [[PNPO]] (-0.54, fdr 4e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +6.8 | 5e-09 | 18/36 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +6.5 | 3e-08 | 26/46 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.90×** | +6.1 | 2e-07 | 21/44 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.64×** | +4.7 | 4e-04 | 10/46 (LoVo, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.5 | 9e-04 | 10/23 (NCI-H2347, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.58×** | +4.3 | 0.001 | 14/44 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.49×** | +3.8 | 0.012 | 9/45 (PANC-1, A-172, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.017 | 9/39 (NCI-H2030, A498, …) | top dose only | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.13 | 4/43 (AsPC-1, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.502×** | -6.3 | 1e-07 | 23/41 (SW 900, A498, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.546×** | -5.8 | 2e-06 | 19/43 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.587×** | -4.9 | 2e-04 | 18/42 (LoVo, COLO 205, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -4.2 | 0.003 | 17/45 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.696×** | -3.5 | 0.052 | 14/46 (PANC-1, KATO III, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.500×** | -3.5 | 0.052 | 12/40 (HCT15, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.697×** | -3.3 | 0.087 | 9/45 (HCT15, KATO III, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -3.2 | 0.092 | 10/37 (A-172, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.05 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0870× (z -8.7) |
| [[HCT15 (line)]] | alt | 8.95 | 0 | 1 | — | [[Elagolix sodium (drug)]] 0.05 µM 0.0412× (z -10.5) |
| [[LoVo (line)]] | wt | 4.13 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0776× (z -10.2) |
| [[PANC-1 (line)]] | alt | 4.87 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -8.5) ⚠ cell-cycle shift, explains ~46% of this change |
| [[SW 900 (line)]] | alt | 4.94 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0565× (z -8.7) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.56 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB12]] | +0.75 | +0.69 / +0.78 | both halves | 7e-06 |  |
| [[TNXB]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[ECT2L]] | +0.73 | +0.68 / +0.75 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.70 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[GUCA1B]] | +0.70 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[CLEC4A]] | +0.70 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[HYPK]] | +0.68 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.67 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GET1-SH3BGR]] | +0.67 | +0.47 / +0.76 | both halves | 2e-05 |  |
| [[PPP1R32]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[DRD4]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[WDR49]] | +0.66 | +0.68 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTPAL]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 | same gene group |
| [[UROS]] | -0.54 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[PNPO]] | -0.54 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[AKAP11]] | -0.54 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ACTR3]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers BNIPL's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.731). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, -20.3); signed map (8.9, 5.7). **Vector** length 63.5, 10.1% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +3.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[Gefitinib (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -4.6 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.9 | -4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | -2.7 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.1 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 interacting protein like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,036,321-151,047,720 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BNIPl-1, BNIPL-2, PP753, BNIP-S, BNIP-Salpha, BNIP-Sbeta |
| Gene groups (HGNC) | BCH domain containing ; CRAL-TRIO lipid binding domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z465](https://www.uniprot.org/uniprotkb/Q7Z465) (Bcl-2/adenovirus E1B 19 kDa-interacting protein 2-like protein):

> May be a bridge molecule between BCL2 and ARHGAP1/CDC42 in promoting cell death.

**Summary**, from NCBI Gene [149428](https://www.ncbi.nlm.nih.gov/gene/149428):

> The protein encoded by this gene interacts with several other proteins, such as BCL2, ARHGAP1, MIF and GFER. It may function as a bridge molecule between BCL2 and ARHGAP1/CDC42 in promoting cell death. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:16976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16976) · Entrez [149428](https://www.ncbi.nlm.nih.gov/gene/149428) · UniProt [Q7Z465](https://www.uniprot.org/uniprotkb/Q7Z465) · Ensembl [ENSG00000163141](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163141)

## Data

Gene col 8642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8642); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8642]; `tensor/DDL_lfc|DDL_z.npy` [8642]; `embed/gene_vectors.npy` [8642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8642 or target_col == 8642). Every well: [[BNIPL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BNIPL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
