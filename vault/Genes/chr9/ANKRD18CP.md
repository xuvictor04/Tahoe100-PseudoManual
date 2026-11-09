---
symbol: "ANKRD18CP"
type: "gene"
col: 8271
ensembl_id: "ENSG00000159712"
name: "ankyrin repeat domain 18C, pseudogene"
location: "9q22.33"
module: 10
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 1
n_dd_up_clean: 7
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ANKRD18CP

*ankyrin repeat domain 18C, pseudogene* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.55× (z +7.4, q 8e-11, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.67× (z +6.0, q 5e-07, up in 7 of 23 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.547× (z -5.0, q 4e-04, down in 12 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.0556×, HEC-1-A 0.216×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.155×, A498 0.302×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.0677×; ⚠ cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KATNAL2]] (+0.66, fdr 1e-05), [[FAM66C]] (+0.61, fdr 1e-05), [[ACCS]] (+0.58, fdr 3e-05); moves opposite to [[GSKIP]] (-0.51, fdr 1e-04), [[MEA1]] (-0.49, fdr 6e-05), [[BACE2]] (-0.49, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clobetasol propionate (drug)]] 0.5 µM (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8271.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.55×** | +7.4 | 8e-11 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.44×** | +6.8 | 4e-09 | 1/5 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.0 | 5e-07 | 7/23 (C-33 A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +5.7 | 2e-06 | 1/10 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +5.1 | 4e-05 | 17/36 (MIA PaCa-2, RKO, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.64×** | +3.9 | 0.009 | 3/26 (J82, C-33 A, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.046 | 4/28 (HEC-1-A, A498, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.34×** | +3.3 | 0.064 | 2/35 (SHP-77, CFPAC-1) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.075 | 4/33 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +3.2 | 0.075 | 4/29 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 1.46× | +3.1 | 0.11 | 3/16 (NCI-H23, LoVo, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.30× | +3.0 | 0.11 | 4/37 (A498, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.44× | +3.0 | 0.11 | 7/30 (A498, HT-29, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8271.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.0556×, HEC-1-A 0.216×; ⚠ cell-cycle shift, would explain all of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.155×, A498 0.302×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (PANC-1 0.0677×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.547×** | -5.0 | 4e-04 | 12/35 (H4, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.675× | -3.2 | 0.24 | 13/36 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.676× | -3.2 | 0.24 | 8/34 (J82, BT-474, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.765× | -3.1 | 0.25 | 9/35 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.693× | -3.0 | 0.25 | 9/29 (PANC-1, H4, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8271. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0556× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -8.6) |
| [[PANC-1 (line)]] | alt | 3.73 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0677× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 7.92 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -10.1) |
| [[A-172 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.932 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.43 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.673 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.765 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.355 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.440 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.616 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.576 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.782 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.874 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.843 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.74 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8271), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KATNAL2]] | +0.66 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[FAM66C]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ACCS]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[LINC02482]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 |  |
| [[CARF]] | +0.54 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[TMCC1-DT]] | +0.54 | +0.52 / +0.41 | both halves | 4e-05 |  |
| [[KLHDC1]] | +0.54 | +0.60 / +0.38 | both halves | 7e-05 |  |
| [[C5]] | +0.53 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[C21orf62-AS1]] | +0.52 | +0.61 / +0.43 | both halves | 4e-05 |  |
| [[LINC00466]] | +0.52 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[PCMTD1-DT]] | +0.52 | +0.58 / +0.35 | both halves | 1e-04 |  |
| [[DDX59-AS1]] | +0.51 | +0.57 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSKIP]] | -0.51 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[MEA1]] | -0.49 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[BACE2]] | -0.49 | -0.55 / -0.36 | both halves | 1e-04 |  |
| [[TMEM184B]] | -0.46 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[KDM7A]] | -0.45 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[LIMCH1]] | -0.44 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[SNX25]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clobetasol propionate (drug)]] 0.5 µM | B | ANKRD18CP activity raises the cells' numbers under Clobetasol propionate 0.5 µM (protects the cells) | lines that do not express ANKRD18CP (6) vs lines expressing it (42) | the lines without ANKRD18CP: 0.80× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ZFHX2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (6.6, 30.6); signed map (36.2, -9.9). **Vector** length 41.2, 5.29% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.1 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.8 | +5.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.8 | +1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.5 | +7.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.3 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.1 | +2.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.1 | +3.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.0 | +2.2 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -1.6 | -3.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -1.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.1 | -3.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 18C, pseudogene |
| Locus type | pseudogene |
| Location | 9q22.33 — chr9:97,156,570-97,221,235 (-) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:43601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:43601) · Entrez [101926917](https://www.ncbi.nlm.nih.gov/gene/101926917) · Ensembl [ENSG00000159712](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000159712)

## Data

Gene col 8271: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8271); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8271, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8271]; `tensor/DDL_lfc|DDL_z.npy` [8271]; `embed/gene_vectors.npy` [8271]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8271 or target_col == 8271). Every well: [[ANKRD18CP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD18CP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
