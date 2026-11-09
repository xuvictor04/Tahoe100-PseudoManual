---
symbol: "ARF4-AS1"
type: "gene"
col: 15710
ensembl_id: "ENSG00000272146"
name: "ARF4 antisense RNA 1"
location: "3p14.3"
module: 53
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# ARF4-AS1

*ARF4 antisense RNA 1* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.72× (z +14.1, q 4e-42, up in 9 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +10.3, q 1e-22, up in 19 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.883× (z -4.1, q 0.016, down in 14 of 45 measured lines) ⚠ position not correctable. The strongest without an alert is [[Ponatinib (drug)]] 0.5 µM: 0.640× (z -4.0, q 0.016, down in 9 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA2012]] (+0.60, fdr 1e-05), [[GP6]] (+0.60, fdr 7e-06), [[RALY-AS1]] (+0.60, fdr 2e-05); moves opposite to [[PKD2]] (-0.49, fdr 1e-04), [[KAT6A]] (-0.49, fdr 4e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SNAI1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15710.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.72×** | +14.1 | 4e-42 | 9/9 (SW480, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.22×** | +13.8 | 4e-41 | 3/3 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.52×** | +11.0 | 1e-25 | 1/1 (NCI-H2347) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +10.3 | 1e-22 | 19/30 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.96×** | +8.6 | 8e-16 | 19/32 (AsPC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.70×** | +6.8 | 1e-09 | 12/43 (NCI-H2347, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +4.8 | 1e-04 | 7/35 (HEC-1-A, Panc 03.27, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.8 | 1e-04 | 2/12 (SHP-77, LoVo) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.54×** | +3.9 | 0.006 | 11/41 (NCI-H2347, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.006 | 4/28 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.007 | 10/42 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +3.7 | 0.010 | 13/45 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.071 | 4/22 (AsPC-1, C32, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.93×** | +3.1 | 0.072 | 1/11 (PANC-1) | top dose only | noisy plate (z scaled); position effect removed |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +3.1 | 0.075 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.078 | 4/42 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~12% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15710.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.883× | -4.1 | 0.016 | 14/45 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.640×** | -4.0 | 0.016 | 9/38 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 5 µM |  | 0.763× | -3.5 | 0.11 | 9/44 (H4, RPMI-7951, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15710. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.920 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15710), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA2012]] | +0.60 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[GP6]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[RALY-AS1]] | +0.60 | +0.47 / +0.67 | both halves | 2e-05 | same gene group |
| [[MIR9-1HG]] | +0.60 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ARF4]] | +0.59 | +0.59 / +0.57 | both halves | 9e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[CPNE9]] | +0.59 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CD200R1]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[LINC02901]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[SMIM41]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[GRIK5]] | +0.56 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[CNBD2]] | +0.56 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[TAF13]] | +0.56 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[GTF2IP14]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKD2]] | -0.49 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[KAT6A]] | -0.49 | -0.46 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SNAI1]] | B | SNAI1 activity raises ARF4-AS1's level | lines that do not express SNAI1 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without SNAI1 | 0.037 | ⚠ within organs, on part of the lines; also absent: TNFSF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.0, -18.1); signed map (13.6, 14.3). **Vector** length 41.2, 4.56% of its response variance represented; |z| ≥ 3 in 930 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +14.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | +4.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.0 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.8 | +1.2 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +0.7 | +1.0 |
|  | [[SBI-0640756 (drug)]] 5 µM |  | +0.7 | +0.5 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.5 | -1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.4 | +0.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.1 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.1 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | ARF4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p14.3 — chr3:57,597,531-57,600,927 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51593](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51593) · Entrez [106144532](https://www.ncbi.nlm.nih.gov/gene/106144532) · Ensembl [ENSG00000272146](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272146)

## Data

Gene col 15710: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15710); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15710, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15710]; `tensor/DDL_lfc|DDL_z.npy` [15710]; `embed/gene_vectors.npy` [15710]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15710 or target_col == 15710). Every well: [[ARF4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARF4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
