---
symbol: "SORCS3"
type: "gene"
col: 7975
ensembl_id: "ENSG00000156395"
name: "sortilin related VPS10 domain containing receptor 3"
location: "10q25.1"
module: 140
arm: "+"
pooled_cpm: 2.04
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# SORCS3

*sortilin related VPS10 domain containing receptor 3* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.76× (z +25.4, q 0e+00, up in 27 of 28 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.135×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USH2A]] (+0.79, fdr 1e-05), [[HPSE2]] (+0.79, fdr 1e-05), [[C8orf34]] (+0.79, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.76×** | +25.4 | 0e+00 | 27/28 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.88×** | +9.9 | 9e-21 | 26/39 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +9.6 | 2e-19 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +9.5 | 3e-19 | 2/8 (HOP62, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +7.1 | 2e-10 | 8/21 (NCI-H460, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +6.8 | 1e-09 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.62×** | +6.4 | 1e-08 | 16/43 (NCI-H1573, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +5.9 | 3e-07 | 10/30 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +5.8 | 4e-07 | 11/32 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.7 | 6e-07 | 7/43 (NCI-H460, A498, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.65×** | +4.7 | 1e-04 | 13/33 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +4.0 | 0.003 | 0/2 | top dose only | noisy plate (z scaled); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.80×** | +4.0 | 0.003 | 1/2 (NCI-H23) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.8 | 0.007 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 0/42 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.0 | 0.087 | 4/23 (NCI-H23, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.5 µM in 1 line (NCI-H460 0.135×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 7.72 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.49× (z +14.7) | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.135× (z -9.2) |
| [[A498 (line)]] | wt | 1.21 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.5× (z +9.4) | — |
| [[A549 (line)]] | wt | 2.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +9.1) | — |
| [[HEC-1-A (line)]] | alt | 1.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +8.7) | — |
| [[LoVo (line)]] | wt | 1.56 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 1.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.8× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.7× (z +9.6) | — |
| [[SW480 (line)]] | alt | 1.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +8.9) | — |
| [[A-172 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.75 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USH2A]] | +0.79 | +0.53 / +0.88 | both halves | 1e-05 |  |
| [[HPSE2]] | +0.79 | +0.55 / +0.84 | both halves | 1e-05 |  |
| [[C8orf34]] | +0.79 | +0.65 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LINC02006]] | +0.78 | +0.56 / +0.82 | both halves | 1e-05 | **novel candidate** |
| [[CCDC26]] | +0.78 | +0.62 / +0.80 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.75 | +0.54 / +0.81 | both halves | 1e-05 |  |
| [[LINC00861]] | +0.75 | +0.53 / +0.79 | both halves | 1e-05 |  |
| [[LINC01579]] | +0.74 | +0.43 / +0.78 | both halves | 3e-05 |  |
| [[HRG-AS1]] | +0.74 | +0.41 / +0.71 | both halves | 4e-05 |  |
| [[SLC27A6]] | +0.74 | +0.43 / +0.77 | both halves | 3e-05 |  |
| [[GALNTL6]] | +0.73 | +0.56 / +0.78 | both halves | 1e-05 |  |
| [[CNBD1]] | +0.73 | +0.50 / +0.78 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SORCS3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNJ6]] | B | KCNJ6 activity raises SORCS3's level | lines that do not express KCNJ6 (23) vs lines expressing it (27) | 1.38× lower at baseline in the lines without KCNJ6 | 0.097 | ⚠ within organs, on part of the lines; also absent: LRP2, ENTHD1, MLLT11; maybe low, not absent |
| [[DISP3]] | B | DISP3 activity raises SORCS3's level | lines that do not express DISP3 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without DISP3 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02609, DPF1, ARHGEF26 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (20.0, 28.5); signed map (32.6, 12.8). **Vector** length 39.1, 4.13% of its response variance represented; |z| ≥ 3 in 997 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.2 | +25.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.3 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -0.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | sortilin related VPS10 domain containing receptor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,641,290-105,265,242 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1059, SORCS |
| Reactome | 3 pathways, smallest: NFG and proNGF binds to p75NTR; p75 NTR receptor-mediated signalling; Death Receptor Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPU3](https://www.uniprot.org/uniprotkb/Q9UPU3) (VPS10 domain-containing receptor SorCS3):

> Plays an important role in modulating synaptic transmission and plasticity in the hippocampus, probably by affecting the trafficking and localization ofAMPA-type glutamate receptors in the postsynaptic density.

**Summary**, from NCBI Gene [22986](https://www.ncbi.nlm.nih.gov/gene/22986):

> This gene encodes a type-I receptor transmembrane protein that is a member of the vacuolar protein sorting 10 receptor family. Proteins of this family are defined by a vacuolar protein sorting 10 domain at the N-terminus. The N-terminal segment of this domain has a consensus motif for proprotein convertase processing, and the C-terminal segment of this domain is characterized by ten conserved cysteine residues. The vacuolar protein sorting 10 domain is followed by a leucine-rich segment, a …

**Accessions** — [HGNC:16699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16699) · Entrez [22986](https://www.ncbi.nlm.nih.gov/gene/22986) · UniProt [Q9UPU3](https://www.uniprot.org/uniprotkb/Q9UPU3) · Ensembl [ENSG00000156395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156395)

## Data

Gene col 7975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7975); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7975]; `tensor/DDL_lfc|DDL_z.npy` [7975]; `embed/gene_vectors.npy` [7975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7975 or target_col == 7975). Every well: [[SORCS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SORCS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
