---
symbol: "ISY1-RAB43"
type: "gene"
col: 15368
ensembl_id: "ENSG00000261796"
name: "ISY1-RAB43 readthrough"
location: "3q21.3"
module: 38
arm: "+"
pooled_cpm: 3.2
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# ISY1-RAB43

*ISY1-RAB43 readthrough* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.88× (z +15.3, q 0e+00, up in 34 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.588× (z -5.4, q 4e-05, down in 16 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM209A]] (+0.83, fdr 7e-06), [[ATP2A1]] (+0.81, fdr 7e-06), [[ARL9]] (+0.80, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[MIR9-1HG]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15368.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +15.3 | 0e+00 | 34/34 (PANC-1, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +11.6 | 2e-28 | 35/43 (SW480, HT-29, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +6.3 | 7e-08 | 18/48 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +6.2 | 8e-08 | 15/35 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +5.1 | 4e-05 | 7/19 (KATO III, A-427, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +4.6 | 5e-04 | 11/41 (NCI-H2347, LS 180, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +4.0 | 0.005 | 1/5 (CFPAC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.47×** | +3.9 | 0.007 | 3/44 (Panc 03.27, C32, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.008 | 9/36 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.009 | 4/47 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.4 | 0.035 | 1/6 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.88×** | +3.4 | 0.037 | 5/40 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.043 | 9/46 (A-172, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.38×** | +3.1 | 0.069 | 8/42 (A-172, LoVo, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.53×** | +3.1 | 0.069 | 2/43 (NCI-H1573, MIA PaCa-2) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.069 | 10/34 (HEC-1-A, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.078 | 4/33 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.089 | 7/41 (C32, SHP-77, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15368.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.588×** | -5.4 | 4e-05 | 16/44 (A498, PANC-1, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.670×** | -3.9 | 0.025 | 14/43 (Panc 03.27, NCI-H2030, …) | two highest doses | composition shift; position effect removed |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | **0.706×** | -3.6 | 0.072 | 8/44 (COLO 205, H4, …) | inconsistent across doses |  |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | **0.692×** | -3.5 | 0.073 | 9/40 (HCT15, HT-29, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.716× | -3.3 | 0.12 | 13/43 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 0.734× | -3.2 | 0.14 | 9/42 (NCI-H1792, SW480, …) | inconsistent across doses |  |
| [[LB-100 (drug)]] 0.05 µM |  | 0.723× | -3.1 | 0.14 | 4/45 (NCI-H23, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15368. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 3.30 | 0 | 1 | — | [[Levobupivacaine (hydrochloride) (drug)]] 0.05 µM 0.0462× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 2.73 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.124× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 3.83 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.5 µM 0.0543× (z -9.3) |
| [[A-172 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.70 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15368), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM209A]] | +0.83 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ATP2A1]] | +0.81 | +0.85 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[ARL9]] | +0.80 | +0.79 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[RRH]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[VWCE]] | +0.77 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[LINC00672]] | +0.77 | +0.73 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC9A5]] | +0.77 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[PYGM]] | +0.76 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[PYY]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.75 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[PHYHD1]] | +0.74 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[SYCE1L]] | +0.74 | +0.71 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR9-1HG]] | C | ISY1-RAB43's natural level weakens MIR9-1HG's drug response | ISY1-RAB43's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.33; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.881). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, -19.1); signed map (12.9, 11.0). **Vector** length 65.7, 9.38% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +15.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.3 | +3.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.3 | +4.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.7 | -3.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | ISY1-RAB43 readthrough |
| Locus type | readthrough (other) |
| Location | 3q21.3 — chr3:129,087,575-129,161,036 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100534599](https://www.ncbi.nlm.nih.gov/gene/100534599):

> This locus represents naturally occurring read-through transcription between the neighboring ISY1 (ISY1 splicing factor homolog) and RAB43 (RAB43, member RAS oncogene family) gene on chromosome 3. The read-through transcript encodes a protein that shares sequence identity with the upstream gene product, but its C-terminus is distinct due to a frameshift relative to the downstream gene. [provided by RefSeq, Mar 2011]

**Accessions** — [HGNC:42969](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:42969) · Entrez [100534599](https://www.ncbi.nlm.nih.gov/gene/100534599) · Ensembl [ENSG00000261796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261796)

## Data

Gene col 15368: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15368); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15368, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15368]; `tensor/DDL_lfc|DDL_z.npy` [15368]; `embed/gene_vectors.npy` [15368]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15368 or target_col == 15368). Every well: [[ISY1-RAB43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ISY1-RAB43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
