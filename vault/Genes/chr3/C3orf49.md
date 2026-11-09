---
symbol: "C3orf49"
type: "gene"
col: 8738
ensembl_id: "ENSG00000163632"
name: "chromosome 3 open reading frame 49"
location: "3p14.1"
module: 21
arm: "+"
pooled_cpm: 2.4
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# C3orf49

*chromosome 3 open reading frame 49* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.00× (z +9.8, q 5e-20, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +7.2, q 1e-10, up in 9 of 16 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.158×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.135×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PART1]] (+0.77, fdr 7e-06), [[C1orf56]] (+0.67, fdr 7e-06), [[ST7-AS2]] (+0.66, fdr 1e-05); moves opposite to [[SIGMAR1]] (-0.58, fdr 2e-05), [[SLC25A39]] (-0.57, fdr 1e-04), [[ICMT]] (-0.57, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TBXT]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 8 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.00×** | +9.8 | 5e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.08×** | +8.9 | 1e-16 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +7.2 | 1e-10 | 9/16 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.38×** | +7.1 | 1e-10 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.14×** | +4.6 | 4e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.98×** | +4.3 | 0.001 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.7 | 0.020 | 0/5 | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.76×** | +3.6 | 0.026 | 0/6 | top dose only | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.12×** | +3.4 | 0.044 | 0/5 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.44×** | +3.2 | 0.071 | 0/21 | top dose only | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8738.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.158×); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H460 0.135×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.604× | -3.0 | 0.96 | 4/36 (KATO III, BT-474, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -12.0) |
| [[A-172 (line)]] | wt | 0.911 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.635 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.703 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.821 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.802 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.933 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.863 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.934 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.800 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.836 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.992 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.898 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.771 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.924 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.853 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.812 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.936 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.865 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.750 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.859 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.740 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.813 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.798 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.817 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.764 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.984 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.842 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.844 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.925 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.999 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.917 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.964 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PART1]] | +0.77 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.67 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.66 | +0.61 / +0.57 | both halves | 1e-05 |  |
| [[LINC02755]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[CNTNAP4]] | +0.64 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SLC23A1]] | +0.62 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[C11orf71]] | +0.62 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[AQP4-AS1]] | +0.62 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[MLANA]] | +0.62 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[C12orf40]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[LRRN3]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[PKD2L2]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIGMAR1]] | -0.58 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[SLC25A39]] | -0.57 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[ICMT]] | -0.57 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[TTLL12]] | -0.56 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[MTHFD1]] | -0.55 | -0.39 / -0.51 | both halves | 5e-05 |  |
| [[IDH3A]] | -0.54 | -0.19 / -0.49 | ⚠ not reproduced | 8e-04 |  |
| [[CS]] | -0.53 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[TGOLN2]] | -0.53 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[FKBP1A]] | -0.52 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[AGO1]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SLC29A1]] | -0.51 | -0.57 / -0.29 | both halves | 3e-04 |  |
| [[PHF6]] | -0.51 | -0.34 / -0.39 | both halves | 1e-04 |  |
| [[APEH]] | -0.51 | -0.43 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBXT]] | C | TBXT activity raises C3orf49's level | lines that do not express TBXT (47) vs lines expressing it (3) | 4.19× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (18.0, 26.1); signed map (32.3, 8.0). **Vector** length 23.6, 2.08% of its response variance represented; |z| ≥ 3 in 801 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.6 | +7.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +1.9 | +3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +8.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.8 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.7 | +3.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | +0.7 | +0.5 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.7 | +1.5 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.6 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | -0.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -3.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.7 | -1.9 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -0.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | chromosome 3 open reading frame 49 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:63,819,299-63,848,636 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q96BT1](https://www.uniprot.org/uniprotkb/Q96BT1) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25190](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25190) · Entrez [132200](https://www.ncbi.nlm.nih.gov/gene/132200) · UniProt [Q96BT1](https://www.uniprot.org/uniprotkb/Q96BT1) · Ensembl [ENSG00000163632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163632)

## Data

Gene col 8738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8738); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8738]; `tensor/DDL_lfc|DDL_z.npy` [8738]; `embed/gene_vectors.npy` [8738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8738 or target_col == 8738). Every well: [[C3orf49 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C3orf49.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
