---
symbol: "SMIM27"
type: "gene"
col: 14018
ensembl_id: "ENSG00000235453"
name: "transition zone microprotein 1"
location: "9p21.1"
module: 24
arm: "+"
pooled_cpm: 2.59
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# SMIM27

*transition zone microprotein 1* — 9p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.92× (z +9.7, q 1e-19, up in 30 of 33 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APOC1]] (+0.79, fdr 7e-06), [[C1orf56]] (+0.78, fdr 7e-06), [[SNHG9]] (+0.77, fdr 1e-05); moves opposite to [[PRELID3B]] (-0.67, fdr 7e-06), [[OCRL]] (-0.66, fdr 1e-04), [[LIN7C]] (-0.66, fdr 4e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IFI27L2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14018.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.92×** | +9.7 | 1e-19 | 30/33 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +7.7 | 3e-12 | 3/3 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +7.4 | 2e-11 | 14/14 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +6.1 | 1e-07 | 2/4 (PANC-1, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~26% of this change | **2.03×** | +4.6 | 6e-04 | 9/14 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.67× | +3.2 | 0.13 | 2/15 (PANC-1, Hs 766T) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | 1.64× | +3.2 | 0.13 | 4/26 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | 1.40× | +3.1 | 0.14 | 4/43 (NCI-H2030, SW 900, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.64× | +3.1 | 0.14 | 6/28 (MIA PaCa-2, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~6% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14018. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.01 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.03 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14018), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 7 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APOC1]] | +0.79 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.78 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[SNHG9]] | +0.77 | +0.51 / +0.83 | both halves | 1e-05 |  |
| [[ZNF232-AS1]] | +0.77 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[NDUFC1]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[NDUFB1]] | +0.75 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[TRIM7-AS2]] | +0.74 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[NAA38]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[C1orf122]] | +0.72 | +0.37 / +0.78 | both halves | 7e-05 |  |
| [[TRIM52-AS1]] | +0.72 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | +0.71 | +0.57 / +0.73 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COX6B1]] | +0.71 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[HIGD2A]] | +0.71 | +0.33 / +0.79 | both halves | 1e-04 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.67 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[OCRL]] | -0.66 | -0.35 / -0.70 | both halves | 1e-04 |  |
| [[LIN7C]] | -0.66 | -0.41 / -0.76 | both halves | 4e-05 |  |
| [[NONO]] | -0.63 | -0.42 / -0.70 | both halves | 4e-05 |  |
| [[SACS]] | -0.62 | -0.61 / -0.57 | both halves | 8e-06 |  |
| [[TFDP1]] | -0.61 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[IPO5]] | -0.61 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[NOLC1]] | -0.61 | -0.52 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI27L2]] | B | IFI27L2 activity raises SMIM27's level | lines that do not express IFI27L2 (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without IFI27L2 | 0.084 | ⚠ within organs, on part of the lines |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.744). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.2, -21.9); signed map (-6.7, 3.0). **Vector** length 40.1, 4.79% of its response variance represented; |z| ≥ 3 in 701 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.8 | +9.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.2 | +3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | -0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.2 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.1 | +2.1 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.9 | -1.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -1.1 | -2.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.1 | -1.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | transition zone microprotein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p21.1 — chr9:32,551,144-32,568,621 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C9orf133, TOPORS-AS1, SMIM27 |
| Matched by | ensembl_id |

**Function**, from UniProt [A0A1B0GUW7](https://www.uniprot.org/uniprotkb/A0A1B0GUW7) (Transition zone microprotein 1):

> Required for ciliogenesis.

**Summary**, from NCBI Gene [100129250](https://www.ncbi.nlm.nih.gov/gene/100129250):

> Involved in cilium assembly. Located in ciliary transition zone. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:31420](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31420) · Entrez [100129250](https://www.ncbi.nlm.nih.gov/gene/100129250) · UniProt [A0A1B0GUW7](https://www.uniprot.org/uniprotkb/A0A1B0GUW7) · Ensembl [ENSG00000235453](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000235453)

## Data

Gene col 14018: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14018); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14018, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14018]; `tensor/DDL_lfc|DDL_z.npy` [14018]; `embed/gene_vectors.npy` [14018]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14018 or target_col == 14018). Every well: [[SMIM27 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM27.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
