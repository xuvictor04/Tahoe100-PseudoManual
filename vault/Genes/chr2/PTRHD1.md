---
symbol: "PTRHD1"
type: "gene"
col: 11592
ensembl_id: "ENSG00000184924"
name: "peptidyl-tRNA hydrolase domain containing 1"
location: "2p23.3"
module: 24
arm: "+"
pooled_cpm: 4.36
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# PTRHD1

*peptidyl-tRNA hydrolase domain containing 1* — 2p23.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.01× (z +9.8, q 5e-20, up in 21 of 22 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0583×).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 15 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHCHD5]] (+0.65, fdr 2e-05), [[SMIM27]] (+0.65, fdr 3e-05), [[ADGRL3-AS1]] (+0.65, fdr 3e-05); moves opposite to [[NOLC1]] (-0.51, fdr 1e-04), [[DNMT1]] (-0.50, fdr 1e-04), [[TFDP1]] (-0.50, fdr 1e-04).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DLL3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11592.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.01×** | +9.8 | 5e-20 | 21/22 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.68×** | +8.9 | 2e-16 | 7/8 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.96×** | +6.6 | 8e-09 | 11/12 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~27% of this change | **1.99×** | +4.9 | 1e-04 | 15/25 (CFPAC-1, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | 1.58× | +3.3 | 0.12 | 9/43 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.38× | +3.2 | 0.12 | 10/46 (CFPAC-1, NCI-H2347, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bendamustine (drug)]] 5 µM |  | 1.59× | +3.2 | 0.12 | 10/37 (A498, SNU-423, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | 1.56× | +3.2 | 0.12 | 10/38 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.35× | +3.1 | 0.14 | 9/36 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11592.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0583×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.600× | -3.6 | 0.19 | 16/35 (SW 900, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | 0.638× | -3.2 | 0.46 | 14/46 (SNU-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11592. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 5.16 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.05 µM 0.0583× (z -10.0) |
| [[A-172 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.05 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.04 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.16 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11592), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 15 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHCHD5]] | +0.65 | +0.47 / +0.73 | both halves | 2e-05 |  |
| [[SMIM27]] | +0.65 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[ADGRL3-AS1]] | +0.65 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[MRPL54]] | +0.65 | +0.45 / +0.70 | both halves | 3e-05 |  |
| [[WDR83OS]] ⚠ | +0.64 | +0.45 / +0.65 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ALKBH7]] | +0.63 | +0.46 / +0.69 | both halves | 2e-05 |  |
| [[ZFAND2A-DT]] | +0.63 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[C11orf1]] | +0.63 | +0.33 / +0.70 | both halves | 1e-04 |  |
| [[MYL6B]] | +0.63 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[APOC1]] | +0.62 | +0.36 / +0.64 | both halves | 1e-04 |  |
| [[NDUFA7]] | +0.60 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[HIGD2A]] | +0.60 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[UXT]] | +0.60 | +0.35 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOLC1]] | -0.51 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[DNMT1]] | -0.50 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[TFDP1]] | -0.50 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[LMNB2]] | -0.50 | -0.29 / -0.54 | both halves | 3e-04 |  |
| [[ITPR3]] | -0.50 | -0.36 / -0.46 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DLL3]] | B | DLL3 activity raises PTRHD1's level | lines that do not express DLL3 (28) vs lines expressing it (22) | 1.32× lower at baseline in the lines without DLL3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LAMC3, FBXO27, INA |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (-42.7, -16.8); signed map (-10.1, 1.4). **Vector** length 38.0, 4.53% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.0 | +3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.2 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.3 | +0.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.3 | +3.3 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.1 | +3.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -1.7 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.2 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.0 | -1.8 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | peptidyl-tRNA hydrolase domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p23.3 — chr2:24,789,728-24,793,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LOC391356; previously C2orf79 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6GMV3](https://www.uniprot.org/uniprotkb/Q6GMV3) (Putative peptidyl-tRNA hydrolase PTRHD1):

> As a putative peptidyl-tRNA hydrolase, it might be involved in releasing tRNAs from the ribosome during protein synthesis (Probable). Some evidence, however, suggests that it lacks peptidyl-tRNA hydrolase activity.

**Summary**, from NCBI Gene [391356](https://www.ncbi.nlm.nih.gov/gene/391356):

> This gene encodes the enzyme peptidyl-tRNA hydrolase. Peptidyl-tRNA hydrolases perform the essential function of recycling peptidyl-tRNAs. Mutations in this gene are associated with autosomal-recessive intellectual disability and parkinsonism. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:33782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33782) · Entrez [391356](https://www.ncbi.nlm.nih.gov/gene/391356) · UniProt [Q6GMV3](https://www.uniprot.org/uniprotkb/Q6GMV3) · Ensembl [ENSG00000184924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184924)

## Data

Gene col 11592: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11592); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11592, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11592]; `tensor/DDL_lfc|DDL_z.npy` [11592]; `embed/gene_vectors.npy` [11592]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11592 or target_col == 11592). Every well: [[PTRHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTRHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
