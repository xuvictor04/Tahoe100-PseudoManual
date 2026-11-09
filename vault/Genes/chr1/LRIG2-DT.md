---
symbol: "LRIG2-DT"
type: "gene"
col: 14175
ensembl_id: "ENSG00000238198"
name: "LRIG2 divergent transcript"
location: "1p13.2"
module: 35
arm: "+"
pooled_cpm: 2.81
n_lines_expressing: 50
n_dd_up: 32
n_dd_down: 1
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# LRIG2-DT

*LRIG2 divergent transcript* — 1p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.53× (z +18.0, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.615× (z -4.9, q 5e-04, down in 19 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.142×, NCI-H1573 0.0918×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.136×; ⚠ cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAXBP1-AS1]] (+0.76, fdr 7e-06), [[ZC2HC1C]] (+0.72, fdr 1e-05), [[APPBP2-DT]] (+0.72, fdr 9e-06).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LINC01905]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.53×** | +18.0 | 0e+00 | 30/32 (HEC-1-A, LS 180, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +10.5 | 1e-23 | 3/12 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.1 | 1e-13 | 1/3 (PANC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.27×** | +7.7 | 3e-12 | 2/6 (PANC-1, HOP62) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +6.0 | 2e-07 | 15/30 (NCI-H460, NCI-H23, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +5.9 | 3e-07 | 13/35 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.8 | 4e-07 | 14/44 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.78×** | +5.8 | 4e-07 | 13/43 (A498, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.49×** | +5.7 | 7e-07 | 7/45 (NCI-H23, RKO, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.68×** | +5.2 | 9e-06 | 11/43 (PANC-1, C32, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.68×** | +5.2 | 9e-06 | 9/45 (PANC-1, SW480, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.66×** | +5.1 | 1e-05 | 12/45 (NCI-H23, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.7 | 1e-04 | 5/16 (NCI-H1792, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.58×** | +4.6 | 1e-04 | 11/43 (A498, BT-474, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.6 | 1e-04 | 10/44 (C-33 A, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +4.3 | 7e-04 | 6/35 (HEC-1-A, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.002 | 9/40 (SW480, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.46×** | +3.7 | 0.008 | 7/40 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.008 | 12/43 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.009 | 3/38 (SW480, C32, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H23 0.142×, NCI-H1573 0.0918×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (NCI-H23 0.136×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.615×** | -4.9 | 5e-04 | 19/42 (NCI-H23, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.894× | -3.9 | 0.029 | 18/48 (A549, A-427, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.723× | -3.3 | 0.19 | 11/42 (SW480, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 9.45 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.136× (z -8.9) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.142× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 2.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.83× (z +9.6) | — |
| [[NCI-H1573 (line)]] | alt | 3.36 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0918× (z -8.5) |
| [[A-172 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.02 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.68 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAXBP1-AS1]] | +0.76 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[ZC2HC1C]] | +0.72 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[APPBP2-DT]] | +0.72 | +0.73 / +0.57 | both halves | 9e-06 | same gene group |
| [[ARL14EP-DT]] | +0.72 | +0.77 / +0.58 | both halves | 7e-06 | same gene group |
| [[KIF6]] | +0.71 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[RTCA-AS1]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[AHI1-DT]] | +0.70 | +0.68 / +0.43 | both halves | 3e-05 | same gene group |
| [[LRRIQ3]] | +0.70 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[UPK2]] | +0.69 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[GAS2]] | +0.69 | +0.63 / +0.43 | both halves | 3e-05 |  |
| [[C2CD5-AS1]] | +0.69 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.69 | +0.68 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01905]] | B | LINC01905 activity raises LRIG2-DT's level | lines that do not express LINC01905 (35) vs lines expressing it (15) | 1.37× lower at baseline in the lines without LINC01905 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000267327, ENSG00000267284, SLC25A24P1 |
| [[TOP2A]] | B | TOP2A activity lowers LRIG2-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.766). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (7.5, 21.7); signed map (32.8, -3.2). **Vector** length 44.9, 4.89% of its response variance represented; |z| ≥ 3 in 1,067 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +18.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +10.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.1 | +5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +3.6 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.3 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.3 | +5.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.8 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | +1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | +1.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.4 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.2 | -4.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.1 | -1.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -2.7 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | +0.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -0.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | LRIG2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1p13.2 — chr1:113,011,687-113,073,113 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:54312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:54312) · Entrez [100996251](https://www.ncbi.nlm.nih.gov/gene/100996251) · Ensembl [ENSG00000238198](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000238198)

## Data

Gene col 14175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14175); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14175]; `tensor/DDL_lfc|DDL_z.npy` [14175]; `embed/gene_vectors.npy` [14175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14175 or target_col == 14175). Every well: [[LRIG2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRIG2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
