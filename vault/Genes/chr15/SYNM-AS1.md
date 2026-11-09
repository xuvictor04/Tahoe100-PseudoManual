---
symbol: "SYNM-AS1"
type: "gene"
col: 15202
ensembl_id: "ENSG00000259475"
name: "SYNM antisense RNA 1"
location: "15q26.3"
module: 21
arm: "+"
pooled_cpm: 5.18
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# SYNM-AS1

*SYNM antisense RNA 1* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.83× (z +24.0, q 0e+00, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.888× (z -5.1, q 2e-04, down in 20 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.703× (z -4.5, q 0.002, down in 15 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 5 µM in 1 line (Hs 766T 0.180×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNGB3]] (+0.81, fdr 7e-06), [[LANCL1-AS1]] (+0.80, fdr 7e-06), [[CTDSPL2-DT]] (+0.80, fdr 7e-06).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.83×** | +24.0 | 0e+00 | 37/40 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +11.8 | 9e-30 | 24/28 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.92×** | +11.7 | 4e-29 | 29/40 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.47×** | +11.0 | 7e-26 | 6/9 (A498, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +7.9 | 2e-13 | 10/16 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.2 | 2e-05 | 12/32 (A498, LoVo, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.50×** | +5.1 | 2e-05 | 14/45 (SK-MEL-2, C32, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +4.9 | 5e-05 | 13/39 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.48×** | +4.9 | 5e-05 | 16/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.0 | 0.004 | 12/38 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.005 | 11/47 (SW1417, SHP-77, …) | top dose only |  |
| [[Decitabine (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.008 | 6/44 (NCI-H1792, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.47×** | +3.5 | 0.022 | 5/41 (LS 180, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.4 | 0.026 | 8/34 (NCI-H1792, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.30×** | +3.3 | 0.036 | 3/46 (SW1417, PANC-1, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.090 | 5/39 (LS 180, RKO, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Medroxyprogesterone acetate (drug)]] 5 µM in 1 line (Hs 766T 0.180×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.888× | -5.1 | 2e-04 | 20/48 (PANC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.703×** | -4.5 | 0.002 | 15/47 (HOP62, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 4.37 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +9.6) | — |
| [[A498 (line)]] | wt | 3.34 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +8.6) | — |
| [[A549 (line)]] | wt | 7.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 3.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 4.72 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.30× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 3.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +13.9) | — |
| [[HOP62 (line)]] | alt | 6.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 4.47 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 5 µM 0.180× (z -8.7) |
| [[LoVo (line)]] | wt | 4.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 4.08 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.08× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 5.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +11.8) | — |
| [[SW480 (line)]] | alt | 5.30 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +11.3) | — |
| [[A-172 (line)]] | wt | 3.78 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.43 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.95 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.75 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.77 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNGB3]] | +0.81 | +0.73 / +0.76 | both halves | 7e-06 |  |
| [[LANCL1-AS1]] | +0.80 | +0.69 / +0.76 | both halves | 7e-06 | same gene group |
| [[CTDSPL2-DT]] | +0.80 | +0.74 / +0.77 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.80 | +0.70 / +0.74 | both halves | 7e-06 | same gene group |
| [[C12orf40]] | +0.78 | +0.65 / +0.78 | both halves | 7e-06 |  |
| [[TTN]] | +0.78 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.78 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[MAP3K20-AS1]] | +0.78 | +0.79 / +0.72 | both halves | 7e-06 | same gene group |
| [[ASB14]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.76 | +0.75 / +0.72 | both halves | 7e-06 | same gene group |
| [[C2CD5-AS1]] | +0.76 | +0.65 / +0.71 | both halves | 7e-06 | same gene group |
| [[SPATA21]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | SYNM-AS1's natural level lowers the cells' numbers under Lapatinib ditosylate 0.5 µM (makes them more sensitive) | SYNM-AS1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.392 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.790). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.9, 26.3); signed map (32.4, 4.5). **Vector** length 51.5, 6.31% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +24.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.6 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.8 | +1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.4 | -0.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | +0.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.8 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -5.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.0 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | SYNM antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 15q26.3 — chr15:98,954,149-99,105,824 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55421) · Entrez [105371016](https://www.ncbi.nlm.nih.gov/gene/105371016) · Ensembl [ENSG00000259475](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259475)

## Data

Gene col 15202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15202); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15202]; `tensor/DDL_lfc|DDL_z.npy` [15202]; `embed/gene_vectors.npy` [15202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15202 or target_col == 15202). Every well: [[SYNM-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNM-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
