---
symbol: "BTG1-DT"
type: "gene"
col: 14448
ensembl_id: "ENSG00000245904"
name: "BTG1 divergent transcript"
location: "12q21.33"
module: 21
arm: "+"
pooled_cpm: 3.5
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 1
n_dd_up_clean: 22
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# BTG1-DT

*BTG1 divergent transcript* — 12q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.36× (z +20.6, q 0e+00, up in 32 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.517× (z -5.2, q 1e-04, down in 22 of 44 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0353×; ⚠ unreliable plate only).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHMP3-AS1]] (+0.74, fdr 7e-06), [[HSPA2-AS1]] (+0.73, fdr 7e-06), [[C2CD5-AS1]] (+0.73, fdr 7e-06); moves opposite to [[PRKDC]] (-0.61, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14448.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.36×** | +20.6 | 0e+00 | 32/32 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.27×** | +12.1 | 3e-31 | 12/12 (HOP62, A549, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.38×** | +9.6 | 2e-19 | 15/18 (A549, HOP62, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.99×** | +8.3 | 2e-14 | 3/6 (HOP62, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.93×** | +8.1 | 5e-14 | 18/23 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.90×** | +7.1 | 1e-10 | 25/35 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.55×** | +7.1 | 1e-10 | 20/31 (HOP62, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +6.9 | 4e-10 | 27/44 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.82×** | +6.6 | 2e-09 | 31/42 (LoVo, hTERT-HPNE, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.31×** | +6.6 | 2e-09 | 23/39 (SHP-77, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.20×** | +6.2 | 3e-08 | 23/43 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +6.1 | 5e-08 | 26/44 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +5.0 | 3e-05 | 13/33 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.8 | 6e-05 | 12/42 (LOX-IMVI, SW1417, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.76×** | +4.5 | 3e-04 | 14/40 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +4.1 | 0.001 | 10/44 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.003 | 13/38 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.005 | 11/43 (KATO III, A498, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.011 | 12/43 (A498, NCI-H2030, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14448.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (NCI-H2030 0.0353×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.517×** | -5.2 | 1e-04 | 22/44 (NCI-H2030, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14448. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 7.53 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 11.0× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 3.96 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +12.4) | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.51× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0353× (z -11.2) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 2.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.3) | — |
| [[A498 (line)]] | wt | 3.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.22× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 1.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.4× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 2.42 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +10.2) | — |
| [[LoVo (line)]] | wt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.85× (z +10.7) | — |
| [[LOX-IMVI (line)]] | wt | 6.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.73× (z +9.5) | — |
| [[PANC-1 (line)]] | alt | 1.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +12.2) | — |
| [[A-427 (line)]] | wt | 3.38 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.33 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.60 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.29 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.23 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.61 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.36 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.77 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14448), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHMP3-AS1]] | +0.74 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[HSPA2-AS1]] | +0.73 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[C2CD5-AS1]] | +0.73 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.73 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[TICAM2-AS1]] | +0.72 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[EOGT-DT]] | +0.71 | +0.56 / +0.69 | both halves | 1e-05 | same gene group |
| [[SNAP25-AS1]] | +0.71 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[HNRNPD-DT]] | +0.71 | +0.65 / +0.69 | both halves | 7e-06 | same gene group |
| [[ZRANB2-AS1]] | +0.70 | +0.58 / +0.70 | both halves | 7e-06 |  |
| [[RN7SL1]] | +0.69 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[FEZ1]] | +0.69 | +0.49 / +0.74 | both halves | 1e-05 |  |
| [[PTPRT]] | +0.69 | +0.58 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.61 | -0.58 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BTG1-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.6% of all compounds | 0.006 | ⚠ off-target possible; 5 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.3, 31.0); signed map (37.0, 6.1). **Vector** length 64.7, 11.3% of its response variance represented; |z| ≥ 3 in 879 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +20.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +9.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +6.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.3 | +2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +3.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.0 | -5.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.9 | -2.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | BTG1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q21.33 — chr12:92,145,573-92,226,557 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55600](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55600) · Entrez [101928617](https://www.ncbi.nlm.nih.gov/gene/101928617) · Ensembl [ENSG00000245904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000245904)

## Data

Gene col 14448: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14448); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14448, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14448]; `tensor/DDL_lfc|DDL_z.npy` [14448]; `embed/gene_vectors.npy` [14448]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14448 or target_col == 14448). Every well: [[BTG1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTG1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
