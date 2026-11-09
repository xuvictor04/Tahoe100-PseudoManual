---
symbol: "PRKCA-AS1"
type: "gene"
col: 15443
ensembl_id: "ENSG00000264630"
name: "PRKCA antisense RNA 1"
location: "17q24.2"
module: 21
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# PRKCA-AS1

*PRKCA antisense RNA 1* — 17q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.83× (z +12.4, q 1e-32, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.70× (z +7.2, q 1e-10, up in 14 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.812× (z -7.1, q 6e-10, down in 29 of 47 measured lines) ⚠ position not correctable.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL2-DT]] (+0.80, fdr 7e-06), [[CHMP3-AS1]] (+0.77, fdr 7e-06), [[HSPA2-AS1]] (+0.75, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[IRF4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15443.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.83×** | +12.4 | 1e-32 | 2/5 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.80×** | +9.9 | 1e-20 | 14/17 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +7.2 | 1e-10 | 14/34 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +6.3 | 5e-08 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.1 | 1e-07 | 20/35 (HCT15, A-172, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +4.8 | 2e-04 | 11/29 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +4.7 | 2e-04 | 12/29 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.7 | 2e-04 | 11/28 (KATO III, AsPC-1, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.62×** | +4.6 | 3e-04 | 5/13 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.004 | 7/35 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~8% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.47×** | +3.5 | 0.020 | 3/36 (PANC-1, NCI-H23, …) | top dose only | position effect removed |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.039 | 7/37 (AsPC-1, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.3 | 0.039 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.2 | 0.055 | 1/15 (NCI-H460) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.83×** | +3.0 | 0.091 | 0/11 | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +3.0 | 0.091 | 6/40 (SNU-423, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15443.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.812×** | -7.1 | 6e-10 | 29/47 (hTERT-HPNE, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15443. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15443), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL2-DT]] | +0.80 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | same gene group |
| [[HSPA2-AS1]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 | same gene group |
| [[TICAM2-AS1]] | +0.74 | +0.65 / +0.75 | both halves | 7e-06 | same gene group |
| [[CNTNAP5]] | +0.74 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[EHBP1-AS1]] | +0.74 | +0.67 / +0.69 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.74 | +0.61 / +0.75 | both halves | 7e-06 | same gene group |
| [[OMG]] | +0.74 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.73 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[RN7SL2]] | +0.72 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[C12orf40]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[USH2A]] | +0.72 | +0.67 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF4]] | B | IRF4 activity raises PRKCA-AS1's level | lines that do not express IRF4 (34) vs lines expressing it (16) | 1.12× lower at baseline in the lines without IRF4 | 0.065 | ⚠ within organs, on part of the lines; also absent: CHL1, CPS1, UPK1B |
| [[S100A13]] | C | S100A13 activity raises PRKCA-AS1's level | lines that do not express S100A13 (4) vs lines expressing it (46) | 1.22× lower at baseline in the lines without S100A13 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CASP4, SP100, KIFC3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 28.1); signed map (33.3, 6.7). **Vector** length 29.6, 2.10% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +9.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +12.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.1 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.5 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | +0.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | PRKCA antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q24.2 — chr17:66,398,069-66,416,854 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51347](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51347) · Entrez [101928001](https://www.ncbi.nlm.nih.gov/gene/101928001) · Ensembl [ENSG00000264630](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000264630)

## Data

Gene col 15443: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15443); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15443, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15443]; `tensor/DDL_lfc|DDL_z.npy` [15443]; `embed/gene_vectors.npy` [15443]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15443 or target_col == 15443). Every well: [[PRKCA-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRKCA-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
