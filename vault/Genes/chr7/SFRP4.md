---
symbol: "SFRP4"
type: "gene"
col: 2766
ensembl_id: "ENSG00000106483"
name: "secreted frizzled related protein 4"
location: "7p14.1"
module: 140
arm: "+"
pooled_cpm: 2.85
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# SFRP4

*secreted frizzled related protein 4* — 7p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.48× (z +11.6, q 1e-28, up in 19 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vemurafenib (drug)]] 0.5 µM in 1 line (SW 1271 0.996×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USH2A]] (+0.78, fdr 7e-06), [[SPATA21]] (+0.76, fdr 7e-06), [[ST7-AS2]] (+0.76, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.48×** | +11.6 | 1e-28 | 19/27 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.71×** | +11.4 | 8e-28 | 2/2 (A498, NCI-H661) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +10.6 | 6e-24 | 8/11 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +9.1 | 1e-17 | 3/3 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +5.7 | 2e-06 | 11/30 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.84×** | +5.5 | 3e-06 | 2/8 (LoVo, PANC-1) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.48×** | +5.0 | 4e-05 | 10/43 (SW480, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +4.8 | 1e-04 | 13/43 (PANC-1, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.65×** | +4.5 | 4e-04 | 7/40 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.001 | 3/43 (SW 900, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +3.8 | 0.006 | 1/8 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.5 | 0.021 | 6/32 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +3.3 | 0.039 | 2/37 (SW480, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.44×** | +3.3 | 0.044 | 0/11 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2766.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Vemurafenib (drug)]] 0.5 µM in 1 line (SW 1271 0.996×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.5 | 0.25 | 18/47 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 5 µM |  | 0.703× | -3.2 | 0.35 | 8/43 (HT-29, C32, …) | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.785× | -3.1 | 0.35 | 8/46 (Hs 766T, PANC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 9.18 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.71× (z +13.7) | — |
| [[A-172 (line)]] | wt | 1.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +8.8) | — |
| [[A-427 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.14 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.04 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USH2A]] | +0.78 | +0.66 / +0.77 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.76 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.76 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.76 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.76 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[PPP1R9A-AS1]] | +0.76 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SLC27A6]] | +0.75 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[GALNTL6]] | +0.75 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.75 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.75 | +0.59 / +0.76 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.74 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.74 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM | C | SFRP4's natural level lowers the cells' numbers under Ropivacaine (hydrochloride monohydrate) 5 µM (makes them more sensitive) | SFRP4's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.080 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, 27.9); signed map (33.8, 10.9). **Vector** length 35.4, 3.33% of its response variance represented; |z| ≥ 3 in 939 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +11.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +10.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +1.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -3.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.1 | -2.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | +0.7 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | secreted frizzled related protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.1 — chr7:37,905,932-38,025,695 (-) |
| Ensembl biotype | protein_coding |
| Also known as | frpHE, FRP-4, FRPHE, FRZB-2 |
| Gene groups (HGNC) | Secreted frizzled-related proteins |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6FHJ7](https://www.uniprot.org/uniprotkb/Q6FHJ7) (Secreted frizzled-related protein 4):

> Soluble frizzled-related proteins (sFRPS) function as modulators of Wnt signaling through direct interaction with Wnts. They have a role in regulating cell growth and differentiation in specific cell types (By similarity). SFRP4 plays a role in bone morphogenesis. May also act as a regulator of adult uterine morphology and function. May also increase apoptosis during ovulation possibly through modulation of FZ1/FZ4/WNT4 signaling (By similarity). Has phosphaturic effects by specifically …

**Summary**, from NCBI Gene [6424](https://www.ncbi.nlm.nih.gov/gene/6424):

> Secreted frizzled-related protein 4 (SFRP4) is a member of the SFRP family that contains a cysteine-rich domain homologous to the putative Wnt-binding site of Frizzled proteins. SFRPs act as soluble modulators of Wnt signaling. The expression of SFRP4 in ventricular myocardium correlates with apoptosis related gene expression. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10778](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10778) · Entrez [6424](https://www.ncbi.nlm.nih.gov/gene/6424) · UniProt [Q6FHJ7](https://www.uniprot.org/uniprotkb/Q6FHJ7) · Ensembl [ENSG00000106483](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106483)

## Data

Gene col 2766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2766); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2766]; `tensor/DDL_lfc|DDL_z.npy` [2766]; `embed/gene_vectors.npy` [2766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2766 or target_col == 2766). Every well: [[SFRP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SFRP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
