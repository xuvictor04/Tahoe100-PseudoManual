---
symbol: "HYDIN"
type: "gene"
col: 8068
ensembl_id: "ENSG00000157423"
name: "HYDIN axonemal central pair apparatus protein"
location: "16q22.2"
module: 61
arm: "+"
pooled_cpm: 3.96
n_lines_expressing: 41
n_dd_up: 33
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# HYDIN

*HYDIN axonemal central pair apparatus protein* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.42× (z +22.8, q 0e+00, up in 23 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC80]] (+0.63, fdr 7e-06), [[ANKRD31]] (+0.63, fdr 7e-06), [[KCNH1]] (+0.62, fdr 1e-05).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[NEMP2-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8068.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.42×** | +22.8 | 0e+00 | 23/25 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.01×** | +21.3 | 0e+00 | 18/24 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.41×** | +19.3 | 0e+00 | 2/4 (NCI-H2347, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.14×** | +17.7 | 0e+00 | 6/10 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.42×** | +14.9 | 0e+00 | 4/5 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.95×** | +11.7 | 1e-29 | 19/28 (RKO, HT-29, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.66×** | +10.6 | 3e-24 | 24/35 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.50×** | +9.9 | 2e-21 | 19/24 (NCI-H2030, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.89×** | +9.7 | 2e-20 | 14/33 (HOP62, Panc 03.27, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.40×** | +9.5 | 1e-19 | 21/32 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +8.8 | 9e-17 | 23/31 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.02×** | +7.6 | 1e-12 | 16/32 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.96×** | +7.3 | 1e-11 | 11/19 (Panc 03.27, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +6.8 | 5e-10 | 4/22 (SW 900, A549, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.4 | 5e-09 | 5/35 (NCI-H2030, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.85×** | +6.4 | 5e-09 | 14/30 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.65×** | +5.5 | 2e-06 | 17/35 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +4.7 | 7e-05 | 7/35 (C32, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8068.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vortioxetine (drug)]] 0.5 µM |  | 0.744× | -3.2 | 0.42 | 3/35 (NCI-H2030, RKO, …) | inconsistent across doses |  |
| [[Berberine (chloride hydrate) (drug)]] 5 µM |  | 0.813× | -3.2 | 0.42 | 4/36 (H4, HepG2/C3A, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.737× | -3.1 | 0.42 | 4/34 (hTERT-HPNE, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8068. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.09 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +14.6) | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +8.5) | — |
| [[NCI-H2347 (line)]] | alt | 3.85 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +9.0) | — |
| [[A-172 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.938 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.900 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.969 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.905 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.974 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.990 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8068), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC80]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ANKRD31]] | +0.63 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[KCNH1]] | +0.62 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[ERC2]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[XKR4]] | +0.60 | +0.74 / +0.49 | both halves | 1e-05 |  |
| [[GRIA4]] | +0.60 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[SPAG17]] | +0.59 | +0.65 / +0.58 | both halves | 7e-06 | STRING 626 |
| [[CACNA1E]] | +0.59 | +0.70 / +0.45 | both halves | 3e-05 |  |
| [[SLC35F1]] | +0.59 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[PCDH11X]] | +0.58 | +0.65 / +0.38 | both halves | 7e-05 | same gene group |
| [[LRRIQ1]] | +0.58 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[NEMP2-DT]] | +0.58 | +0.65 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HYDIN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KCNH7]] | B | KCNH7 activity raises HYDIN's level | lines that do not express KCNH7 (35) vs lines expressing it (15) | 1.84× lower at baseline in the lines without KCNH7 | 0.097 | ⚠ within organs, on part of the lines; also absent: FUT9, ENSG00000289309, PI15; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEMP2-DT]] | B | HYDIN activity lowers NEMP2-DT's level | lines that do not express HYDIN (9) vs lines expressing it (41) | 2.11× higher at baseline in the lines without HYDIN | 0.048 | ⚠ within organs, on part of the lines; also absent: SNRPN, ZNF613, MOCS1; maybe low, not absent |
| [[NSF]] | B | HYDIN activity raises NSF's level | lines that do not express HYDIN (9) vs lines expressing it (41) | 1.15× lower at baseline in the lines without HYDIN | 0.096 | ⚠ within organs, on part of the lines; also absent: SNRPN, ZNF613, MOCS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 30.3); signed map (33.4, 20.4). **Vector** length 39.9, 5.41% of its response variance represented; |z| ≥ 3 in 790 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.5 | +19.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +17.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.0 | +14.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +22.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +21.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +6.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.4 | +2.6 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.3 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -0.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | HYDIN axonemal central pair apparatus protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:70,802,084-71,230,722 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp434D0513, KIAA1864, PPP1R31, CILD5 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0P3](https://www.uniprot.org/uniprotkb/Q4G0P3) (Axonemal central pair apparatus protein HYDIN):

> Required for ciliary motility (By similarity). Required for localization of SPEF2 to the ciliary axoneme in ciliated respiratory epithelial cells.

**Summary**, from NCBI Gene [54768](https://www.ncbi.nlm.nih.gov/gene/54768):

> This gene encodes a protein that may be involved in cilia motility. Mutations in this gene cause of autosomal recessive primary ciliary dyskinesia-5, a disorder characterized by the accumulation of cerebrospinal fluid within the ventricles of the brain. A duplicate copy of this gene has been found in humans on chromosome 1. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:19368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19368) · Entrez [54768](https://www.ncbi.nlm.nih.gov/gene/54768) · UniProt [Q4G0P3](https://www.uniprot.org/uniprotkb/Q4G0P3) · Ensembl [ENSG00000157423](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157423)

## Data

Gene col 8068: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8068); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8068, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8068]; `tensor/DDL_lfc|DDL_z.npy` [8068]; `embed/gene_vectors.npy` [8068]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8068 or target_col == 8068). Every well: [[HYDIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HYDIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
