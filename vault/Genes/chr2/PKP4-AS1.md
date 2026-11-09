---
symbol: "PKP4-AS1"
type: "gene"
col: 12860
ensembl_id: "ENSG00000204380"
name: "PKP4 antisense RNA 1"
location: "2q24.1"
module: 166
arm: "+"
pooled_cpm: 2.1
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# PKP4-AS1

*PKP4 antisense RNA 1* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.05× (z +9.6, q 3e-19, up in 19 of 30 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (PANC-1 0.0989×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OBI1-AS1]] (+0.79, fdr 7e-06), [[HPSE2]] (+0.74, fdr 7e-06), [[PTPRT]] (+0.73, fdr 1e-05).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC02566]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MGC4859]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12860.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +9.6 | 3e-19 | 19/30 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.76×** | +9.6 | 3e-19 | 6/9 (HOP62, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.51×** | +8.4 | 1e-14 | 0/0 | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +7.8 | 1e-12 | 1/2 (PANC-1) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.19×** | +7.4 | 2e-11 | 2/8 (PANC-1, SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.46×** | +5.0 | 5e-05 | 11/33 (BT-474, NCI-H1573, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.54×** | +4.0 | 0.004 | 6/40 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +3.9 | 0.007 | 4/22 (LoVo, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +3.9 | 0.007 | 2/10 (NCI-H1573, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.5 | 0.022 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.077 | 1/21 (A498) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.26× | +3.1 | 0.10 | 3/44 (MIA PaCa-2, NCI-H1573, …) | rises with dose | position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.0 | 0.10 | 2/31 (BT-474, HT-29) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 1.38× | +3.0 | 0.10 | 2/22 (LOX-IMVI, LoVo) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12860.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Topotecan (hydrochloride) (drug)]] 0.05 µM in 1 line (PANC-1 0.0989×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Norepinephrine (hydrochloride) (drug)]] 0.5 µM |  | 0.701× | -3.4 | 0.27 | 7/40 (KATO III, SW 900, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | 0.707× | -3.3 | 0.27 | 6/44 (Hs 766T, H4, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12860. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 3.13 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +10.6) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[PANC-1 (line)]] | alt | 2.00 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0989× (z -9.5) |
| [[A-172 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12860), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OBI1-AS1]] | +0.79 | +0.71 / +0.78 | both halves | 7e-06 | same gene group |
| [[HPSE2]] | +0.74 | +0.72 / +0.71 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.73 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[ST7-AS2]] | +0.73 | +0.57 / +0.77 | both halves | 1e-05 | same gene group |
| [[G2E3-AS1]] | +0.72 | +0.59 / +0.67 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.72 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[LINC00861]] | +0.72 | +0.47 / +0.75 | both halves | 2e-05 |  |
| [[USH2A]] | +0.71 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[DCC]] | +0.71 | +0.45 / +0.77 | both halves | 3e-05 |  |
| [[TEX11]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[SPATC1]] | +0.71 | +0.58 / +0.74 | both halves | 7e-06 |  |
| [[SLC13A4]] | +0.71 | +0.41 / +0.74 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02566]] | B | LINC02566 activity raises PKP4-AS1's level | lines that do not express LINC02566 (43) vs lines expressing it (7) | 1.42× lower at baseline in the lines without LINC02566 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000241168, LINC02327, ENSG00000289605 |
| [[LINC01358]] | B | LINC01358 activity lowers PKP4-AS1's level | lines that do not express LINC01358 (14) vs lines expressing it (36) | 1.07× higher at baseline in the lines without LINC01358 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, BMPER, FRMD4A; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MGC4859]] | C | PKP4-AS1's natural level weakens MGC4859's drug response | PKP4-AS1's natural level across 39 lines (lineage-adjusted; a glimpse) | r -0.72, reverse -0.29; direction clear | 0.053 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.7, 28.7); signed map (32.0, 11.6). **Vector** length 34.2, 3.04% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +3.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +1.2 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.0 | +2.0 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -2.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.0 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | PKP4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2q24.1 — chr2:158,658,337-158,735,002 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52580) · Entrez [100129029](https://www.ncbi.nlm.nih.gov/gene/100129029) · Ensembl [ENSG00000204380](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204380)

## Data

Gene col 12860: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12860); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12860, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12860]; `tensor/DDL_lfc|DDL_z.npy` [12860]; `embed/gene_vectors.npy` [12860]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12860 or target_col == 12860). Every well: [[PKP4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKP4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
