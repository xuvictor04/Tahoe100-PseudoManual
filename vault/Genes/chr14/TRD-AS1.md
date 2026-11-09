---
symbol: "TRD-AS1"
type: "gene"
col: 14727
ensembl_id: "ENSG00000251002"
name: "TRD antisense RNA 1"
location: "14q11.2"
module: 75
arm: "+"
pooled_cpm: 2.41
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# TRD-AS1

*TRD antisense RNA 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 10.0× (z +21.0, q 0e+00, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.89× (z +20.4, q 0e+00, up in 25 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0684×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYO18B]] (+0.67, fdr 7e-06), [[OPCML]] (+0.67, fdr 1e-05), [[GRM7]] (+0.67, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14727.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **10.0×** | +21.0 | 0e+00 | 10/10 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.89×** | +20.4 | 0e+00 | 25/28 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **9.13×** | +18.3 | 0e+00 | 4/5 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.53×** | +17.7 | 0e+00 | 4/4 (SW 900, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.34×** | +11.0 | 5e-26 | 21/31 (SW 900, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +9.6 | 9e-20 | 14/30 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.58×** | +8.6 | 6e-16 | 19/35 (BT-474, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.93×** | +8.4 | 2e-15 | 22/38 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.06×** | +6.7 | 2e-09 | 1/3 (SW 900) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **2.02×** | +6.4 | 9e-09 | 19/41 (SHP-77, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.92×** | +5.9 | 2e-07 | 12/30 (RPMI-7951, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.0 | 2e-05 | 2/17 (SW 900, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.4 | 5e-04 | 5/40 (HEC-1-A, A549, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.41×** | +4.2 | 0.001 | 8/33 (C32, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +4.1 | 0.002 | 6/38 (SHP-77, SNU-423, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.004 | 7/41 (NCI-H2347, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.012 | 5/29 (C32, A549, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.012 | 5/19 (HS-578T, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.39×** | +3.0 | 0.066 | 5/37 (SHP-77, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.43×** | +3.0 | 0.071 | 0/15 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14727.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Canagliflozin (drug)]] 0.05 µM in 1 line (HEC-1-A 0.0684×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trifluridine (drug)]] 0.5 µM |  | 0.688× | -3.4 | 0.35 | 10/34 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14727. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 19.4 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 24.9× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.38× (z +10.0) | — |
| [[CFPAC-1 (line)]] | alt | 3.77 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 19.5× (z +8.6) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 6.89 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0684× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 4.47 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 21.0× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 0.862 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.463 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.849 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.979 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.790 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.740 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.778 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.809 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.620 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.875 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.722 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.526 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 7.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.921 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14727), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYO18B]] | +0.67 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[OPCML]] | +0.67 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[GRM7]] | +0.67 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[DPP6]] | +0.67 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[HRG-AS1]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 | same gene group |
| [[CACNG2]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[CCDC170]] | +0.66 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[G2E3-AS1]] | +0.65 | +0.60 / +0.57 | both halves | 9e-06 | same gene group |
| [[SPATA21]] | +0.64 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[ZNF774]] | +0.64 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[SEC1P]] | +0.64 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[CLVS1]] | +0.64 | +0.45 / +0.67 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TRD-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNIP4]] | B | KCNIP4 activity raises TRD-AS1's level | lines that do not express KCNIP4 (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without KCNIP4 | 0.092 | ⚠ within organs, on part of the lines; also absent: MLLT3, TEX9, MAMDC2-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.7, 31.3); signed map (37.6, 7.8). **Vector** length 46.5, 6.40% of its response variance represented; |z| ≥ 3 in 912 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.5 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.3 | +18.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +20.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.8 | +21.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +4.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.6 | +2.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.6 | +1.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -2.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.1 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | TRD antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:22,197,446-22,484,462 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56197) · Entrez [105370401](https://www.ncbi.nlm.nih.gov/gene/105370401) · Ensembl [ENSG00000251002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000251002)

## Data

Gene col 14727: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14727); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14727, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14727]; `tensor/DDL_lfc|DDL_z.npy` [14727]; `embed/gene_vectors.npy` [14727]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14727 or target_col == 14727). Every well: [[TRD-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRD-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
