---
symbol: "CARNMT1-AS1"
type: "gene"
col: 12765
ensembl_id: "ENSG00000203321"
name: "CARNMT1 antisense RNA 1"
location: "9q21.13"
module: 21
arm: "+"
pooled_cpm: 3.91
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# CARNMT1-AS1

*CARNMT1 antisense RNA 1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +12.3, q 9e-32, up in 30 of 38 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gemfibrozil (drug)]] 5 µM in 1 line (NCI-H1792 0.152×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA2-AS1]] (+0.80, fdr 7e-06), [[C2CD5-AS1]] (+0.78, fdr 7e-06), [[PSMD14-DT]] (+0.77, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +12.3 | 9e-32 | 30/38 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.59×** | +10.0 | 3e-21 | 21/23 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.50×** | +9.3 | 2e-18 | 4/7 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +7.2 | 8e-11 | 5/10 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.1 | 4e-05 | 16/44 (LoVo, HOP62, …) | top dose only |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +4.2 | 0.002 | 6/39 (C32, Hs 766T, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.2 | 0.002 | 8/23 (AsPC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.44×** | +3.8 | 0.010 | 6/41 (A498, LoVo, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.7 | 0.015 | 9/37 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.044 | 5/40 (LoVo, Hs 766T, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.76×** | +3.1 | 0.100 | 0/8 | top dose only | noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.33× | +3.0 | 0.12 | 3/40 (KATO III, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12765.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Gemfibrozil (drug)]] 5 µM in 1 line (NCI-H1792 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -5.4 | 4e-05 | 19/48 (LS 180, PANC-1, …) | inconsistent across doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.737× | -3.3 | 0.32 | 4/47 (LoVo, NCI-H661, …) | inconsistent across doses | position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.748× | -3.1 | 0.36 | 12/46 (NCI-H2030, NCI-H2347, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 3.20 | 0 | 1 | — | [[Gemfibrozil (drug)]] 5 µM 0.152× (z -8.6) |
| [[A-172 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.63 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.84 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA2-AS1]] | +0.80 | +0.67 / +0.77 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.78 | +0.70 / +0.70 | both halves | 7e-06 | same gene group |
| [[PSMD14-DT]] | +0.77 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.77 | +0.68 / +0.73 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.74 | +0.53 / +0.77 | both halves | 1e-05 | same gene group |
| [[PPP1R42]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[OOEP]] | +0.73 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[C1orf56]] | +0.72 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[BIRC6-AS2-1]] | +0.72 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[ST7-AS2]] | +0.72 | +0.67 / +0.60 | both halves | 7e-06 | same gene group |
| [[CHMP3-AS1]] | +0.72 | +0.55 / +0.72 | both halves | 1e-05 | same gene group |
| [[CNGB3]] | +0.72 | +0.55 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.4, 26.0); signed map (32.8, 3.0). **Vector** length 37.5, 3.52% of its response variance represented; |z| ≥ 3 in 805 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +5.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +2.1 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +0.9 | +1.6 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.6 | -5.4 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.1 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.0 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -1.6 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.0 | -1.6 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | CARNMT1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 9q21.13 — chr9:74,952,968-74,996,293 (+) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously C9orf41-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51188](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51188) · Entrez [101927380](https://www.ncbi.nlm.nih.gov/gene/101927380) · Ensembl [ENSG00000203321](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203321)

## Data

Gene col 12765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12765); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12765]; `tensor/DDL_lfc|DDL_z.npy` [12765]; `embed/gene_vectors.npy` [12765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12765 or target_col == 12765). Every well: [[CARNMT1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARNMT1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
