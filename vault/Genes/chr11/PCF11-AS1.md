---
symbol: "PCF11-AS1"
type: "gene"
col: 15643
ensembl_id: "ENSG00000269939"
name: "PCF11 antisense RNA 1"
location: "11q14.1"
module: 15
arm: "+"
pooled_cpm: 2.11
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PCF11-AS1

*PCF11 antisense RNA 1* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.64× (z +12.3, q 3e-32, up in 25 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD42-DT]] (+0.82, fdr 7e-06, ⚠ read-through risk), [[EIF3J-DT]] (+0.76, fdr 7e-06), [[FBXO28]] (+0.71, fdr 1e-05), [[URM1]] (+0.71, fdr 1e-05); moves opposite to [[SSX2IP]] (-0.68, fdr 7e-06), [[SSRP1]] (-0.65, fdr 1e-05), [[LMNB2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.64×** | +12.3 | 3e-32 | 25/30 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.74×** | +8.7 | 9e-16 | 9/12 (NCI-H2347, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +6.7 | 4e-09 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +5.1 | 4e-05 | 10/44 (HEC-1-A, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +5.0 | 7e-05 | 12/39 (SHP-77, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +4.9 | 7e-05 | 9/26 (HS-578T, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.3 | 0.002 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +3.8 | 0.009 | 6/31 (SW 900, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.017 | 4/44 (HEC-1-A, A498, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.48×** | +3.5 | 0.024 | 5/38 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.2 | 0.069 | 1/11 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.64×** | +3.2 | 0.071 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.91× | +3.0 | 0.11 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clofarabine (drug)]] 0.5 µM |  | 0.704× | -3.2 | 0.86 | 7/42 (NCI-H1573, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.958 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD42-DT]] | +0.82 | +0.76 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 0.0 kb 3′ of ANKRD42-DT on the same strand (can correlate by spillover, not regulation) |
| [[EIF3J-DT]] | +0.76 | +0.59 / +0.72 | both halves | 7e-06 |  |
| [[FBXO28]] | +0.71 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[URM1]] | +0.71 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB8OS]] | +0.69 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[USP34-DT]] | +0.68 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SPATA1]] | +0.68 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[RSL1D1-DT]] | +0.67 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[OOEP]] | +0.67 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[ZNF529-AS1]] | +0.66 | +0.55 / +0.57 | both halves | 1e-05 | same gene group |
| [[C2CD5-AS1]] | +0.66 | +0.55 / +0.51 | both halves | 1e-05 | same gene group |
| [[DENND6A-AS1]] | +0.65 | +0.46 / +0.51 | both halves | 3e-05 | same gene group |
| [[SMIM27]] | +0.65 | +0.51 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | -0.68 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[SSRP1]] | -0.65 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.62 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[PHF6]] | -0.61 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[DNMT1]] | -0.61 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MTHFD1]] | -0.60 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[CS]] | -0.60 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[PDHA1]] | -0.59 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ATP5F1A]] | -0.59 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[ICMT]] | -0.59 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[TRAF7]] | -0.58 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[G3BP1]] | -0.58 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PCF11-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.0, 24.2); signed map (-0.4, -1.6). **Vector** length 38.6, 3.88% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +12.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.0 | +8.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.9 | +5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +1.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.8 | +0.3 |
|  | [[Rapamycin (drug)]] 0.05 µM |  | +0.7 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -1.8 | -2.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -0.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.0 | -0.4 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.8 | -1.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -0.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | PCF11 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q14.1 — chr11:83,185,521-83,187,036 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ENST00000602322.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52263) · Entrez [106736475](https://www.ncbi.nlm.nih.gov/gene/106736475) · Ensembl [ENSG00000269939](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269939)

## Data

Gene col 15643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15643); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15643]; `tensor/DDL_lfc|DDL_z.npy` [15643]; `embed/gene_vectors.npy` [15643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15643 or target_col == 15643). Every well: [[PCF11-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCF11-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
