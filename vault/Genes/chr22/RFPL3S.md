---
symbol: "RFPL3S"
type: "gene"
col: 13018
ensembl_id: "ENSG00000205853"
name: "RFPL3 antisense"
location: "22q12.3"
module: 38
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# RFPL3S

*RFPL3 antisense* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.21× (z +14.7, q 0e+00, up in 32 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belumosudil (drug)]] 5 µM: 0.600× (z -4.4, q 0.005, down in 20 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0454×; ⚠ cell-cycle shift, would explain all of this change); [[Omeprazole (sodium) (drug)]] 5 µM in 1 line (HCT15 0.0414×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PILRA]] (+0.83, fdr 7e-06), [[SMIM41]] (+0.82, fdr 7e-06), [[ARL9]] (+0.82, fdr 7e-06).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.21×** | +14.7 | 0e+00 | 32/35 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.92×** | +9.6 | 3e-19 | 19/35 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.65×** | +8.3 | 1e-14 | 13/21 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +7.4 | 2e-11 | 20/37 (NCI-H23, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.26×** | +7.3 | 4e-11 | 28/45 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.41×** | +6.9 | 4e-10 | 22/38 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.23×** | +6.3 | 2e-08 | 14/46 (NCI-H1573, LoVo, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.94×** | +5.9 | 3e-07 | 21/45 (SHP-77, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.78×** | +5.1 | 2e-05 | 13/44 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **1.74×** | +4.9 | 4e-05 | 9/20 (HOP62, MIA PaCa-2, …) | rises with dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.74×** | +4.7 | 1e-04 | 10/31 (LoVo, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.73×** | +4.7 | 1e-04 | 1/2 (NCI-H2347) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +3.9 | 0.005 | 9/45 (A498, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.49×** | +3.5 | 0.017 | 5/33 (J82, SW480, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.53×** | +3.5 | 0.017 | 6/33 (LoVo, HepG2/C3A, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.55×** | +3.5 | 0.017 | 6/41 (LS 180, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.51×** | +3.3 | 0.036 | 2/42 (LOX-IMVI, LoVo) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.052 | 3/29 (BT-474, KATO III, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13018.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0454×; ⚠ cell-cycle shift, would explain all of this change); [[Omeprazole (sodium) (drug)]] 5 µM in 1 line (HCT15 0.0414×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.600×** | -4.4 | 0.005 | 20/39 (Hs 766T, NCI-H2030, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.683× | -3.5 | 0.15 | 9/44 (C32, KATO III, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 5.64 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +9.1) | [[Omeprazole (sodium) (drug)]] 5 µM 0.0414× (z -8.6) |
| [[LoVo (line)]] | wt | 8.22 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.60× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 8.23 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0454× (z -13.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 6.88 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +10.9) | — |
| [[A-172 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.02 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.29 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PILRA]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[SMIM41]] | +0.82 | +0.81 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ARL9]] | +0.82 | +0.86 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[COL20A1]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FNDC7]] | +0.80 | +0.86 / +0.74 | both halves | 7e-06 |  |
| [[VWCE]] | +0.80 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[TINCR]] | +0.80 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[PYGM]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HPX]] | +0.79 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[TTC36]] | +0.79 | +0.79 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[TMEM25]] | +0.78 | +0.75 / +0.75 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.78 | +0.76 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F2]] | B | F2 activity raises RFPL3S's level | lines that do not express F2 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without F2 | 0.067 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises RFPL3S's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without LINC00334 | 0.073 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.833). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.8, -18.3); signed map (14.7, 12.4). **Vector** length 68.0, 10.4% of its response variance represented; |z| ≥ 3 in 1,171 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +3.5 | +4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +14.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +2.4 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.9 | +1.4 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.5 | +0.9 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.0 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | +0.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.6 | -0.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.6 | -4.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.5 | -2.3 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.9 | -2.1 |
|  | [[Bexarotene (drug)]] 5 µM |  | -1.8 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | RFPL3 antisense |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 22q12.3 — chr22:32,359,886-32,382,106 (-) |
| Ensembl biotype | lncRNA |
| Also known as | RFPL3-AS, NCRNA00005; previously RFPL3-AS1 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

UniProt [P0C7P2](https://www.uniprot.org/uniprotkb/P0C7P2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:9981](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9981) · Entrez [10737](https://www.ncbi.nlm.nih.gov/gene/10737) · UniProt [P0C7P2](https://www.uniprot.org/uniprotkb/P0C7P2) · Ensembl [ENSG00000205853](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205853)

## Data

Gene col 13018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13018); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13018]; `tensor/DDL_lfc|DDL_z.npy` [13018]; `embed/gene_vectors.npy` [13018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13018 or target_col == 13018). Every well: [[RFPL3S — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RFPL3S.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
