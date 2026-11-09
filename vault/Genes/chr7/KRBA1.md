---
symbol: "KRBA1"
type: "gene"
col: 5457
ensembl_id: "ENSG00000133619"
name: "KRAB domain containing 3"
location: "7q36.1"
module: 132
arm: "+"
pooled_cpm: 4.01
n_lines_expressing: 37
n_dd_up: 0
n_dd_down: 8
n_dd_up_clean: 0
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# KRBA1

*KRAB domain containing 3* — 7q36.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.650× (z -6.2, q 3e-07, down in 16 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOX10]] (+0.57, fdr 3e-05), [[LZTR1]] (+0.57, fdr 3e-05), [[SHANK3]] (+0.55, fdr 4e-05); moves opposite to [[LINC01019]] (-0.42, fdr 1e-04), [[TOMM20L-DT]] (-0.42, fdr 1e-04), [[MROH3P]] (-0.42, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MROH3P]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC01019]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5457.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cytarabine (drug)]] 5 µM |  | 1.42× | +3.2 | 0.25 | 3/32 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.37× | +3.2 | 0.25 | 3/34 (A498, A-172, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.37× | +3.2 | 0.25 | 1/33 (J82) | inconsistent across doses | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | 1.24× | +3.0 | 0.33 | 2/35 (MIA PaCa-2, H4) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5457.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.650×** | -6.2 | 3e-07 | 16/27 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -4.7 | 7e-04 | 9/20 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.438×** | -4.4 | 0.002 | 12/31 (NCI-H460, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~12% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.666×** | -4.1 | 0.005 | 9/18 (C32, NCI-H460, …) | two highest doses | composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.648×** | -4.0 | 0.007 | 11/30 (C-33 A, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.665×** | -3.8 | 0.016 | 5/32 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.695×** | -3.7 | 0.018 | 10/34 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.535×** | -3.3 | 0.063 | 5/25 (A-172, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5457. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 16.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0808× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C-33 A (line)]] | alt | 10.5 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0649× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 5.93 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[PANC-1 (line)]] | alt | 3.09 | 0 | 1 | — | [[Bergenin (drug)]] 0.5 µM 0.0556× (z -13.0) |
| [[SNU-423 (line)]] | alt | 5.39 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0721× (z -9.3) |
| [[A-172 (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.224 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.238 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.804 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.214 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.200 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.694 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.40 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.290 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.215 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.222 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5457), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOX10]] | +0.57 | +0.62 / +0.46 | both halves | 3e-05 |  |
| [[LZTR1]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[SHANK3]] | +0.55 | +0.42 / +0.56 | both halves | 4e-05 |  |
| [[CACNA1H]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DPYSL4]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SLC4A3]] | +0.53 | +0.33 / +0.62 | both halves | 1e-04 |  |
| [[SEPTIN5]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[MOCS1]] | +0.52 | +0.45 / +0.57 | both halves | 3e-05 |  |
| [[ARFRP1]] | +0.51 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[RIPOR1]] | +0.51 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[A2M]] | +0.49 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[ANKRD52]] | +0.48 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01019]] | -0.42 | -0.32 / -0.46 | both halves | 1e-04 |  |
| [[TOMM20L-DT]] | -0.42 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[MROH3P]] | -0.42 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[LINC00672]] | -0.41 | -0.40 / -0.37 | both halves | 7e-05 |  |
| [[GAL3ST1]] | -0.41 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[CDK13]] | -0.41 | -0.28 / -0.43 | both halves | 3e-04 |  |
| [[LINC01504]] | -0.41 | -0.43 / -0.24 | both halves | 5e-04 |  |
| [[GP6]] | -0.41 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[AVIL]] | -0.41 | -0.36 / -0.39 | both halves | 9e-05 |  |
| [[GLCCI1]] | -0.40 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[ANKHD1]] | -0.40 | -0.28 / -0.45 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MROH3P]] | B | MROH3P activity lowers KRBA1's level | lines that do not express MROH3P (29) vs lines expressing it (21) | 2.17× higher at baseline in the lines without MROH3P | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[CERS4]] | C | CERS4 activity raises KRBA1's level | lines that do not express CERS4 (17) vs lines expressing it (33) | 3.23× lower at baseline in the lines without CERS4 | 0.028 | ⚠ within organs, on part of the lines; also absent: UPK1A-AS1, PCSK1N, CHST10; co-absent with the target |
| [[SMARCD3]] | C | SMARCD3 activity raises KRBA1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 1.89× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01019]] | B | KRBA1 activity raises LINC01019's level | lines that do not express KRBA1 (13) vs lines expressing it (37) | 1.06× lower at baseline in the lines without KRBA1 | 0.051 | ⚠ within organs, on part of the lines; also absent: C2orf74, SNRPN, DNAAF9 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.529). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 42.7); signed map (-15.8, 43.0). **Vector** length 45.0, 6.32% of its response variance represented; |z| ≥ 3 in 756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.0 | +1.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.2 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.1 | +0.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.0 | +2.7 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.0 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.9 | +2.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -1.5 | -4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -1.4 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.2 | -4.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -2.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.0 | -1.4 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -1.0 | -3.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.1 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | KRAB domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:149,714,781-149,734,575 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1862; previously KRBA1 |
| Gene groups (HGNC) | KRAB domain containing |
| Matched by | ensembl_id |

UniProt [A5PL33](https://www.uniprot.org/uniprotkb/A5PL33) carries no function annotation.

**Summary**, from NCBI Gene [84626](https://www.ncbi.nlm.nih.gov/gene/84626):

> Predicted to be involved in regulation of DNA-templated transcription. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22228) · Entrez [84626](https://www.ncbi.nlm.nih.gov/gene/84626) · UniProt [A5PL33](https://www.uniprot.org/uniprotkb/A5PL33) · Ensembl [ENSG00000133619](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133619)

## Data

Gene col 5457: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5457); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5457, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5457]; `tensor/DDL_lfc|DDL_z.npy` [5457]; `embed/gene_vectors.npy` [5457]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5457 or target_col == 5457). Every well: [[KRBA1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KRBA1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
