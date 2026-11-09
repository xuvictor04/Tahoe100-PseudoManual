---
symbol: "ABHD14A"
type: "gene"
col: 14542
ensembl_id: "ENSG00000248487"
name: "abhydrolase domain containing 14A"
location: "3p21.2"
module: 24
arm: "+"
pooled_cpm: 2.22
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 2
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ABHD14A

*abhydrolase domain containing 14A* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.47× (z +9.3, q 5e-18, up in 19 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.505× (z -7.1, q 1e-09, down in 25 of 33 measured lines).
> Its strongest partners by |cos| (81 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT2]] (+0.60, fdr 1e-04), [[ABHD15]] (+0.59, fdr 6e-05), [[RAF1]] (+0.59, fdr 8e-05); moves opposite to [[R3HDM4]] (-0.52, fdr 5e-04), [[RNF123]] (-0.51, fdr 5e-04), [[TAF1]] (-0.47, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.47×** | +9.3 | 5e-18 | 19/28 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +9.3 | 6e-18 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +7.4 | 2e-11 | 11/11 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.46×** | +6.3 | 3e-08 | 10/12 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.73×** | +5.7 | 1e-06 | 8/43 (NCI-H2347, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +5.2 | 2e-05 | 1/3 (HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.67×** | +3.8 | 0.014 | 7/13 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.55× | +3.1 | 0.14 | 6/24 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.51× | +3.0 | 0.16 | 4/44 (HepG2/C3A, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.505×** | -7.1 | 1e-09 | 25/33 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.541×** | -4.2 | 0.007 | 16/36 (A-172, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -4.1 | 0.008 | 15/31 (NCI-H23, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.602×** | -3.7 | 0.029 | 13/43 (HT-29, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.628×** | -3.4 | 0.077 | 13/40 (A-427, MIA PaCa-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.574 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.763 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.868 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.69 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.573 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 19 of them with an alert (⚠; 19 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT2]] | +0.60 | +0.33 / +0.61 | both halves | 1e-04 |  |
| [[ABHD15]] | +0.59 | +0.39 / +0.61 | both halves | 6e-05 | same gene group; STRING 530 |
| [[RAF1]] | +0.59 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[ENDOG]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZNF232-AS1]] | +0.58 | +0.40 / +0.60 | both halves | 4e-05 |  |
| [[TLCD1]] | +0.57 | +0.17 / +0.63 | ⚠ one half (not replicated) | 0.001 |  |
| [[PANK1]] | +0.57 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[SMIM27]] | +0.56 | +0.30 / +0.59 | both halves | 2e-04 |  |
| [[TMEM98]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[EED]] | +0.56 | +0.26 / +0.57 | both halves | 3e-04 |  |
| [[MFSD14A]] | +0.54 | +0.40 / +0.25 | both halves | 4e-04 |  |
| [[FMC1]] | +0.54 | +0.36 / +0.57 | both halves | 1e-04 |  |
| [[LAMTOR2]] | +0.52 | +0.48 / +0.59 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[R3HDM4]] | -0.52 | -0.23 / -0.54 | both halves | 5e-04 |  |
| [[RNF123]] | -0.51 | -0.24 / -0.45 | both halves | 5e-04 |  |
| [[TAF1]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[UVSSA]] | -0.46 | -0.36 / -0.39 | both halves | 1e-04 |  |
| [[LIMS1]] | -0.46 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[GRIPAP1]] | -0.45 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[KCTD21]] | -0.45 | -0.33 / -0.28 | both halves | 3e-04 |  |
| [[SAMD4B]] | -0.45 | -0.36 / -0.39 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises ABHD14A's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC00847]] | C | LINC00847 activity lowers ABHD14A's level | lines that do not express LINC00847 (4) vs lines expressing it (46) | 1.73× higher at baseline in the lines without LINC00847 | 0.053 | ⚠ few lines (4 vs 46); across organs; also absent: DDR1, FTH1, HEIH; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.349). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.6, 18.8); signed map (17.6, -6.9). **Vector** length 37.3, 3.99% of its response variance represented; |z| ≥ 3 in 807 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +9.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.9 | +6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.0 | +3.0 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.4 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.3 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.2 | -3.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -3.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -2.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | abhydrolase domain containing 14A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,971,426-51,981,196 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564O243, DORZ1 |
| Gene groups (HGNC) | Abhydrolase domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BUJ0](https://www.uniprot.org/uniprotkb/Q9BUJ0) (Protein ABHD14A):

> Possible role in granule neuron development.

**Summary**, from NCBI Gene [25864](https://www.ncbi.nlm.nih.gov/gene/25864):

> Predicted to enable hydrolase activity. Predicted to be located in membrane. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24538](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24538) · Entrez [25864](https://www.ncbi.nlm.nih.gov/gene/25864) · UniProt [Q9BUJ0](https://www.uniprot.org/uniprotkb/Q9BUJ0) · Ensembl [ENSG00000248487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000248487)

## Data

Gene col 14542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14542); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14542]; `tensor/DDL_lfc|DDL_z.npy` [14542]; `embed/gene_vectors.npy` [14542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14542 or target_col == 14542). Every well: [[ABHD14A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABHD14A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
