---
symbol: "TIMM8B"
type: "gene"
col: 7462
ensembl_id: "ENSG00000150779"
name: "translocase of inner mitochondrial membrane 8 homolog B"
location: "11q23.1"
module: 7
arm: "+"
pooled_cpm: 8.88
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TIMM8B

*translocase of inner mitochondrial membrane 8 homolog B* — 11q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.38× (z +9.9, q 3e-20, up in 38 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (C-33 A 0.0654×); [[Folic acid (drug)]] 5 µM in 1 line (A-427 0.217×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJC30]] (+0.67, fdr 1e-05), [[PRR3]] (+0.64, fdr 4e-05), [[EXOC3-AS1]] (+0.64, fdr 7e-06); moves opposite to [[CTSK]] (-0.51, fdr 2e-05), [[DAP]] (-0.50, fdr 3e-05), [[ODF2]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.38×** | +9.9 | 3e-20 | 38/44 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **3.25×** | +9.5 | 5e-19 | 26/31 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.03×** | +8.6 | 2e-15 | 31/36 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.46×** | +6.7 | 3e-09 | 21/24 (SW480, PANC-1, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.37×** | +6.7 | 3e-09 | 13/15 (SNU-423, PANC-1, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.26×** | +6.6 | 5e-09 | 35/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.07×** | +5.9 | 3e-07 | 32/47 (KATO III, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.1 | 2e-05 | 25/48 (A-172, A498, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.82×** | +4.8 | 8e-05 | 26/46 (LS 180, SW480, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +3.8 | 0.007 | 22/43 (AsPC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.62×** | +3.7 | 0.010 | 21/45 (A-172, NCI-H1792, …) | two highest doses | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.023 | 15/47 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.36×** | +3.5 | 0.024 | 17/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +3.4 | 0.028 | 19/42 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.061 | 16/47 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7462.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM in 1 line (C-33 A 0.0654×); [[Folic acid (drug)]] 5 µM in 1 line (A-427 0.217×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Hydroxyurea (drug)]] 5 µM |  | 0.641× | -3.5 | 0.28 | 17/47 (SK-MEL-2, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 7.80 | 0 | 1 | — | [[Folic acid (drug)]] 5 µM 0.217× (z -8.7) |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0654× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 6.50 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.62× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | — |
| [[A-172 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.31 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.47 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.79 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJC30]] | +0.67 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[PRR3]] | +0.64 | +0.68 / +0.41 | both halves | 4e-05 |  |
| [[EXOC3-AS1]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[YTHDF2]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[MRPL20]] | +0.63 | +0.75 / +0.51 | both halves | 1e-05 | STRING 534 |
| [[MRPL44]] | +0.62 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[TMEM69]] | +0.61 | +0.66 / +0.44 | both halves | 3e-05 |  |
| [[OXLD1]] | +0.60 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[SCGB2B2]] | +0.59 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[DDX28]] | +0.59 | +0.65 / +0.44 | both halves | 3e-05 |  |
| [[UQCRFS1]] | +0.59 | +0.60 / +0.47 | both halves | 2e-05 | pathway: HALLMARK_OXIDATIVE_PHOSPHORYLATION |
| [[SMAD1]] | +0.57 | +0.67 / +0.27 | both halves | 3e-04 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSK]] | -0.51 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[DAP]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[ODF2]] | -0.49 | -0.66 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TIMM8B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.506). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.7, 9.0); signed map (-6.4, -29.3). **Vector** length 51.4, 8.37% of its response variance represented; |z| ≥ 3 in 643 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +5.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +3.5 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | +1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -0.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -3.5 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | translocase of inner mitochondrial membrane 8 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.1 — chr11:112,084,800-112,086,798 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TIM8B, DDP2, FLJ21744, MGC102866, MGC117373 |
| Hallmark sets | OXIDATIVE_PHOSPHORYLATION |
| Reactome | 2 pathways, smallest: Mitochondrial protein import; Protein localization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5J9](https://www.uniprot.org/uniprotkb/Q9Y5J9) (Mitochondrial import inner membrane translocase subunit Tim8 B):

> Probable mitochondrial intermembrane chaperone that participates in the import and insertion of some multi-pass transmembrane proteins into the mitochondrial inner membrane. Also required for the transfer of beta-barrel precursors from the TOM complex to the sorting and assembly machinery (SAM complex) of the outer membrane. Acts as a chaperone-like protein that protects the hydrophobic precursors from aggregation and guide them through the mitochondrial intermembrane space (By similarity).

**Summary**, from NCBI Gene [26521](https://www.ncbi.nlm.nih.gov/gene/26521):

> This gene encodes a member of a well-conserved family of proteins with similarity to yeast Tim mitochondrial import proteins. This gene is encoded by a nuclear gene and is transported into the intermembrane space of the mitochondrion. When formed into complexes, these proteins guide membrane-spanning proteins across the mitochondrial intermembrane space before they are added into the mitochondrial inner membrane. This gene is adjacent to succinate dehydrogenase, subunit D (SDHD), in which …

**Accessions** — [HGNC:11818](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11818) · Entrez [26521](https://www.ncbi.nlm.nih.gov/gene/26521) · UniProt [Q9Y5J9](https://www.uniprot.org/uniprotkb/Q9Y5J9) · Ensembl [ENSG00000150779](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150779)

## Data

Gene col 7462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7462); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7462]; `tensor/DDL_lfc|DDL_z.npy` [7462]; `embed/gene_vectors.npy` [7462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7462 or target_col == 7462). Every well: [[TIMM8B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIMM8B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
