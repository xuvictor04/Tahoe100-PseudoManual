---
symbol: "DRD4"
type: "gene"
col: 924
ensembl_id: "ENSG00000069696"
name: "dopamine receptor D4"
location: "11p15.5"
module: 52
arm: "+"
pooled_cpm: 3.17
n_lines_expressing: 45
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 3
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# DRD4

*dopamine receptor D4* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +6.1, q 5e-07, up in 14 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.349× (z -9.2, q 2e-17, down in 28 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP1R32]] (+0.73, fdr 7e-06), [[ANKS3]] (+0.69, fdr 7e-06), [[VPS53]] (+0.68, fdr 7e-06); moves opposite to [[VEZF1]] (-0.69, fdr 7e-06), [[ARMT1]] (-0.68, fdr 7e-06), [[GMFB]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TTC30A]] → it (grade B ⚠); 3 go from it, the strongest it → [[SCARB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 924.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.1 | 5e-07 | 14/30 (C32, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.69×** | +4.8 | 4e-04 | 13/40 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.5 | 0.001 | 10/36 (SW480, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.084 | 7/27 (HEC-1-A, SW480, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +3.3 | 0.099 | 1/23 (HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 924.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.349×** | -9.2 | 2e-17 | 28/38 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **0.785×** | -7.6 | 8e-12 | 28/41 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.499×** | -6.3 | 5e-08 | 21/38 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.606×** | -4.4 | 0.002 | 7/17 (HEC-1-A, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.601×** | -4.3 | 0.002 | 12/28 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.620×** | -4.2 | 0.003 | 14/32 (LS 180, AsPC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.713×** | -4.0 | 0.005 | 16/31 (SW1417, SNU-423, …) | all doses, flat | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.675×** | -3.6 | 0.026 | 12/40 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.686×** | -3.2 | 0.092 | 6/37 (HOP62, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.707×** | -3.2 | 0.092 | 12/35 (A498, KATO III, …) | all doses, flat |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.713× | -3.1 | 0.11 | 9/38 (H4, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.717× | -3.0 | 0.12 | 8/37 (KATO III, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 924. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.35 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0676× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 5.76 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -10.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0934× (z -9.6) |
| [[A498 (line)]] | wt | 3.79 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0974× (z -9.4) |
| [[SNU-423 (line)]] | alt | 8.07 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0684× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~1% of this change |
| [[A549 (line)]] | wt | 2.31 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0453× (z -8.5) |
| [[A-172 (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 3.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.712 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.827 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.692 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.562 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.04 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.723 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 924), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R32]] | +0.73 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[ANKS3]] | +0.69 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[VPS53]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[QPCTL]] | +0.67 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[GET1-SH3BGR]] | +0.67 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[UQCRH]] | +0.66 | +0.53 / +0.71 | both halves | 1e-05 |  |
| [[NPIPB11]] | +0.66 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.66 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[BNIPL]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[CSNK1G2]] | +0.65 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[LINC02935]] | +0.65 | +0.64 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VEZF1]] | -0.69 | -0.58 / -0.72 | both halves | 7e-06 |  |
| [[ARMT1]] | -0.68 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[GMFB]] | -0.68 | -0.63 / -0.65 | both halves | 7e-06 |  |
| [[ZNF260]] | -0.68 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[COMMD8]] | -0.65 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[CFL2]] | -0.65 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[ZBTB33]] | -0.64 | -0.56 / -0.62 | both halves | 1e-05 |  |
| [[UROS]] | -0.63 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[RFK]] | -0.63 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[DCLRE1A]] | -0.62 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[AKAP11]] | -0.62 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[NCOA4]] | -0.62 | -0.55 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TTC30A]] | B | TTC30A activity raises DRD4's level | lines that do not express TTC30A (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without TTC30A | 0.025 | ⚠ within organs, on part of the lines; also absent: WDR35, GGT7, AGK; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers DRD4's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARB1]] | B | DRD4 activity strengthens SCARB1's drug response | lines that do not express DRD4 (5) vs lines expressing it (42) | the lines without DRD4 respond 0.38× as strongly (z diff +3.39); strongest at Homoharringtonine 0.5 µM: 0.90x vs 0.37x (z diff +6.5) | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[FAM156A]] | B | DRD4 activity raises FAM156A's level | lines that do not express DRD4 (5) vs lines expressing it (45) | 1.68× lower at baseline in the lines without DRD4 | 0.085 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SCARB1]] | B | DRD4 activity raises SCARB1's level | lines that do not express DRD4 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without DRD4 | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.597). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-13.8, -2.5); signed map (-46.1, 3.0). **Vector** length 51.7, 7.61% of its response variance represented; |z| ≥ 3 in 795 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.3 | +6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +4.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.6 | +1.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +1.5 | +4.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.0 | +1.9 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +0.9 | +1.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.4 | -9.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -1.9 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.8 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.7 | -4.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.3 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | dopamine receptor D4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:637,269-640,706 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Dopamine receptors |
| Reactome | 6 pathways, smallest: Amine ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P21917](https://www.uniprot.org/uniprotkb/P21917) (Dopamine receptor D4):

> G protein-coupled receptor for dopamine, a catecholamine neurotransmitter hormone that functions as the brain's 'reward chemical', driving motivation, reinforcement learning and pleasure. In addition to dopamine, also activated by epinephrine and norepinephrine, and by numerous synthetic agonists and drugs. Ligand binding causes a conformation change that triggers signaling via guanine nucleotide-binding proteins (G proteins) and modulates the activity of downstream effectors, such as adenylate …

**Summary**, from NCBI Gene [1815](https://www.ncbi.nlm.nih.gov/gene/1815):

> This gene encodes the D4 subtype of the dopamine receptor. The D4 subtype is a G-protein coupled receptor which inhibits adenylyl cyclase. It is a target for drugs which treat schizophrenia and Parkinson disease. Mutations in this gene have been associated with various behavioral phenotypes, including autonomic nervous system dysfunction, attention deficit/hyperactivity disorder, and the personality trait of novelty seeking. This gene contains a polymorphic number (2-10 copies) of tandem 48 nt …

**Accessions** — [HGNC:3025](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3025) · Entrez [1815](https://www.ncbi.nlm.nih.gov/gene/1815) · UniProt [P21917](https://www.uniprot.org/uniprotkb/P21917) · Ensembl [ENSG00000069696](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069696)

## Data

Gene col 924: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 924); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 924, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 924]; `tensor/DDL_lfc|DDL_z.npy` [924]; `embed/gene_vectors.npy` [924]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 924 or target_col == 924). Every well: [[DRD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DRD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
