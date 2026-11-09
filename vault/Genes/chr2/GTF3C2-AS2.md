---
symbol: "GTF3C2-AS2"
type: "gene"
col: 13937
ensembl_id: "ENSG00000234072"
name: "GTF3C2 antisense RNA 2"
location: "2p23.3"
module: 15
arm: "+"
pooled_cpm: 5.29
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# GTF3C2-AS2

*GTF3C2 antisense RNA 2* — 2p23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +17.8, q 0e+00, up in 38 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.711× (z -4.0, q 0.042, down in 17 of 44 measured lines) ⚠ cell-cycle shift, explains ~66% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0873×); [[Apalutamide (drug)]] 0.05 µM in 1 line (A-172 0.0889×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF213-AS1]] (+0.80, fdr 7e-06), [[ZNF596]] (+0.76, fdr 7e-06), [[MYLK4]] (+0.74, fdr 7e-06); moves opposite to [[ISCA2]] (-0.70, fdr 2e-05), [[TTBK2]] (-0.64, fdr 9e-05), [[HPF1]] (-0.62, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13937.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +17.8 | 0e+00 | 38/40 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.00×** | +12.2 | 1e-31 | 12/14 (NCI-H460, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +9.5 | 5e-19 | 18/29 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.07×** | +8.7 | 4e-16 | 14/24 (LS 180, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.6 | 4e-12 | 5/9 (SW480, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +7.5 | 8e-12 | 16/35 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.73×** | +6.5 | 5e-09 | 22/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.41×** | +5.8 | 5e-07 | 17/46 (A498, NCI-H2347, …) | rises with dose | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +5.4 | 4e-06 | 10/48 (LS 180, A-427, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +5.2 | 1e-05 | 15/40 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.46×** | +4.5 | 4e-04 | 13/44 (HEC-1-A, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.4 | 6e-04 | 15/41 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.35×** | +3.6 | 0.013 | 6/27 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +3.5 | 0.022 | 8/38 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.023 | 13/47 (BT-474, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.30×** | +3.0 | 0.095 | 7/44 (A549, A498, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13937.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0873×); [[Apalutamide (drug)]] 0.05 µM in 1 line (A-172 0.0889×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.711×** | -4.0 | 0.042 | 17/44 (A-427, PANC-1, …) | rises with dose | composition shift |
| [[Imiquimod (maleate) (drug)]] 0.05 µM |  | 0.751× | -3.2 | 0.33 | 9/40 (A-172, C-33 A, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 0.609× | -3.1 | 0.33 | 8/35 (LOX-IMVI, NCI-H23, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13937. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 4.62 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0889× (z -9.0) |
| [[PANC-1 (line)]] | alt | 6.20 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 8.38 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0873× (z -10.3) |
| [[SW480 (line)]] | alt | 9.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +8.9) | — |
| [[A-427 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.63 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.52 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.86 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.50 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13937), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF213-AS1]] | +0.80 | +0.74 / +0.66 | both halves | 7e-06 | same gene group |
| [[ZNF596]] | +0.76 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MYLK4]] | +0.74 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[LENG8-AS1]] | +0.74 | +0.64 / +0.64 | both halves | 7e-06 | same gene group |
| [[MSTO1]] | +0.73 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[CTTN-DT]] | +0.72 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[GLIPR1-AS1]] | +0.71 | +0.62 / +0.51 | both halves | 1e-05 | same gene group |
| [[SNHG22]] | +0.70 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[SNHG10]] | +0.70 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[ZFHX2-AS1]] | +0.70 | +0.53 / +0.52 | both halves | 1e-05 | same gene group |
| [[SIAH2-AS1]] | +0.70 | +0.59 / +0.45 | both halves | 3e-05 | same gene group |
| [[NIPBL-DT]] | +0.70 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISCA2]] | -0.70 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[TTBK2]] | -0.64 | -0.36 / -0.54 | both halves | 9e-05 |  |
| [[HPF1]] | -0.62 | -0.27 / -0.47 | both halves | 3e-04 |  |
| [[PAFAH1B3]] | -0.61 | -0.35 / -0.33 | both halves | 1e-04 |  |
| [[ALAD]] | -0.60 | -0.47 / -0.29 | both halves | 2e-04 |  |
| [[GPATCH11]] | -0.59 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[USP2]] | -0.59 | -0.38 / -0.43 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GTF3C2-AS2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.779). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-6.1, 21.8); signed map (30.0, -17.5). **Vector** length 56.1, 7.22% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +17.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +7.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.5 | +9.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +4.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.2 | +1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +3.0 |
|  | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM |  | +0.9 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -0.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | +0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -2.2 | -4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -1.3 | -0.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.2 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | GTF3C2 antisense RNA 2 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p23.3 — chr2:27,356,246-27,367,622 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AC074117.10, AC074117.1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55699) · Entrez [105374363](https://www.ncbi.nlm.nih.gov/gene/105374363) · Ensembl [ENSG00000234072](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000234072)

## Data

Gene col 13937: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13937); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13937, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13937]; `tensor/DDL_lfc|DDL_z.npy` [13937]; `embed/gene_vectors.npy` [13937]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13937 or target_col == 13937). Every well: [[GTF3C2-AS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GTF3C2-AS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
