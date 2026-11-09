---
symbol: "MMACHC"
type: "gene"
col: 5367
ensembl_id: "ENSG00000132763"
name: "metabolism of cobalamin associated C"
location: "1p34.1"
module: 1
arm: "+"
pooled_cpm: 4.33
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# MMACHC

*metabolism of cobalamin associated C* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.06× (z +12.7, q 2e-34, up in 19 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.56× (z +5.1, q 4e-05, up in 14 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 6.70×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.776× (z -4.1, q 0.014, down in 16 of 38 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (A498 0.0895×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT6]] (+0.64, fdr 1e-05), [[OSGEPL1]] (+0.62, fdr 1e-05), [[METAP1D]] (+0.60, fdr 3e-05); moves opposite to [[TMEM184B]] (-0.49, fdr 6e-05), [[CCNYL1]] (-0.48, fdr 5e-05), [[CERS5]] (-0.48, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[KLRG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 6.70×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.06×** | +12.7 | 2e-34 | 19/22 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.79×** | +11.2 | 7e-27 | 5/6 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.0 | 2e-13 | 6/11 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.89×** | +7.2 | 6e-11 | 9/25 (NCI-H2030, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 4e-05 | 14/44 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.76×** | +4.6 | 4e-04 | 4/12 (LoVo, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +4.1 | 0.003 | 7/45 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +3.5 | 0.031 | 9/42 (LoVo, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5367.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Pemetrexed (drug)]] 5 µM in 1 line (A498 0.0895×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.776×** | -4.1 | 0.014 | 16/38 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.699×** | -4.1 | 0.014 | 15/44 (SW480, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -3.3 | 0.18 | 10/48 (HepG2/C3A, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5367. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.78 | 0 | 1 | — | [[Pemetrexed (drug)]] 5 µM 0.0895× (z -9.0) |
| [[LoVo (line)]] | wt | 5.00 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.70× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.89 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5367), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT6]] | +0.64 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[OSGEPL1]] | +0.62 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[METAP1D]] | +0.60 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[ZZZ3]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[N6AMT1]] | +0.57 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[USP24]] | +0.57 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[SLX4IP]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[COG8]] | +0.56 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[HGH1]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[DPH5]] | +0.55 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[UTP15]] | +0.55 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[PPIL1]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | -0.49 | -0.60 / -0.38 | both halves | 6e-05 |  |
| [[CCNYL1]] | -0.48 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[CERS5]] | -0.48 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[RELL1]] | -0.47 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[GUK1]] | -0.47 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[GNB2]] | -0.46 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[GDI1]] | -0.46 | -0.44 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLRG1]] | B | KLRG1 activity raises MMACHC's level | lines that do not express KLRG1 (8) vs lines expressing it (42) | 1.31× lower at baseline in the lines without KLRG1 | 0.042 | ⚠ within organs, on part of the lines; also absent: DUXAP10, CD226, DUXAP8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.563). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.3, 20.2); signed map (9.5, -40.2). **Vector** length 36.5, 3.39% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.9 | +5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.6 | +3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.2 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -1.2 |
|  | [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -0.9 | -2.2 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | metabolism of cobalamin associated C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:45,500,300-45,513,382 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564I122, cblC |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Reactome | 7 pathways, smallest: Cobalamin (Cbl) metabolism; Defects in cobalamin (B12) metabolism; Cobalamin (Cbl, vitamin B12) transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4U1](https://www.uniprot.org/uniprotkb/Q9Y4U1) (Cyanocobalamin reductase / alkylcobalamin dealkylase):

> Cobalamin (vitamin B12) cytosolic chaperone that catalyzes the reductive decyanation of cyanocob(III)alamin (cyanocobalamin, CNCbl) to yield cob(II)alamin and cyanide, using FAD or FMN as cofactors and NADPH as cosubstrate. Cyanocobalamin constitutes the inactive form of vitamin B12 introduced from the diet, and is converted into the active cofactors methylcobalamin (MeCbl) involved in methionine biosynthesis, and 5'-deoxyadenosylcobalamin (AdoCbl) involved in the TCA cycle. Forms a complex …

**Summary**, from NCBI Gene [25974](https://www.ncbi.nlm.nih.gov/gene/25974):

> The exact function of the protein encoded by this gene is not known, however, its C-terminal region shows similarity to TonB, a bacterial protein involved in energy transduction for cobalamin (vitamin B12) uptake. Hence, it is postulated that this protein may have a role in the binding and intracellular trafficking of cobalamin. Mutations in this gene are associated with methylmalonic aciduria and homocystinuria type cblC. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:24525](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24525) · Entrez [25974](https://www.ncbi.nlm.nih.gov/gene/25974) · UniProt [Q9Y4U1](https://www.uniprot.org/uniprotkb/Q9Y4U1) · Ensembl [ENSG00000132763](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132763)

## Data

Gene col 5367: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5367); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5367, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5367]; `tensor/DDL_lfc|DDL_z.npy` [5367]; `embed/gene_vectors.npy` [5367]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5367 or target_col == 5367). Every well: [[MMACHC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMACHC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
