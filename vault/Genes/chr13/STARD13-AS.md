---
symbol: "STARD13-AS"
type: "gene"
col: 14087
ensembl_id: "ENSG00000236581"
name: "STARD13 antisense RNA"
location: "13q13.1"
module: 21
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# STARD13-AS

*STARD13 antisense RNA* — 13q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.90× (z +10.5, q 4e-23, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +8.3, q 3e-14, up in 20 of 36 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST7-AS2]] (+0.70, fdr 7e-06), [[RBMS3-AS3]] (+0.70, fdr 7e-06), [[SLC13A4]] (+0.70, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[STARD13]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14087.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +10.5 | 4e-23 | 2/5 (HOP62, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +9.4 | 1e-18 | 10/16 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +8.3 | 3e-14 | 20/36 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.47×** | +8.1 | 1e-13 | 1/5 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +4.9 | 1e-04 | 6/14 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.13×** | +4.1 | 0.005 | 8/36 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +4.0 | 0.006 | 10/41 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.6 | 0.025 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.036 | 6/46 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.3 | 0.056 | 0/14 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.24×** | +3.2 | 0.078 | 6/35 (HS-578T, A-172, …) | rises with dose | composition shift |
| [[Pralsetinib (drug)]] 0.05 µM |  | 1.37× | +3.0 | 0.11 | 0/43 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14087.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -4.1 | 0.025 | 17/47 (Panc 03.27, A-427, …) | inconsistent across doses |  |
| [[Balsalazide (sodium hydrate) (drug)]] 0.5 µM |  | 0.719× | -3.4 | 0.20 | 2/44 (LoVo, SW480) | two highest doses | position effect removed |
| [[Benproperine (phosphate) (drug)]] 0.05 µM |  | 0.702× | -3.2 | 0.23 | 7/43 (CFPAC-1, A498, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 5 µM |  | 0.806× | -3.2 | 0.23 | 8/47 (NCI-H1792, H4, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14087. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.12 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14087), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST7-AS2]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 | same gene group |
| [[RBMS3-AS3]] | +0.70 | +0.65 / +0.61 | both halves | 7e-06 | same gene group |
| [[SLC13A4]] | +0.70 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[SAMD4A-AS1]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 | same gene group |
| [[BMAL2-AS1]] | +0.68 | +0.62 / +0.62 | both halves | 7e-06 | same gene group |
| [[SLC8A1-AS1]] | +0.67 | +0.57 / +0.66 | both halves | 1e-05 | same gene group |
| [[MIR4300HG]] | +0.67 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[SYT16]] | +0.67 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[OPCML]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 | same gene group |
| [[A2ML1-AS1]] | +0.66 | +0.52 / +0.66 | both halves | 1e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD13]] | B | STARD13 activity raises STARD13-AS's level | lines that do not express STARD13 (7) vs lines expressing it (43) | 1.42× lower at baseline in the lines without STARD13 | 0.011 | ⚠ within organs, on part of the lines |
| [[PAMR1]] | B | PAMR1 activity raises STARD13-AS's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.26× lower at baseline in the lines without PAMR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[LINC00922]] | B | LINC00922 activity raises STARD13-AS's level | lines that do not express LINC00922 (9) vs lines expressing it (41) | 1.05× lower at baseline in the lines without LINC00922 | 0.060 | ⚠ within organs, on part of the lines; also absent: MGC4859, ENSG00000250149, LINC01811; maybe low, not absent |
| [[CDK6-AS1]] | B | CDK6-AS1 activity raises STARD13-AS's level | lines that do not express CDK6-AS1 (6) vs lines expressing it (44) | 1.32× lower at baseline in the lines without CDK6-AS1 | 0.070 | ⚠ within organs, on part of the lines; also absent: PLS3, CDK6, UACA; maybe low, not absent |
| [[XIRP2]] | C | XIRP2 activity raises STARD13-AS's level | lines that do not express XIRP2 (3) vs lines expressing it (47) | 1.39× lower at baseline in the lines without XIRP2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PDE11A, ENSG00000214803, ENSG00000228566; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (17.6, 26.6); signed map (31.0, 8.8). **Vector** length 34.6, 2.99% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +9.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +2.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.3 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.3 | +2.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.1 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.9 | -0.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.9 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | STARD13 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q13.1 — chr13:33,180,401-33,281,584 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously STARD13-AS2 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40873) · Entrez [100874241](https://www.ncbi.nlm.nih.gov/gene/100874241) · Ensembl [ENSG00000236581](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236581)

## Data

Gene col 14087: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14087); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14087, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14087]; `tensor/DDL_lfc|DDL_z.npy` [14087]; `embed/gene_vectors.npy` [14087]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14087 or target_col == 14087). Every well: [[STARD13-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STARD13-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
