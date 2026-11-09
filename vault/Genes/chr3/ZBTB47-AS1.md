---
symbol: "ZBTB47-AS1"
type: "gene"
col: 13734
ensembl_id: "ENSG00000230084"
name: "ZBTB47 and NKTR antisense RNA 1"
location: "3p22.1"
module: 21
arm: "+"
pooled_cpm: 15.97
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ZBTB47-AS1

*ZBTB47 and NKTR antisense RNA 1* — 3p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +10.0, q 1e-20, up in 33 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +4.5, q 9e-04, up in 19 of 46 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HCT15 0.0918×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.222×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.184×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (H4 0.147×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOGT-DT]] (+0.80, fdr 7e-06), [[FAM217A]] (+0.80, fdr 7e-06), [[TICAM2-AS1]] (+0.78, fdr 7e-06); moves opposite to [[RTL6]] (-0.65, fdr 7e-06), [[SLC35A4]] (-0.64, fdr 7e-06), [[DCLRE1A]] (-0.63, fdr 9e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Riluzole hydrochloride (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13734.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.0 | 1e-20 | 33/41 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.08×** | +9.8 | 2e-20 | 26/31 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +5.9 | 9e-07 | 26/43 (NCI-H2030, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.50×** | +5.3 | 2e-05 | 20/35 (KATO III, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.5 | 9e-04 | 19/46 (A498, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +4.4 | 0.001 | 24/46 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.1 | 0.003 | 20/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.33×** | +3.8 | 0.010 | 14/47 (A498, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.2 | 0.092 | 15/43 (NCI-H2030, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13734.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (HCT15 0.0918×); [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.222×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 0.184×; ⚠ toxic; transcription drop); [[Thymol (drug)]] 0.5 µM in 1 line (H4 0.147×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.860× | -7.5 | 4e-11 | 15/48 (SW1417, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | 0.797× | -3.0 | 0.72 | 8/47 (HS-578T, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13734. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 15.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.147× (z -8.5) |
| [[HCT15 (line)]] | alt | 19.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0918× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.222× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -8.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 17.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13734), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOGT-DT]] | +0.80 | +0.73 / +0.83 | both halves | 7e-06 |  |
| [[FAM217A]] | +0.80 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.78 | +0.76 / +0.76 | both halves | 7e-06 | same gene group |
| [[C12orf73]] | +0.78 | +0.63 / +0.80 | both halves | 7e-06 |  |
| [[FLJ40194]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.76 | +0.68 / +0.75 | both halves | 7e-06 | same gene group |
| [[RN7SL1]] | +0.75 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[LRRC37A16P]] | +0.75 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[EFCAB14-AS1]] | +0.73 | +0.69 / +0.71 | both halves | 7e-06 | same gene group |
| [[KIZ-AS1]] ⚠ | +0.72 | +0.73 / +0.68 | both halves | 7e-06 | same gene group; ⚠ in the vector space only through flagged drug-doses |
| [[MAL2-AS1]] | +0.72 | +0.62 / +0.73 | both halves | 7e-06 | same gene group |
| [[CNGB3]] | +0.72 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[SPTBN1-AS2]] | +0.70 | +0.59 / +0.69 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTL6]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[SLC35A4]] | -0.64 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[DCLRE1A]] | -0.63 | -0.57 / -0.64 | both halves | 9e-06 |  |
| [[IFRD2]] | -0.60 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[BBS10]] | -0.60 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[APEX2]] | -0.60 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.59 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[GEMIN4]] | -0.59 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[NOL11]] | -0.57 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.57 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[HASPIN]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PRMT5]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Riluzole hydrochloride (drug)]] 5 µM | C | ZBTB47-AS1's natural level raises the cells' numbers under Riluzole hydrochloride 5 µM (protects the cells) | ZBTB47-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.268 over the table, 0.043 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 28.3); signed map (34.7, 4.8). **Vector** length 57.5, 8.40% of its response variance represented; |z| ≥ 3 in 642 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | +0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.1 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.6 | -0.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -1.3 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ZBTB47 and NKTR antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3p22.1 — chr3:42,601,961-42,654,388 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:41174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:41174) · Entrez [101928323](https://www.ncbi.nlm.nih.gov/gene/101928323) · Ensembl [ENSG00000230084](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000230084)

## Data

Gene col 13734: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13734); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13734, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13734]; `tensor/DDL_lfc|DDL_z.npy` [13734]; `embed/gene_vectors.npy` [13734]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13734 or target_col == 13734). Every well: [[ZBTB47-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB47-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
