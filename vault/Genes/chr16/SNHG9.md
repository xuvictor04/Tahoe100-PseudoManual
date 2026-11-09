---
symbol: "SNHG9"
type: "gene"
col: 14925
ensembl_id: "ENSG00000255198"
name: "small nucleolar RNA host gene 9"
location: "16p13.3"
module: 24
arm: "+"
pooled_cpm: 5.29
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SNHG9

*small nucleolar RNA host gene 9* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.32× (z +9.3, q 9e-18, up in 35 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 15.5×, KATO III 9.48×, AsPC-1 15.0×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNHG19]] (+0.86, fdr 7e-06), [[DCTN6-DT]] (+0.81, fdr 7e-06), [[TRIM52-AS1]] (+0.80, fdr 1e-05); moves opposite to [[API5]] (-0.75, fdr 7e-06), [[LIN7C]] (-0.73, fdr 4e-05), [[PRELID3B]] (-0.72, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA9]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 12 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14925.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (A549 15.5×, KATO III 9.48×, AsPC-1 15.0×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.32×** | +9.3 | 9e-18 | 35/37 (A549, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **9.35×** | +7.7 | 6e-12 | 25/25 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **4.33×** | +5.2 | 3e-05 | 30/34 (SW480, LS 180, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **6.12×** | +5.0 | 7e-05 | 22/24 (PANC-1, HEC-1-A, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **4.51×** | +5.0 | 8e-05 | 9/12 (PANC-1, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **3.84×** | +4.6 | 4e-04 | 5/8 (PANC-1, HS-578T, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.39×** | +4.4 | 9e-04 | 24/36 (LS 180, hTERT-HPNE, …) | rises with dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~37% of this change | **3.32×** | +4.1 | 0.003 | 22/29 (A-172, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **3.08×** | +4.0 | 0.004 | 32/44 (SW480, KATO III, …) | two highest doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~44% of this change | **2.92×** | +3.8 | 0.007 | 14/24 (PANC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **2.40×** | +3.1 | 0.092 | 24/46 (KATO III, SW480, …) | two highest doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 2.43× | +3.1 | 0.11 | 21/42 (A-172, LS 180, …) | top dose only | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | 2.32× | +3.0 | 0.11 | 22/46 (KATO III, LS 180, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.412× | -3.1 | 0.78 | 23/46 (HEC-1-A, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.74 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 4.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 3.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.0× (z +8.8) | — |
| [[KATO III (line)]] | alt | 7.69 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.48× (z +9.1) | — |
| [[A-172 (line)]] | wt | 8.15 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.61 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.02 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.25 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 13 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG19]] | +0.86 | +0.74 / +0.88 | both halves | 7e-06 | same gene group |
| [[DCTN6-DT]] | +0.81 | +0.62 / +0.86 | both halves | 7e-06 |  |
| [[TRIM52-AS1]] | +0.80 | +0.52 / +0.84 | both halves | 1e-05 |  |
| [[TMEM258]] | +0.77 | +0.58 / +0.79 | both halves | 8e-06 |  |
| [[SMIM27]] | +0.77 | +0.51 / +0.83 | both halves | 1e-05 |  |
| [[CSKMT]] | +0.74 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.74 | +0.63 / +0.77 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG25]] | +0.74 | +0.61 / +0.81 | both halves | 7e-06 | same gene group |
| [[LAMTOR5]] | +0.74 | +0.48 / +0.84 | both halves | 2e-05 |  |
| [[FBXL15]] | +0.73 | +0.54 / +0.80 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | +0.73 | +0.55 / +0.77 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[DNLZ]] | +0.73 | +0.49 / +0.75 | both halves | 1e-05 |  |
| [[APOC1]] | +0.73 | +0.50 / +0.75 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.73 | +0.50 / +0.82 | both halves | 1e-05 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[API5]] | -0.75 | -0.61 / -0.76 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.73 | -0.41 / -0.80 | both halves | 4e-05 |  |
| [[PRELID3B]] | -0.72 | -0.51 / -0.77 | both halves | 1e-05 |  |
| [[NONO]] | -0.70 | -0.50 / -0.78 | both halves | 1e-05 |  |
| [[STIP1]] | -0.69 | -0.62 / -0.71 | both halves | 7e-06 |  |
| [[PTPN11]] | -0.69 | -0.47 / -0.73 | both halves | 2e-05 |  |
| [[CCT7]] | -0.68 | -0.56 / -0.72 | both halves | 1e-05 |  |
| [[PDAP1]] | -0.67 | -0.44 / -0.71 | both halves | 3e-05 |  |
| [[NRAS]] | -0.67 | -0.50 / -0.72 | both halves | 1e-05 |  |
| [[CCT5]] | -0.67 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.67 | -0.40 / -0.76 | both halves | 5e-05 |  |
| [[PRKDC]] | -0.66 | -0.63 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA9]] | B | HOXA9 activity raises SNHG9's level | lines that do not express HOXA9 (31) vs lines expressing it (19) | 1.32× lower at baseline in the lines without HOXA9 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HOXA11, IGFL2-AS1, GPA33 |
| [[MIR4458HG]] | B | MIR4458HG activity lowers SNHG9's level | lines that do not express MIR4458HG (12) vs lines expressing it (38) | 1.30× higher at baseline in the lines without MIR4458HG | 0.090 | ⚠ within organs, on part of the lines; also absent: PDE3B, LINC02226 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.855). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-41.4, -21.6); signed map (-29.6, 7.9). **Vector** length 66.5, 18.3% of its response variance represented; |z| ≥ 3 in 570 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.51 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +9.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.0 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +2.8 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.8 | +2.1 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +1.7 | +1.9 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.0 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +0.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.8 | -2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.7 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 9 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.3 — chr16:1,964,895-1,965,509 (+) |
| Ensembl biotype | lncRNA |
| Also known as | DKFZp686N06141, NCRNA00062 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [735301](https://www.ncbi.nlm.nih.gov/gene/735301):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:33102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33102) · Entrez [735301](https://www.ncbi.nlm.nih.gov/gene/735301) · Ensembl [ENSG00000255198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255198)

## Data

Gene col 14925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14925); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14925]; `tensor/DDL_lfc|DDL_z.npy` [14925]; `embed/gene_vectors.npy` [14925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14925 or target_col == 14925). Every well: [[SNHG9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
