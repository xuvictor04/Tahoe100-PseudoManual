---
symbol: "DMXL1-DT"
type: "gene"
col: 14618
ensembl_id: "ENSG00000249494"
name: "DMXL1 divergent transcript"
location: "5q23.1"
module: 23
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 3
n_dd_up_clean: 28
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# DMXL1-DT

*DMXL1 divergent transcript* — 5q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.16× (z +13.5, q 8e-39, up in 31 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.579× (z -4.5, q 0.003, down in 17 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0771×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSMCE1-DT]] (+0.71, fdr 7e-06), [[HSPA2-AS1]] (+0.70, fdr 7e-06), [[UGDH-AS1]] (+0.69, fdr 7e-06); moves opposite to [[APEX2]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14618.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +13.5 | 8e-39 | 31/32 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.53×** | +10.1 | 2e-21 | 3/3 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.96×** | +9.0 | 4e-17 | 31/40 (LoVo, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.99×** | +8.4 | 5e-15 | 1/5 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.8 | 1e-12 | 5/9 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.28×** | +6.8 | 8e-10 | 24/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +6.3 | 3e-08 | 14/38 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +6.2 | 3e-08 | 13/45 (A-427, NCI-H1573, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +5.8 | 4e-07 | 14/29 (HS-578T, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.01×** | +5.8 | 4e-07 | 22/45 (MIA PaCa-2, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.01×** | +5.8 | 4e-07 | 24/45 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.99×** | +5.7 | 5e-07 | 22/45 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.89×** | +5.3 | 6e-06 | 16/46 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +5.0 | 2e-05 | 14/46 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.5 | 3e-04 | 13/46 (A-172, HOP62, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.45×** | +4.2 | 1e-03 | 13/46 (MIA PaCa-2, A498, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.1 | 0.001 | 13/34 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 5/47 (A498, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14618.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Imiquimod (maleate) (drug)]] 5 µM in 1 line (A498 0.0771×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.579×** | -4.5 | 0.003 | 17/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.628×** | -3.9 | 0.032 | 20/47 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -3.7 | 0.048 | 14/41 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.671× | -3.3 | 0.13 | 14/46 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Cytarabine (drug)]] 5 µM |  | 0.682× | -3.1 | 0.25 | 6/41 (SNU-1, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14618. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.39 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0771× (z -9.0) |
| [[LoVo (line)]] | wt | 4.24 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +10.3) | — |
| [[A-172 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.83 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14618), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMCE1-DT]] | +0.71 | +0.74 / +0.71 | both halves | 7e-06 | same gene group |
| [[HSPA2-AS1]] | +0.70 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[UGDH-AS1]] | +0.69 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[CFAP43]] | +0.68 | +0.71 / +0.66 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.68 | +0.77 / +0.68 | both halves | 7e-06 |  |
| [[TAGAP-AS1]] | +0.68 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[CD72]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[OXA1L-DT]] | +0.68 | +0.75 / +0.68 | both halves | 7e-06 | same gene group |
| [[ANKHD1-DT]] | +0.68 | +0.74 / +0.65 | both halves | 7e-06 | same gene group |
| [[ZNF236-DT]] | +0.67 | +0.61 / +0.57 | both halves | 1e-05 | same gene group |
| [[APPBP2-DT]] | +0.67 | +0.77 / +0.57 | both halves | 9e-06 | same gene group |
| [[DNAJC27-AS1]] | +0.67 | +0.79 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APEX2]] | -0.58 | -0.46 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DMXL1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.614). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.7, 20.8); signed map (31.2, -6.9). **Vector** length 51.7, 6.99% of its response variance represented; |z| ≥ 3 in 1,036 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.8 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +13.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.1 | +6.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +5.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.4 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.3 | +5.8 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.3 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +1.2 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.1 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | DMXL1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q23.1 — chr5:119,006,347-119,070,902 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55568](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55568) · Entrez [105379143](https://www.ncbi.nlm.nih.gov/gene/105379143) · Ensembl [ENSG00000249494](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249494)

## Data

Gene col 14618: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14618); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14618, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14618]; `tensor/DDL_lfc|DDL_z.npy` [14618]; `embed/gene_vectors.npy` [14618]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14618 or target_col == 14618). Every well: [[DMXL1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMXL1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
