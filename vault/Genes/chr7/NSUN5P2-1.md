---
symbol: "NSUN5P2-1"
type: "gene"
col: 16512
ensembl_id: "ENSG00000290831"
name: ""
location: ""
module: 24
arm: "+"
pooled_cpm: 2.46
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# NSUN5P2-1

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 3.45× (z +7.3, q 2e-10, up in 11 of 14 measured lines) ⚠ toxic. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NSUN5P1-1]] (+0.92, fdr 7e-06), [[SNHG19]] (+0.74, fdr 1e-05), [[SMIM26]] (+0.73, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[SNHG9]] (+0.70, fdr 1e-05); moves opposite to [[MOB1A]] (-0.72, fdr 1e-05), [[MAPRE1]] (-0.70, fdr 5e-05), [[AP2M1]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Omeprazole (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16512.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.45×** | +7.3 | 2e-10 | 11/14 (NCI-H2347, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.99×** | +6.7 | 5e-09 | 6/12 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.59×** | +5.6 | 4e-06 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.24×** | +4.6 | 7e-04 | 2/4 (SW1417, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | 2.62× | +3.2 | 0.12 | 3/21 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.67× | +3.2 | 0.12 | 5/28 (BT-474, LS 180, …) | top dose only | position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | 1.70× | +3.1 | 0.12 | 4/25 (LoVo, HEC-1-A, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | 1.66× | +3.1 | 0.12 | 10/37 (LoVo, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~30% of this change | 1.65× | +3.1 | 0.12 | 1/12 (HEC-1-A) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.65× | +3.1 | 0.12 | 11/42 (LoVo, HOP62, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 16512.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.575× | -3.4 | 0.28 | 8/43 (NCI-H1573, BT-474, …) | inconsistent across doses |  |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.559× | -3.3 | 0.28 | 4/43 (LS 180, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16512. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.954 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.855 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.862 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.950 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.27 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.806 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.73 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16512), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 11 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSUN5P1-1]] | +0.92 | +0.82 / +0.93 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.74 | +0.50 / +0.78 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | +0.73 | +0.60 / +0.71 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG9]] | +0.70 | +0.57 / +0.77 | both halves | 1e-05 |  |
| [[MINCR]] | +0.70 | +0.39 / +0.78 | both halves | 6e-05 |  |
| [[EPB41L4A-AS1]] | +0.68 | +0.56 / +0.70 | both halves | 1e-05 |  |
| [[SNHG7]] | +0.68 | +0.47 / +0.74 | both halves | 2e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.68 | +0.51 / +0.74 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MED10]] | +0.68 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[MRPL23]] | +0.67 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ZNF593]] | +0.67 | +0.57 / +0.68 | both halves | 8e-06 |  |
| [[SNHG8]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[CHCHD5]] | +0.65 | +0.38 / +0.63 | both halves | 6e-05 |  |
| [[UQCC3]] | +0.65 | +0.40 / +0.73 | both halves | 5e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MOB1A]] | -0.72 | -0.53 / -0.77 | both halves | 1e-05 |  |
| [[MAPRE1]] | -0.70 | -0.40 / -0.72 | both halves | 5e-05 |  |
| [[AP2M1]] | -0.70 | -0.59 / -0.69 | both halves | 7e-06 |  |
| [[TWF1]] | -0.68 | -0.43 / -0.74 | both halves | 3e-05 |  |
| [[TGOLN2]] | -0.68 | -0.63 / -0.74 | both halves | 7e-06 |  |
| [[LIN7C]] | -0.64 | -0.33 / -0.67 | both halves | 1e-04 |  |
| [[CAPRIN1]] | -0.63 | -0.37 / -0.68 | both halves | 8e-05 |  |
| [[TMX1]] | -0.63 | -0.58 / -0.61 | both halves | 8e-06 |  |
| [[TARDBP]] | -0.63 | -0.41 / -0.64 | both halves | 4e-05 |  |
| [[PSME3]] | -0.62 | -0.30 / -0.68 | both halves | 2e-04 |  |
| [[PIGT]] | -0.61 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[PGRMC1]] | -0.61 | -0.49 / -0.62 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Omeprazole (drug)]] 5 µM | C | NSUN5P2-1's natural level lowers the cells' numbers under Omeprazole 5 µM (makes them more sensitive) | NSUN5P2-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.73 | 0.181 over the table, 0.006 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[crizotinib (drug)]] 5 µM | C | NSUN5P2-1's natural level raises the cells' numbers under crizotinib 5 µM (protects the cells) | NSUN5P2-1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.71 | 0.250 over the table, 0.021 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.722). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-40.8, -21.4); signed map (-29.6, 6.1). **Vector** length 39.5, 5.21% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.8 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +1.5 | +2.7 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +2.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -2.4 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -2.8 |

## What is on record

> [!warning] No registry record
> NSUN5P2-1 has no HGNC entry matched to it: no approved name, no gene group, no cross-references. The quantification assigned reads to this identifier and that is what is known; nothing more is claimed.

## Data

Gene col 16512: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16512); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16512, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16512]; `tensor/DDL_lfc|DDL_z.npy` [16512]; `embed/gene_vectors.npy` [16512]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16512 or target_col == 16512). Every well: [[NSUN5P2-1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NSUN5P2-1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
