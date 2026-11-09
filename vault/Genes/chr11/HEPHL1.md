---
symbol: "HEPHL1"
type: "gene"
col: 11180
ensembl_id: "ENSG00000181333"
name: "hephaestin like 1"
location: "11q21"
module: 27
arm: "+"
pooled_cpm: 4.16
n_lines_expressing: 5
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# HEPHL1

*hephaestin like 1* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.68× (z +11.4, q 2e-27, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.20× (z +9.2, q 7e-18, up in 0 of 2 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 0.380×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02964]] (+0.67, fdr 8e-06), [[KLK7]] (+0.61, fdr 9e-06), [[ADGRG5]] (+0.58, fdr 2e-05); moves opposite to [[HOXA9]] (-0.45, fdr 1e-04), [[PUS10]] (-0.45, fdr 1e-04), [[HOXA11]] (-0.43, fdr 1e-04).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANO4]] → it (grade C ⚠); 4 go from it, the strongest it → [[MEST]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.68×** | +11.4 | 2e-27 | 1/1 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.36×** | +9.8 | 3e-20 | 1/1 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.20×** | +9.2 | 7e-18 | 0/2 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.50×** | +7.8 | 1e-12 | 1/1 (SW1417) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +4.6 | 4e-04 | 2/3 (SW1417, HT-29) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +4.5 | 6e-04 | 0/1 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.35×** | +4.2 | 0.002 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.13×** | +4.1 | 0.002 | 1/1 (SW1417) | top dose only | noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.008 | 0/3 | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.94×** | +3.7 | 0.012 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.90×** | +3.6 | 0.018 | 0/1 | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.87×** | +3.2 | 0.059 | 0/1 | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (SW1417 0.380×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 159 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.2) |
| [[A-172 (line)]] | wt | 0.510 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.459 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.591 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.564 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.520 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.530 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.628 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.597 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.494 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.602 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.528 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.619 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.695 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.412 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.492 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.475 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.633 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.607 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.460 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.538 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.795 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.774 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.735 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02964]] | +0.67 | +0.60 / +0.57 | both halves | 8e-06 | **novel candidate** |
| [[KLK7]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[ADGRG5]] | +0.58 | +0.61 / +0.46 | both halves | 2e-05 |  |
| [[IGFL4]] | +0.56 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[VWA2]] | +0.56 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[AZGP1]] | +0.54 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[KLK6]] | +0.53 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SKAP1]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[MAOB]] | +0.53 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[LINC01819]] | +0.52 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[GJB1]] | +0.52 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[VIL1]] | +0.51 | +0.53 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA9]] | -0.45 | -0.47 / -0.34 | both halves | 1e-04 |  |
| [[PUS10]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[HOXA11]] | -0.43 | -0.40 / -0.36 | both halves | 1e-04 |  |
| [[DHX29]] | -0.43 | -0.45 / -0.26 | both halves | 4e-04 |  |
| [[NDUFS3]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[TADA2B]] | -0.42 | -0.39 / -0.28 | both halves | 3e-04 |  |
| [[WHAMM]] | -0.40 | -0.39 / -0.32 | both halves | 2e-04 |  |
| [[ATAD2B]] | -0.39 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[CIDECP1]] | -0.39 | -0.38 / -0.22 | both halves | 6e-04 |  |
| [[TRAPPC13]] | -0.39 | -0.25 / -0.45 | both halves | 4e-04 |  |
| [[HOXA10]] | -0.39 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[THAP3]] | -0.39 | -0.37 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANO4]] | C | ANO4 activity raises HEPHL1's level | lines that do not express ANO4 (30) vs lines expressing it (20) | 1.34× lower at baseline in the lines without ANO4 | 0.096 | ⚠ within organs, on part of the lines; also absent: LINC01194, INA, ZNF667-AS1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEST]] | B | HEPHL1 activity raises MEST's level | lines that do not express HEPHL1 (45) vs lines expressing it (5) | 2.44× lower at baseline in the lines without HEPHL1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KRT20, GPR15, APOB |
| [[SLC30A10]] | B | HEPHL1 activity raises SLC30A10's level | lines that do not express HEPHL1 (45) vs lines expressing it (5) | 4.45× lower at baseline in the lines without HEPHL1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KRT20, GPR15, APOB |
| [[HOXA9]] | C | HEPHL1 activity raises HOXA9's level | lines that do not express HEPHL1 (45) vs lines expressing it (5) | 6.96× lower at baseline in the lines without HEPHL1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KRT20, GPR15, APOB; co-absent with the target |
| [[KLK6]] | C | HEPHL1 activity raises KLK6's level | lines that do not express HEPHL1 (45) vs lines expressing it (5) | 8.61× lower at baseline in the lines without HEPHL1 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KRT20, GPR15, APOB; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.419). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.8, 44.9); signed map (64.7, 13.8). **Vector** length 6.34, 1.67% of its response variance represented; |z| ≥ 3 in 54 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +0.6 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.6 | +11.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.6 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.3 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.2 | +0.4 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.1 | +0.3 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -0.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | +0.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.2 | +1.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.2 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.1 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.1 | -1.2 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | -0.1 | -0.4 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | hephaestin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,021,354-94,114,208 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686F22190, Zp |
| Gene groups (HGNC) | Multicopper ferroxidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6MZM0](https://www.uniprot.org/uniprotkb/Q6MZM0) (Ferroxidase HEPHL1):

> Is a copper-binding glycoprotein with ferroxidase activity. It oxidizes Fe(2+) to Fe(3+) without releasing radical oxygen species. May be involved in the regulation of intracellular iron content.

**Summary**, from NCBI Gene [341208](https://www.ncbi.nlm.nih.gov/gene/341208):

> Enables ferroxidase activity. Involved in intracellular iron ion homeostasis. Predicted to be located in membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30477) · Entrez [341208](https://www.ncbi.nlm.nih.gov/gene/341208) · UniProt [Q6MZM0](https://www.uniprot.org/uniprotkb/Q6MZM0) · Ensembl [ENSG00000181333](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181333)

## Data

Gene col 11180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11180); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11180]; `tensor/DDL_lfc|DDL_z.npy` [11180]; `embed/gene_vectors.npy` [11180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11180 or target_col == 11180). Every well: [[HEPHL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HEPHL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
