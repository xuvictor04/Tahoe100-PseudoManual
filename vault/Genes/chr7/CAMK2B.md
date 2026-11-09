---
symbol: "CAMK2B"
type: "gene"
col: 661
ensembl_id: "ENSG00000058404"
name: "calcium/calmodulin dependent protein kinase II beta"
location: "7p13"
module: 102
arm: "+"
pooled_cpm: 3.31
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# CAMK2B

*calcium/calmodulin dependent protein kinase II beta* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +12.1, q 7e-31, up in 7 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.87× (z +12.0, q 1e-30, up in 30 of 44 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.185×, Panc 03.27 0.132×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.134×, A-427 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (C-33 A 0.0453×; ⚠ cell-cycle shift, explains ~9% of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.0853×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0530×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CELF5]] (+0.73, fdr 7e-06), [[SYN1]] (+0.70, fdr 7e-06), [[KCNQ2]] (+0.67, fdr 7e-06).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 661.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +12.1 | 7e-31 | 7/13 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.87×** | +12.0 | 1e-30 | 30/44 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.02×** | +11.3 | 2e-27 | 27/44 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +10.9 | 2e-25 | 2/4 (MIA PaCa-2, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +9.7 | 4e-20 | 13/31 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.32×** | +9.6 | 1e-19 | 20/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +9.3 | 2e-18 | 1/4 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +6.6 | 3e-09 | 14/35 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.68×** | +5.9 | 3e-07 | 15/42 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.29×** | +4.9 | 5e-05 | 2/7 (MIA PaCa-2, NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.003 | 11/43 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.36×** | +3.4 | 0.027 | 3/23 (Panc 03.27, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +3.4 | 0.027 | 5/36 (A-172, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 661.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.185×, Panc 03.27 0.132×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (A498 0.134×, A-427 0.173×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.05 µM in 1 line (C-33 A 0.0453×; ⚠ cell-cycle shift, explains ~9% of this change); [[Cysteamine (hydrochloride) (drug)]] 0.5 µM in 1 line (SHP-77 0.0853×); [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM in 1 line (RPMI-7951 0.0530×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.741× | -3.5 | 0.27 | 8/43 (Panc 03.27, RPMI-7951, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.753× | -3.3 | 0.27 | 8/44 (A-427, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 661. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 12.9 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.8) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -12.1) |
| [[A498 (line)]] | wt | 2.18 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0453× (z -11.3) ⚠ cell-cycle shift, explains ~9% of this change |
| [[Panc 03.27 (line)]] | alt | 5.28 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 9.37 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0530× (z -9.3) |
| [[SHP-77 (line)]] | alt | 7.57 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0853× (z -9.9) |
| [[A-172 (line)]] | wt | 7.50 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.939 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.893 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.81 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.887 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.73 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.967 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.828 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.981 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.929 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.61 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 661), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CELF5]] | +0.73 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[SYN1]] | +0.70 | +0.61 / +0.73 | both halves | 7e-06 | pathway: Neuronal System; STRING 451 |
| [[KCNQ2]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 | pathway: Neuronal System |
| [[TMEM266]] | +0.64 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[GSG1L]] | +0.63 | +0.57 / +0.68 | both halves | 9e-06 |  |
| [[CDH23]] | +0.63 | +0.51 / +0.75 | both halves | 1e-05 |  |
| [[RASGEF1C]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[BMP8A]] | +0.60 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[GPM6B]] | +0.60 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[JAKMIP1]] | +0.60 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[LHX4]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[SYN2]] | +0.59 | +0.43 / +0.64 | both halves | 3e-05 | pathway: Neuronal System |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises CAMK2B's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.82× lower at baseline in the lines without CHD5 | 0.029 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[RET]] | B | RET activity raises CAMK2B's level | lines that do not express RET (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without RET | 0.036 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[SDK1]] | B | SDK1 activity raises CAMK2B's level | lines that do not express SDK1 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without SDK1 | 0.043 | ⚠ within organs, on part of the lines; also absent: PCBP3, ACKR3, SLIT3 |
| [[DPYSL5]] | B | DPYSL5 activity raises CAMK2B's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 1.65× lower at baseline in the lines without DPYSL5 | 0.059 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5 |
| [[ADGRA2]] | B | ADGRA2 activity raises CAMK2B's level | lines that do not express ADGRA2 (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without ADGRA2 | 0.068 | ⚠ within organs, on part of the lines; also absent: CERCAM, SPEG, STARD9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.6, 35.2); signed map (28.1, 20.6). **Vector** length 51.5, 6.66% of its response variance represented; |z| ≥ 3 in 1,044 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +10.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +6.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.7 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.4 | +3.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.3 | +2.9 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -3.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.4 | -3.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.4 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | calcium/calmodulin dependent protein kinase II beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,210,019-44,334,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAM2, CAMK2, CaMKIIβ; previously CAMKB |
| Gene groups (HGNC) | CAMK2 family |
| Hallmark sets | MYOGENESIS |
| Reactome | 57 pathways, smallest: CREB1 phosphorylation through the activation of CaMKII/CaMKK/CaMKIV cascasde; CaMK IV-mediated phosphorylation of CREB; Ras activation upon Ca2+ influx through NMDA receptor |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13554](https://www.uniprot.org/uniprotkb/Q13554) (Calcium/calmodulin-dependent protein kinase type II subunit beta):

> Calcium/calmodulin-dependent protein kinase that functions autonomously after Ca(2+)/calmodulin-binding and autophosphorylation, and is involved in dendritic spine and synapse formation, neuronal plasticity and regulation of sarcoplasmic reticulum Ca(2+) transport in skeletal muscle. In neurons, plays an essential structural role in the reorganization of the actin cytoskeleton during plasticity by binding and bundling actin filaments in a kinase-independent manner. This structural function is …

**Summary**, from NCBI Gene [816](https://www.ncbi.nlm.nih.gov/gene/816):

> The product of this gene belongs to the serine/threonine protein kinase family and to the Ca(2+)/calmodulin-dependent protein kinase subfamily. Calcium signaling is crucial for several aspects of plasticity at glutamatergic synapses. In mammalian cells, the enzyme is composed of four different chains: alpha, beta, gamma, and delta. The product of this gene is a beta chain. It is possible that distinct isoforms of this chain have different cellular localizations and interact differently with …

**Accessions** — [HGNC:1461](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1461) · Entrez [816](https://www.ncbi.nlm.nih.gov/gene/816) · UniProt [Q13554](https://www.uniprot.org/uniprotkb/Q13554) · Ensembl [ENSG00000058404](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058404)

## Data

Gene col 661: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 661); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 661, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 661]; `tensor/DDL_lfc|DDL_z.npy` [661]; `embed/gene_vectors.npy` [661]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 661 or target_col == 661). Every well: [[CAMK2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMK2B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
