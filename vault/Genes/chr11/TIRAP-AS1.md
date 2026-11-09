---
symbol: "TIRAP-AS1"
type: "gene"
col: 14913
ensembl_id: "ENSG00000255062"
name: "TIRAP antisense RNA 1"
location: "11q24.2"
module: 15
arm: "+"
pooled_cpm: 2.44
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# TIRAP-AS1

*TIRAP antisense RNA 1* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.90× (z +9.5, q 2e-18, up in 20 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.659× (z -4.4, q 0.007, down in 11 of 43 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNPY2-AS1]] (+0.66, fdr 1e-05), [[THBS4]] (+0.64, fdr 1e-05), [[NINJ2]] (+0.63, fdr 1e-04); moves opposite to [[CAST]] (-0.55, fdr 2e-04), [[SPAG9]] (-0.55, fdr 2e-04), [[DHTKD1]] (-0.54, fdr 7e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +9.5 | 2e-18 | 20/29 (PANC-1, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.51×** | +9.2 | 1e-17 | 8/9 (KATO III, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +9.1 | 1e-17 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.14×** | +7.6 | 4e-12 | 0/0 | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +6.4 | 2e-08 | 12/39 (SW480, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +5.7 | 1e-06 | 7/44 (HEC-1-A, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +5.0 | 4e-05 | 3/11 (HOP62, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.22×** | +4.3 | 0.001 | 1/2 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.035 | 2/45 (SW1417, SW480) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.38×** | +3.3 | 0.050 | 3/36 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.050 | 3/41 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.2 | 0.066 | 7/27 (NCI-H2030, PANC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +3.2 | 0.066 | 3/27 (NCI-H2347, A-427, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.090 | 4/46 (SW 1271, SW480, …) | top dose only |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.097 | 4/35 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.659×** | -4.4 | 0.007 | 11/43 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.692×** | -3.9 | 0.032 | 12/44 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.698×** | -3.8 | 0.032 | 12/45 (SW480, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 4.40 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0431× (z -10.0) |
| [[A-172 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.874 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.07 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.45 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 6.10 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNPY2-AS1]] | +0.66 | +0.56 / +0.51 | both halves | 1e-05 | same gene group |
| [[THBS4]] | +0.64 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NINJ2]] | +0.63 | +0.44 / +0.33 | both halves | 1e-04 |  |
| [[STARD7-AS1]] | +0.62 | +0.51 / +0.39 | both halves | 5e-05 | same gene group |
| [[CTTN-DT]] | +0.62 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GTF3C2-AS2]] | +0.62 | +0.53 / +0.41 | both halves | 4e-05 | same gene group |
| [[TLCD3A]] | +0.61 | +0.31 / +0.45 | both halves | 2e-04 |  |
| [[SPRYD4]] | +0.61 | +0.51 / +0.46 | both halves | 3e-05 |  |
| [[RMDN2]] | +0.60 | +0.45 / +0.36 | both halves | 9e-05 |  |
| [[POU6F1]] | +0.60 | +0.43 / +0.35 | both halves | 1e-04 |  |
| [[GABPB1]] | +0.59 | +0.56 / +0.22 | both halves | 6e-04 |  |
| [[MYLK4]] | +0.59 | +0.41 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAST]] | -0.55 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[SPAG9]] | -0.55 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[DHTKD1]] | -0.54 | -0.44 / -0.20 | both halves | 7e-04 |  |
| [[HERC1]] | -0.53 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[ALAD]] | -0.53 | -0.34 / -0.18 | ⚠ not reproduced | 9e-04 |  |
| [[CHP1]] | -0.53 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[GDE1]] | -0.52 | -0.27 / -0.27 | both halves | 3e-04 |  |
| [[STUB1]] | -0.51 | -0.31 / -0.09 | ⚠ not reproduced | 0.003 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises TIRAP-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[OPRD1]] | B | OPRD1 activity raises TIRAP-AS1's level | lines that do not express OPRD1 (28) vs lines expressing it (22) | 1.28× lower at baseline in the lines without OPRD1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PHYHIPL, GPC3, RAB3C; maybe low, not absent |
| [[C10orf95-AS1]] | C | C10orf95-AS1 activity raises TIRAP-AS1's level | lines that do not express C10orf95-AS1 (4) vs lines expressing it (46) | 1.53× lower at baseline in the lines without C10orf95-AS1 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: CHD7, NRTN, ENSG00000256673; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.541). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.8, 21.5); signed map (29.8, -18.2). **Vector** length 40.1, 3.99% of its response variance represented; |z| ≥ 3 in 979 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +9.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +2.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +2.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.2 |
| fall | [[Belinostat (drug)]] 5 µM |  | -1.7 | -3.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.5 | -4.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.3 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.2 | -1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -0.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | TIRAP antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11q24.2 — chr11:126,294,296-126,304,323 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56069) · Entrez [105369557](https://www.ncbi.nlm.nih.gov/gene/105369557) · Ensembl [ENSG00000255062](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255062)

## Data

Gene col 14913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14913); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14913]; `tensor/DDL_lfc|DDL_z.npy` [14913]; `embed/gene_vectors.npy` [14913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14913 or target_col == 14913). Every well: [[TIRAP-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TIRAP-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
