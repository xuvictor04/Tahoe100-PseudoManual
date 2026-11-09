---
symbol: "RUSC1-AS1"
type: "gene"
col: 13491
ensembl_id: "ENSG00000225855"
name: "RUSC1 antisense RNA 1"
location: "1q22"
module: 35
arm: "+"
pooled_cpm: 2.14
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# RUSC1-AS1

*RUSC1 antisense RNA 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 3.17× (z +8.1, q 4e-13, up in 0 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +7.4, q 2e-11, up in 17 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.430× (z -6.4, q 1e-07, down in 23 of 45 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.535× (z -4.7, q 5e-04, down in 18 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sulfatinib (drug)]] 5 µM in 1 line (NCI-H23 0.0553×).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUMO2P17]] (+0.72, fdr 1e-05), [[ZBTB22]] (+0.67, fdr 1e-05), [[ATXN7L3-AS1]] (+0.66, fdr 2e-05); moves opposite to [[NBPF3]] (-0.58, fdr 7e-05), [[ABHD6]] (-0.57, fdr 1e-04), [[ATG4C]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYP1B1-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13491.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +8.1 | 4e-13 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.00×** | +8.0 | 4e-13 | 0/1 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +7.4 | 2e-11 | 17/32 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.78×** | +6.2 | 1e-07 | 13/34 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.05×** | +5.4 | 6e-06 | 2/10 (MIA PaCa-2, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.085 | 9/35 (NCI-H23, SW480, …) | all doses, flat | position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | 1.52× | +3.1 | 0.13 | 5/34 (NCI-H2030, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | 1.54× | +3.0 | 0.17 | 2/22 (J82, NCI-H460) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13491.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Sulfatinib (drug)]] 5 µM in 1 line (NCI-H23 0.0553×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.430×** | -6.4 | 1e-07 | 23/45 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.505×** | -5.0 | 2e-04 | 15/39 (RPMI-7951, Panc 03.27, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.535×** | -4.7 | 5e-04 | 18/44 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.602×** | -3.8 | 0.015 | 11/45 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.603×** | -3.8 | 0.015 | 15/39 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.619×** | -3.6 | 0.028 | 9/41 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.648×** | -3.3 | 0.086 | 7/42 (HS-578T, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.52 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13491. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 4.21 | 0 | 1 | — | [[Sulfatinib (drug)]] 5 µM 0.0553× (z -8.5) |
| [[A-172 (line)]] | wt | 4.30 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.25 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.13 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13491), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMO2P17]] | +0.72 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB22]] | +0.67 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ATXN7L3-AS1]] | +0.66 | +0.49 / +0.62 | both halves | 2e-05 | same gene group |
| [[MED28-DT]] | +0.65 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[MYLK4]] | +0.65 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[AP1G2-AS1]] | +0.65 | +0.52 / +0.51 | both halves | 1e-05 | same gene group |
| [[PSMG3-AS1]] | +0.63 | +0.64 / +0.40 | both halves | 5e-05 | same gene group |
| [[MC1R]] | +0.62 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[ATN1]] | +0.62 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[KRBA2]] | +0.62 | +0.61 / +0.24 | both halves | 4e-04 |  |
| [[NRL]] | +0.62 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[GPR137]] | +0.62 | +0.65 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF3]] | -0.58 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[ABHD6]] | -0.57 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[ATG4C]] | -0.57 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[KLHL8]] | -0.57 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[ZNF215]] | -0.55 | -0.54 / -0.37 | both halves | 9e-05 |  |
| [[PIBF1]] | -0.55 | -0.42 / -0.38 | both halves | 7e-05 |  |
| [[RMND1]] | -0.54 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[SMYD3]] | -0.54 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[UBE3D]] | -0.54 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[GPATCH11]] | -0.54 | -0.23 / -0.47 | both halves | 5e-04 |  |
| [[RALGAPA2]] | -0.53 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[SLC2A3]] | -0.53 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1-AS1]] | B | CYP1B1-AS1 activity raises RUSC1-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without CYP1B1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises RUSC1-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.651). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (11.7, 20.5); signed map (26.8, -3.2). **Vector** length 46.4, 5.43% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +7.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.4 | +6.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +1.2 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.3 | +2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +1.2 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.2 | +2.8 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +1.1 | +0.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -2.2 | -3.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.1 | -4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | RUSC1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 1q22 — chr1:155,316,863-155,324,176 (-) |
| Ensembl biotype | lncRNA |
| Also known as | FLJ35976; previously C1orf104 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q66K80](https://www.uniprot.org/uniprotkb/Q66K80) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:26680](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26680) · Entrez [284618](https://www.ncbi.nlm.nih.gov/gene/284618) · UniProt [Q66K80](https://www.uniprot.org/uniprotkb/Q66K80) · Ensembl [ENSG00000225855](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225855)

## Data

Gene col 13491: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13491); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13491, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13491]; `tensor/DDL_lfc|DDL_z.npy` [13491]; `embed/gene_vectors.npy` [13491]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13491 or target_col == 13491). Every well: [[RUSC1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RUSC1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
