---
symbol: "EXOC3-AS1"
type: "gene"
col: 13328
ensembl_id: "ENSG00000221990"
name: "EXOC3 antisense RNA 1"
location: "5p15.33"
module: 7
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# EXOC3-AS1

*EXOC3 antisense RNA 1* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 4.61× (z +9.3, q 8e-18, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 2.38× (z +8.1, q 2e-13, up in 28 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.818× (z -4.5, q 0.004, down in 24 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.526× (z -4.2, q 0.006, down in 19 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0637×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM44-AS1]] (+0.75, fdr 7e-06), [[DNAJC30]] (+0.72, fdr 7e-06), [[CLN8-AS1]] (+0.64, fdr 5e-05); moves opposite to [[DAZAP1]] (-0.50, fdr 4e-05), [[TBCD]] (-0.50, fdr 4e-05), [[TBC1D31]] (-0.49, fdr 8e-04, ⚠ one half only (not replicated)), [[TRAF7]] (-0.49, fdr 3e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF737]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13328.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.61×** | +9.3 | 8e-18 | 1/1 (PANC-1) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.38×** | +8.1 | 2e-13 | 28/45 (A-172, SW480, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +7.4 | 3e-11 | 16/29 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +7.1 | 1e-10 | 0/0 | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.88×** | +7.0 | 4e-10 | 7/12 (MIA PaCa-2, J82, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.19×** | +5.0 | 7e-05 | 7/12 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.03×** | +4.6 | 3e-04 | 16/35 (SW480, A-172, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.92×** | +4.1 | 0.003 | 16/41 (A549, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~24% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.021 | 7/30 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.68×** | +3.4 | 0.035 | 13/47 (A498, HOP62, …) | two highest doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +3.3 | 0.043 | 2/19 (A-427, A-172) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.58× | +3.0 | 0.11 | 1/11 (NCI-H2030) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~15% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13328.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Oxaprozin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0637×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.818×** | -4.5 | 0.004 | 24/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.526×** | -4.2 | 0.006 | 19/46 (A-427, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.530×** | -4.0 | 0.010 | 15/38 (CFPAC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13328. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 2.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 3.72 | 0 | 1 | — | [[Oxaprozin (drug)]] 0.05 µM 0.0637× (z -9.8) |
| [[A-172 (line)]] | wt | 2.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.914 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.686 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13328), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM44-AS1]] | +0.75 | +0.77 / +0.73 | both halves | 7e-06 | same gene group |
| [[DNAJC30]] | +0.72 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[CLN8-AS1]] | +0.64 | +0.40 / +0.73 | both halves | 5e-05 | same gene group |
| [[MED11]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[TIMM8B]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[MILIP]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | +0.62 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[SP2-DT]] | +0.62 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[DDX28]] | +0.61 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[C11orf1]] | +0.60 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[SNRPB2]] | +0.60 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ZNF407-AS1]] | +0.59 | +0.73 / +0.60 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAZAP1]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TBCD]] | -0.50 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[TBC1D31]] | -0.49 | -0.19 / -0.54 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TRAF7]] | -0.49 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[PRPS2]] | -0.49 | -0.47 / -0.35 | both halves | 1e-04 |  |
| [[ODF2]] | -0.48 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF737]] | B | ZNF737 activity raises EXOC3-AS1's level | lines that do not express ZNF737 (18) vs lines expressing it (32) | 1.40× lower at baseline in the lines without ZNF737 | 0.006 | ⚠ within organs, on part of the lines; also absent: ZNF85, ZNF66, ZNF90 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.461). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.9, 9.0); signed map (-5.2, -2.3). **Vector** length 38.3, 4.40% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.2 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +7.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.0 | +0.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.2 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.0 | -1.7 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | EXOC3 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p15.33 — chr5:441,498-443,160 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C5orf55 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q8N2X6](https://www.uniprot.org/uniprotkb/Q8N2X6) carries no function annotation.

**Summary**, from NCBI Gene [116349](https://www.ncbi.nlm.nih.gov/gene/116349):

> Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25175) · Entrez [116349](https://www.ncbi.nlm.nih.gov/gene/116349) · UniProt [Q8N2X6](https://www.uniprot.org/uniprotkb/Q8N2X6) · Ensembl [ENSG00000221990](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221990)

## Data

Gene col 13328: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13328); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13328, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13328]; `tensor/DDL_lfc|DDL_z.npy` [13328]; `embed/gene_vectors.npy` [13328]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13328 or target_col == 13328). Every well: [[EXOC3-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EXOC3-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
