---
symbol: "TRAPPC2L"
type: "gene"
col: 9475
ensembl_id: "ENSG00000167515"
name: "trafficking protein particle complex subunit 2L"
location: "16q24.3"
module: 122
arm: "+"
pooled_cpm: 7.19
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# TRAPPC2L

*trafficking protein particle complex subunit 2L* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.04× (z +9.3, q 9e-18, up in 28 of 31 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.68× (z +5.8, q 1e-06, up in 27 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.66×; ⚠ toxic; transcription drop).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Vortioxetine (drug)]] 5 µM in 1 line (HS-578T 0.0639×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-423 0.141×; ⚠ toxic; cell-cycle shift, explains ~57% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HS-578T 0.0788×); [[Menadione (drug)]] 0.5 µM in 1 line (SW48 0.0697×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RFXANK]] (+0.66, fdr 4e-05), [[GET3]] (+0.64, fdr 7e-06), [[VPS11]] (+0.62, fdr 8e-06); moves opposite to [[SPCS3]] (-0.51, fdr 4e-05), [[SLC4A7]] (-0.51, fdr 3e-05), [[CYCS]] (-0.50, fdr 1e-04).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (A498 5.66×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +9.3 | 9e-18 | 28/31 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.77×** | +8.2 | 7e-14 | 11/13 (Hs 766T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +5.8 | 1e-06 | 27/42 (A498, A549, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +4.9 | 1e-04 | 25/35 (CFPAC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.78×** | +4.8 | 2e-04 | 22/39 (KATO III, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.86×** | +4.8 | 2e-04 | 13/19 (HOP62, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.11×** | +3.4 | 0.059 | 12/36 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.45× | +3.1 | 0.13 | 9/46 (NCI-H2030, A498, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9475.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Vortioxetine (drug)]] 5 µM in 1 line (HS-578T 0.0639×; ⚠ toxic); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (SNU-423 0.141×; ⚠ toxic; cell-cycle shift, explains ~57% of this change); [[Pitavastatin (Calcium) (drug)]] 0.5 µM in 1 line (HS-578T 0.0788×); [[Menadione (drug)]] 0.5 µM in 1 line (SW48 0.0697×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.746× | -3.3 | 0.64 | 11/48 (CFPAC-1, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9475. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 4.88 | 0 | 2 (1 ⚠) | — | [[Vortioxetine (drug)]] 5 µM 0.0639× (z -10.4) ⚠ toxic · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0788× (z -9.6) |
| [[A498 (line)]] | wt | 8.37 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.66× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~57% of this change |
| [[SW48 (line)]] | wt | 7.56 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0697× (z -8.5) |
| [[A-172 (line)]] | wt | 7.97 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.13 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.88 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.68 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.00 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9475), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RFXANK]] | +0.66 | +0.42 / +0.67 | both halves | 4e-05 |  |
| [[GET3]] | +0.64 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[VPS11]] | +0.62 | +0.72 / +0.57 | both halves | 8e-06 |  |
| [[C11orf1]] | +0.60 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[PTRHD1]] ⚠ | +0.57 | +0.27 / +0.66 | both halves | 3e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM126A]] | +0.57 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[TSC1]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 | pathway: Rab regulation of trafficking |
| [[UROD]] | +0.55 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[DPP7]] | +0.55 | +0.49 / +0.57 | both halves | 2e-05 |  |
| [[SPNS1]] | +0.55 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[FLCN]] | +0.55 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[MRPL37]] | +0.54 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[DPH1]] | +0.54 | +0.44 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPCS3]] | -0.51 | -0.40 / -0.57 | both halves | 4e-05 |  |
| [[SLC4A7]] | -0.51 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[CYCS]] | -0.50 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[ASPH]] | -0.49 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[CALM2]] | -0.48 | -0.31 / -0.50 | both halves | 2e-04 |  |
| [[ACSL4]] | -0.48 | -0.28 / -0.54 | both halves | 3e-04 |  |
| [[DIAPH1]] | -0.48 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[DNAJC10]] | -0.46 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[BMAL2]] | -0.46 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[HNRNPA2B1]] | -0.46 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[DDX46]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.5, -17.2); signed map (-9.8, -21.0). **Vector** length 45.1, 6.32% of its response variance represented; |z| ≥ 3 in 575 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +5.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.8 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.3 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.5 | -0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | +0.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 2L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,856,220-88,862,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC176 |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UL33](https://www.uniprot.org/uniprotkb/Q9UL33) (Trafficking protein particle complex subunit 2-like protein):

> Plays a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [51693](https://www.ncbi.nlm.nih.gov/gene/51693):

> This gene encodes a protein that interacts with the tethering factor trafficking protein particle (TRAPP complex). TRAPP complexes mediate the contact between vescicles and target membranes, and thus, are involved in vescicle-mediated transport of proteins and lipids. The encoded protein is related to the X-linked trafficking protein particle complex 2. A related pseudogene is located on the X chromosome. Alternative splicing results in multiple transcript variants encoding different isoforms. …

**Accessions** — [HGNC:30887](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30887) · Entrez [51693](https://www.ncbi.nlm.nih.gov/gene/51693) · UniProt [Q9UL33](https://www.uniprot.org/uniprotkb/Q9UL33) · Ensembl [ENSG00000167515](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167515)

## Data

Gene col 9475: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9475); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9475, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9475]; `tensor/DDL_lfc|DDL_z.npy` [9475]; `embed/gene_vectors.npy` [9475]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9475 or target_col == 9475). Every well: [[TRAPPC2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
