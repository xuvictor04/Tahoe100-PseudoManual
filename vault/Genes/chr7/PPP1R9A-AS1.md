---
symbol: "PPP1R9A-AS1"
type: "gene"
col: 14064
ensembl_id: "ENSG00000236197"
name: "PPP1R9A antisense RNA 1"
location: "7q21.3"
module: 75
arm: "+"
pooled_cpm: 3.44
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# PPP1R9A-AS1

*PPP1R9A antisense RNA 1* — 7q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.19× (z +13.4, q 1e-38, up in 35 of 40 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.0747×; ⚠ toxic); [[Sacubitril_Valsartan (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0720×); [[Talc (drug)]] 5 µM in 1 line (C32 0.0501×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNTNAP5]] (+0.83, fdr 7e-06), [[LRRC4C]] (+0.82, fdr 7e-06), [[ST7-AS2]] (+0.82, fdr 7e-06).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GREB1]] → it (grade B ⚠); 2 go from it, the strongest it → [[HRG-AS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14064.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +13.4 | 1e-38 | 35/40 (C32, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +13.4 | 1e-38 | 17/23 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.32×** | +9.8 | 3e-20 | 3/5 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.69×** | +8.9 | 5e-17 | 21/37 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.67×** | +6.2 | 6e-08 | 16/44 (A549, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +6.1 | 8e-08 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.8 | 2e-04 | 8/45 (A498, AN3 CA, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.3 | 0.001 | 7/24 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.46×** | +4.2 | 0.002 | 8/33 (A-172, Hs 766T, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.005 | 12/44 (MIA PaCa-2, AsPC-1, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.4 | 0.040 | 3/37 (LOX-IMVI, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pralsetinib (drug)]] 0.05 µM |  | **1.33×** | +3.3 | 0.047 | 2/44 (MIA PaCa-2, AsPC-1) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.3 | 0.047 | 2/14 (SW1417, HEC-1-A) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.068 | 5/44 (BT-474, HepG2/C3A, …) | inconsistent across doses |  |
| [[Canagliflozin (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.075 | 4/33 (HEC-1-A, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14064.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Fingolimod (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1573 0.0747×; ⚠ toxic); [[Sacubitril_Valsartan (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0720×); [[Talc (drug)]] 5 µM in 1 line (C32 0.0501×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.914× | -3.8 | 0.074 | 13/48 (A-172, COLO 205, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | 0.741× | -3.4 | 0.17 | 12/44 (C32, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.762× | -3.3 | 0.19 | 5/46 (A549, LoVo, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | 0.835× | -3.1 | 0.29 | 10/44 (hTERT-HPNE, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14064. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 3.32 | 1 | 1 | [[Auranofin (drug)]] 5 µM 23.1× (z +9.0) | [[Talc (drug)]] 5 µM 0.0501× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 3.88 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0747× (z -9.5) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 3.76 | 0 | 1 | — | [[Sacubitril_Valsartan (drug)]] 0.05 µM 0.0720× (z -9.1) |
| [[A-172 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.28 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.02 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.59 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.69 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14064), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNTNAP5]] | +0.83 | +0.79 / +0.78 | both halves | 7e-06 |  |
| [[LRRC4C]] | +0.82 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[ST7-AS2]] | +0.82 | +0.76 / +0.76 | both halves | 7e-06 | same gene group |
| [[MYO16]] | +0.82 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[USH2A]] | +0.82 | +0.77 / +0.78 | both halves | 7e-06 |  |
| [[DPP6]] | +0.81 | +0.71 / +0.72 | both halves | 7e-06 |  |
| [[DLEU7]] | +0.80 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.80 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[C8orf34]] | +0.79 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.79 | +0.66 / +0.74 | both halves | 7e-06 | same gene group |
| [[LINC02006]] | +0.79 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[RBMS3-AS3]] | +0.79 | +0.74 / +0.64 | both halves | 7e-06 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GREB1]] | B | GREB1 activity raises PPP1R9A-AS1's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 1.24× lower at baseline in the lines without GREB1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HRG-AS1]] | C | PPP1R9A-AS1's natural level weakens HRG-AS1's drug response | PPP1R9A-AS1's natural level across 44 lines (lineage-adjusted; a glimpse) | r -0.70, reverse -0.32; direction not clear | 0.029 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | PPP1R9A-AS1's natural level lowers the cells' numbers under Flumatinib (mesylate) 0.5 µM (makes them more sensitive) | PPP1R9A-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.339 over the table, 0.028 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.863). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.8, 27.7); signed map (33.3, 12.3). **Vector** length 40.6, 3.80% of its response variance represented; |z| ≥ 3 in 948 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +8.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | +13.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.7 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -3.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | +0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.0 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -2.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.8 | -2.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.8 | -2.1 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -0.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | PPP1R9A antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 7q21.3 — chr7:95,035,731-95,214,338 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40696) · Entrez [105375405](https://www.ncbi.nlm.nih.gov/gene/105375405) · Ensembl [ENSG00000236197](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236197)

## Data

Gene col 14064: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14064); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14064, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14064]; `tensor/DDL_lfc|DDL_z.npy` [14064]; `embed/gene_vectors.npy` [14064]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14064 or target_col == 14064). Every well: [[PPP1R9A-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R9A-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
