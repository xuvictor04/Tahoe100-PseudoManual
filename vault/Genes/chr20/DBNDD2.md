---
symbol: "DBNDD2"
type: "gene"
col: 14399
ensembl_id: "ENSG00000244274"
name: "dysbindin domain containing 2"
location: "20q13.12"
module: 24
arm: "+"
pooled_cpm: 12.43
n_lines_expressing: 42
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# DBNDD2

*dysbindin domain containing 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.10× (z +6.3, q 2e-07, up in 21 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.29× (z +4.1, q 0.008, up in 20 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.423× (z -7.3, q 2e-10, down in 29 of 39 measured lines).
> Its strongest partners by |cos| (65 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 39 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAS5]] (+0.59, fdr 4e-05), [[RNF7]] (+0.54, fdr 2e-04), [[RANGRF]] (+0.54, fdr 1e-04); moves opposite to [[ANP32E]] (-0.47, fdr 2e-04), [[CCDC61]] (-0.46, fdr 3e-04), [[SLX4]] (-0.44, fdr 4e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.10×** | +6.3 | 2e-07 | 21/28 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.03×** | +5.8 | 2e-06 | 11/19 (HS-578T, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.29×** | +4.1 | 0.008 | 20/33 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.59×** | +3.9 | 0.012 | 16/31 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.8 | 0.015 | 17/33 (COLO 205, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +3.7 | 0.021 | 8/19 (CFPAC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.02×** | +3.5 | 0.042 | 17/35 (Hs 766T, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +3.0 | 0.17 | 1/40 (SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.423×** | -7.3 | 2e-10 | 29/39 (C-33 A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.433×** | -7.1 | 4e-10 | 31/39 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.443×** | -6.9 | 1e-09 | 32/39 (KATO III, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.610×** | -5.9 | 5e-07 | 25/36 (RKO, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.656×** | -3.6 | 0.041 | 18/39 (SW1417, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 0.761× | -3.3 | 0.10 | 15/37 (MIA PaCa-2, SW48, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 35.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.201× (z -13.3) |
| [[KATO III (line)]] | alt | 27.0 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -12.2) |
| [[C-33 A (line)]] | alt | 19.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.1000× (z -10.1) |
| [[HT-29 (line)]] | alt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.8) |
| [[SW1417 (line)]] | alt | 43.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -11.0) |
| [[A-172 (line)]] | wt | 5.74 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.78 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.84 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 16.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 31 of them with an alert (⚠; 28 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS5]] | +0.59 | +0.42 / +0.65 | both halves | 4e-05 |  |
| [[RNF7]] | +0.54 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[RANGRF]] | +0.54 | +0.34 / +0.61 | both halves | 1e-04 |  |
| [[SMNDC1]] | +0.52 | +0.45 / +0.40 | both halves | 4e-05 |  |
| [[RPP21]] | +0.51 | +0.28 / +0.67 | both halves | 3e-04 |  |
| [[STOML2]] | +0.51 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[PQBP1]] | +0.51 | +0.25 / +0.60 | both halves | 4e-04 |  |
| [[RPS15]] ⚠ | +0.50 | +0.29 / +0.61 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[DNLZ]] | +0.49 | +0.20 / +0.62 | both halves | 7e-04 |  |
| [[FBXL15]] | +0.49 | +0.34 / +0.51 | both halves | 1e-04 |  |
| [[RPS23]] | +0.48 | +0.32 / +0.57 | both halves | 2e-04 |  |
| [[STARD10]] | +0.47 | +0.28 / +0.54 | both halves | 3e-04 |  |
| [[ZFAS1]] | +0.46 | +0.27 / +0.53 | both halves | 3e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANP32E]] | -0.47 | -0.30 / -0.54 | both halves | 2e-04 |  |
| [[CCDC61]] | -0.46 | -0.27 / -0.50 | both halves | 3e-04 |  |
| [[SLX4]] | -0.44 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[HNRNPA3]] | -0.44 | -0.14 / -0.58 | ⚠ one half (not replicated) | 0.002 |  |
| [[TRIM52]] | -0.40 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[DHFR]] | -0.40 | -0.08 / -0.51 | ⚠ one half (not replicated) | 0.003 |  |
| [[HMGN1]] | -0.40 | -0.21 / -0.47 | both halves | 7e-04 |  |
| [[ILF2]] | -0.40 | -0.17 / -0.39 | ⚠ not reproduced | 0.001 |  |
| [[UGGT1]] | -0.39 | -0.10 / -0.49 | ⚠ not reproduced | 0.003 |  |
| [[LINC03009]] | -0.39 | -0.07 / -0.49 | ⚠ not reproduced | 0.004 |  |
| [[HNRNPA2B1]] | -0.39 | -0.16 / -0.55 | ⚠ one half (not replicated) | 0.001 |  |
| [[PARK7]] ⚠ | -0.39 | -0.21 / -0.47 | both halves | 7e-04 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises DBNDD2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.420). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.1, -20.0); signed map (-13.1, -0.4). **Vector** length 49.5, 9.37% of its response variance represented; |z| ≥ 3 in 549 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.4 | +2.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +2.2 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.1 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.7 | +4.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +0.1 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -0.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.1 | -0.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | dysbindin domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,406,057-45,410,610 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSMNP1; previously C20orf35 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQY9](https://www.uniprot.org/uniprotkb/Q9BQY9) (Dysbindin domain-containing protein 2):

> May modulate the activity of casein kinase-1. Inhibits CSNK1D autophosphorylation (in vitro).

**Summary**, from NCBI Gene [55861](https://www.ncbi.nlm.nih.gov/gene/55861):

> Predicted to enable ATPase binding activity. Involved in negative regulation of protein kinase activity. Predicted to be located in cytoplasm. Predicted to be active in endoplasmic reticulum and lysosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15881](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15881) · Entrez [55861](https://www.ncbi.nlm.nih.gov/gene/55861) · UniProt [Q9BQY9](https://www.uniprot.org/uniprotkb/Q9BQY9) · Ensembl [ENSG00000244274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000244274)

## Data

Gene col 14399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14399); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14399]; `tensor/DDL_lfc|DDL_z.npy` [14399]; `embed/gene_vectors.npy` [14399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14399 or target_col == 14399). Every well: [[DBNDD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DBNDD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
