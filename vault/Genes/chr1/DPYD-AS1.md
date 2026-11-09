---
symbol: "DPYD-AS1"
type: "gene"
col: 13872
ensembl_id: "ENSG00000232878"
name: "DPYD antisense RNA 1"
location: "1p21.3"
module: 140
arm: "+"
pooled_cpm: 2.24
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 0
n_dd_up_clean: 14
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/140"]
generated_by: "tahoemap"
---

# DPYD-AS1

*DPYD antisense RNA 1* — 1p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.04× (z +14.8, q 0e+00, up in 28 of 31 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4300HG]] (+0.80, fdr 7e-06), [[A2ML1-AS1]] (+0.79, fdr 7e-06), [[USH2A]] (+0.78, fdr 7e-06).
> It is in [[Module 140]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.04×** | +14.8 | 0e+00 | 28/31 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +10.0 | 6e-21 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +9.8 | 3e-20 | 9/13 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.29×** | +7.8 | 9e-13 | 22/41 (NCI-H1792, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.51×** | +6.7 | 2e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.70×** | +5.0 | 6e-05 | 2/13 (SW480, A498) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +4.8 | 1e-04 | 4/23 (SW480, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +4.8 | 1e-04 | 7/33 (A-172, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +4.8 | 1e-04 | 12/43 (NCI-H1792, KATO III, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +4.5 | 4e-04 | 10/38 (C32, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +4.3 | 0.001 | 5/32 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.002 | 5/44 (A-172, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +3.7 | 0.008 | 6/37 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.6 | 0.013 | 0/3 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.6 | 0.014 | 5/23 (C32, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +3.4 | 0.024 | 3/27 (HEC-1-A, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.026 | 6/38 (NCI-H460, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.065 | 5/43 (SK-MEL-2, NCI-H460, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.40×** | +3.0 | 0.067 | 2/33 (HEC-1-A, A498) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.072 | 3/23 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.54×** | +2.9 | 0.093 | 2/36 (Hs 766T, A498) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.874× | -4.3 | 0.008 | 14/46 (J82, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4300HG]] | +0.80 | +0.66 / +0.80 | both halves | 7e-06 |  |
| [[A2ML1-AS1]] | +0.79 | +0.68 / +0.71 | both halves | 7e-06 | same gene group |
| [[USH2A]] | +0.78 | +0.65 / +0.80 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.77 | +0.65 / +0.75 | both halves | 7e-06 | same gene group |
| [[SLC23A1]] | +0.76 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[SCHLAP1]] | +0.76 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.75 | +0.58 / +0.69 | both halves | 7e-06 | same gene group |
| [[CNTNAP5]] | +0.74 | +0.60 / +0.77 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.74 | +0.60 / +0.67 | both halves | 7e-06 | same gene group |
| [[GALNTL6]] | +0.74 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.73 | +0.54 / +0.71 | both halves | 1e-05 | same gene group |
| [[LUZP2]] | +0.73 | +0.55 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DPYD-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ENTHD1]] | B | ENTHD1 activity raises DPYD-AS1's level | lines that do not express ENTHD1 (28) vs lines expressing it (22) | 1.35× lower at baseline in the lines without ENTHD1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CRLF2, TNFAIP6, ENSG00000289600 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 140]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.4, 27.9); signed map (33.4, 8.5). **Vector** length 41.7, 4.64% of its response variance represented; |z| ≥ 3 in 888 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +6.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +4.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.5 | +3.0 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -4.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | +0.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | DPYD antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p21.3 — chr1:97,095,923-97,322,955 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40195) · Entrez [100873932](https://www.ncbi.nlm.nih.gov/gene/100873932) · Ensembl [ENSG00000232878](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232878)

## Data

Gene col 13872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13872); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13872]; `tensor/DDL_lfc|DDL_z.npy` [13872]; `embed/gene_vectors.npy` [13872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13872 or target_col == 13872). Every well: [[DPYD-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYD-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
