---
symbol: "TP73-AS1"
type: "gene"
col: 13588
ensembl_id: "ENSG00000227372"
name: "Gfo/Idh/MocA-like oxidoreductase domain containing 3, pseudogene"
location: "1p36.32"
module: 7
arm: "+"
pooled_cpm: 3.47
n_lines_expressing: 33
n_dd_up: 6
n_dd_down: 6
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# TP73-AS1

*Gfo/Idh/MocA-like oxidoreductase domain containing 3, pseudogene* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +5.6, q 1e-05, up in 1 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.53× (z +4.6, q 5e-04, up in 9 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.373× (z -10.7, q 3e-24, down in 18 of 24 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.487× (z -7.8, q 1e-12, down in 17 of 28 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF513]] (+0.57, fdr 1e-05), [[ARFRP1]] (+0.56, fdr 1e-05), [[ZNF512B]] (+0.55, fdr 1e-05); moves opposite to [[SLC25A27]] (-0.50, fdr 4e-04), [[LCORL]] (-0.47, fdr 2e-04), [[CRNDE]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[DMAP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13588.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +5.6 | 1e-05 | 1/6 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.3 | 3e-05 | 6/17 (HEC-1-A, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +4.6 | 5e-04 | 9/30 (Hs 766T, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.53×** | +4.6 | 5e-04 | 5/15 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.53×** | +4.6 | 5e-04 | 11/30 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.26×** | +3.5 | 0.044 | 5/29 (NCI-H1573, NCI-H23, …) | top dose only | low cells (technical?) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.34× | +3.2 | 0.11 | 4/24 (SHP-77, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.35× | +3.2 | 0.11 | 7/22 (NCI-H23, A549, …) | rises with dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13588.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.373×** | -10.7 | 3e-24 | 18/24 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.487×** | -7.8 | 1e-12 | 17/28 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -7.3 | 5e-11 | 16/30 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.555×** | -6.4 | 2e-08 | 16/29 (PANC-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.585×** | -5.8 | 8e-07 | 10/28 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.635×** | -4.9 | 9e-05 | 9/30 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13588. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.7 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.325× (z -8.7) |
| [[Hs 766T (line)]] | wt | 6.68 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0573× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Pemigatinib (drug)]] 0.05 µM 0.0647× (z -10.3) |
| [[NCI-H460 (line)]] | wt | 3.63 | 0 | 2 | — | [[Digitoxin (drug)]] 0.05 µM 0.0435× (z -13.8) |
| [[SHP-77 (line)]] | alt | 10.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0822× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.881 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.278 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.299 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.379 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.271 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.276 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.366 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.257 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.313 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.268 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.92 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.258 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.258 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13588), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF513]] | +0.57 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ARFRP1]] | +0.56 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[ZNF512B]] | +0.55 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[TAF1C]] | +0.54 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[ZNF772]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ZNF229]] | +0.53 | +0.58 / +0.36 | both halves | 9e-05 |  |
| [[LRRC14]] | +0.53 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[JMJD4]] | +0.53 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ASB6]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[DRG2]] | +0.51 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[FAM83H]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ZNF414]] | +0.51 | +0.50 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC25A27]] | -0.50 | -0.54 / -0.26 | both halves | 4e-04 |  |
| [[LCORL]] | -0.47 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[CRNDE]] | -0.45 | -0.42 / -0.34 | both halves | 1e-04 |  |
| [[OXR1]] | -0.44 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[CBX3]] | -0.44 | -0.39 / -0.41 | both halves | 5e-05 |  |
| [[ARHGAP19]] | -0.44 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[ZNRF2]] | -0.43 | -0.39 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DMAP1]] | B | TP73-AS1 activity raises DMAP1's level | lines that do not express TP73-AS1 (17) vs lines expressing it (33) | 1.16× lower at baseline in the lines without TP73-AS1 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000176593, ZNF606, GAMT; its own permutation p |
| [[KTI12]] | B | TP73-AS1 activity lowers KTI12's level | lines that do not express TP73-AS1 (17) vs lines expressing it (33) | 1.00× higher at baseline in the lines without TP73-AS1 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: ENSG00000176593, ZNF606, GAMT |

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.489). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-47.9, -1.5); signed map (-7.7, -31.5). **Vector** length 32.2, 3.75% of its response variance represented; |z| ≥ 3 in 640 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.0 | +5.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +0.4 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.3 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +1.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +0.9 | +1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.9 | +2.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -6.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.8 | -10.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -7.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -0.8 | -0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.7 | -0.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -0.7 | -1.2 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | Gfo/Idh/MocA-like oxidoreductase domain containing 3, pseudogene |
| Locus type | pseudogene |
| Location | 1p36.32 — chr1:3,738,434-3,746,742 (-) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | PDAM; previously KIAA0495, TP73-AS1 |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:29052](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29052) · Entrez [57212](https://www.ncbi.nlm.nih.gov/gene/57212) · Ensembl [ENSG00000227372](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227372)

## Data

Gene col 13588: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13588); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13588, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13588]; `tensor/DDL_lfc|DDL_z.npy` [13588]; `embed/gene_vectors.npy` [13588]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13588 or target_col == 13588). Every well: [[TP73-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TP73-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
