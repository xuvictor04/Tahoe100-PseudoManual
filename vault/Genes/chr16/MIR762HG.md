---
symbol: "MIR762HG"
type: "gene"
col: 15260
ensembl_id: "ENSG00000260083"
name: "MIR762 host gene"
location: "16p11.2"
module: 15
arm: "+"
pooled_cpm: 4.05
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 4
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# MIR762HG

*MIR762 host gene* — 16p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.49× (z +12.5, q 2e-33, up in 36 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.593× (z -4.9, q 5e-04, down in 16 of 43 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0902×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPN10-DT]] (+0.75, fdr 7e-06), [[TAF11]] (+0.73, fdr 1e-05), [[RENO1]] (+0.72, fdr 7e-06); moves opposite to [[SPTAN1]] (-0.63, fdr 1e-05), [[HUWE1]] (-0.60, fdr 1e-05), [[AKAP11]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANXA2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +12.5 | 2e-33 | 36/40 (A498, LoVo, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +7.2 | 2e-10 | 16/24 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.62×** | +6.7 | 5e-09 | 15/46 (SHP-77, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.59×** | +4.5 | 8e-04 | 12/46 (SW480, C32, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +4.5 | 8e-04 | 0/5 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +4.3 | 0.002 | 8/28 (SW1417, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.52×** | +3.8 | 0.014 | 2/10 (NCI-H460, SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.014 | 8/35 (NCI-H1792, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.041 | 8/41 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.4 | 0.044 | 11/38 (Hs 766T, J82, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.37× | +3.0 | 0.13 | 4/45 (SW480, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15260.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Verteporfin (drug)]] 5 µM in 1 line (HS-578T 0.0902×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.593×** | -4.9 | 5e-04 | 16/43 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.716× | -3.1 | 0.48 | 12/42 (NCI-H23, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +10.2) | — |
| [[HS-578T (line)]] | alt | 4.06 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0902× (z -8.5) |
| [[A-172 (line)]] | wt | 6.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.32 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.83 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN10-DT]] | +0.75 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TAF11]] | +0.73 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[RENO1]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[ZNF398]] | +0.69 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[GOT1-DT]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[MIR4458HG]] | +0.69 | +0.52 / +0.75 | both halves | 1e-05 | same gene group |
| [[VPS13B-DT]] | +0.68 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[SEPTIN1]] | +0.67 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[WASH2P-1]] | +0.67 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[DENND10]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[C8orf76]] | +0.66 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[ZNF358]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTAN1]] | -0.63 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[HUWE1]] | -0.60 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.58 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[YWHAZ]] | -0.56 | -0.60 / -0.57 | both halves | 9e-06 |  |
| [[CSRP1]] | -0.56 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[POLR2E]] | -0.55 | -0.36 / -0.59 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA2]] | C | ANXA2 activity lowers MIR762HG's level | lines that do not express ANXA2 (4) vs lines expressing it (46) | 1.47× higher at baseline in the lines without ANXA2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PHF11, RARG, NABP1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.697). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.2, 22.7); signed map (0.1, -1.0). **Vector** length 49.1, 6.11% of its response variance represented; |z| ≥ 3 in 752 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +12.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.6 | +6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +7.2 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | +2.0 | +3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.0 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +4.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.5 | +3.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.5 | +2.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -2.9 | -4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | MIR762 host gene |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p11.2 — chr16:30,875,222-30,895,220 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | MicroRNA non-coding host genes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51386) · Entrez [101928736](https://www.ncbi.nlm.nih.gov/gene/101928736) · Ensembl [ENSG00000260083](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000260083)

## Data

Gene col 15260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15260); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15260]; `tensor/DDL_lfc|DDL_z.npy` [15260]; `embed/gene_vectors.npy` [15260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15260 or target_col == 15260). Every well: [[MIR762HG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MIR762HG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
