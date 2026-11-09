---
symbol: "NENF"
type: "gene"
col: 3942
ensembl_id: "ENSG00000117691"
name: "neudesin neurotrophic factor"
location: "1q32.3"
module: 48
arm: "+"
pooled_cpm: 23.82
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# NENF

*neudesin neurotrophic factor* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +6.6, q 2e-08, up in 38 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.359× (z -10.0, q 9e-21, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 11 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MZT2B]] (+0.81, fdr 7e-06), [[COX7C]] (+0.79, fdr 7e-06), [[ATOX1]] (+0.78, fdr 7e-06); moves opposite to [[CYREN]] (-0.70, fdr 1e-05), [[SLC35A4]] (-0.70, fdr 1e-05), [[TASOR]] (-0.70, fdr 7e-06).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BEX3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3942.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +6.6 | 2e-08 | 38/42 (C-33 A, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +5.1 | 1e-04 | 24/33 (LoVo, C32, …) | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.12×** | +5.0 | 1e-04 | 27/37 (Hs 766T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.86×** | +4.4 | 0.001 | 32/45 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.67×** | +3.7 | 0.026 | 31/46 (NCI-H460, NCI-H1792, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +3.3 | 0.080 | 28/43 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3942.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.359×** | -10.0 | 9e-21 | 45/47 (A-427, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.392×** | -6.7 | 6e-09 | 43/47 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.506×** | -4.7 | 6e-04 | 35/48 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.625× | -3.1 | 0.27 | 27/48 (hTERT-HPNE, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3942. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 44.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.242× (z -12.8) |
| [[A-427 (line)]] | wt | 29.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 31.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 25.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -9.3) |
| [[HOP62 (line)]] | alt | 24.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -13.7) |
| [[HS-578T (line)]] | alt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -9.0) |
| [[J82 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.130× (z -10.0) |
| [[LS 180 (line)]] | wt | 19.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 40.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 25.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.2) |
| [[PANC-1 (line)]] | alt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.5) |
| [[SNU-423 (line)]] | alt | 25.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -13.3) |
| [[A498 (line)]] | wt | 41.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 14.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3942), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 11 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MZT2B]] | +0.81 | +0.84 / +0.75 | both halves | 7e-06 |  |
| [[COX7C]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[ATOX1]] | +0.78 | +0.63 / +0.77 | both halves | 7e-06 |  |
| [[COMMD6]] | +0.78 | +0.65 / +0.82 | both halves | 7e-06 |  |
| [[UBL5]] | +0.77 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[PFDN5]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 |  |
| [[ATP5MJ]] | +0.77 | +0.71 / +0.81 | both halves | 7e-06 |  |
| [[RPS19]] | +0.77 | +0.68 / +0.79 | both halves | 7e-06 |  |
| [[UBA52]] | +0.77 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[RPLP1]] | +0.77 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[RPLP2]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 |  |
| [[RPS14]] | +0.76 | +0.75 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYREN]] | -0.70 | -0.79 / -0.54 | both halves | 1e-05 |  |
| [[SLC35A4]] | -0.70 | -0.78 / -0.54 | both halves | 1e-05 |  |
| [[TASOR]] | -0.70 | -0.72 / -0.64 | both halves | 7e-06 |  |
| [[GTF2H3]] | -0.69 | -0.77 / -0.62 | both halves | 7e-06 |  |
| [[MIS12]] | -0.68 | -0.71 / -0.60 | both halves | 7e-06 |  |
| [[THOC6]] | -0.66 | -0.54 / -0.69 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BEX3]] | B | BEX3 activity raises NENF's level | lines that do not express BEX3 (7) vs lines expressing it (43) | 1.65× lower at baseline in the lines without BEX3 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000283491, LRP12, KIRREL1 |
| [[FGD1]] | B | FGD1 activity raises NENF's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without FGD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.795). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-46.2, -24.2); signed map (-35.8, 8.1). **Vector** length 78.3, 24.8% of its response variance represented; |z| ≥ 3 in 480 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Aerobic respiration and respiratory electron transport* (reactome, mean cos +0.60 to 31); *Respiratory electron transport* (reactome, mean cos +0.59 to 24); *oxidative phosphorylation* (hallmark, mean cos +0.60 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +3.6 | +3.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | +0.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +0.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.6 | +1.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +0.4 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.3 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.2 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -10.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -2.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.8 | -0.7 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | -1.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | neudesin neurotrophic factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:212,432,920-212,446,379 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CIR2, SCIRP10, SPUF |
| Gene groups (HGNC) | Membrane associated progesterone receptor family; Cytochrome b5 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMX5](https://www.uniprot.org/uniprotkb/Q9UMX5) (Neudesin):

> Acts as a neurotrophic factor in postnatal mature neurons enhancing neuronal survival. Promotes cell proliferation and neurogenesis in undifferentiated neural progenitor cells at the embryonic stage and inhibits differentiation of astrocytes (By similarity). Its neurotrophic activity is exerted via MAPK1/ERK2, MAPK3/ERK1 and AKT1/AKT pathways (By similarity). Neurotrophic activity is enhanced by binding to heme (By similarity). Also acts as an anorexigenic neurotrophic factor that contributes …

**Summary**, from NCBI Gene [29937](https://www.ncbi.nlm.nih.gov/gene/29937):

> This gene encodes a neurotrophic factor that may play a role in neuron differentiation and development. A pseudogene of this gene is found on chromosome 12. Alternate splicing of this gene results in multiple transcript variants. [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:30384](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30384) · Entrez [29937](https://www.ncbi.nlm.nih.gov/gene/29937) · UniProt [Q9UMX5](https://www.uniprot.org/uniprotkb/Q9UMX5) · Ensembl [ENSG00000117691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117691)

## Data

Gene col 3942: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3942); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3942, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3942]; `tensor/DDL_lfc|DDL_z.npy` [3942]; `embed/gene_vectors.npy` [3942]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3942 or target_col == 3942). Every well: [[NENF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NENF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
