---
symbol: "TMED6"
type: "gene"
col: 8059
ensembl_id: "ENSG00000157315"
name: "transmembrane p24 trafficking protein 6"
location: "16q22.1"
module: 39
arm: "+"
pooled_cpm: 2.49
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# TMED6

*transmembrane p24 trafficking protein 6* — 16q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.03× (z +10.6, q 2e-23, up in 20 of 32 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SW480 0.136×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H460 0.0599×); [[Lumateperone (tosylate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0562×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLGN3]] (+0.76, fdr 7e-06), [[GABRR2]] (+0.76, fdr 7e-06), [[MYOCOS]] (+0.76, fdr 7e-06).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8059.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.03×** | +10.6 | 2e-23 | 20/32 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.4 | 1e-14 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +7.3 | 4e-11 | 2/10 (SW480, SHP-77) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +6.5 | 1e-08 | 10/32 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +6.3 | 5e-08 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +5.0 | 5e-05 | 9/27 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 2e-04 | 5/40 (HT-29, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.52×** | +4.4 | 6e-04 | 4/46 (SW480, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.006 | 5/44 (A498, NCI-H2030, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.8 | 0.010 | 4/31 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.014 | 6/27 (LS 180, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.025 | 5/44 (SW480, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.027 | 2/41 (PANC-1, HOP62) | all doses, flat |  |
| [[Gemfibrozil (drug)]] 0.05 µM |  | **1.34×** | +3.1 | 0.083 | 0/42 | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.34×** | +3.1 | 0.083 | 6/28 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8059.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Thymol (drug)]] 0.5 µM in 1 line (SW480 0.136×); [[Benproperine (phosphate) (drug)]] 5 µM in 1 line (NCI-H460 0.0599×); [[Lumateperone (tosylate) (drug)]] 0.5 µM in 1 line (NCI-H1573 0.0562×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.733× | -3.1 | 0.34 | 9/21 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.810× | -3.1 | 0.34 | 10/42 (SW1417, NCI-H2347, …) | top dose only |  |
| [[Decitabine (drug)]] 5 µM |  | 0.735× | -3.1 | 0.34 | 8/42 (HEC-1-A, HOP62, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8059. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 2.77 | 0 | 1 | — | [[Asciminib (drug)]] 5 µM 0.0544× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 2.48 | 0 | 1 | — | [[Lumateperone (tosylate) (drug)]] 0.5 µM 0.0562× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 2.32 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0599× (z -10.1) |
| [[PANC-1 (line)]] | alt | 1.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0809× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change |
| [[SW480 (line)]] | alt | 6.83 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.136× (z -11.0) |
| [[A-172 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.747 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8059), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLGN3]] | +0.76 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[GABRR2]] | +0.76 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[MYOCOS]] | +0.76 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[SMIM15-AS1]] | +0.75 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[ARL9]] | +0.74 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.74 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[BAAT]] | +0.74 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[TMEM236]] | +0.73 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[MIRLET7IHG]] | +0.73 | +0.71 / +0.59 | both halves | 7e-06 |  |
| [[CDKL4]] | +0.73 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 |  |
| [[RFPL3S]] | +0.71 | +0.73 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TMED6's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00334]] | B | LINC00334 activity raises TMED6's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.20× lower at baseline in the lines without LINC00334 | 0.096 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[TRIM72]] | C | TRIM72 activity raises TMED6's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without TRIM72 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |
| [[DCAF4L1]] | C | DCAF4L1's natural level weakens TMED6's drug response | DCAF4L1's natural level across 45 lines (lineage-adjusted; a glimpse) | r -0.65, reverse -0.13; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.0, -15.3); signed map (15.4, 5.2). **Vector** length 46.6, 4.89% of its response variance represented; |z| ≥ 3 in 1,265 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +6.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.5 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.5 | +6.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +1.1 | +3.6 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.0 | +1.5 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.1 | -3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | -1.5 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.6 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.1 — chr16:69,343,250-69,351,786 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC23911, p24gamma5, p24g5 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Matched by | ensembl_id |

UniProt [Q8WW62](https://www.uniprot.org/uniprotkb/Q8WW62) carries no function annotation.

**Summary**, from NCBI Gene [146456](https://www.ncbi.nlm.nih.gov/gene/146456):

> Predicted to be involved in Golgi organization; endoplasmic reticulum to Golgi vesicle-mediated transport; and intracellular protein transport. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in several cellular components, including COPII-coated ER to Golgi transport vesicle; Golgi apparatus; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28331) · Entrez [146456](https://www.ncbi.nlm.nih.gov/gene/146456) · UniProt [Q8WW62](https://www.uniprot.org/uniprotkb/Q8WW62) · Ensembl [ENSG00000157315](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157315)

## Data

Gene col 8059: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8059); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8059, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8059]; `tensor/DDL_lfc|DDL_z.npy` [8059]; `embed/gene_vectors.npy` [8059]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8059 or target_col == 8059). Every well: [[TMED6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
