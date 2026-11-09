---
symbol: "ECSCR"
type: "gene"
col: 14632
ensembl_id: "ENSG00000249751"
name: "endothelial cell surface expressed chemotaxis and apoptosis regulator"
location: "5q31.2"
module: 9
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 15
n_dd_up: 7
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ECSCR

*endothelial cell surface expressed chemotaxis and apoptosis regulator* — 5q31.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.46× (z +10.2, q 8e-22, up in 1 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +7.3, q 4e-11, up in 5 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.151×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KISS1]] (+0.57, fdr 1e-05), [[SLC14A1]] (+0.55, fdr 2e-05), [[CCDC190]] (+0.55, fdr 3e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[STING1]] → it (grade B ⚠); 5 go from it, the strongest it → [[ZPLD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14632.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.46×** | +10.2 | 8e-22 | 1/1 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.20×** | +8.7 | 7e-16 | 1/2 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.79×** | +7.7 | 3e-12 | 1/1 (Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +7.3 | 4e-11 | 5/6 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.23×** | +4.1 | 0.005 | 0/1 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.06×** | +3.8 | 0.013 | 0/2 | top dose only | cell-cycle shift (explains ~20% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.52×** | +3.5 | 0.040 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.85× | +3.1 | 0.13 | 0/1 | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 2.99× | +3.0 | 0.15 | 0/0 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14632.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (Hs 766T 0.151×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.491× | -3.5 | 0.26 | 4/11 (C32, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14632. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -15.0) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.904 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.549 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.310 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.458 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.866 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.570 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.918 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.865 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.600 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.454 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.751 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.666 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.453 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.449 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.285 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.436 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.328 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.000 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.502 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.525 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.368 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.534 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.346 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.349 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14632), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KISS1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SLC14A1]] | +0.55 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[CCDC190]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SIM1]] | +0.55 | +0.52 / +0.41 | both halves | 4e-05 | **novel candidate** |
| [[DOK5]] | +0.54 | +0.56 / +0.45 | both halves | 3e-05 |  |
| [[GRIA1]] | +0.54 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[LINC01592]] | +0.54 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[HTR1F]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[MILR1]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[ADAMTSL3]] | +0.53 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[PECAM1]] | +0.53 | +0.38 / +0.53 | both halves | 6e-05 |  |
| [[XG]] | +0.53 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STING1]] | B | STING1 activity raises ECSCR's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.40× lower at baseline in the lines without STING1 | 0.095 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[SIM1]] | C | SIM1 activity raises ECSCR's level | lines that do not express SIM1 (43) vs lines expressing it (7) | 2.36× lower at baseline in the lines without SIM1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PSG9, PSG1, KRT5; co-absent with the target |
| [[DOK5]] | C | DOK5 activity raises ECSCR's level | lines that do not express DOK5 (40) vs lines expressing it (10) | 1.93× lower at baseline in the lines without DOK5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, ENSG00000230258, IGFBP5; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZPLD1]] | B | ECSCR activity raises ZPLD1's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 2.12× lower at baseline in the lines without ECSCR | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent |
| [[STING1]] | B | ECSCR activity raises STING1's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 3.68× lower at baseline in the lines without ECSCR | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent |
| [[SPRED3]] | B | ECSCR activity raises SPRED3's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 1.42× lower at baseline in the lines without ECSCR | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent |
| [[RHOJ]] | C | ECSCR activity raises RHOJ's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 3.36× lower at baseline in the lines without ECSCR | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent; co-absent with the target |
| [[MANCR]] | C | ECSCR activity raises MANCR's level | lines that do not express ECSCR (35) vs lines expressing it (15) | 3.18× lower at baseline in the lines without ECSCR | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, ADGRF5, ENSG00000243486; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.248). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.5, 19.3); signed map (34.4, 30.1). **Vector** length 18.1, 3.74% of its response variance represented; |z| ≥ 3 in 225 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +7.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +8.7 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.2 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.8 | +0.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.6 | +0.8 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.6 | -3.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.6 | -1.8 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.5 | -2.4 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -0.5 | -0.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.5 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | endothelial cell surface expressed chemotaxis and apoptosis regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.2 — chr5:139,448,560-139,462,743 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ECSM2, ARIA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q19T08](https://www.uniprot.org/uniprotkb/Q19T08) (Endothelial cell-specific chemotaxis regulator):

> Regulates endothelial chemotaxis and tube formation. Has a role in angiogenesis and apoptosis via modulation of the actin cytoskeleton and facilitation of proteasomal degradation of the apoptosis inhibitors BIRC3/IAP1 and BIRC2/IAP2.

**Summary**, from NCBI Gene [641700](https://www.ncbi.nlm.nih.gov/gene/641700):

> The protein encoded by this gene is primarily found in endothelial cells and blood vessels, where it is involved in cell shape changes and EGF-induced cell migration. It can enhance the activation of vascular endothelial growth factor receptor-2/kinase insert domain receptor and also promote the proteolysis of internalized kinase insert domain receptor. This gene may play a role in angiogenesis-related diseases. Alternative splicing results in multiple transcript variants. [provided by RefSeq, …

**Accessions** — [HGNC:35454](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35454) · Entrez [641700](https://www.ncbi.nlm.nih.gov/gene/641700) · UniProt [Q19T08](https://www.uniprot.org/uniprotkb/Q19T08) · Ensembl [ENSG00000249751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000249751)

## Data

Gene col 14632: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14632); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14632, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14632]; `tensor/DDL_lfc|DDL_z.npy` [14632]; `embed/gene_vectors.npy` [14632]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14632 or target_col == 14632). Every well: [[ECSCR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ECSCR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
