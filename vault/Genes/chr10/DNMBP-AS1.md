---
symbol: "DNMBP-AS1"
type: "gene"
col: 13608
ensembl_id: "ENSG00000227695"
name: "DNMBP antisense RNA 1"
location: "10q24.2"
module: 165
arm: "+"
pooled_cpm: 2.63
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# DNMBP-AS1

*DNMBP antisense RNA 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.32× (z +13.3, q 8e-38, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.49× (z +6.4, q 2e-08, up in 14 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.908× (z -4.1, q 0.020, down in 16 of 47 measured lines) ⚠ position not correctable. The strongest without an alert is [[Clopidogrel (drug)]] 0.5 µM: 0.732× (z -3.6, q 0.054, down in 4 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RETREG1-AS1]] (+0.64, fdr 1e-05), [[DLGAP2]] (+0.60, fdr 2e-05), [[HMGA2-AS1]] (+0.59, fdr 1e-05).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LINC01234]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13608.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.32×** | +13.3 | 8e-38 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.89×** | +7.3 | 5e-11 | 6/15 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +7.3 | 5e-11 | 2/6 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.49×** | +6.4 | 2e-08 | 14/34 (HEC-1-A, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.8 | 2e-04 | 10/34 (A498, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +4.8 | 2e-04 | 1/5 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 7/44 (HOP62, HT-29, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.0 | 0.004 | 5/27 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +3.8 | 0.010 | 3/32 (NCI-H23, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.5 | 0.026 | 3/14 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.34×** | +3.4 | 0.035 | 2/29 (SNU-423, NCI-H23) | inconsistent across doses | position effect removed |
| [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.096 | 4/33 (SW 900, SW480, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.096 | 2/35 (SW480, A-172) | rises with dose | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.11 | 3/30 (SW480, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13608.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -4.1 | 0.020 | 16/47 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.732×** | -3.6 | 0.054 | 4/44 (HepG2/C3A, A549, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.732×** | -3.6 | 0.054 | 7/44 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.807×** | -3.5 | 0.055 | 9/43 (Panc 03.27, HOP62, …) | rises with dose | position effect removed |
| [[Phenytoin (sodium) (drug)]] 5 µM |  | 0.757× | -3.1 | 0.20 | 5/43 (SNU-1, NCI-H460, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13608. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 1.92 | 0 | 2 | — | [[Bicalutamide (drug)]] 5 µM 0.159× (z -19.7) |
| [[NCI-H1573 (line)]] | alt | 2.85 | 0 | 1 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 0.05 µM 0.0816× (z -8.5) |
| [[A-172 (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.94 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.87 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.85 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13608), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RETREG1-AS1]] | +0.64 | +0.67 / +0.51 | both halves | 1e-05 | same gene group |
| [[DLGAP2]] | +0.60 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[HMGA2-AS1]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 | same gene group |
| [[EVI2B]] | +0.59 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PECAM1]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[LINC01579]] | +0.57 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[PICART1]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[COL23A1]] | +0.57 | +0.37 / +0.55 | both halves | 8e-05 |  |
| [[RYR3]] | +0.56 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[RYR1]] | +0.55 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[CNTNAP5]] | +0.55 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[INSYN2A]] | +0.55 | +0.35 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01234]] | B | LINC01234 activity lowers DNMBP-AS1's level | lines that do not express LINC01234 (12) vs lines expressing it (38) | 1.13× higher at baseline in the lines without LINC01234 | 0.064 | ⚠ within organs, on part of the lines; also absent: NXPH4, COP1-DT, LINC00276; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.650). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.5, 31.3); signed map (29.7, 16.6). **Vector** length 32.8, 2.66% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.7 | +13.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.1 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +0.7 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -1.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.0 | -3.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -0.9 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -0.9 | +0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -0.9 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | DNMBP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 10q24.2 — chr10:99,927,010-99,959,050 (+) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ40792, bA287G8.2; previously NCRNA00093 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:20431](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20431) · Entrez [100188954](https://www.ncbi.nlm.nih.gov/gene/100188954) · Ensembl [ENSG00000227695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000227695)

## Data

Gene col 13608: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13608); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13608, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13608]; `tensor/DDL_lfc|DDL_z.npy` [13608]; `embed/gene_vectors.npy` [13608]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13608 or target_col == 13608). Every well: [[DNMBP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNMBP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
