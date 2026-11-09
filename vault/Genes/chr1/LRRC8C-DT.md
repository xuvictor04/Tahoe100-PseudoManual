---
symbol: "LRRC8C-DT"
type: "gene"
col: 13828
ensembl_id: "ENSG00000231999"
name: "LRRC8C divergent transcript"
location: "1p22.2"
module: 35
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# LRRC8C-DT

*LRRC8C divergent transcript* — 1p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.17× (z +17.7, q 0e+00, up in 32 of 35 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD14-DT]] (+0.80, fdr 7e-06), [[PAXBP1-AS1]] (+0.77, fdr 7e-06), [[HSD11B1-AS1]] (+0.77, fdr 7e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC02384]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13828.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +17.7 | 0e+00 | 32/35 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +7.9 | 7e-13 | 15/27 (HOP62, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.67×** | +7.8 | 1e-12 | 17/35 (LOX-IMVI, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.7 | 1e-12 | 1/4 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +6.9 | 8e-10 | 2/2 (A498, PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.52×** | +6.4 | 1e-08 | 12/46 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.77×** | +6.1 | 7e-08 | 4/13 (CFPAC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.46×** | +5.8 | 4e-07 | 14/44 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +5.6 | 2e-06 | 12/34 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +5.5 | 2e-06 | 10/45 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 2e-05 | 10/41 (Hs 766T, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +4.7 | 1e-04 | 8/41 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.48×** | +4.2 | 0.001 | 3/16 (SW480, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.9 | 0.003 | 4/15 (NCI-H1792, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.048 | 3/42 (LOX-IMVI, J82, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.068 | 2/36 (CFPAC-1, SW 900) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.5 µM |  | **1.33×** | +3.1 | 0.068 | 3/40 (SW 900, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 2.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 5.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +9.4) | — |
| [[A-172 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.959 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.80 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.34 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD14-DT]] | +0.80 | +0.74 / +0.63 | both halves | 7e-06 | same gene group |
| [[PAXBP1-AS1]] | +0.77 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[HSD11B1-AS1]] | +0.77 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[FEZ1]] | +0.76 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[INTS6-AS1]] | +0.75 | +0.73 / +0.49 | both halves | 1e-05 |  |
| [[MALINC1]] | +0.75 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.74 | +0.72 / +0.46 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.74 | +0.68 / +0.47 | both halves | 2e-05 |  |
| [[UPP2]] | +0.74 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[SEPTIN7-DT]] | +0.73 | +0.72 / +0.49 | both halves | 1e-05 | same gene group |
| [[OOEP]] | +0.73 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[UPK2]] | +0.73 | +0.68 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02384]] | B | LINC02384 activity raises LRRC8C-DT's level | lines that do not express LINC02384 (26) vs lines expressing it (24) | 1.37× lower at baseline in the lines without LINC02384 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers LRRC8C-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity raises LRRC8C-DT's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without RASSF8-AS1 | 0.025 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[CNN3-DT]] | B | CNN3-DT activity raises LRRC8C-DT's level | lines that do not express CNN3-DT (8) vs lines expressing it (42) | 1.39× lower at baseline in the lines without CNN3-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent |
| [[LINC01122]] | B | LINC01122 activity lowers LRRC8C-DT's level | lines that do not express LINC01122 (12) vs lines expressing it (38) | 1.25× higher at baseline in the lines without LINC01122 | 0.061 | ⚠ within organs, on part of the lines; also absent: CERS4, MAP9, APBA2; maybe low, not absent |
| [[PAMR1]] | B | PAMR1 activity strengthens LRRC8C-DT's drug response | lines that do not express PAMR1 (28) vs lines expressing it (18) | the lines without PAMR1 respond 0.67× as strongly (z diff +0.62); strongest at Idarubicin (hydrochloride) 5 µM: 2.71x vs 4.46x (z diff +2.4) | 0.069 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CNN3-DT]] | B | CNN3-DT activity strengthens LRRC8C-DT's drug response | lines that do not express CNN3-DT (8) vs lines expressing it (38) | the lines without CNN3-DT respond 0.50× as strongly (z diff +1.10); strongest at Dinaciclib 0.5 µM: 0.66x vs 1.65x (z diff +3.1) | 0.077 | ⚠ within organs, on part of the lines; also absent: MPP2, CNN3, SLC35F1; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.786). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (10.8, 22.6); signed map (30.7, -1.5). **Vector** length 45.8, 5.15% of its response variance represented; |z| ≥ 3 in 968 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +17.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +7.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +7.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.1 | +2.3 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -1.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | -1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +0.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.7 | -0.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -1.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | -0.9 | -1.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.9 | +0.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -0.9 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | LRRC8C divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p22.2 — chr1:89,581,291-89,633,003 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ27354 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:53731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53731) · Entrez [400761](https://www.ncbi.nlm.nih.gov/gene/400761) · Ensembl [ENSG00000231999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000231999)

## Data

Gene col 13828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13828); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13828]; `tensor/DDL_lfc|DDL_z.npy` [13828]; `embed/gene_vectors.npy` [13828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13828 or target_col == 13828). Every well: [[LRRC8C-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC8C-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
