---
symbol: "APPBP2-DT"
type: "gene"
col: 15191
ensembl_id: "ENSG00000259349"
name: "APPBP2 divergent transcript"
location: "17q23.2"
module: 35
arm: "+"
pooled_cpm: 3.42
n_lines_expressing: 50
n_dd_up: 33
n_dd_down: 4
n_dd_up_clean: 27
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# APPBP2-DT

*APPBP2 divergent transcript* — 17q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.23× (z +14.1, q 1e-42, up in 31 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.518× (z -5.6, q 1e-05, down in 20 of 42 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGP]] (+0.75, fdr 7e-06), [[AHI1-DT]] (+0.74, fdr 1e-05), [[LRIG2-DT]] (+0.72, fdr 9e-06); moves opposite to [[DGKD]] (-0.58, fdr 2e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +14.1 | 1e-42 | 31/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **2.53×** | +11.2 | 1e-26 | 30/45 (SW480, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.85×** | +11.1 | 4e-26 | 26/29 (A498, SW480, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.60×** | +7.8 | 6e-13 | 2/6 (CFPAC-1, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +6.3 | 4e-08 | 5/8 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +6.1 | 1e-07 | 17/45 (A-172, A498, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +6.0 | 1e-07 | 11/20 (LS 180, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ponatinib (drug)]] 5 µM |  | **2.02×** | +6.0 | 1e-07 | 24/46 (KATO III, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.91×** | +5.5 | 2e-06 | 21/46 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.86×** | +5.3 | 8e-06 | 14/40 (BT-474, A498, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.2 | 1e-05 | 18/36 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.5 | 3e-04 | 3/13 (CFPAC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.44×** | +4.2 | 0.001 | 9/45 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.007 | 4/45 (HEC-1-A, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.008 | 15/44 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.009 | 7/45 (BT-474, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +3.6 | 0.011 | 11/46 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +3.5 | 0.012 | 11/43 (A498, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +3.5 | 0.012 | 6/42 (A549, A-172, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -5.6 | 1e-05 | 20/42 (LS 180, C32, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.634×** | -3.9 | 0.027 | 9/46 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.647×** | -3.7 | 0.035 | 14/44 (A-427, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.662×** | -3.5 | 0.056 | 11/46 (NCI-H23, SNU-423, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.692× | -3.2 | 0.17 | 12/46 (CHP-212, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.703× | -3.0 | 0.24 | 13/42 (A498, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~23% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 2.70 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0659× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 4.15 | 0 | 1 | — | [[Roxadustat (drug)]] 5 µM 0.0579× (z -9.3) |
| [[A-172 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.64 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGP]] | +0.75 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.74 | +0.78 / +0.54 | both halves | 1e-05 | same gene group |
| [[LRIG2-DT]] | +0.72 | +0.73 / +0.57 | both halves | 9e-06 | same gene group |
| [[FAM227B]] | +0.71 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[LRRIQ3]] | +0.71 | +0.75 / +0.59 | both halves | 7e-06 |  |
| [[ZNF236-DT]] | +0.71 | +0.57 / +0.62 | both halves | 1e-05 | same gene group |
| [[IDNK]] | +0.70 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CDNF]] | +0.70 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[NSMCE1-DT]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 | same gene group |
| [[OXA1L-DT]] | +0.69 | +0.73 / +0.52 | both halves | 1e-05 | same gene group |
| [[RAB21]] | +0.68 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[TMEM202-AS1]] | +0.68 | +0.74 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DGKD]] | -0.58 | -0.58 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers APPBP2-DT's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FAM66C]] | B | FAM66C activity raises APPBP2-DT's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.51× lower at baseline in the lines without FAM66C | 0.079 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[LINC02175]] | B | LINC02175 activity raises APPBP2-DT's level | lines that do not express LINC02175 (7) vs lines expressing it (43) | 1.29× lower at baseline in the lines without LINC02175 | 0.089 | ⚠ within organs, on part of the lines; also absent: CEP41, LRRIQ3, FAM182B; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.731). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (6.1, 20.4); signed map (31.3, -8.1). **Vector** length 55.0, 7.82% of its response variance represented; |z| ≥ 3 in 1,054 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +4.8 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +14.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +6.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.6 | -0.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.6 | +4.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -2.4 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.2 | +3.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.1 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.7 | -2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -3.9 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.2 | -1.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.3 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.1 | -1.5 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -1.1 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | APPBP2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17q23.2 — chr17:60,526,272-60,550,798 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55423) · Entrez [120017341](https://www.ncbi.nlm.nih.gov/gene/120017341) · Ensembl [ENSG00000259349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259349)

## Data

Gene col 15191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15191); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15191]; `tensor/DDL_lfc|DDL_z.npy` [15191]; `embed/gene_vectors.npy` [15191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15191 or target_col == 15191). Every well: [[APPBP2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APPBP2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
