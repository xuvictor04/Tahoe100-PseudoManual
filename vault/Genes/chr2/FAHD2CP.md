---
symbol: "FAHD2CP"
type: "gene"
col: 13802
ensembl_id: "ENSG00000231584"
name: "fumarylacetoacetate hydrolase domain containing 2C, pseudogene"
location: "2q11.2"
module: 38
arm: "+"
pooled_cpm: 2.86
n_lines_expressing: 48
n_dd_up: 5
n_dd_down: 8
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# FAHD2CP

*fumarylacetoacetate hydrolase domain containing 2C, pseudogene* — 2q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.24× (z +6.4, q 7e-08, up in 26 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.485× (z -5.8, q 5e-06, down in 19 of 45 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.509× (z -5.4, q 2e-05, down in 17 of 37 measured lines).
> Its strongest partners by |cos| (76 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 24 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RBM45]] (+0.56, fdr 1e-05), [[FAHD2B]] (+0.52, fdr 5e-05), [[ECHDC3]] (+0.50, fdr 5e-05); moves opposite to [[POLG2]] (-0.52, fdr 4e-04), [[PIK3R3]] (-0.51, fdr 4e-04), [[FGF18]] (-0.51, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +6.4 | 7e-08 | 26/45 (HOP62, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.82×** | +4.8 | 5e-04 | 13/41 (SW 900, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +4.2 | 0.004 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.67×** | +4.1 | 0.006 | 18/42 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +3.4 | 0.086 | 4/43 (SK-MEL-2, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.485×** | -5.8 | 5e-06 | 19/45 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.509×** | -5.4 | 2e-05 | 17/37 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.301×** | -5.0 | 1e-04 | 18/36 (NCI-H460, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.599×** | -4.1 | 0.007 | 16/40 (NCI-H1792, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.621×** | -3.8 | 0.018 | 14/26 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.653×** | -3.4 | 0.062 | 10/45 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.655×** | -3.4 | 0.062 | 6/42 (SW48, HT-29, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.2 | 0.087 | 16/46 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | **0.658×** | -3.2 | 0.087 | 15/22 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 0.677× | -3.1 | 0.11 | 9/37 (LoVo, C32, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.673× | -3.0 | 0.13 | 5/43 (SW 1271, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.56 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 3.90 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0483× (z -9.9) |
| [[NCI-H460 (line)]] | wt | 3.49 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0719× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[SW480 (line)]] | alt | 3.90 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0603× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[A-172 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.35 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.83 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.299 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.658 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.767 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBM45]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FAHD2B]] | +0.52 | +0.57 / +0.39 | both halves | 5e-05 |  |
| [[ECHDC3]] | +0.50 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[MIOS]] | +0.49 | +0.38 / +0.58 | both halves | 7e-05 |  |
| [[OCRL]] | +0.48 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[TTC12]] | +0.48 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[TMEM242]] | +0.48 | +0.22 / +0.54 | both halves | 6e-04 |  |
| [[TOP3B]] | +0.47 | +0.30 / +0.56 | both halves | 2e-04 |  |
| [[ANXA7]] | +0.46 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[MOCS1]] | +0.46 | +0.18 / +0.52 | ⚠ one half (not replicated) | 9e-04 |  |
| [[BPHL]] | +0.45 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[TMEM209]] | +0.44 | +0.30 / +0.53 | both halves | 2e-04 |  |
| [[TMEM177]] | +0.44 | +0.42 / +0.43 | both halves | 4e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 23 of them with an alert (⚠; 23 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLG2]] | -0.52 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[PIK3R3]] | -0.51 | -0.25 / -0.35 | both halves | 4e-04 |  |
| [[FGF18]] | -0.51 | -0.31 / -0.49 | both halves | 2e-04 |  |
| [[TRIM72]] | -0.50 | -0.25 / -0.54 | both halves | 4e-04 |  |
| [[PTPN22]] | -0.50 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[LDHC]] | -0.49 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[KLHL15]] | -0.47 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[TLE4]] | -0.47 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[PTPN6]] | -0.47 | -0.20 / -0.47 | ⚠ not reproduced | 7e-04 |  |
| [[BCL2L14]] | -0.46 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[LRRC23]] | -0.46 | -0.24 / -0.47 | both halves | 5e-04 |  |
| [[VWCE]] | -0.46 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[DISC1]] | -0.45 | -0.22 / -0.47 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers FAHD2CP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CCDC113]] | C | CCDC113 activity raises FAHD2CP's level | lines that do not express CCDC113 (3) vs lines expressing it (47) | 1.79× lower at baseline in the lines without CCDC113 | 0.074 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DNMT3B, DBNDD1, SPDL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction -0.418). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.2, -24.1); signed map (-6.0, -34.0). **Vector** length 40.5, 4.37% of its response variance represented; |z| ≥ 3 in 1,004 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.0 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +0.9 | +1.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +0.8 | +0.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | +0.7 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.7 | -0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +0.7 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +0.6 | -0.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.6 | +0.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | fumarylacetoacetate hydrolase domain containing 2C, pseudogene |
| Locus type | pseudogene |
| Location | 2q11.2 — chr2:96,013,730-96,021,608 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:44135](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44135) · Entrez [729234](https://www.ncbi.nlm.nih.gov/gene/729234) · Ensembl [ENSG00000231584](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231584)

## Data

Gene col 13802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13802); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13802]; `tensor/DDL_lfc|DDL_z.npy` [13802]; `embed/gene_vectors.npy` [13802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13802 or target_col == 13802). Every well: [[FAHD2CP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAHD2CP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
