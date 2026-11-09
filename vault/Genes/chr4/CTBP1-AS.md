---
symbol: "CTBP1-AS"
type: "gene"
col: 15972
ensembl_id: "ENSG00000280927"
name: "CTBP1 antisense RNA"
location: "4p16.3"
module: 21
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 0
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021", "evidence-flagged-only"]
generated_by: "tahoemap"
---

# CTBP1-AS

*CTBP1 antisense RNA* — 4p16.3

## At a glance

> [!summary] In this data
> ⚠ It is in the vector space only through drug-doses that carry an alert for it (its significant pooled drug-doses and per-line responses; `embed/genes.parquet` evidence_flagged_only): its vector, partners and module rest on changes that may come from what those drug-doses did to the cells rather than from its own regulation.
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.39× (z +9.2, q 2e-17, up in 15 of 16 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Delamanid (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0729×); [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0671×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RN7SL2]] (+0.88, fdr 7e-06), [[ZRANB2-AS1]] (+0.81, fdr 7e-06), [[FAM217A]] (+0.81, fdr 7e-06); moves opposite to [[LIN7C]] (-0.70, fdr 1e-05), [[TMX1]] (-0.69, fdr 7e-06), [[AP2M1]] (-0.69, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.39×** | +9.2 | 2e-17 | 15/16 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.09×** | +8.2 | 9e-14 | 5/5 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +4.9 | 2e-04 | 3/6 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.86×** | +4.7 | 4e-04 | 4/15 (HEC-1-A, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.0 | 0.007 | 3/24 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.5 | 0.040 | 8/34 (NCI-H460, A-172, …) | top dose only |  |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.53×** | +3.2 | 0.088 | 9/36 (NCI-H2347, NCI-H23, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.2 | 0.088 | 7/20 (J82, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.53×** | +3.2 | 0.088 | 11/32 (NCI-H2030, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15972.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Delamanid (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0729×); [[Belinostat (drug)]] 5 µM in 1 line (HEC-1-A 0.0671×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ciclopirox (drug)]] 0.5 µM |  | 0.670× | -3.0 | 0.74 | 9/44 (AsPC-1, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.15 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0671× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 2.99 | 0 | 1 | — | [[Delamanid (drug)]] 0.5 µM 0.0729× (z -9.3) |
| [[A-172 (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.56 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.63 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.09 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.88 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.23 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RN7SL2]] | +0.88 | +0.75 / +0.87 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.81 | +0.74 / +0.82 | both halves | 7e-06 | same gene group |
| [[FAM217A]] | +0.81 | +0.76 / +0.78 | both halves | 7e-06 |  |
| [[VPS39-DT]] | +0.81 | +0.72 / +0.79 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.81 | +0.69 / +0.83 | both halves | 7e-06 |  |
| [[CCDC65]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.79 | +0.71 / +0.86 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.79 | +0.72 / +0.81 | both halves | 7e-06 | same gene group |
| [[HSPA2-AS1]] | +0.78 | +0.81 / +0.81 | both halves | 7e-06 | same gene group |
| [[MAL2-AS1]] | +0.77 | +0.70 / +0.78 | both halves | 7e-06 | same gene group |
| [[RN7SL1]] | +0.76 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.76 | +0.77 / +0.74 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LIN7C]] | -0.70 | -0.56 / -0.71 | both halves | 1e-05 |  |
| [[TMX1]] | -0.69 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[AP2M1]] | -0.69 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.68 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[TWF1]] | -0.66 | -0.51 / -0.67 | both halves | 1e-05 |  |
| [[TGOLN2]] | -0.66 | -0.62 / -0.67 | both halves | 7e-06 |  |
| [[ALG10]] | -0.65 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[RPE]] | -0.64 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[PSME3]] | -0.64 | -0.45 / -0.68 | both halves | 3e-05 |  |
| [[MMGT1]] | -0.64 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[MTHFD1]] | -0.64 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[PRKDC]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- ⚠ **In the space only through flagged drug-doses**: its significant pooled drug-doses and per-line responses all carry an alert (`embed/genes.parquet` evidence_flagged_only), so its module and partners may reflect what those drug-doses did to the cells.
- **Nodal map** (x, y) = (14.3, 28.5); signed map (33.9, 6.0). **Vector** length 32.8, 2.95% of its response variance represented; |z| ≥ 3 in 712 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.5 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | -0.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.2 | +2.7 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.2 | +2.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -0.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -0.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.0 | -2.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | CTBP1 antisense RNA |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 4p16.3 — chr4:1,210,120-1,218,591 (+) |
| Ensembl biotype | lncRNA |
| Also known as | PCAT10 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48337) · Entrez [285463](https://www.ncbi.nlm.nih.gov/gene/285463) · Ensembl [ENSG00000280927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000280927)

## Data

Gene col 15972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15972); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15972]; `tensor/DDL_lfc|DDL_z.npy` [15972]; `embed/gene_vectors.npy` [15972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15972 or target_col == 15972). Every well: [[CTBP1-AS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTBP1-AS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
