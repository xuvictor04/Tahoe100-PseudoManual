---
symbol: "PTPMT1"
type: "gene"
col: 3147
ensembl_id: "ENSG00000110536"
name: "protein tyrosine phosphatase mitochondrial 1"
location: "11p11.2"
module: 36
arm: "+"
pooled_cpm: 16.85
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# PTPMT1

*protein tyrosine phosphatase mitochondrial 1* — 11p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +9.0, q 2e-16, up in 35 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.673× (z -5.4, q 4e-05, down in 31 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFS6]] (+0.68, fdr 7e-06), [[C22orf39]] (+0.60, fdr 2e-05), [[CIAPIN1]] (+0.59, fdr 1e-05); moves opposite to [[APLP2]] (-0.48, fdr 1e-04), [[FOSB]] (-0.48, fdr 3e-05), [[KLHL32]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +9.0 | 2e-16 | 35/39 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +7.2 | 1e-10 | 24/28 (A-172, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.66×** | +4.9 | 2e-04 | 24/40 (NCI-H2347, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.63×** | +4.3 | 0.002 | 21/31 (SNU-423, Hs 766T, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +3.7 | 0.020 | 18/41 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.29×** | +3.5 | 0.047 | 18/48 (Panc 03.27, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.673×** | -5.4 | 4e-05 | 31/47 (RKO, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.652×** | -4.1 | 0.012 | 26/47 (KATO III, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.688×** | -3.6 | 0.064 | 18/47 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 5 µM |  | 0.518× | -3.1 | 0.28 | 15/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.525× | -3.0 | 0.28 | 16/46 (HT-29, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 11.6 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.140× (z -8.9) |
| [[RKO (line)]] | wt | 24.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -8.5) |
| [[A-172 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.59 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 23.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFS6]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[C22orf39]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CIAPIN1]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[ARHGEF11]] | +0.59 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[CCDC66]] | +0.57 | +0.39 / +0.54 | both halves | 5e-05 |  |
| [[DHX30]] | +0.57 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[PCGF6]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[LSM6]] | +0.56 | +0.38 / +0.61 | both halves | 6e-05 |  |
| [[VPS54]] | +0.55 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[NRF1]] | +0.55 | +0.53 / +0.43 | both halves | 3e-05 |  |
| [[ERCC8]] | +0.55 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[XPO4]] | +0.54 | +0.50 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APLP2]] | -0.48 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[FOSB]] | -0.48 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[KLHL32]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[YWHAZ]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[SDCBP]] | -0.47 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MORF4L2]] | -0.47 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[SPAG9]] | -0.46 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ATF3]] | -0.46 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[IQGAP1]] | -0.46 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[TUBB3]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[TENT5C]] | -0.46 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[IDS]] | -0.45 | -0.30 / -0.54 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PTPMT1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-20.6, -1.9); signed map (-10.7, -23.4). **Vector** length 50.7, 9.20% of its response variance represented; |z| ≥ 3 in 490 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.3 | +1.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +1.8 | +1.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.7 | +2.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +2.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.1 | +1.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -3.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase mitochondrial 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p11.2 — chr11:47,565,430-47,573,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PLIP, DUSP23, MOSP |
| Gene groups (HGNC) | Atypical dual specificity phosphatases; Phosphoinositide phosphatases |
| Reactome | 4 pathways, smallest: Synthesis of PG; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WUK0](https://www.uniprot.org/uniprotkb/Q8WUK0) (Phosphatidylglycerophosphatase and protein-tyrosine phosphatase 1):

> Lipid phosphatase which dephosphorylates phosphatidylglycerophosphate (PGP) to phosphatidylglycerol (PG) (By similarity). PGP is an essential intermediate in the biosynthetic pathway of cardiolipin, a mitochondrial-specific phospholipid regulating the membrane integrity and activities of the organelle. Has also been shown to display phosphatase activity toward phosphoprotein substrates, specifically mediates dephosphorylation of mitochondrial proteins, thereby playing an essential role in ATP …

**Summary**, from NCBI Gene [114971](https://www.ncbi.nlm.nih.gov/gene/114971):

> Predicted to enable phosphatidylglycerophosphatase activity and phosphatidylinositol-5-phosphate phosphatase activity. Involved in cardiolipin biosynthetic process; mitochondrial fragmentation involved in apoptotic process; and regulation of intrinsic apoptotic signaling pathway. Located in nucleus. Is active in mitochondrion. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26965](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26965) · Entrez [114971](https://www.ncbi.nlm.nih.gov/gene/114971) · UniProt [Q8WUK0](https://www.uniprot.org/uniprotkb/Q8WUK0) · Ensembl [ENSG00000110536](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110536)

## Data

Gene col 3147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3147); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3147]; `tensor/DDL_lfc|DDL_z.npy` [3147]; `embed/gene_vectors.npy` [3147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3147 or target_col == 3147). Every well: [[PTPMT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPMT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
