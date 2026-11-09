---
symbol: "TEX29"
type: "gene"
col: 7725
ensembl_id: "ENSG00000153495"
name: "testis expressed 29"
location: "13q34"
module: 37
arm: "+"
pooled_cpm: 4.47
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 6
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# TEX29

*testis expressed 29* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.31× (z +11.2, q 1e-26, up in 33 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.522× (z -5.9, q 2e-06, down in 15 of 26 measured lines) ⚠ toxic. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.647× (z -4.0, q 0.020, down in 21 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02936]] (+0.78, fdr 7e-06), [[PHKG1]] (+0.77, fdr 7e-06), [[TMEM269]] (+0.75, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LYG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.31×** | +11.2 | 1e-26 | 33/38 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +6.1 | 3e-07 | 21/37 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +5.2 | 4e-05 | 16/36 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +4.8 | 2e-04 | 19/47 (SW480, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +4.7 | 3e-04 | 11/36 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.2 | 0.003 | 14/38 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.48×** | +3.5 | 0.037 | 10/44 (A-172, LoVo, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.92×** | +3.2 | 0.086 | 5/36 (LS 180, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7725.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.522×** | -5.9 | 2e-06 | 15/26 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.647×** | -4.0 | 0.020 | 21/43 (HCT15, NCI-H1573, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.681×** | -3.6 | 0.050 | 19/44 (LOX-IMVI, KATO III, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.487×** | -3.6 | 0.050 | 10/29 (HS-578T, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.692×** | -3.5 | 0.055 | 10/45 (CHP-212, RPMI-7951, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.690×** | -3.3 | 0.084 | 12/43 (LoVo, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | 0.710× | -3.1 | 0.13 | 15/44 (LOX-IMVI, SNU-423, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.793× | -3.1 | 0.13 | 10/46 (SK-MEL-2, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 6.00 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0778× (z -11.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.107× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 7.56 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 5 µM 0.0913× (z -8.5) |
| [[HS-578T (line)]] | alt | 5.08 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.0753× (z -9.7) |
| [[J82 (line)]] | alt | 4.08 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0858× (z -8.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[LOX-IMVI (line)]] | wt | 5.33 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0615× (z -10.4) |
| [[NCI-H1573 (line)]] | alt | 7.74 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0912× (z -9.6) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 3.38 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0794× (z -9.9) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 4.71 | 0 | 1 (1 ⚠) | — | [[Cytarabine (drug)]] 5 µM 0.0715× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 2.88 | 0 | 1 | — | [[Cilostazol (drug)]] 5 µM 0.0572× (z -8.9) |
| [[SW480 (line)]] | alt | 5.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.38 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.97 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.67 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02936]] | +0.78 | +0.80 / +0.82 | both halves | 7e-06 |  |
| [[PHKG1]] | +0.77 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[TMEM269]] | +0.75 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[WDR49]] | +0.74 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[ARL9]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[CCNP]] | +0.74 | +0.68 / +0.73 | both halves | 7e-06 |  |
| [[PHYHD1]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[HCLS1]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.73 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[LINC03016]] | +0.73 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[CCDC181]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CD200R1]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYG1]] | B | LYG1 activity raises TEX29's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without LYG1 | 0.034 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers TEX29's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC01482]] | B | LINC01482 activity raises TEX29's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without LINC01482 | 0.088 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[WDR49]] | C | WDR49 activity raises TEX29's level | lines that do not express WDR49 (3) vs lines expressing it (47) | 1.53× lower at baseline in the lines without WDR49 | 0.075 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FOXP1, ENSG00000286952, CORIN; maybe low, not absent |
| [[TRIM72]] | C | TRIM72 activity raises TEX29's level | lines that do not express TRIM72 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without TRIM72 | 0.081 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC02133, LYG1, LINC01762; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.796). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.5, -18.4); signed map (12.5, 8.0). **Vector** length 71.7, 11.7% of its response variance represented; |z| ≥ 3 in 931 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +4.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | +4.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +5.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.0 | +2.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.0 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -2.2 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -3.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.2 | -3.0 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -3.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 29 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:111,316,184-111,344,249 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA474D23.1, MGC35169; previously C13orf16 |
| Matched by | ensembl_id |

UniProt [Q8N6K0](https://www.uniprot.org/uniprotkb/Q8N6K0) carries no function annotation.

**Summary**, from NCBI Gene [121793](https://www.ncbi.nlm.nih.gov/gene/121793):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20370) · Entrez [121793](https://www.ncbi.nlm.nih.gov/gene/121793) · UniProt [Q8N6K0](https://www.uniprot.org/uniprotkb/Q8N6K0) · Ensembl [ENSG00000153495](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153495)

## Data

Gene col 7725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7725); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7725]; `tensor/DDL_lfc|DDL_z.npy` [7725]; `embed/gene_vectors.npy` [7725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7725 or target_col == 7725). Every well: [[TEX29 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX29.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
