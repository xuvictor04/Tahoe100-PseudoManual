---
symbol: "LPAR2"
type: "gene"
col: 749
ensembl_id: "ENSG00000064547"
name: "lysophosphatidic acid receptor 2"
location: "19p13.11"
module: 31
arm: "+"
pooled_cpm: 3.04
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 5
n_dd_up_clean: 1
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# LPAR2

*lysophosphatidic acid receptor 2* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +8.5, q 8e-15, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.59× (z +3.3, q 0.084, up in 2 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.633× (z -4.6, q 0.001, down in 11 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GMIP]] (+0.63, fdr 7e-06, ⚠ same locus), [[PAQR6]] (+0.59, fdr 2e-05), [[LAT]] (+0.55, fdr 2e-05), [[ARHGEF5]] (+0.53, fdr 1e-05); moves opposite to [[PARK7]] (-0.53, fdr 1e-04, ⚠ PARK7 in the vector space only through flagged drug-doses), [[EID1]] (-0.50, fdr 6e-05), [[CXADR]] (-0.49, fdr 3e-05), [[DOP1A]] (-0.48, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TMC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +8.5 | 8e-15 | 2/4 (A498, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +5.2 | 7e-05 | 4/17 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +4.7 | 4e-04 | 2/7 (A498, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.011 | 5/19 (HCT15, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.00×** | +3.6 | 0.035 | 3/9 (PANC-1, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.60×** | +3.4 | 0.073 | 0/10 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.59×** | +3.3 | 0.084 | 2/27 (LS 180, SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.53× | +3.0 | 0.17 | 1/31 (HT-29) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.633×** | -4.6 | 0.001 | 11/45 (HOP62, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.727×** | -4.5 | 0.001 | 16/31 (PANC-1, SW480, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.425×** | -4.5 | 0.001 | 12/36 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.675×** | -4.0 | 0.011 | 9/45 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -3.7 | 0.020 | 12/27 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.722× | -3.1 | 0.18 | 6/41 (HS-578T, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 5.25 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0741× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 3.34 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0881× (z -8.8) ⚠ cell-cycle shift, explains ~7% of this change |
| [[HEC-1-A (line)]] | alt | 3.81 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.101× (z -8.5) |
| [[PANC-1 (line)]] | alt | 2.49 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -13.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.64 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.34 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.79 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMIP]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.5 kb, same strand: neighbours can correlate without regulation) |
| [[PAQR6]] | +0.59 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[LAT]] | +0.55 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[ARHGEF5]] | +0.53 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ADCY7]] | +0.53 | +0.39 / +0.59 | both halves | 6e-05 | pathway: G alpha (i) signalling events |
| [[SPRED3]] | +0.53 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[ARHGAP27]] | +0.53 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ARHGEF1]] | +0.52 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[LIMD2]] | +0.51 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[ALKBH6]] | +0.51 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[PLEKHN1]] | +0.50 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[SLC22A20P]] | +0.50 | +0.50 / +0.44 | both halves | 3e-05 |  |
| [[FPGS]] | +0.50 | +0.49 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARK7]] ⚠ | -0.53 | -0.32 / -0.55 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[EID1]] | -0.50 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[CXADR]] | -0.49 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[DOP1A]] | -0.48 | -0.46 / -0.42 | both halves | 4e-05 |  |
| [[ATP5F1A]] | -0.48 | -0.28 / -0.58 | both halves | 3e-04 |  |
| [[SLC44A1]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LRP11]] | -0.47 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[IFT80]] | -0.47 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[MLLT3]] | -0.46 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[ATRAID]] | -0.46 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[WDPCP]] | -0.46 | -0.38 / -0.44 | both halves | 7e-05 |  |
| [[TMEM14C]] | -0.45 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[PRDX2]] | -0.45 | -0.40 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMC6]] | B | TMC6 activity raises LPAR2's level | lines that do not express TMC6 (12) vs lines expressing it (38) | 1.54× lower at baseline in the lines without TMC6 | 0.006 | ⚠ within organs, on part of the lines; also absent: CAMSAP3, FGFR4, LSR |
| [[CXADR]] | B | CXADR activity raises LPAR2's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.23× lower at baseline in the lines without CXADR | 0.028 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[SLC16A5]] | B | SLC16A5 activity raises LPAR2's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 1.17× lower at baseline in the lines without SLC16A5 | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.332). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.9, -9.3); signed map (9.5, 16.5). **Vector** length 39.1, 3.97% of its response variance represented; |z| ≥ 3 in 895 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +8.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +2.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +1.2 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.5 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.0 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -2.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -2.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.5 | -3.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -1.7 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | lysophosphatidic acid receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,623,655-19,628,930 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EDG-4, LPA2; previously EDG4 |
| Gene groups (HGNC) | Lysophosphatidic acid receptors |
| Reactome | 7 pathways, smallest: Lysosphingolipid and LPA receptors; Class A/1 (Rhodopsin-like receptors); G alpha (q) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBW0](https://www.uniprot.org/uniprotkb/Q9HBW0) (Lysophosphatidic acid receptor 2):

> Receptor for lysophosphatidic acid (LPA), a mediator of diverse cellular activities. Seems to be coupled to the G(i)/G(o), G(12)/G(13), and G(q) families of heteromeric G proteins. Plays a key role in phospholipase C-beta (PLC-beta) signaling pathway. Stimulates phospholipase C (PLC) activity in a manner that is independent of RALA activation.

**Summary**, from NCBI Gene [9170](https://www.ncbi.nlm.nih.gov/gene/9170):

> This gene encodes a member of family I of the G protein-coupled receptors, as well as the EDG family of proteins. This protein functions as a lysophosphatidic acid (LPA) receptor and contributes to Ca2+ mobilization, a critical cellular response to LPA in cells, through association with Gi and Gq proteins. An alternative splice variant has been described but its full length sequence has not been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3168](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3168) · Entrez [9170](https://www.ncbi.nlm.nih.gov/gene/9170) · UniProt [Q9HBW0](https://www.uniprot.org/uniprotkb/Q9HBW0) · Ensembl [ENSG00000064547](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064547)

## Data

Gene col 749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 749); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 749]; `tensor/DDL_lfc|DDL_z.npy` [749]; `embed/gene_vectors.npy` [749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 749 or target_col == 749). Every well: [[LPAR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LPAR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
