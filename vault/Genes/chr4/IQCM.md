---
symbol: "IQCM"
type: "gene"
col: 13986
ensembl_id: "ENSG00000234828"
name: "IQ motif containing M"
location: "4q31.23"
module: 19
arm: "+"
pooled_cpm: 3.56
n_lines_expressing: 45
n_dd_up: 18
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# IQCM

*IQ motif containing M* — 4q31.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 7.88× (z +22.3, q 0e+00, up in 17 of 21 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.196×, NCI-H460 0.168×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SK-MEL-2 0.120×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.143×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0831×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCNMB2]] (+0.82, fdr 7e-06), [[PCDH15]] (+0.81, fdr 7e-06), [[LINC00461]] (+0.74, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **7.88×** | +22.3 | 0e+00 | 17/21 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **4.70×** | +11.8 | 7e-30 | 23/32 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.62×** | +11.3 | 4e-27 | 1/3 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.27×** | +11.1 | 2e-26 | 3/8 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +9.1 | 9e-18 | 22/34 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +7.4 | 1e-11 | 1/5 (A-172) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +6.2 | 5e-08 | 11/24 (C32, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.9 | 3e-07 | 4/34 (A498, SW480, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +5.8 | 4e-07 | 4/15 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +5.3 | 6e-06 | 10/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +5.1 | 1e-05 | 9/23 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +4.8 | 8e-05 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.05×** | +3.9 | 0.004 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.012 | 4/36 (NCI-H460, NCI-H1792, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.60×** | +3.5 | 0.020 | 10/18 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.086 | 1/19 (SW480) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13986.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.196×, NCI-H460 0.168×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (SK-MEL-2 0.120×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.143×; ⚠ cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.143×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0831×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.656× | -3.2 | 0.31 | 7/21 (NCI-H460, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.749× | -3.2 | 0.31 | 6/39 (NCI-H2030, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.664× | -3.1 | 0.31 | 4/32 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.654× | -3.0 | 0.36 | 5/31 (SNU-423, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -9.6) |
| [[SW480 (line)]] | alt | 1.17 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 15.0× (z +10.7) | — |
| [[A498 (line)]] | wt | 1.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.3) | — |
| [[HEC-1-A (line)]] | alt | 1.06 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 18.6× (z +8.5) | — |
| [[LoVo (line)]] | wt | 0.978 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.4× (z +8.5) | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0704× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.805 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.965 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.827 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.976 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.946 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.939 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.929 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.957 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.965 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.960 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.987 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.937 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.803 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.984 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.982 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNMB2]] | +0.82 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[PCDH15]] | +0.81 | +0.68 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[LINC00461]] | +0.74 | +0.70 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[NKAIN2]] | +0.71 | +0.54 / +0.67 | both halves | 1e-05 | **novel candidate** |
| [[GRID2]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ASXL3]] | +0.68 | +0.55 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[LINC02208]] | +0.67 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[LINC01122]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[SOX6]] | +0.66 | +0.76 / +0.47 | both halves | 2e-05 |  |
| [[ANO3]] | +0.66 | +0.50 / +0.69 | both halves | 1e-05 | **novel candidate** |
| [[ADGRL3]] | +0.66 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[LSAMP]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers IQCM's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PDE1A]] | B | PDE1A activity raises IQCM's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 2.71× lower at baseline in the lines without PDE1A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent |
| [[SPDYE10]] | B | SPDYE10 activity lowers IQCM's level | lines that do not express SPDYE10 (10) vs lines expressing it (40) | 1.19× higher at baseline in the lines without SPDYE10 | 0.055 | ⚠ within organs, on part of the lines; also absent: SSPOP, SCML2, DISP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.698). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.4, 34.5); signed map (42.6, 39.1). **Vector** length 53.9, 9.79% of its response variance represented; |z| ≥ 3 in 856 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +22.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +9.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.7 | -3.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.7 | -2.5 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | IQ motif containing M |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.23 — chr4:149,351,709-149,896,233 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [A0A1B0GVH7](https://www.uniprot.org/uniprotkb/A0A1B0GVH7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53443) · Entrez [285423](https://www.ncbi.nlm.nih.gov/gene/285423) · UniProt [A0A1B0GVH7](https://www.uniprot.org/uniprotkb/A0A1B0GVH7) · Ensembl [ENSG00000234828](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234828)

## Data

Gene col 13986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13986); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13986]; `tensor/DDL_lfc|DDL_z.npy` [13986]; `embed/gene_vectors.npy` [13986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13986 or target_col == 13986). Every well: [[IQCM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IQCM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
