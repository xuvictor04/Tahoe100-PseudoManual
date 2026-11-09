---
symbol: "MILIP"
type: "gene"
col: 15465
ensembl_id: "ENSG00000265688"
name: "MYC inducible lncRNA inactivating p53"
location: "17q25.3"
module: 25
arm: "-"
pooled_cpm: 2.02
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# MILIP

*MYC inducible lncRNA inactivating p53* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.71× (z +8.6, q 6e-15, up in 23 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.295× (z -7.4, q 9e-11, down in 24 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2030 0.0628×).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM131B-AS2]] (+0.70, fdr 7e-06), [[LINC00685]] (+0.67, fdr 1e-05), [[SPATC1]] (+0.65, fdr 7e-06); moves opposite to [[SRP9]] (-0.60, fdr 8e-05), [[PTAR1]] (-0.59, fdr 1e-04), [[LANCL1]] (-0.58, fdr 4e-05).
> It sits in the **-** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15465.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.71×** | +8.6 | 6e-15 | 23/26 (A549, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.63×** | +7.5 | 2e-11 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.75×** | +5.7 | 3e-06 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.62×** | +5.6 | 3e-06 | 11/22 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **2.28×** | +5.0 | 7e-05 | 3/6 (HOP62, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.97×** | +4.1 | 0.004 | 12/31 (CHP-212, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.92×** | +4.0 | 0.006 | 11/26 (A-172, SW480, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.008 | 9/42 (NCI-H2030, A498, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.77×** | +3.3 | 0.052 | 9/27 (SW480, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15465.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Glycyrrhizic acid (drug)]] 5 µM in 1 line (NCI-H2030 0.0628×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.295×** | -7.4 | 9e-11 | 24/37 (SHP-77, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.415×** | -5.3 | 3e-05 | 22/45 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.580× | -3.3 | 0.20 | 12/36 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.581× | -3.1 | 0.23 | 11/43 (BT-474, LS 180, …) | rises with dose | plate-row cell shift; position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 4.35 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 5 µM 0.0628× (z -8.6) |
| [[A-172 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.553 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.931 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.816 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.89 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.935 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.849 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.980 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.729 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM131B-AS2]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[LINC00685]] | +0.67 | +0.57 / +0.73 | both halves | 1e-05 |  |
| [[SPATC1]] | +0.65 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[EXOC3-AS1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[MSX1]] | +0.61 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[PRRT3-AS1]] | +0.58 | +0.49 / +0.64 | both halves | 1e-05 |  |
| [[SPSB2]] | +0.58 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[HYAL1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.56 | +0.46 / +0.57 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[EXOSC4]] | +0.55 | +0.28 / +0.70 | both halves | 3e-04 |  |
| [[ZBTB7A]] | +0.54 | +0.30 / +0.61 | both halves | 2e-04 |  |
| [[ABHD15]] | +0.54 | +0.44 / +0.68 | both halves | 3e-05 |  |
| [[EFNA2]] | +0.54 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP9]] | -0.60 | -0.37 / -0.65 | both halves | 8e-05 |  |
| [[PTAR1]] | -0.59 | -0.36 / -0.66 | both halves | 1e-04 |  |
| [[LANCL1]] | -0.58 | -0.41 / -0.58 | both halves | 4e-05 |  |
| [[DPY19L4]] | -0.58 | -0.36 / -0.64 | both halves | 9e-05 |  |
| [[TMEM237]] | -0.57 | -0.21 / -0.60 | both halves | 7e-04 |  |
| [[DHFR]] | -0.54 | -0.24 / -0.63 | both halves | 4e-04 |  |
| [[MRPL42]] | -0.54 | -0.30 / -0.55 | both halves | 2e-04 |  |
| [[LIN7C]] | -0.54 | -0.08 / -0.66 | ⚠ one half (not replicated) | 0.003 |  |
| [[TMEM106B]] | -0.53 | -0.21 / -0.62 | both halves | 7e-04 |  |
| [[MANEA]] | -0.52 | -0.27 / -0.58 | both halves | 3e-04 |  |
| [[ATPAF1]] | -0.52 | -0.57 / -0.40 | both halves | 4e-05 |  |
| [[BMS1P2]] | -0.51 | -0.33 / -0.55 | both halves | 1e-04 |  |
| [[MDH2]] | -0.51 | -0.58 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MILIP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TOP2B]] | B | TOP2B activity lowers MILIP's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **-** arm (projection on the module's main direction -0.513). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-48.8, 8.8); signed map (11.3, 17.1). **Vector** length 40.9, 5.36% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +8.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +1.8 |
|  | [[Bendamustine (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +1.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.0 | -7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -5.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.9 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.3 | -2.9 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MYC inducible lncRNA inactivating p53 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q25.3 — chr17:81,927,829-81,930,753 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously MAFG-AS1, MAFG-DT |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43649](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43649) · Entrez [92659](https://www.ncbi.nlm.nih.gov/gene/92659) · Ensembl [ENSG00000265688](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000265688)

## Data

Gene col 15465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15465); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15465]; `tensor/DDL_lfc|DDL_z.npy` [15465]; `embed/gene_vectors.npy` [15465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15465 or target_col == 15465). Every well: [[MILIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MILIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
