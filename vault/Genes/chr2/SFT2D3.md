---
symbol: "SFT2D3"
type: "gene"
col: 10375
ensembl_id: "ENSG00000173349"
name: "SFT2 domain containing 3"
location: "2q14.3"
module: 7
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# SFT2D3

*SFT2 domain containing 3* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.28× (z +11.3, q 5e-27, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +9.4, q 1e-18, up in 14 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLPP6]] (+0.65, fdr 7e-06), [[DDX28]] (+0.63, fdr 7e-06), [[MRPL50]] (+0.62, fdr 2e-05); moves opposite to [[TTC3]] (-0.62, fdr 7e-05), [[ARL3]] (-0.59, fdr 4e-04), [[GFPT1]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10375.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.28×** | +11.3 | 5e-27 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +10.1 | 1e-21 | 0/1 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +9.4 | 1e-18 | 14/27 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.16×** | +7.9 | 3e-13 | 2/11 (HT-29, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +7.0 | 3e-10 | 5/43 (SW480, LoVo, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.6 | 4e-04 | 6/42 (PANC-1, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.6 | 4e-04 | 6/23 (KATO III, LS 180, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.4 | 7e-04 | 3/9 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.0 | 0.005 | 2/12 (A-427, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.66×** | +3.7 | 0.012 | 1/9 (A498) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +3.4 | 0.031 | 0/1 | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10375.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | 0.781× | -3.6 | 0.18 | 6/44 (HEC-1-A, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Rifaximin (drug)]] 0.5 µM |  | 0.745× | -3.0 | 0.69 | 6/41 (RPMI-7951, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10375. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.911 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10375), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLPP6]] | +0.65 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DDX28]] | +0.63 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[MRPL50]] | +0.62 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[HPS6]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TLCD3A]] | +0.62 | +0.34 / +0.53 | both halves | 1e-04 |  |
| [[ZNF629]] | +0.62 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[MRM1]] | +0.60 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZNF747]] | +0.60 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[YTHDF2]] | +0.60 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[TYSND1]] | +0.60 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[C6orf120]] | +0.60 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[TSC22D1]] | +0.60 | +0.52 / +0.36 | both halves | 9e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC3]] | -0.62 | -0.59 / -0.38 | both halves | 7e-05 |  |
| [[ARL3]] | -0.59 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[GFPT1]] | -0.58 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[TSC2]] | -0.56 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[SEC63]] | -0.56 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[COG6]] | -0.56 | -0.57 / -0.36 | both halves | 9e-05 | STRING 412 |
| [[USP48]] | -0.55 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[UBE2Q2P2]] | -0.54 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[SEPTIN2]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[NKTR]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[HEATR5B]] | -0.51 | -0.63 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[RNF187]] | -0.51 | -0.40 / -0.25 | both halves | 4e-04 |  |
| [[TUBE1]] | -0.51 | -0.45 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SFT2D3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[RPP25]] | B | RPP25 activity raises SFT2D3's level | lines that do not express RPP25 (14) vs lines expressing it (36) | 1.12× lower at baseline in the lines without RPP25 | 0.090 | ⚠ within organs, on part of the lines; also absent: ENSG00000229970, ODF3B, EPHA10 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.530). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-38.5, 17.7); signed map (-3.2, -26.5). **Vector** length 26.2, 1.79% of its response variance represented; |z| ≥ 3 in 998 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +9.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.9 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +11.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.3 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.8 | +1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.7 |
|  | [[Belzutifan (drug)]] 5 µM |  | +0.8 | +2.0 |
| fall | [[Artesunate (drug)]] 5 µM |  | -1.2 | -3.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -0.8 |
|  | [[Tomivosertib (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | SFT2 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:127,701,497-127,705,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5391 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q587I9](https://www.uniprot.org/uniprotkb/Q587I9) (Vesicle transport protein SFT2C):

> May be involved in fusion of retrograde transport vesicles derived from an endocytic compartment with the Golgi complex.

**Summary**, from NCBI Gene [84826](https://www.ncbi.nlm.nih.gov/gene/84826):

> Predicted to be involved in protein transport and vesicle-mediated transport. Predicted to be located in cytoplasm; endomembrane system; and membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28767](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28767) · Entrez [84826](https://www.ncbi.nlm.nih.gov/gene/84826) · UniProt [Q587I9](https://www.uniprot.org/uniprotkb/Q587I9) · Ensembl [ENSG00000173349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173349)

## Data

Gene col 10375: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10375); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10375, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10375]; `tensor/DDL_lfc|DDL_z.npy` [10375]; `embed/gene_vectors.npy` [10375]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10375 or target_col == 10375). Every well: [[SFT2D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFT2D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
