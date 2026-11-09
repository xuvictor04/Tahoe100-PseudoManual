---
symbol: "MOCS2-DT"
type: "gene"
col: 14505
ensembl_id: "ENSG00000247796"
name: "MOCS2 divergent transcript"
location: "5q11.2"
module: 39
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 8
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# MOCS2-DT

*MOCS2 divergent transcript* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.04× (z +7.1, q 6e-10, up in 1 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 0.05 µM: 2.37× (z +5.6, q 2e-06, up in 18 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.294× (z -8.4, q 2e-14, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPTBN5]] (+0.71, fdr 7e-06), [[PDE2A]] (+0.68, fdr 7e-06), [[MPP4]] (+0.68, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ITGA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14505.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.04×** | +7.1 | 6e-10 | 1/7 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.71×** | +6.6 | 1e-08 | 1/5 (HOP62) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **2.37×** | +5.6 | 2e-06 | 18/37 (NCI-H2347, A549, …) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **2.26×** | +5.6 | 2e-06 | 20/44 (HepG2/C3A, AsPC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +5.3 | 1e-05 | 2/14 (A498, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.73×** | +3.8 | 0.014 | 10/33 (A-172, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 1.39× | +3.2 | 0.10 | 8/40 (A-427, NCI-H2347, …) | top dose only | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14505.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.294×** | -8.4 | 2e-14 | 30/43 (HepG2/C3A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.313×** | -8.0 | 3e-13 | 26/37 (LoVo, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.364×** | -7.0 | 6e-10 | 22/36 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.501×** | -6.8 | 2e-09 | 19/29 (HepG2/C3A, AsPC-1, …) | top dose only | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.443×** | -5.6 | 2e-06 | 18/32 (NCI-H1573, SW480, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.541×** | -4.2 | 0.002 | 16/42 (HepG2/C3A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.554×** | -4.1 | 0.004 | 14/42 (A-427, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.575×** | -3.7 | 0.017 | 17/34 (AsPC-1, SW 900, …) | top dose only | composition shift; position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.673× | -3.1 | 0.13 | 14/40 (HepG2/C3A, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14505. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 50.6 | 0 | 21 (6 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.0209× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 8.36 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0449× (z -12.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.0210× (z -11.4) |
| [[NCI-H1573 (line)]] | alt | 5.52 | 0 | 2 (1 ⚠) | — | [[Budesonide (drug)]] 0.5 µM 0.0470× (z -8.7) |
| [[A-427 (line)]] | wt | 3.95 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 0.0756× (z -8.6) |
| [[LoVo (line)]] | wt | 5.54 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0372× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 1 | — | [[Resveratrol (drug)]] 0.5 µM 0.0726× (z -8.8) |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0352× (z -8.7) |
| [[A-172 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.868 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.08 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14505), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTBN5]] | +0.71 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[PDE2A]] | +0.68 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[MPP4]] | +0.68 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[XG]] | +0.67 | +0.57 / +0.72 | both halves | 8e-06 |  |
| [[AADAC]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[SELPLG]] | +0.65 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MSANTD1]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[TMEM236]] | +0.64 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[SLC22A13]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[HPX]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[OIT3]] | +0.63 | +0.53 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2]] | B | ITGA2 activity raises MOCS2-DT's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ITGA2 | 0.019 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[RAI14]] | B | RAI14 activity raises MOCS2-DT's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 1.89× lower at baseline in the lines without RAI14 | 0.044 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[SMCO2]] | B | SMCO2 activity raises MOCS2-DT's level | lines that do not express SMCO2 (9) vs lines expressing it (41) | 1.84× lower at baseline in the lines without SMCO2 | 0.089 | ⚠ within organs, on part of the lines; also absent: BMAL2, MIR31HG, ITGA2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.605). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.9, -13.4); signed map (17.7, 10.6). **Vector** length 79.9, 15.2% of its response variance represented; |z| ≥ 3 in 1,144 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.2 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.1 | +2.6 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.0 | -8.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.8 | -4.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.3 | -7.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -8.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.8 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -0.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | MOCS2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5q11.2 — chr5:53,109,816-53,127,673 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27417](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27417) · Entrez [257396](https://www.ncbi.nlm.nih.gov/gene/257396) · Ensembl [ENSG00000247796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000247796)

## Data

Gene col 14505: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14505); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14505, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14505]; `tensor/DDL_lfc|DDL_z.npy` [14505]; `embed/gene_vectors.npy` [14505]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14505 or target_col == 14505). Every well: [[MOCS2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MOCS2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
