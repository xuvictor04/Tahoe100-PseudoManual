---
symbol: "IGF2BP2-AS1"
type: "gene"
col: 8808
ensembl_id: "ENSG00000163915"
name: "IGF2BP2 antisense RNA 1"
location: "3q27.2"
module: 21
arm: "+"
pooled_cpm: 2.56
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# IGF2BP2-AS1

*IGF2BP2 antisense RNA 1* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +7.7, q 1e-11, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.65× (z +4.5, q 7e-04, up in 11 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.831× (z -6.0, q 1e-06, down in 23 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.651× (z -3.9, q 0.030, down in 13 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0647×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.0779×); [[Allantoin (drug)]] 0.05 µM in 1 line (HOP62 0.0771×; ⚠ transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02755]] (+0.71, fdr 1e-05), [[EVI2B]] (+0.68, fdr 1e-05), [[AKAP13-AS1]] (+0.64, fdr 1e-05); moves opposite to [[ECHS1]] (-0.53, fdr 2e-04), [[SEPTIN7P14]] (-0.51, fdr 5e-04), [[PDHA1]] (-0.50, fdr 3e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC02742]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +7.7 | 1e-11 | 2/5 (NCI-H2347, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +6.1 | 3e-07 | 13/24 (HOP62, SW1417, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.5 | 7e-06 | 3/15 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.48×** | +5.0 | 1e-04 | 11/35 (NCI-H1573, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +4.5 | 7e-04 | 11/46 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.5 | 7e-04 | 9/34 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.9 | 0.007 | 5/21 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.54×** | +3.9 | 0.007 | 3/11 (LOX-IMVI, LoVo, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.028 | 1/33 (NCI-H2030) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.031 | 4/38 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.080 | 4/25 (Panc 03.27, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.1 | 0.083 | 9/39 (HepG2/C3A, SW1417, …) | rises with dose | cell-cycle shift (explains ~23% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8808.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0647×; ⚠ cell-cycle shift, explains ~41% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (SK-MEL-2 0.0779×); [[Allantoin (drug)]] 0.05 µM in 1 line (HOP62 0.0771×; ⚠ transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.831×** | -6.0 | 1e-06 | 23/47 (HOP62, Hs 766T, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.651×** | -3.9 | 0.030 | 13/43 (NCI-H2030, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.692× | -3.3 | 0.16 | 13/44 (LOX-IMVI, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.717× | -3.0 | 0.35 | 7/44 (RPMI-7951, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 6.26 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0647× (z -9.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0779× (z -9.0) |
| [[HOP62 (line)]] | alt | 2.85 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0771× (z -8.6) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.82 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.49 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02755]] | +0.71 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[EVI2B]] | +0.68 | +0.53 / +0.67 | both halves | 1e-05 |  |
| [[AKAP13-AS1]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 | same gene group |
| [[C12orf40]] | +0.64 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[SPATC1]] | +0.61 | +0.35 / +0.62 | both halves | 1e-04 |  |
| [[HPSE2]] | +0.61 | +0.46 / +0.54 | both halves | 2e-05 |  |
| [[PART1]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PRKCA-AS1]] | +0.60 | +0.44 / +0.64 | both halves | 3e-05 | same gene group |
| [[CTBP1-AS]] ⚠ | +0.60 | +0.49 / +0.61 | both halves | 1e-05 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[OMG]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[BIRC6-AS2-1]] | +0.59 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[OSCAR]] | +0.59 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[HVCN1]] | +0.58 | +0.43 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHS1]] | -0.53 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[SEPTIN7P14]] | -0.51 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[PDHA1]] | -0.50 | -0.28 / -0.48 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02742]] | B | LINC02742 activity raises IGF2BP2-AS1's level | lines that do not express LINC02742 (34) vs lines expressing it (16) | 1.31× lower at baseline in the lines without LINC02742 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000255029, ENSG00000254526, ENSG00000255227 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.579). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.0, 29.1); signed map (32.2, 9.0). **Vector** length 33.5, 2.98% of its response variance represented; |z| ≥ 3 in 885 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +2.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.6 | +5.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.2 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | IGF2BP2 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q27.2 — chr3:185,712,528-185,729,787 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ32900; previously C3orf65 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q96M15](https://www.uniprot.org/uniprotkb/Q96M15) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:32674](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32674) · Entrez [646600](https://www.ncbi.nlm.nih.gov/gene/646600) · UniProt [Q96M15](https://www.uniprot.org/uniprotkb/Q96M15) · Ensembl [ENSG00000163915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163915)

## Data

Gene col 8808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8808); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8808]; `tensor/DDL_lfc|DDL_z.npy` [8808]; `embed/gene_vectors.npy` [8808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8808 or target_col == 8808). Every well: [[IGF2BP2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF2BP2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
