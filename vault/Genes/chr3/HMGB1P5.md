---
symbol: "HMGB1P5"
type: "gene"
col: 5399
ensembl_id: "ENSG00000132967"
name: "high mobility group box 1 pseudogene 5"
location: "3p24.3"
module: 67
arm: "+"
pooled_cpm: 2.45
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/067", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# HMGB1P5

*high mobility group box 1 pseudogene 5* — 3p24.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.56× (z +11.5, q 1e-27, up in 10 of 10 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD4-AS1]] (+0.79, fdr 7e-06), [[CENPW]] (+0.70, fdr 7e-06), [[NUDT1]] (+0.69, fdr 1e-05); moves opposite to [[PCNP]] (-0.58, fdr 2e-05), [[PLPBP]] (-0.54, fdr 7e-05), [[SNHG29]] (-0.51, fdr 3e-05).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MIR924HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5399.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **5.56×** | +11.5 | 1e-27 | 10/10 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **5.37×** | +10.8 | 8e-25 | 2/3 (PANC-1, A498) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.85×** | +8.4 | 1e-14 | 4/4 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +5.1 | 5e-05 | 6/13 (J82, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.99×** | +4.6 | 5e-04 | 13/21 (NCI-H460, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **1.91×** | +4.3 | 0.001 | 5/12 (HT-29, A498, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.80×** | +3.9 | 0.007 | 12/46 (PANC-1, KATO III, …) | rises with dose | composition shift; position effect removed |
| [[Bendamustine (drug)]] 5 µM |  | 1.63× | +3.2 | 0.11 | 5/27 (C-33 A, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | 1.57× | +3.1 | 0.14 | 7/41 (KATO III, SW480, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5399.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.839× | -4.0 | 0.033 | 23/47 (HS-578T, HEC-1-A, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.591× | -3.2 | 0.36 | 9/45 (hTERT-HPNE, J82, …) | inconsistent across doses | position effect removed |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.629× | -3.1 | 0.41 | 3/44 (Panc 03.27, RKO, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5399. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.935 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.22 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5399), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD4-AS1]] | +0.79 | +0.74 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[CENPW]] | +0.70 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NUDT1]] | +0.69 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[PTMAP2]] ⚠ | +0.66 | +0.55 / +0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF5AL1]] | +0.64 | +0.48 / +0.70 | both halves | 2e-05 | **novel candidate** |
| [[TIMM10]] | +0.63 | +0.51 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[C9orf40]] | +0.63 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[SAPCD2]] | +0.60 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[HMGB1]] | +0.60 | +0.76 / +0.48 | both halves | 2e-05 |  |
| [[UBE2T]] | +0.59 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[GMNN]] | +0.59 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[FEN1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[KIF18B]] | +0.58 | +0.59 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNP]] | -0.58 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[PLPBP]] | -0.54 | -0.50 / -0.37 | both halves | 7e-05 |  |
| [[SNHG29]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CDC16]] | -0.49 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SRP72]] | -0.48 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[ZFAND1]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[TPP1]] | -0.48 | -0.32 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR924HG]] | B | MIR924HG activity lowers HMGB1P5's level | lines that do not express MIR924HG (8) vs lines expressing it (42) | 1.21× higher at baseline in the lines without MIR924HG | 0.094 | ⚠ within organs, on part of the lines; also absent: MIR193BHG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.560). A single-armed module: all its genes lie on one side of its main direction.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-31.4, -51.7); signed map (-43.5, -38.3). **Vector** length 34.6, 3.60% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.55 to 4); *Nucleosome assembly* (reactome, mean cos +0.55 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +2.1 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +0.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +0.8 | +1.9 |
|  | [[AZD-7648 (drug)]] 0.5 µM |  | +0.8 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.8 | +2.5 |
| fall | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -0.9 | -2.7 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group box 1 pseudogene 5 |
| Locus type | pseudogene |
| Location | 3p24.3 — chr3:22,381,819-22,382,460 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | ; previously HMG1L5, HMGB1L15, HMGB1P2, HMGB1L5 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:4997](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4997) · Entrez [10354](https://www.ncbi.nlm.nih.gov/gene/10354) · Ensembl [ENSG00000132967](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132967)

## Data

Gene col 5399: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5399); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5399, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5399]; `tensor/DDL_lfc|DDL_z.npy` [5399]; `embed/gene_vectors.npy` [5399]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5399 or target_col == 5399). Every well: [[HMGB1P5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGB1P5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
