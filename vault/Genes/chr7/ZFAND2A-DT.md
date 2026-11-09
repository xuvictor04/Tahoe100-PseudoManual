---
symbol: "ZFAND2A-DT"
type: "gene"
col: 13689
ensembl_id: "ENSG00000229043"
name: "ZFAND2A divergent transcript"
location: "7p22.3"
module: 24
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# ZFAND2A-DT

*ZFAND2A divergent transcript* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.76× (z +6.9, q 3e-09, up in 2 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.98× (z +4.8, q 2e-04, up in 12 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.452× (z -5.6, q 1e-05, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCTN6-DT]] (+0.72, fdr 3e-05), [[CHCHD5]] (+0.70, fdr 2e-05), [[FAM182B]] (+0.68, fdr 1e-05); moves opposite to [[NUP188]] (-0.63, fdr 1e-04), [[PSME3]] (-0.61, fdr 8e-05), [[GSPT1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EID2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13689.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +6.9 | 3e-09 | 2/2 (PANC-1, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.27×** | +5.6 | 7e-06 | 7/14 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +5.5 | 8e-06 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.08×** | +5.2 | 3e-05 | 6/16 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.98×** | +4.8 | 2e-04 | 12/33 (A-172, NCI-H23, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +4.5 | 7e-04 | 12/41 (NCI-H2347, A498, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.4 | 1e-03 | 13/30 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.9 | 0.007 | 7/21 (SW1417, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +3.5 | 0.033 | 5/14 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.17×** | +3.3 | 0.065 | 4/18 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.36× | +3.1 | 0.11 | 6/39 (KATO III, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13689.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.452×** | -5.6 | 1e-05 | 22/36 (SNU-423, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -3.9 | 0.018 | 16/44 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.675×** | -3.9 | 0.018 | 15/29 (SHP-77, KATO III, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.610×** | -3.5 | 0.072 | 12/34 (A-172, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 0.641× | -3.1 | 0.20 | 9/36 (HCT15, C-33 A, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.623× | -3.1 | 0.20 | 9/40 (NCI-H23, SNU-423, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13689. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 5.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -9.5) |
| [[A-172 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.669 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.711 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.20 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.25 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.78 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.866 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.724 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.78 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.930 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.656 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.42 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13689), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 8 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCTN6-DT]] | +0.72 | +0.45 / +0.77 | both halves | 3e-05 | same gene group |
| [[CHCHD5]] | +0.70 | +0.46 / +0.70 | both halves | 2e-05 |  |
| [[FAM182B]] | +0.68 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[NDUFB4]] | +0.68 | +0.39 / +0.73 | both halves | 5e-05 |  |
| [[CLN8-AS1]] | +0.68 | +0.46 / +0.72 | both halves | 2e-05 |  |
| [[MINCR]] | +0.68 | +0.43 / +0.75 | both halves | 3e-05 |  |
| [[C11orf1]] | +0.68 | +0.49 / +0.72 | both halves | 1e-05 |  |
| [[ZNF232-AS1]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[AKAP1-DT]] | +0.66 | +0.56 / +0.68 | both halves | 1e-05 | same gene group |
| [[SMIM27]] | +0.65 | +0.49 / +0.69 | both halves | 1e-05 |  |
| [[SNHG19]] | +0.64 | +0.34 / +0.69 | both halves | 1e-04 |  |
| [[IFI27L2]] | +0.64 | +0.50 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP188]] | -0.63 | -0.35 / -0.66 | both halves | 1e-04 |  |
| [[PSME3]] | -0.61 | -0.37 / -0.69 | both halves | 8e-05 |  |
| [[GSPT1]] | -0.61 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[MCM7]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.60 | -0.38 / -0.63 | both halves | 7e-05 |  |
| [[TFDP1]] | -0.59 | -0.52 / -0.58 | both halves | 1e-05 |  |
| [[ELK4]] | -0.59 | -0.36 / -0.68 | both halves | 9e-05 |  |
| [[MTHFD1]] | -0.59 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[NOLC1]] | -0.58 | -0.38 / -0.61 | both halves | 7e-05 |  |
| [[DNMT1]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[SMC1A]] | -0.57 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[IPO5]] | -0.57 | -0.41 / -0.63 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EID2B]] | B | EID2B activity raises ZFAND2A-DT's level | lines that do not express EID2B (13) vs lines expressing it (37) | 1.73× lower at baseline in the lines without EID2B | 0.011 | ⚠ within organs, on part of the lines; also absent: ANTXR1, SIRPA, MSRB3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.708). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-42.3, -16.6); signed map (-9.3, 0.8). **Vector** length 38.3, 4.74% of its response variance represented; |z| ≥ 3 in 762 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.6 | +5.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.4 | +1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.3 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.1 | +1.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | -5.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.5 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.4 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -2.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -2.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.0 | -2.2 |
|  | [[Diphenhydramine (drug)]] 0.05 µM |  | -0.9 | -2.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.9 | -2.3 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -0.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ZFAND2A divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7p22.3 — chr7:1,160,374-1,165,607 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41187](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41187) · Entrez [101927021](https://www.ncbi.nlm.nih.gov/gene/101927021) · Ensembl [ENSG00000229043](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000229043)

## Data

Gene col 13689: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13689); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13689, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13689]; `tensor/DDL_lfc|DDL_z.npy` [13689]; `embed/gene_vectors.npy` [13689]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13689 or target_col == 13689). Every well: [[ZFAND2A-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAND2A-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
