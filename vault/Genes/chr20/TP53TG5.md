---
symbol: "TP53TG5"
type: "gene"
col: 4511
ensembl_id: "ENSG00000124251"
name: "TP53 target 5"
location: "20q13.12"
module: 21
arm: "+"
pooled_cpm: 2.36
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# TP53TG5

*TP53 target 5* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +12.5, q 7e-33, up in 28 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0567×); [[Idoxuridine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0724×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL2-DT]] (+0.76, fdr 7e-06), [[DNAJC9-AS1-1]] (+0.76, fdr 7e-06), [[SLC13A4]] (+0.73, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CACNG2]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SLC13A4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4511.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +12.5 | 7e-33 | 28/33 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.33×** | +7.6 | 1e-11 | 0/0 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +6.9 | 9e-10 | 7/13 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +6.3 | 4e-08 | 1/3 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.3 | 1e-05 | 2/10 (A498, SW480) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.006 | 6/37 (HT-29, HS-578T, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +3.7 | 0.015 | 1/20 (NCI-H1573) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.70×** | +3.5 | 0.030 | 1/4 (HEC-1-A) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.051 | 4/38 (SNU-423, HS-578T, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4511.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Harringtonine (drug)]] 0.5 µM in 1 line (RKO 0.0567×); [[Idoxuridine (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0724×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.695× | -3.3 | 0.42 | 9/44 (A-172, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.713× | -3.1 | 0.42 | 7/46 (LOX-IMVI, RKO, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4511. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 3.19 | 0 | 1 | — | [[Idoxuridine (drug)]] 0.05 µM 0.0724× (z -8.8) |
| [[RKO (line)]] | wt | 6.74 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0567× (z -10.0) |
| [[A-172 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.82 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4511), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL2-DT]] | +0.76 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[DNAJC9-AS1-1]] | +0.76 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[SLC13A4]] | +0.73 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[CCDC73]] | +0.73 | +0.55 / +0.73 | both halves | 1e-05 |  |
| [[CHMP3-AS1]] | +0.72 | +0.56 / +0.75 | both halves | 1e-05 |  |
| [[RELA-DT]] | +0.71 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.71 | +0.53 / +0.72 | both halves | 1e-05 |  |
| [[PKD2L2]] | +0.71 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.71 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.71 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.70 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[SPATC1]] | +0.70 | +0.56 / +0.74 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNG2]] | B | CACNG2 activity lowers TP53TG5's level | lines that do not express CACNG2 (9) vs lines expressing it (41) | 1.41× higher at baseline in the lines without CACNG2 | 0.024 | ⚠ within organs, on part of the lines; also absent: FRMD3, NFATC2, ENSG00000285082; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC13A4]] | C | TP53TG5's natural level weakens SLC13A4's drug response | TP53TG5's natural level across 46 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.14; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 25.4); signed map (31.1, 4.7). **Vector** length 37.7, 3.69% of its response variance represented; |z| ≥ 3 in 853 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +2.3 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +0.9 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.2 | -3.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.0 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.8 |
|  | [[Relugolix (drug)]] 0.5 µM |  | -0.9 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TP53 target 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:45,372,557-45,407,889 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CLG01, dJ453C12.5; previously C20orf10 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2B4](https://www.uniprot.org/uniprotkb/Q9Y2B4) (TP53-target gene 5 protein):

> May play a significant role in p53/TP53-mediating signaling pathway.

**Summary**, from NCBI Gene [27296](https://www.ncbi.nlm.nih.gov/gene/27296):

> Predicted to be involved in intracellular signal transduction and negative regulation of cell growth. Located in chromosome and nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15856](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15856) · Entrez [27296](https://www.ncbi.nlm.nih.gov/gene/27296) · UniProt [Q9Y2B4](https://www.uniprot.org/uniprotkb/Q9Y2B4) · Ensembl [ENSG00000124251](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000124251)

## Data

Gene col 4511: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4511); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4511, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4511]; `tensor/DDL_lfc|DDL_z.npy` [4511]; `embed/gene_vectors.npy` [4511]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4511 or target_col == 4511). Every well: [[TP53TG5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TP53TG5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
