---
symbol: "HERC2P10"
type: "gene"
col: 15238
ensembl_id: "ENSG00000259845"
name: "HERC2 pseudogene 10"
location: "15q13.2"
module: 67
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 36
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# HERC2P10

*HERC2 pseudogene 10* — 15q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.27× (z +8.7, q 2e-15, up in 0 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Lidocaine (hydrochloride) (drug)]] 0.05 µM: 1.52× (z +4.6, q 6e-04, up in 1 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.591× (z -5.5, q 9e-06, down in 10 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRIM2]] (+0.53, fdr 4e-05), [[CENPI]] (+0.53, fdr 3e-05), [[PARPBP]] (+0.52, fdr 6e-05); moves opposite to [[ZMYM5]] (-0.50, fdr 1e-04), [[ATOSA]] (-0.49, fdr 4e-05), [[RNF19B]] (-0.48, fdr 2e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[HELLPAR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15238.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.27×** | +8.7 | 2e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.82×** | +6.1 | 3e-07 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.52×** | +4.6 | 6e-04 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.52×** | +4.6 | 6e-04 | 1/11 (LoVo) | all doses, flat | low cells (technical?); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.17×** | +4.5 | 1e-03 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.05 µM |  | **1.51×** | +4.2 | 0.003 | 2/14 (SW480, HEC-1-A) | inconsistent across doses | low cells (technical?); position effect removed |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.029 | 0/20 | inconsistent across doses | low cells (technical?) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.56×** | +3.5 | 0.029 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +3.5 | 0.029 | 5/13 (RPMI-7951, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.81×** | +3.4 | 0.035 | 0/23 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (drug)]] 0.05 µM |  | **1.36×** | +3.4 | 0.035 | 0/24 | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.068 | 1/15 (SW480) | inconsistent across doses |  |
| [[Sonidegib (drug)]] 5 µM |  | **1.71×** | +3.1 | 0.089 | 0/9 | top dose only | noisy plate (z scaled); position effect removed |
| [[Orlistat (drug)]] 0.05 µM |  | **1.35×** | +3.0 | 0.095 | 1/14 (hTERT-HPNE) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15238.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.591×** | -5.5 | 9e-06 | 10/25 (A549, HOP62, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.604×** | -5.5 | 9e-06 | 8/29 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.9 | 2e-04 | 9/20 (C32, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.7 | 0.025 | 9/31 (SK-MEL-2, CFPAC-1, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -3.4 | 0.059 | 11/25 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[OTS514 (drug)]] 0.05 µM | ⚠ transcription drop | **0.719×** | -3.4 | 0.059 | 6/25 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 0.5 µM |  | **0.652×** | -3.3 | 0.059 | 5/31 (SK-MEL-2, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.737×** | -3.3 | 0.059 | 3/27 (LOX-IMVI, LS 180, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.756× | -3.1 | 0.14 | 4/31 (A-172, HOP62, …) | two highest doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15238. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 35.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.110× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 9.55 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.287× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.69 | 0 | 1 | — | [[Menadione (drug)]] 0.05 µM 0.0660× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 2.24 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0344× (z -10.4) |
| [[HOP62 (line)]] | alt | 2.36 | 0 | 1 | — | [[Retinoic acid (drug)]] 0.5 µM 0.0540× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 19.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.104× (z -17.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.999 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.30 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.587 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.671 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.439 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.953 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.93 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.691 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.645 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.905 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.675 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.846 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.792 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15238), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRIM2]] | +0.53 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[CENPI]] | +0.53 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[PARPBP]] | +0.52 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[NEIL3]] | +0.52 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[CCDC150]] | +0.51 | +0.53 / +0.36 | both halves | 1e-04 |  |
| [[IQGAP3]] | +0.51 | +0.54 / +0.37 | both halves | 8e-05 |  |
| [[POLQ]] | +0.50 | +0.50 / +0.35 | both halves | 1e-04 |  |
| [[MRPS27]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[CIT]] | +0.49 | +0.47 / +0.37 | both halves | 9e-05 |  |
| [[SPATA5]] | +0.49 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[MIR924HG]] | +0.49 | +0.51 / +0.33 | both halves | 1e-04 |  |
| [[POLA1]] | +0.48 | +0.50 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.50 | -0.35 / -0.52 | both halves | 1e-04 |  |
| [[ATOSA]] | -0.49 | -0.43 / -0.43 | both halves | 4e-05 |  |
| [[RNF19B]] | -0.48 | -0.29 / -0.46 | both halves | 2e-04 |  |
| [[LNX2]] | -0.48 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[CREBRF]] | -0.48 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[PIK3IP1]] | -0.47 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[TAB3]] | -0.47 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[TERF2IP]] | -0.47 | -0.31 / -0.52 | both halves | 2e-04 |  |
| [[LACTB]] | -0.47 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[ABCA5]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[RPS27L]] | -0.47 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[FBXL3]] | -0.46 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HELLPAR]] | B | HERC2P10 activity raises HELLPAR's level | lines that do not express HERC2P10 (14) vs lines expressing it (36) | 1.73× lower at baseline in the lines without HERC2P10 | 0.079 | ⚠ within organs, on part of the lines; also absent: TENM3, SHANK1, TENM3-AS1; maybe low, not absent |
| cells under [[Gemcitabine (drug)]] 5 µM | B | HERC2P10 activity lowers the cells' numbers under Gemcitabine 5 µM (makes them more sensitive) | lines that do not express HERC2P10 (14) vs lines expressing it (34) | the lines without HERC2P10: 1.16× the cells of the other lines | 0.0995 | ⚠ within organs, on part of the lines; also absent: TENM3, SHANK1, TENM3-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.445). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.2, -52.9); signed map (-45.8, -41.1). **Vector** length 29.8, 3.21% of its response variance represented; |z| ≥ 3 in 793 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.8 | +6.1 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.6 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +0.9 | +2.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.6 | +2.5 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.6 | +0.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -3.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | +0.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.6 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | HERC2 pseudogene 10 |
| Locus type | pseudogene |
| Location | 15q13.2 — chr15:30,815,271-30,844,153 (+) |
| Ensembl biotype | unprocessed_pseudogene |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:39056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:39056) · Entrez [390561](https://www.ncbi.nlm.nih.gov/gene/390561) · Ensembl [ENSG00000259845](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000259845)

## Data

Gene col 15238: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15238); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15238, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15238]; `tensor/DDL_lfc|DDL_z.npy` [15238]; `embed/gene_vectors.npy` [15238]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15238 or target_col == 15238). Every well: [[HERC2P10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC2P10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
