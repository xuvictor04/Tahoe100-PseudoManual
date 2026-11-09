---
symbol: "BORCS8"
type: "gene"
col: 14900
ensembl_id: "ENSG00000254901"
name: "BLOC-1 related complex subunit 8"
location: "19p13.11"
module: 7
arm: "+"
pooled_cpm: 3.4
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# BORCS8

*BLOC-1 related complex subunit 8* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +7.5, q 3e-11, up in 11 of 20 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 1.54× (z +3.7, q 0.009, up in 10 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.413× (z -4.1, q 0.028, down in 14 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC14]] (+0.63, fdr 7e-06), [[JMJD4]] (+0.62, fdr 1e-05), [[PIGQ]] (+0.60, fdr 2e-05); moves opposite to [[YBX1]] (-0.51, fdr 6e-04), [[ARL5A]] (-0.46, fdr 5e-05), [[CREG1]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 11 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.38×** | +7.5 | 3e-11 | 11/20 (PANC-1, SW1417, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.15×** | +6.4 | 4e-08 | 3/6 (CFPAC-1, PANC-1, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.62×** | +5.9 | 7e-07 | 20/38 (PANC-1, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.02×** | +5.6 | 3e-06 | 4/7 (NCI-H2347, PANC-1, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.86×** | +5.4 | 9e-06 | 22/45 (SK-MEL-2, COLO 205, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.85×** | +5.3 | 9e-06 | 23/46 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.77×** | +4.9 | 6e-05 | 20/44 (SNU-423, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.68×** | +4.5 | 5e-04 | 10/24 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.66×** | +4.2 | 0.002 | 9/31 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.61×** | +3.9 | 0.005 | 11/36 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +3.7 | 0.009 | 10/35 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.031 | 10/45 (HS-578T, PANC-1, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.035 | 3/31 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **1.47×** | +3.2 | 0.056 | 5/28 (A-427, Hs 766T, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.079 | 5/32 (NCI-H1573, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | **1.42×** | +3.0 | 0.091 | 4/37 (SW480, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.413×** | -4.1 | 0.028 | 14/40 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.674× | -3.5 | 0.13 | 13/46 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.687× | -3.3 | 0.16 | 15/43 (SW480, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.54 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC14]] | +0.63 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[JMJD4]] | +0.62 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[PIGQ]] | +0.60 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[ZNF513]] | +0.58 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[MED11]] | +0.56 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[ARL16]] | +0.55 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[TM2D2]] | +0.55 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[VPS25]] | +0.55 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[SLC66A1]] | +0.54 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[DDX28]] | +0.54 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[FLAD1]] | +0.54 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[C12orf43]] | +0.53 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YBX1]] | -0.51 | -0.22 / -0.47 | both halves | 6e-04 |  |
| [[ARL5A]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[CREG1]] | -0.45 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[MZT1]] | -0.45 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[HSD17B11]] | -0.44 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[SLC44A1]] | -0.43 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[DPYSL2]] | -0.43 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[MANEA]] | -0.43 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[PPP1CB]] | -0.42 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BORCS8's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.423). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-46.7, 0.3); signed map (-5.1, -26.5). **Vector** length 38.0, 3.82% of its response variance represented; |z| ≥ 3 in 816 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | +2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | +2.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | +2.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.4 | +2.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -2.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | BLOC-1 related complex subunit 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,176,903-19,192,591 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MEF2BNB |
| Gene groups (HGNC) | BLOC-1 related complex subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FH0](https://www.uniprot.org/uniprotkb/Q96FH0) (BLOC-1-related complex subunit 8):

> As part of the BLOC-one-related complex (BORC), it plays a role in the movement and localization of lysosomes at the cell periphery. Associated with the cytosolic face of lysosomes, BORC recruits ARL8B to the lysosomal membrane and couples lysosomes to microtubule plus-end-directed kinesin motors, driving lysosome movement toward the cell periphery.

**Summary**, from NCBI Gene [729991](https://www.ncbi.nlm.nih.gov/gene/729991):

> Involved in heart development. Part of BORC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:37247](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:37247) · Entrez [729991](https://www.ncbi.nlm.nih.gov/gene/729991) · UniProt [Q96FH0](https://www.uniprot.org/uniprotkb/Q96FH0) · Ensembl [ENSG00000254901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000254901)

## Data

Gene col 14900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14900); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14900]; `tensor/DDL_lfc|DDL_z.npy` [14900]; `embed/gene_vectors.npy` [14900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14900 or target_col == 14900). Every well: [[BORCS8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BORCS8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
