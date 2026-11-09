---
symbol: "CASKIN1"
type: "gene"
col: 9565
ensembl_id: "ENSG00000167971"
name: "CASK interacting protein 1"
location: "16p13.3"
module: 53
arm: "+"
pooled_cpm: 2.87
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# CASKIN1

*CASK interacting protein 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.10× (z +10.2, q 1e-21, up in 18 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.412× (z -8.6, q 5e-15, down in 25 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUNDC3A-AS1]] (+0.61, fdr 1e-05), [[CDKL2]] (+0.59, fdr 1e-05), [[CAPN12]] (+0.57, fdr 4e-05).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP3K15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9565.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.10×** | +10.2 | 1e-21 | 18/31 (A549, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +9.4 | 1e-18 | 1/3 (PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.6 | 9e-04 | 3/15 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.3 | 0.002 | 7/34 (HEC-1-A, SW480, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.59× | +3.2 | 0.15 | 2/23 (SW480, NCI-H23) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.17 | 0/23 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9565.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.412×** | -8.6 | 5e-15 | 25/37 (BT-474, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.523×** | -6.3 | 1e-07 | 22/42 (SNU-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.532×** | -5.9 | 8e-07 | 21/38 (Hs 766T, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.573×** | -5.4 | 9e-06 | 17/41 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.607×** | -4.8 | 1e-04 | 17/44 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.690×** | -3.6 | 0.029 | 9/37 (hTERT-HPNE, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.692×** | -3.6 | 0.029 | 13/28 (A549, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.727× | -3.1 | 0.14 | 11/33 (HOP62, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.728× | -3.1 | 0.14 | 13/35 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.731× | -3.0 | 0.14 | 14/40 (CFPAC-1, SNU-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9565. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 5.30 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0518× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 5.66 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0553× (z -10.1) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H23 (line)]] | alt | 4.85 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0942× (z -9.2) |
| [[A-172 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.785 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.720 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.727 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.788 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.679 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.32 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9565), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUNDC3A-AS1]] | +0.61 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[CDKL2]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[CAPN12]] | +0.57 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[FLRT1]] | +0.57 | +0.44 / +0.61 | both halves | 3e-05 |  |
| [[GDF1]] | +0.57 | +0.53 / +0.52 | both halves | 1e-05 |  |
| [[DHDH]] | +0.55 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[APC2]] | +0.55 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[ISM2]] | +0.54 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[ITGA7]] | +0.54 | +0.39 / +0.57 | both halves | 6e-05 |  |
| [[CELF5]] | +0.53 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[RSPH9]] | +0.52 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[LZTS2]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K15]] | B | MAP3K15 activity raises CASKIN1's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 1.70× lower at baseline in the lines without MAP3K15 | 0.045 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[CHD5]] | B | CHD5 activity raises CASKIN1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without CHD5 | 0.099 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (41.2, -19.0); signed map (13.1, 16.4). **Vector** length 47.4, 6.08% of its response variance represented; |z| ≥ 3 in 933 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.4 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +3.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.8 | +4.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +3.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | -1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.1 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.3 | -5.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -8.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -6.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -1.6 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -1.0 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | CASK interacting protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:2,177,180-2,196,605 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1306, ANKS5A |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Sterile alpha motif domain containing; SH3 domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WXD9](https://www.uniprot.org/uniprotkb/Q8WXD9) (Caskin-1):

> May link the scaffolding protein CASK to downstream intracellular effectors.

**Summary**, from NCBI Gene [57524](https://www.ncbi.nlm.nih.gov/gene/57524):

> Enables identical protein binding activity. Predicted to be involved in regulation of postsynaptic density assembly and signal transduction. Predicted to be located in cytoplasm. Predicted to be active in glutamatergic synapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20879](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20879) · Entrez [57524](https://www.ncbi.nlm.nih.gov/gene/57524) · UniProt [Q8WXD9](https://www.uniprot.org/uniprotkb/Q8WXD9) · Ensembl [ENSG00000167971](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167971)

## Data

Gene col 9565: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9565); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9565, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9565]; `tensor/DDL_lfc|DDL_z.npy` [9565]; `embed/gene_vectors.npy` [9565]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9565 or target_col == 9565). Every well: [[CASKIN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASKIN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
