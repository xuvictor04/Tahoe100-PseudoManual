---
symbol: "ENKD1"
type: "gene"
col: 4474
ensembl_id: "ENSG00000124074"
name: "enkurin domain containing 1"
location: "16q22.1"
module: 24
arm: "+"
pooled_cpm: 3.73
n_lines_expressing: 45
n_dd_up: 1
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ENKD1

*enkurin domain containing 1* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +5.2, q 1e-04, up in 1 of 9 measured lines) ⚠ toxic; transcription drop.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.568× (z -4.6, q 0.002, down in 20 of 39 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C1orf35]] (+0.73, fdr 1e-05), [[RBMX2]] (+0.68, fdr 2e-05), [[PCGF1]] (+0.68, fdr 5e-05, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[LIN7B]] (+0.68, fdr 3e-05); moves opposite to [[MOB1A]] (-0.65, fdr 3e-05), [[DHFR]] (-0.62, fdr 4e-05), [[LIN7C]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ING2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +5.2 | 1e-04 | 1/9 (A498) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.90× | +3.5 | 0.13 | 10/30 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | 1.52× | +3.4 | 0.13 | 9/30 (HEC-1-A, SHP-77, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.51× | +3.3 | 0.13 | 7/29 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.80× | +3.2 | 0.13 | 7/26 (Hs 766T, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.80× | +3.2 | 0.13 | 3/33 (HOP62, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.31× | +3.1 | 0.15 | 6/41 (Panc 03.27, SW480, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.76× | +3.1 | 0.15 | 6/19 (HEC-1-A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 1.48× | +3.0 | 0.15 | 8/30 (HT-29, RPMI-7951, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.568×** | -4.6 | 0.002 | 20/39 (HT-29, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.702×** | -4.1 | 0.009 | 15/41 (Hs 766T, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.607×** | -4.1 | 0.009 | 19/42 (HT-29, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 7.65 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0929× (z -9.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.806 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.421 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.676 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 10 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1orf35]] | +0.73 | +0.54 / +0.77 | both halves | 1e-05 | STRING 439 |
| [[RBMX2]] | +0.68 | +0.48 / +0.75 | both halves | 2e-05 |  |
| [[PCGF1]] ⚠ | +0.68 | +0.40 / +0.74 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[LIN7B]] | +0.68 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[SMIM26]] ⚠ | +0.66 | +0.46 / +0.71 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PMM1]] | +0.66 | +0.40 / +0.70 | both halves | 4e-05 |  |
| [[FBXW5]] | +0.65 | +0.47 / +0.70 | both halves | 2e-05 |  |
| [[RFNG]] | +0.65 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[RPP21]] | +0.64 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[POLR2I]] | +0.63 | +0.32 / +0.68 | both halves | 2e-04 |  |
| [[ZNHIT3]] | +0.63 | +0.40 / +0.62 | both halves | 4e-05 |  |
| [[ZNF324]] | +0.63 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.62 | +0.31 / +0.69 | both halves | 2e-04 |  |
| [[TARS2]] | +0.62 | +0.32 / +0.70 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.65 | -0.46 / -0.66 | both halves | 3e-05 |  |
| [[DHFR]] | -0.62 | -0.42 / -0.63 | both halves | 4e-05 |  |
| [[LIN7C]] | -0.60 | -0.36 / -0.66 | both halves | 1e-04 |  |
| [[STMP1]] | -0.60 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[SLC39A10]] | -0.59 | -0.27 / -0.60 | both halves | 3e-04 |  |
| [[STK26]] | -0.58 | -0.38 / -0.60 | both halves | 7e-05 |  |
| [[TMX1]] | -0.58 | -0.46 / -0.61 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.57 | -0.32 / -0.63 | both halves | 2e-04 |  |
| [[HNRNPA3]] | -0.57 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[BTBD1]] | -0.57 | -0.31 / -0.63 | both halves | 2e-04 |  |
| [[RCN1]] | -0.57 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[EMB]] | -0.57 | -0.32 / -0.60 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ING2]] | B | ENKD1 activity lowers ING2's level | lines that do not express ENKD1 (5) vs lines expressing it (45) | 1.13× higher at baseline in the lines without ENKD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3; maybe low, not absent; its own permutation p |
| [[FRG1]] | B | ENKD1 activity lowers FRG1's level | lines that do not express ENKD1 (5) vs lines expressing it (45) | 1.24× higher at baseline in the lines without ENKD1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.676). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.3, -15.2); signed map (-17.0, -2.5). **Vector** length 41.4, 5.34% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +3.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +3.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +2.7 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.2 | +3.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +3.0 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.1 | -1.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | enkurin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:67,662,945-67,667,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434A1319, FBB11; previously C16orf48 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0I2](https://www.uniprot.org/uniprotkb/Q9H0I2) (Enkurin domain-containing protein 1):

> Microtubule-binding protein which regulates microtubule organization and stability. Promotes the stability of astral microtubules and facilitates the proper orientation of the mitotic spindle. This allows the oriented division of basal keratinocytes and contributes to epidermal stratification (By similarity). Required for the assembly of both primary and motile cilia. Destabilizes the interaction between CCP110 and CEP97 by competing with CEP97 for binding to CCP110 which promotes the removal …

**Summary**, from NCBI Gene [84080](https://www.ncbi.nlm.nih.gov/gene/84080):

> Enables alpha-tubulin binding activity and microtubule binding activity. Involved in establishment of mitotic spindle orientation and non-motile cilium assembly. Located in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25246](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25246) · Entrez [84080](https://www.ncbi.nlm.nih.gov/gene/84080) · UniProt [Q9H0I2](https://www.uniprot.org/uniprotkb/Q9H0I2) · Ensembl [ENSG00000124074](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124074)

## Data

Gene col 4474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4474); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4474]; `tensor/DDL_lfc|DDL_z.npy` [4474]; `embed/gene_vectors.npy` [4474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4474 or target_col == 4474). Every well: [[ENKD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ENKD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
