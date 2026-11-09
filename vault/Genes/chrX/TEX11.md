---
symbol: "TEX11"
type: "gene"
col: 4186
ensembl_id: "ENSG00000120498"
name: "testis expressed 11"
location: "Xq13.1"
module: 166
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 0
n_dd_up_clean: 28
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# TEX11

*testis expressed 11* — Xq13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.92× (z +16.1, q 0e+00, up in 12 of 15 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0972×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.269×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PTPRT]] (+0.77, fdr 2e-05), [[PWRN1]] (+0.73, fdr 1e-05), [[HPSE2]] (+0.73, fdr 7e-06).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4186.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.92×** | +16.1 | 0e+00 | 12/15 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.81×** | +14.1 | 1e-42 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.28×** | +12.1 | 2e-31 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.12×** | +10.9 | 2e-25 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **8.35×** | +9.2 | 3e-18 | 14/25 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.16×** | +9.1 | 1e-17 | 8/24 (C32, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **7.55×** | +8.8 | 1e-16 | 8/10 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.68×** | +8.2 | 2e-14 | 16/26 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +5.6 | 2e-06 | 9/35 (A498, RPMI-7951, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +5.4 | 3e-06 | 2/21 (A549, SW480) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.46×** | +5.4 | 3e-06 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.8 | 7e-05 | 0/4 | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +4.8 | 7e-05 | 2/8 (PANC-1, NCI-H460) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +4.4 | 5e-04 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.44×** | +4.3 | 6e-04 | 1/27 (NCI-H460) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 2/36 (HEC-1-A, SW480) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.004 | 0/36 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.87×** | +3.7 | 0.005 | 1/10 (SW480) | all doses, stronger at high dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.005 | 1/19 (SW480) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.026 | 1/21 (A498) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.034 | 6/40 (C-33 A, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4186.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.0972×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 0.269×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | 0.666× | -3.4 | 0.40 | 7/19 (A-172, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4186. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 50.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0972× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.269× (z -8.5) |
| [[A-172 (line)]] | wt | 0.857 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.576 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.673 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.918 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.630 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.643 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.712 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.779 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.658 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.725 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.729 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.827 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.875 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.679 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.960 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.782 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.652 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.626 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.998 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.647 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.697 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.732 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.686 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.567 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.604 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.655 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.819 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.793 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.748 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.726 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.653 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.692 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.677 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4186), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRT]] | +0.77 | +0.47 / +0.77 | both halves | 2e-05 |  |
| [[PWRN1]] | +0.73 | +0.50 / +0.74 | both halves | 1e-05 |  |
| [[HPSE2]] | +0.73 | +0.59 / +0.73 | both halves | 7e-06 |  |
| [[OBI1-AS1]] | +0.72 | +0.55 / +0.75 | both halves | 1e-05 |  |
| [[PKP4-AS1]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[USH2A]] | +0.71 | +0.54 / +0.73 | both halves | 1e-05 |  |
| [[SLC27A6]] | +0.70 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[A2ML1-AS1]] | +0.70 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[HRG-AS1]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[UBOX5-AS1]] | +0.69 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.69 | +0.55 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TEX11's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.0% of all compounds | 0.089 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MGC4859]] | C | MGC4859's natural level weakens TEX11's drug response | MGC4859's natural level across 32 lines (lineage-adjusted; a glimpse) | r -0.80, reverse -0.63; direction not clear | 0.050 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.702). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, 29.1); signed map (32.0, 11.6). **Vector** length 23.1, 2.06% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +16.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.2 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +14.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +10.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +8.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +4.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.9 |
| fall | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.7 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.7 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq13.1 — chrX:70,528,940-70,908,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSGA3, TGC1, ZIP4, ZIP4H, MZIP4, Spo22 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IYF3](https://www.uniprot.org/uniprotkb/Q8IYF3) (Testis-expressed protein 11):

> Regulator of crossing-over during meiosis. Involved in initiation and/or maintenance of chromosome synapsis and formation of crossovers.

**Summary**, from NCBI Gene [56159](https://www.ncbi.nlm.nih.gov/gene/56159):

> This gene is X-linked and is expressed in only male germ cells. Two alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11733](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11733) · Entrez [56159](https://www.ncbi.nlm.nih.gov/gene/56159) · UniProt [Q8IYF3](https://www.uniprot.org/uniprotkb/Q8IYF3) · Ensembl [ENSG00000120498](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120498)

## Data

Gene col 4186: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4186); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4186, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4186]; `tensor/DDL_lfc|DDL_z.npy` [4186]; `embed/gene_vectors.npy` [4186]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4186 or target_col == 4186). Every well: [[TEX11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
