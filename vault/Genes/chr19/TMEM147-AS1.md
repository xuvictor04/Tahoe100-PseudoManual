---
symbol: "TMEM147-AS1"
type: "gene"
col: 14063
ensembl_id: "ENSG00000236144"
name: "TMEM147 antisense RNA 1"
location: "19q13.12"
module: 1
arm: "+"
pooled_cpm: 2.42
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 0
n_dd_up_clean: 6
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# TMEM147-AS1

*TMEM147 antisense RNA 1* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.52× (z +9.1, q 4e-17, up in 3 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +4.1, q 0.005, up in 7 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADCK1]] (+0.73, fdr 1e-05), [[DPH5-DT]] (+0.69, fdr 1e-05), [[KICS2]] (+0.69, fdr 1e-05); moves opposite to [[GNB2]] (-0.66, fdr 1e-05), [[ARL3]] (-0.65, fdr 1e-05), [[MGST3]] (-0.63, fdr 6e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MIR1915HG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14063.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.52×** | +9.1 | 4e-17 | 3/3 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +7.9 | 6e-13 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.34×** | +6.7 | 5e-09 | 7/11 (HS-578T, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.4 | 0.002 | 2/9 (KATO III, HOP62) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.005 | 7/25 (HEC-1-A, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.8 | 0.011 | 9/35 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.95×** | +3.7 | 0.015 | 1/13 (HEC-1-A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.018 | 9/32 (HOP62, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +3.5 | 0.027 | 7/29 (Hs 766T, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.37×** | +3.4 | 0.032 | 2/45 (NCI-H2347, NCI-H661) | top dose only | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +3.2 | 0.076 | 8/44 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +3.1 | 0.095 | 3/45 (HS-578T, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14063.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | 0.451× | -3.3 | 0.27 | 11/24 (NCI-H460, KATO III, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.662× | -3.3 | 0.27 | 8/46 (LoVo, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.669× | -3.2 | 0.27 | 9/40 (C-33 A, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14063. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.60 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.675 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.612 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.619 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.62 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.704 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.40 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14063), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADCK1]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[DPH5-DT]] | +0.69 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[KICS2]] | +0.69 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[RBM26-AS1]] | +0.68 | +0.63 / +0.58 | both halves | 8e-06 | same gene group |
| [[SLC5A6]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MRM1]] | +0.68 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PIGW]] | +0.68 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[SPRYD4]] | +0.67 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[EME2]] | +0.66 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ZNF783]] ⚠ | +0.66 | +0.57 / +0.59 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CYP4V2]] | +0.66 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[ZNF239]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[UTP15]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNB2]] | -0.66 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[ARL3]] | -0.65 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[MGST3]] | -0.63 | -0.62 / -0.39 | both halves | 6e-05 |  |
| [[ECI2]] | -0.61 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[COX6A1]] | -0.61 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[KLHL7]] | -0.61 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[SUFU]] | -0.60 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[PPP1R12B]] | -0.60 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[CBFA2T2]] | -0.60 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[MACO1]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[RAB11FIP1]] | -0.60 | -0.54 / -0.46 | both halves | 3e-05 |  |
| [[ACTR6]] | -0.60 | -0.50 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR1915HG]] | B | MIR1915HG activity raises TMEM147-AS1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.42× lower at baseline in the lines without MIR1915HG | 0.014 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[LIMCH1]] | B | LIMCH1 activity lowers TMEM147-AS1's level | lines that do not express LIMCH1 (16) vs lines expressing it (34) | 1.24× higher at baseline in the lines without LIMCH1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SNCAIP, TTC6, DIO2 |
| [[FTCDNL1]] | B | FTCDNL1 activity raises TMEM147-AS1's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 1.31× lower at baseline in the lines without FTCDNL1 | 0.056 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.619). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.3, 9.6); signed map (25.3, -29.3). **Vector** length 47.1, 5.77% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +9.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.5 | +6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +2.8 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.7 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +3.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.6 | -3.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -1.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.1 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | TMEM147 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19q13.12 — chr19:35,540,738-35,546,029 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51273](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51273) · Entrez [100506469](https://www.ncbi.nlm.nih.gov/gene/100506469) · Ensembl [ENSG00000236144](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236144)

## Data

Gene col 14063: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14063); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14063, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14063]; `tensor/DDL_lfc|DDL_z.npy` [14063]; `embed/gene_vectors.npy` [14063]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14063 or target_col == 14063). Every well: [[TMEM147-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM147-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
