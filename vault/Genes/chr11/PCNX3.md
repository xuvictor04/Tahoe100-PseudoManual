---
symbol: "PCNX3"
type: "gene"
col: 12351
ensembl_id: "ENSG00000197136"
name: "pecanex 3"
location: "11q13.1"
module: 127
arm: "+"
pooled_cpm: 13.41
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# PCNX3

*pecanex 3* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.33× (z +6.6, q 2e-08, up in 39 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 0.104×, NCI-H1573 0.170×, AsPC-1 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (RKO 0.0789×); [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.112×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C-33 A 0.0973×); [[Omeprazole (drug)]] 0.5 µM in 1 line (HCT15 0.0963×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BLTP2]] (+0.76, fdr 7e-06), [[CDK9]] (+0.76, fdr 7e-06), [[NOP9]] (+0.74, fdr 7e-06); moves opposite to [[CHMP2B]] (-0.64, fdr 1e-05), [[ABCA5]] (-0.62, fdr 1e-05), [[EIF1B]] (-0.60, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +6.6 | 2e-08 | 39/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.29×** | +6.5 | 2e-08 | 39/47 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +5.0 | 9e-05 | 28/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.75×** | +4.1 | 0.004 | 27/47 (KATO III, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +4.1 | 0.004 | 30/44 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.48× | +3.0 | 0.22 | 17/47 (Hs 766T, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12351.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 3 lines (NCI-H460 0.104×, NCI-H1573 0.170×, AsPC-1 0.172×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (RKO 0.0789×); [[Digitoxin (drug)]] 0.5 µM in 1 line (KATO III 0.112×; ⚠ cell-cycle shift, explains ~0% of this change); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (C-33 A 0.0973×); [[Omeprazole (drug)]] 0.5 µM in 1 line (HCT15 0.0963×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib (drug)]] 0.05 µM |  | 0.647× | -3.3 | 0.46 | 21/45 (SNU-1, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.675× | -3.2 | 0.46 | 19/46 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~19% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[BT-474 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~79% of this change |
| [[C-33 A (line)]] | alt | 17.6 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0973× (z -9.4) |
| [[HCT15 (line)]] | alt | 13.5 | 0 | 1 | — | [[Omeprazole (drug)]] 0.5 µM 0.0963× (z -9.1) |
| [[KATO III (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.112× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 8.04 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.104× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[RKO (line)]] | wt | 13.2 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0789× (z -11.4) |
| [[A-172 (line)]] | wt | 9.90 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLTP2]] | +0.76 | +0.71 / +0.77 | both halves | 7e-06 |  |
| [[CDK9]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[NOP9]] | +0.74 | +0.62 / +0.76 | both halves | 7e-06 |  |
| [[INTS1]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 | STRING 793 |
| [[TUBGCP6]] | +0.74 | +0.63 / +0.76 | both halves | 7e-06 |  |
| [[AKT1]] | +0.73 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[GCN1]] | +0.72 | +0.64 / +0.80 | both halves | 7e-06 | same gene group |
| [[CCAR2]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[ARHGAP4]] | +0.72 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[E2F4]] | +0.72 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[MFN2]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ARF3]] | +0.69 | +0.60 / +0.73 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP2B]] | -0.64 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[ABCA5]] | -0.62 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.60 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[MPLKIP]] | -0.58 | -0.45 / -0.66 | both halves | 3e-05 |  |
| [[ZMYM5]] | -0.58 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[LRCH3]] | -0.57 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ZNF330]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.57 | -0.46 / -0.59 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PCNX3's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LAMA5]] | B | LAMA5 activity raises PCNX3's level | lines that do not express LAMA5 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without LAMA5 | 0.079 | ⚠ within organs, on part of the lines; also absent: ARHGEF16, NRARP, KRT18; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.768). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-18.3, -26.9); signed map (-13.6, -31.3). **Vector** length 86.6, 18.5% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.1 | +0.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | +1.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.8 | +0.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +4.1 |
|  | [[(S)-Crizotinib (drug)]] 5 µM |  | +1.8 | +1.4 |
|  | [[Ivermectin (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.3 | -1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.1 | -1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -1.6 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.0 | -1.9 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | pecanex 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,615,776-65,637,439 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22427; previously PCNXL3 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Pecanex family |
| Matched by | ensembl_id |

UniProt [Q9H6A9](https://www.uniprot.org/uniprotkb/Q9H6A9) carries no function annotation.

**Summary**, from NCBI Gene [399909](https://www.ncbi.nlm.nih.gov/gene/399909):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18760) · Entrez [399909](https://www.ncbi.nlm.nih.gov/gene/399909) · UniProt [Q9H6A9](https://www.uniprot.org/uniprotkb/Q9H6A9) · Ensembl [ENSG00000197136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197136)

## Data

Gene col 12351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12351); `tables/drug_effects.parquet` (8 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12351]; `tensor/DDL_lfc|DDL_z.npy` [12351]; `embed/gene_vectors.npy` [12351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12351 or target_col == 12351). Every well: [[PCNX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCNX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
