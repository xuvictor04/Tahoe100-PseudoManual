---
symbol: "RN7SL76P"
type: "gene"
col: 14294
ensembl_id: "ENSG00000241959"
name: "RNA, 7SL, cytoplasmic 76, pseudogene"
location: "7q36.1"
module: 39
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# RN7SL76P

*RNA, 7SL, cytoplasmic 76, pseudogene* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 1.91× (z +5.0, q 4e-04, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 1.61× (z +3.9, q 0.016, up in 7 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.527× (z -5.3, q 7e-05, down in 18 of 43 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.548× (z -4.8, q 4e-04, down in 20 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01909]] (+0.64, fdr 7e-06), [[LINC02803]] (+0.62, fdr 1e-05), [[EPHX3]] (+0.60, fdr 1e-05); moves opposite to [[MRPL39]] (-0.51, fdr 1e-05), [[LTA4H]] (-0.51, fdr 3e-05), [[MRI1]] (-0.47, fdr 5e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IMPG2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +5.0 | 4e-04 | 0/5 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.83×** | +4.8 | 5e-04 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.61×** | +3.9 | 0.016 | 7/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.00× | +3.0 | 0.38 | 0/6 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.527×** | -5.3 | 7e-05 | 18/43 (Panc 03.27, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.538×** | -5.1 | 9e-05 | 20/45 (AsPC-1, A498, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.548×** | -4.8 | 4e-04 | 20/37 (C32, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.565×** | -4.7 | 4e-04 | 16/45 (KATO III, H4, …) | top dose only | cell-cycle shift (explains ~12% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.599×** | -4.1 | 0.006 | 14/21 (HT-29, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.609×** | -3.9 | 0.008 | 16/33 (SW 900, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.623×** | -3.9 | 0.008 | 17/43 (Hs 766T, HT-29, …) | all doses, stronger at high dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.05 µM |  | **0.629×** | -3.5 | 0.030 | 7/40 (HepG2/C3A, SNU-423, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.670×** | -3.3 | 0.062 | 13/28 (AsPC-1, C32, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.691× | -3.0 | 0.12 | 8/44 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Cytarabine (drug)]] 5 µM |  | 0.682× | -3.0 | 0.12 | 10/38 (Panc 03.27, SHP-77, …) | top dose only | cell-cycle shift (explains ~19% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.21 | 0 | 2 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0626× (z -12.2) |
| [[AsPC-1 (line)]] | alt | 5.07 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0759× (z -8.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 2.66 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0637× (z -8.6) |
| [[HOP62 (line)]] | alt | 2.13 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0543× (z -8.7) |
| [[HT-29 (line)]] | alt | 5.94 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0697× (z -9.9) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 5.16 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0738× (z -9.3) |
| [[A-172 (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.887 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.84 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01909]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[LINC02803]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[EPHX3]] | +0.60 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[IL20RB]] | +0.59 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[FLACC1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[SYCE1L]] | +0.59 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[GARIN1A]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[ATP2A1]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CRK]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[C19orf38]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[PILRA]] | +0.56 | +0.41 / +0.56 | both halves | 4e-05 |  |
| [[C21orf91-OT1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL39]] | -0.51 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[MRI1]] | -0.47 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SDHAF3]] | -0.45 | -0.34 / -0.49 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IMPG2]] | C | IMPG2 activity lowers RN7SL76P's level | lines that do not express IMPG2 (4) vs lines expressing it (46) | 1.59× higher at baseline in the lines without IMPG2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, CLEC2D, LINC01341; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.513). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.2, -15.1); signed map (16.2, 8.3). **Vector** length 51.0, 6.51% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.0 | +2.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.4 | +0.9 |
|  | [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | +1.0 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -2.3 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -4.8 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -1.9 | -0.4 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | RNA, 7SL, cytoplasmic 76, pseudogene |
| Locus type | pseudogene |
| Location | 7q36.1 — chr7:151,464,650-151,464,938 (-) |
| Ensembl biotype | misc_RNA |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:46092](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:46092) · Entrez [106479251](https://www.ncbi.nlm.nih.gov/gene/106479251) · Ensembl [ENSG00000241959](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000241959)

## Data

Gene col 14294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14294); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14294]; `tensor/DDL_lfc|DDL_z.npy` [14294]; `embed/gene_vectors.npy` [14294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14294 or target_col == 14294). Every well: [[RN7SL76P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RN7SL76P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
