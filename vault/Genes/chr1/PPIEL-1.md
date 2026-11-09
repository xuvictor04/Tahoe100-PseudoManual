---
symbol: "PPIEL-1"
type: "gene"
col: 16595
ensembl_id: "ENSG00000291129"
name: ""
location: ""
module: 38
arm: "+"
pooled_cpm: 6.68
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PPIEL-1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.43× (z +12.4, q 3e-32, up in 32 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.643× (z -4.4, q 0.006, down in 20 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPIEL]] (+0.93, fdr 7e-06, ⚠ same locus), [[IDI2-AS1]] (+0.87, fdr 7e-06), [[TRIM72]] (+0.81, fdr 7e-06), [[FNDC7]] (+0.80, fdr 7e-06); moves opposite to [[USP30]] (-0.65, fdr 7e-06), [[PEX2]] (-0.65, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[SLC26A4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16595.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.43×** | +12.4 | 3e-32 | 32/41 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +11.3 | 3e-27 | 36/42 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.33×** | +10.0 | 4e-21 | 33/47 (LoVo, PANC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +8.3 | 2e-14 | 26/40 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.13×** | +7.1 | 1e-10 | 24/40 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.98×** | +6.4 | 1e-08 | 3/12 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~14% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **1.77×** | +5.6 | 2e-06 | 21/47 (LoVo, HOP62, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.8 | 1e-04 | 19/46 (HOP62, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +4.4 | 8e-04 | 22/44 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.002 | 9/39 (HCT15, SW480, …) | all doses, flat | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.0 | 0.003 | 18/42 (HT-29, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Naproxen (drug)]] 0.05 µM |  | **1.54×** | +3.9 | 0.004 | 15/42 (PANC-1, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.5 | 0.021 | 9/33 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.46×** | +3.5 | 0.021 | 6/44 (LoVo, A498, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -4.4 | 0.006 | 20/45 (LOX-IMVI, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.475×** | -3.9 | 0.030 | 16/43 (PANC-1, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.509×** | -3.5 | 0.083 | 12/37 (AsPC-1, C32, …) | top dose only | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 0.707× | -3.3 | 0.15 | 8/43 (PANC-1, SW48, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 8.73 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.116× (z -8.8) |
| [[C32 (line)]] | wt | 7.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +9.7) | — |
| [[HOP62 (line)]] | alt | 7.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +9.5) | — |
| [[Hs 766T (line)]] | wt | 3.46 | 0 | 1 | — | [[Roxadustat (drug)]] 0.5 µM 0.0603× (z -9.0) |
| [[HT-29 (line)]] | alt | 9.97 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[J82 (line)]] | alt | 7.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -10.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 5.91 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0877× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 3.79 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +8.8) | — |
| [[SW480 (line)]] | alt | 8.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.6) | — |
| [[A-172 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.81 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.49 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPIEL]] | +0.93 | +0.95 / +0.87 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[IDI2-AS1]] | +0.87 | +0.87 / +0.83 | both halves | 7e-06 |  |
| [[TRIM72]] | +0.81 | +0.82 / +0.74 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.80 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[PILRA]] | +0.79 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[GARIN1A]] | +0.79 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.78 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[MMP25]] | +0.76 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[C3orf20]] | +0.76 | +0.81 / +0.59 | both halves | 7e-06 |  |
| [[SLC2A9]] | +0.76 | +0.82 / +0.58 | both halves | 7e-06 |  |
| [[USP50]] | +0.76 | +0.81 / +0.58 | both halves | 7e-06 |  |
| [[ARL9]] | +0.75 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[PYGM]] | +0.74 | +0.72 / +0.75 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP30]] | -0.65 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[PEX2]] | -0.65 | -0.68 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC26A4]] | B | SLC26A4 activity raises PPIEL-1's level | lines that do not express SLC26A4 (7) vs lines expressing it (43) | 1.66× lower at baseline in the lines without SLC26A4 | 0.011 | ⚠ within organs, on part of the lines; also absent: HES4; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers PPIEL-1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IMPA1P1]] | B | IMPA1P1 activity raises PPIEL-1's level | lines that do not express IMPA1P1 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without IMPA1P1 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |
| [[KCNQ4]] | B | KCNQ4 activity raises PPIEL-1's level | lines that do not express KCNQ4 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without KCNQ4 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000248993; maybe low, not absent; its own permutation p |
| [[NABP1]] | C | NABP1 activity raises PPIEL-1's level | lines that do not express NABP1 (4) vs lines expressing it (46) | 1.77× lower at baseline in the lines without NABP1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, LACC1, NMI; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.0, -15.7); signed map (16.1, 9.8). **Vector** length 76.4, 12.8% of its response variance represented; |z| ≥ 3 in 1,239 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.9 | +12.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +11.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +1.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +1.7 |
| fall | [[Brivudine (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.2 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.0 | -2.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.0 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -1.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.4 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.3 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.0 | +0.1 |

## What is on record

> [!warning] No registry record
> PPIEL-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16595); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16595]; `tensor/DDL_lfc|DDL_z.npy` [16595]; `embed/gene_vectors.npy` [16595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16595 or target_col == 16595). Every well: [[PPIEL-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPIEL-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
