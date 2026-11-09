---
symbol: "MME-AS1"
type: "gene"
col: 14245
ensembl_id: "ENSG00000240666"
name: "MME antisense RNA 1"
location: "3q25.2"
module: 21
arm: "+"
pooled_cpm: 2.23
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MME-AS1

*MME antisense RNA 1* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.08× (z +9.3, q 9e-18, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Temsirolimus (drug)]] 0.5 µM: 1.48× (z +3.4, q 0.048, up in 4 of 19 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.0586×; ⚠ cell-cycle shift, explains ~33% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL2]] (+0.65, fdr 1e-05), [[MME]] (+0.65, fdr 7e-06, ⚠ same locus), [[RHOQ-AS1]] (+0.64, fdr 1e-05), [[A2ML1-AS1]] (+0.63, fdr 3e-05); moves opposite to [[PRELID3B]] (-0.51, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MME]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14245.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.08×** | +9.3 | 9e-18 | 1/3 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +7.9 | 9e-13 | 5/11 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.93×** | +5.6 | 3e-06 | 1/8 (LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +5.5 | 5e-06 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.54×** | +3.7 | 0.023 | 3/18 (J82, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.82×** | +3.7 | 0.024 | 1/5 (hTERT-HPNE) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.48×** | +3.4 | 0.048 | 4/19 (A-172, hTERT-HPNE, …) | inconsistent across doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.048 | 1/30 (PANC-1) | rises with dose | position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.048 | 4/23 (J82, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +3.3 | 0.057 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.077 | 1/20 (LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.1 | 0.077 | 0/2 | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.1 | 0.089 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14245.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (SNU-423 0.0586×; ⚠ cell-cycle shift, explains ~33% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.861× | -4.8 | 1e-03 | 14/46 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14245. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 4.26 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0586× (z -9.1) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-172 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.16 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.23 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.02 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.68 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14245), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 12 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL2]] | +0.65 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[MME]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RHOQ-AS1]] | +0.64 | +0.53 / +0.68 | both halves | 1e-05 | same gene group |
| [[A2ML1-AS1]] | +0.63 | +0.45 / +0.69 | both halves | 3e-05 | same gene group |
| [[ZRANB2-AS1]] | +0.62 | +0.46 / +0.65 | both halves | 3e-05 | same gene group |
| [[CCDC65]] | +0.62 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[RN7SL1]] | +0.62 | +0.46 / +0.62 | both halves | 3e-05 |  |
| [[FAM217A]] | +0.62 | +0.46 / +0.62 | both halves | 2e-05 |  |
| [[TICAM2-AS1]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 | same gene group |
| [[KIZ-AS1]] ⚠ | +0.61 | +0.57 / +0.58 | both halves | 8e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[SLC26A5]] | +0.61 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[BIRC6-AS2-1]] | +0.61 | +0.38 / +0.71 | both halves | 7e-05 |  |
| [[LRRC37A16P]] | +0.60 | +0.35 / +0.64 | both halves | 1e-04 |  |
| [[C2CD5-AS1]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRELID3B]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MME]] | B | MME activity raises MME-AS1's level | lines that do not express MME (30) vs lines expressing it (20) | 1.90× lower at baseline in the lines without MME | 3e-04 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[NETO1]] | B | NETO1 activity raises MME-AS1's level | lines that do not express NETO1 (43) vs lines expressing it (7) | 1.84× lower at baseline in the lines without NETO1 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, GPR15, SYT4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.658). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 29.6); signed map (35.6, 5.6). **Vector** length 36.8, 3.72% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +5.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +0.9 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.1 | -2.1 |
|  | [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -0.9 | -1.3 |
|  | [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.8 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | MME antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q25.2 — chr3:155,158,370-155,183,285 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40376](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40376) · Entrez [100873918](https://www.ncbi.nlm.nih.gov/gene/100873918) · Ensembl [ENSG00000240666](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240666)

## Data

Gene col 14245: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14245); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14245, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14245]; `tensor/DDL_lfc|DDL_z.npy` [14245]; `embed/gene_vectors.npy` [14245]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14245 or target_col == 14245). Every well: [[MME-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MME-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
