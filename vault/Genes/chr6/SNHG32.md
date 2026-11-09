---
symbol: "SNHG32"
type: "gene"
col: 12864
ensembl_id: "ENSG00000204387"
name: "small nucleolar RNA host gene 32"
location: "6p21.33"
module: 20
arm: "-"
pooled_cpm: 68.48
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# SNHG32

*small nucleolar RNA host gene 32* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 2.25× (z +4.9, q 3e-04, up in 40 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPB41L4A-AS1]] (+0.88, fdr 7e-06), [[SNHG8]] (+0.87, fdr 7e-06), [[SNHG7]] (+0.85, fdr 7e-06); moves opposite to [[VMA21]] (-0.74, fdr 7e-06), [[TGOLN2]] (-0.73, fdr 7e-06), [[TARDBP]] (-0.71, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12864.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +4.9 | 3e-04 | 40/48 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.76×** | +4.9 | 3e-04 | 34/48 (AsPC-1, HEC-1-A, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +4.5 | 0.002 | 44/48 (A-427, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.003 | 33/48 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +4.0 | 0.007 | 40/48 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.06×** | +3.7 | 0.024 | 37/49 (SHP-77, HCT15, …) | two highest doses | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 5 µM |  | 1.72× | +3.2 | 0.11 | 39/48 (A-427, NCI-H23, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | 1.71× | +3.1 | 0.12 | 31/50 (H4, RKO, …) | top dose only | cell-cycle shift (explains ~1% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12864.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | 0.585× | -3.2 | 0.50 | 32/48 (PANC-1, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.575× | -3.1 | 0.50 | 32/47 (LOX-IMVI, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12864. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 53.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +9.5) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[C32 (line)]] | wt | 44.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +8.6) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[HEC-1-A (line)]] | alt | 40.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +8.8) ⚠ cell-cycle shift, explains ~40% of this change | — |
| [[A-172 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 42.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 64.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 75.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 204 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 65.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 99.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 77.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 69.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 79.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 56.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12864), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 17 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L4A-AS1]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | same gene group |
| [[SNHG8]] | +0.87 | +0.85 / +0.87 | both halves | 7e-06 | same gene group |
| [[SNHG7]] | +0.85 | +0.85 / +0.88 | both halves | 7e-06 | same gene group |
| [[SNHG6]] | +0.84 | +0.79 / +0.90 | both halves | 7e-06 | same gene group |
| [[SNHG12]] | +0.83 | +0.82 / +0.81 | both halves | 7e-06 | same gene group |
| [[NACA4P]] ⚠ | +0.78 | +0.64 / +0.84 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[ATF4]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[TAF1D]] | +0.75 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[NKAP]] | +0.74 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | +0.73 | +0.69 / +0.74 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RBMX2]] | +0.73 | +0.76 / +0.69 | both halves | 7e-06 |  |
| [[ZFAS1]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 | same gene group |
| [[ADPRM]] | +0.72 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.71 | +0.64 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.74 | -0.65 / -0.70 | both halves | 7e-06 |  |
| [[TGOLN2]] | -0.73 | -0.71 / -0.69 | both halves | 7e-06 |  |
| [[TARDBP]] | -0.71 | -0.54 / -0.76 | both halves | 1e-05 |  |
| [[TMX1]] | -0.71 | -0.69 / -0.68 | both halves | 7e-06 |  |
| [[EIF5A]] | -0.71 | -0.70 / -0.61 | both halves | 7e-06 |  |
| [[CDK2]] | -0.69 | -0.76 / -0.61 | both halves | 7e-06 |  |
| [[FKBP1A]] | -0.69 | -0.70 / -0.64 | both halves | 7e-06 |  |
| [[BANF1]] | -0.69 | -0.68 / -0.64 | both halves | 7e-06 |  |
| [[RBBP7]] | -0.69 | -0.67 / -0.62 | both halves | 7e-06 |  |
| [[NUP155]] | -0.67 | -0.61 / -0.68 | both halves | 7e-06 |  |
| [[EMC1]] | -0.66 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[GPAA1]] | -0.66 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.654). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.7, -28.7); signed map (-15.3, -2.3). **Vector** length 107, 47.6% of its response variance represented; |z| ≥ 3 in 541 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.8 | +4.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.8 | +1.7 |
|  | [[Adagrasib (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +0.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +1.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.9 | +1.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.7 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.3 | +3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.1 | -3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.1 | -2.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.6 | -0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.6 | -1.5 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -2.5 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 32 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21.33 — chr6:31,834,608-31,839,766 (+) |
| Ensembl biotype | lncRNA |
| Also known as | D6S57, G8; previously C6orf48 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [50854](https://www.ncbi.nlm.nih.gov/gene/50854):

> Predicted to enable double-stranded RNA binding activity. Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19078](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19078) · Entrez [50854](https://www.ncbi.nlm.nih.gov/gene/50854) · Ensembl [ENSG00000204387](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204387)

## Data

Gene col 12864: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12864); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12864, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12864]; `tensor/DDL_lfc|DDL_z.npy` [12864]; `embed/gene_vectors.npy` [12864]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12864 or target_col == 12864). Every well: [[SNHG32 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG32.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
