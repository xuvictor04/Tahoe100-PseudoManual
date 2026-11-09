---
symbol: "PCBP1"
type: "gene"
col: 9817
ensembl_id: "ENSG00000169564"
name: "poly(rC) binding protein 1"
location: "2p13.3"
module: 7
arm: "+"
pooled_cpm: 69.67
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# PCBP1

*poly(rC) binding protein 1* — 2p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.66× (z +7.9, q 1e-12, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.584× (z -8.4, q 3e-14, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF845]] (+0.62, fdr 4e-05), [[ZNF510]] (+0.61, fdr 7e-05), [[RBM15B]] (+0.61, fdr 1e-05); moves opposite to [[NFATC2IP]] (-0.51, fdr 4e-04), [[ATP1B3]] (-0.49, fdr 2e-04), [[CSAD]] (-0.47, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF548]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9817.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.66×** | +7.9 | 1e-12 | 42/49 (COLO 205, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +6.6 | 1e-08 | 31/49 (NCI-H23, A549, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.48×** | +6.0 | 3e-07 | 38/47 (HOP62, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.04×** | +5.8 | 1e-06 | 34/48 (KATO III, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.7 | 1e-06 | 32/44 (A549, A498, …) | two highest doses | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.5 | 3e-06 | 35/48 (A-172, HEC-1-A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.26×** | +3.6 | 0.029 | 24/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +3.4 | 0.042 | 23/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9817.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.584×** | -8.4 | 3e-14 | 44/48 (SW 900, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -7.4 | 4e-11 | 37/49 (A498, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -6.4 | 3e-08 | 35/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.685×** | -5.9 | 5e-07 | 35/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | **0.726×** | -5.0 | 7e-05 | 40/48 (RPMI-7951, SHP-77, …) | two highest doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.745×** | -4.4 | 1e-03 | 34/48 (AN3 CA, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.757×** | -4.3 | 0.001 | 33/48 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.782×** | -3.7 | 0.014 | 25/49 (HepG2/C3A, PANC-1, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.844× | -3.7 | 0.014 | 17/48 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.638×** | -3.7 | 0.014 | 26/49 (AsPC-1, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.800×** | -3.5 | 0.025 | 24/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.813×** | -3.2 | 0.058 | 19/48 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trimetrexate (drug)]] 5 µM |  | 0.861× | -3.1 | 0.077 | 13/49 (A549, C-33 A, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.810×** | -3.1 | 0.078 | 17/48 (CHP-212, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Fostamatinib (disodium hexahydrate) (drug)]] 5 µM | ⚠ unreliable plate only | **0.823×** | -3.0 | 0.091 | 16/48 (HT-29, C32, …) | top dose only | position effect removed |
| [[Bergenin (drug)]] 5 µM |  | 0.868× | -3.0 | 0.099 | 6/49 (RKO, HOP62, …) | two highest doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9817. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 54.9 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 64.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +8.6) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -10.8) |
| [[A549 (line)]] | wt | 72.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +10.2) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 90.6 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.475× (z -8.5) |
| [[AN3 CA (line)]] | alt | 104 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -10.5) |
| [[CFPAC-1 (line)]] | alt | 88.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.392× (z -8.5) |
| [[HOP62 (line)]] | alt | 50.1 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.44× (z +8.8) ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 89.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 88.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 81.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.487× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 64.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.387× (z -8.9) |
| [[SW1417 (line)]] | alt | 92.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.439× (z -8.8) |
| [[A-172 (line)]] | wt | 60.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 89.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 92.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 50.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 56.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 72.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 52.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 85.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 73.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 85.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 69.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 90.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 92.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 66.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 73.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 71.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9817), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF845]] | +0.62 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[ZNF510]] | +0.61 | +0.57 / +0.38 | both halves | 7e-05 |  |
| [[RBM15B]] | +0.61 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[NELFE]] | +0.60 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[SF3A2]] | +0.60 | +0.60 / +0.46 | both halves | 3e-05 | pathway: Dengue Virus-Host Interactions; STRING 666 |
| [[PABIR1]] | +0.59 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[HNRNPH2]] | +0.59 | +0.51 / +0.72 | both halves | 1e-05 | same gene group; pathway: Dengue Virus-Host Interactions; STRING 603 |
| [[ZNF211]] | +0.59 | +0.61 / +0.38 | both halves | 7e-05 |  |
| [[POP4]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[DNAJC14]] | +0.58 | +0.65 / +0.49 | both halves | 1e-05 |  |
| [[ZBTB6]] | +0.58 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[FEM1B]] | +0.58 | +0.65 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFATC2IP]] | -0.51 | -0.59 / -0.26 | both halves | 4e-04 |  |
| [[ATP1B3]] | -0.49 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[CSAD]] | -0.47 | -0.45 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF548]] | B | ZNF548 activity lowers PCBP1's level | lines that do not express ZNF548 (6) vs lines expressing it (44) | 1.16× higher at baseline in the lines without ZNF548 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF547, TRAPPC2B, ZNF264 |
| [[TOP2A]] | B | TOP2A activity raises PCBP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.572). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-34.1, 11.5); signed map (-0.4, -28.8). **Vector** length 93.9, 23.8% of its response variance represented; |z| ≥ 3 in 837 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.7 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +5.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.3 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | +4.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.4 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.1 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | -0.4 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -4.0 | -3.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.0 | -3.2 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.3 | +0.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | +0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -3.7 |
|  | [[Bergenin (drug)]] 0.5 µM |  | -1.8 | -5.0 |

## What is on record

|  |  |
|---|---|
| Name | poly(rC) binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.3 — chr2:70,087,477-70,089,203 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HNRPE1, hnRNP-E1, HNRPX, hnRNP-X |
| Gene groups (HGNC) | Heterogeneous nuclear ribonucleoproteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 9 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; mRNA Splicing - Major Pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15365](https://www.uniprot.org/uniprotkb/Q15365) (Poly(rC)-binding protein 1):

> Single-stranded nucleic acid binding protein that binds preferentially to oligo dC. Together with PCBP2, required for erythropoiesis, possibly by regulating mRNA splicing (By similarity).; (Microbial infection) In case of infection by poliovirus, plays a role in initiation of viral RNA replication in concert with the viral protein 3CD.

**Summary**, from NCBI Gene [5093](https://www.ncbi.nlm.nih.gov/gene/5093):

> This intronless gene is thought to have been generated by retrotransposition of a fully processed PCBP-2 mRNA. This gene and PCBP-2 have paralogues (PCBP3 and PCBP4) which are thought to have arisen as a result of duplication events of entire genes. The protein encoded by this gene appears to be multifunctional. It along with PCBP-2 and hnRNPK corresponds to the major cellular poly(rC)-binding protein. It contains three K-homologous (KH) domains which may be involved in RNA binding. This …

**Accessions** — [HGNC:8647](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8647) · Entrez [5093](https://www.ncbi.nlm.nih.gov/gene/5093) · UniProt [Q15365](https://www.uniprot.org/uniprotkb/Q15365) · Ensembl [ENSG00000169564](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169564)

## Data

Gene col 9817: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9817); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9817, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9817]; `tensor/DDL_lfc|DDL_z.npy` [9817]; `embed/gene_vectors.npy` [9817]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9817 or target_col == 9817). Every well: [[PCBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
