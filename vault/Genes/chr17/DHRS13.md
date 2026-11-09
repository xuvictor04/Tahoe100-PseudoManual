---
symbol: "DHRS13"
type: "gene"
col: 9483
ensembl_id: "ENSG00000167536"
name: "dehydrogenase/reductase 13"
location: "17q11.2"
module: 105
arm: "+"
pooled_cpm: 6.2
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# DHRS13

*dehydrogenase/reductase 13* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 2.04× (z +8.2, q 1e-13, up in 25 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.490× (z -11.7, q 1e-28, down in 30 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM210A]] (+0.70, fdr 7e-06), [[GGA2]] (+0.70, fdr 7e-06), [[SEC31B]] (+0.68, fdr 7e-06); moves opposite to [[CPLANE1]] (-0.51, fdr 3e-05), [[SH3D19]] (-0.50, fdr 3e-05), [[PARVA]] (-0.49, fdr 4e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM145]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9483.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +8.2 | 1e-13 | 25/44 (LoVo, HCT15, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.68×** | +5.5 | 8e-06 | 10/16 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.6 | 9e-04 | 9/39 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.4 | 0.001 | 12/40 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.2 | 0.003 | 14/34 (KATO III, NCI-H23, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.86×** | +3.7 | 0.017 | 13/43 (A-172, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.35×** | +3.5 | 0.037 | 11/37 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.17 | 5/37 (HT-29, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9483.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.490×** | -11.7 | 1e-28 | 30/42 (C32, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.397×** | -10.7 | 3e-24 | 28/40 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.674×** | -4.4 | 0.002 | 12/33 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.014 | 16/44 (C32, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.720×** | -3.6 | 0.038 | 17/43 (C32, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9483. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 17.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0863× (z -17.8) |
| [[HEC-1-A (line)]] | alt | 19.8 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.2) |
| [[A-172 (line)]] | wt | 10.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0460× (z -14.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.152× (z -13.3) |
| [[LoVo (line)]] | wt | 3.65 | 0 | 2 | — | [[Mozavaptan (drug)]] 0.05 µM 0.0594× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -13.6) |
| [[C-33 A (line)]] | alt | 7.45 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0704× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 8.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0706× (z -11.2) |
| [[SNU-423 (line)]] | alt | 9.01 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -11.3) |
| [[A-427 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.53 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9483), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM210A]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[GGA2]] | +0.70 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[SEC31B]] | +0.68 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[POM121]] | +0.67 | +0.69 / +0.57 | both halves | 1e-05 |  |
| [[PDK3]] | +0.67 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[AK2]] | +0.67 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[HERC3]] | +0.66 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[HDAC3]] | +0.66 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[POM121C]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[PDK1]] | +0.65 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[SAP30-DT]] | +0.64 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[WDR45B]] | +0.63 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPLANE1]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[SH3D19]] | -0.50 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[PARVA]] | -0.49 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[EPC2]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM145]] | B | TMEM145 activity raises DHRS13's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without TMEM145 | 0.034 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[RRAGD]] | B | RRAGD activity raises DHRS13's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without RRAGD | 0.036 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.762). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.0, -19.1); signed map (-38.9, 22.2). **Vector** length 69.0, 11.6% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.0 | +5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.1 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.4 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.5 | -11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.6 | -2.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.5 | -3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | dehydrogenase/reductase 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:28,897,781-28,903,079 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23280, SDR7C5 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UX07](https://www.uniprot.org/uniprotkb/Q6UX07) (Dehydrogenase/reductase SDR family member 13):

> Putative oxidoreductase.

**Summary**, from NCBI Gene [147015](https://www.ncbi.nlm.nih.gov/gene/147015):

> Predicted to enable oxidoreductase activity. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28326](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28326) · Entrez [147015](https://www.ncbi.nlm.nih.gov/gene/147015) · UniProt [Q6UX07](https://www.uniprot.org/uniprotkb/Q6UX07) · Ensembl [ENSG00000167536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167536)

## Data

Gene col 9483: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9483); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9483, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9483]; `tensor/DDL_lfc|DDL_z.npy` [9483]; `embed/gene_vectors.npy` [9483]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9483 or target_col == 9483). Every well: [[DHRS13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
