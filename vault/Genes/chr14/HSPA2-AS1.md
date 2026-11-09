---
symbol: "HSPA2-AS1"
type: "gene"
col: 15170
ensembl_id: "ENSG00000259116"
name: "HSPA2 and ZBTB1 antisense RNA 1"
location: "14q23.3"
module: 21
arm: "+"
pooled_cpm: 4.6
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# HSPA2-AS1

*HSPA2 and ZBTB1 antisense RNA 1* — 14q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.84× (z +10.7, q 4e-24, up in 21 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.54× (z +6.3, q 6e-08, up in 26 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0908×; ⚠ transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (AsPC-1 0.0762×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (C32 0.0628×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.101×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.87, fdr 7e-06), [[ZRANB2-AS1]] (+0.86, fdr 7e-06), [[TTC36-AS1]] (+0.84, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HAND2-AS1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SETD9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15170.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +10.7 | 4e-24 | 21/26 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +8.2 | 8e-14 | 6/7 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.3 | 6e-08 | 26/40 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +6.2 | 6e-08 | 8/13 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +5.9 | 4e-07 | 18/33 (CFPAC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.48×** | +5.7 | 1e-06 | 14/39 (LoVo, SNU-423, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.9 | 8e-05 | 18/44 (SHP-77, SK-MEL-2, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.35× | +3.1 | 0.12 | 6/46 (LoVo, SW1417, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.35× | +3.1 | 0.12 | 7/38 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.36× | +3.1 | 0.12 | 7/31 (NCI-H2030, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15170.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 1 line (NCI-H23 0.0908×; ⚠ transcription drop); [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (AsPC-1 0.0762×); [[Triamcinolone (drug)]] 0.5 µM in 1 line (C32 0.0628×); [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (HEC-1-A 0.101×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.837× | -6.4 | 1e-07 | 28/48 (SNU-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 0.740× | -3.1 | 0.59 | 9/47 (SNU-1, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15170. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.66 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0762× (z -8.9) |
| [[C32 (line)]] | wt | 4.90 | 0 | 1 | — | [[Triamcinolone (drug)]] 0.5 µM 0.0628× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 4.31 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.101× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 6.91 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0908× (z -9.8) ⚠ transcription drop |
| [[A-172 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.15 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15170), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.87 | +0.81 / +0.80 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.86 | +0.74 / +0.88 | both halves | 7e-06 | same gene group |
| [[TTC36-AS1]] | +0.84 | +0.82 / +0.79 | both halves | 7e-06 | same gene group |
| [[FLJ40194]] | +0.84 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.83 | +0.78 / +0.77 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.83 | +0.74 / +0.83 | both halves | 7e-06 | same gene group |
| [[CNGB3]] | +0.82 | +0.74 / +0.82 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.82 | +0.77 / +0.80 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.82 | +0.74 / +0.83 | both halves | 7e-06 |  |
| [[EOGT-DT]] | +0.81 | +0.75 / +0.79 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.81 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.81 | +0.73 / +0.79 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HAND2-AS1]] | B | HAND2-AS1 activity raises HSPA2-AS1's level | lines that do not express HAND2-AS1 (20) vs lines expressing it (30) | 1.12× lower at baseline in the lines without HAND2-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: LINC02269, NPTX1, VAT1L; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SETD9]] | C | HSPA2-AS1's natural level weakens SETD9's drug response | HSPA2-AS1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.23; direction not clear | 0.073 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.904). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.3, 27.4); signed map (33.3, 5.0). **Vector** length 43.4, 4.62% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +3.9 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +6.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.3 | +3.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -6.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.0 | -0.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | HSPA2 and ZBTB1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q23.3 — chr14:64,513,952-64,540,368 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55433](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55433) · Entrez [102723809](https://www.ncbi.nlm.nih.gov/gene/102723809) · Ensembl [ENSG00000259116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259116)

## Data

Gene col 15170: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15170); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15170, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15170]; `tensor/DDL_lfc|DDL_z.npy` [15170]; `embed/gene_vectors.npy` [15170]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15170 or target_col == 15170). Every well: [[HSPA2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPA2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
