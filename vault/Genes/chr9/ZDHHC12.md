---
symbol: "ZDHHC12"
type: "gene"
col: 8351
ensembl_id: "ENSG00000160446"
name: "zDHHC palmitoyltransferase 12"
location: "9q34.11"
module: 48
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 49
n_dd_up: 3
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/048"]
generated_by: "tahoemap"
---

# ZDHHC12

*zDHHC palmitoyltransferase 12* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.03× (z +7.2, q 3e-10, up in 6 of 10 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change. None of them is without an alert.
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.190× (z -11.2, q 2e-26, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNRNP25]] (+0.73, fdr 1e-05), [[CENPW]] (+0.70, fdr 7e-06), [[TMEM276]] (+0.68, fdr 9e-06); moves opposite to [[LTO1]] (-0.64, fdr 1e-05), [[CROCC]] (-0.62, fdr 6e-05), [[ZNF621]] (-0.59, fdr 3e-04).
> It sits in the **+** arm of [[Module 048]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PRDX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8351.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **3.03×** | +7.2 | 3e-10 | 6/10 (HT-29, A498, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.35×** | +5.8 | 2e-06 | 14/24 (A498, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~34% of this change | **2.16×** | +5.2 | 3e-05 | 18/27 (HOP62, J82, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.62× | +3.3 | 0.14 | 17/45 (A498, RKO, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | 1.59× | +3.2 | 0.18 | 14/46 (COLO 205, MIA PaCa-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8351.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.190×** | -11.2 | 2e-26 | 32/37 (A-172, A498, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.352×** | -10.0 | 6e-21 | 32/38 (J82, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.503×** | -4.6 | 7e-04 | 25/44 (NCI-H460, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.501×** | -4.5 | 0.001 | 26/44 (COLO 205, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.496×** | -3.9 | 0.011 | 23/41 (A498, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.337×** | -3.8 | 0.011 | 18/38 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.567×** | -3.8 | 0.011 | 19/46 (AN3 CA, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -3.7 | 0.015 | 21/43 (Panc 03.27, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.619×** | -3.2 | 0.076 | 19/44 (BT-474, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.621×** | -3.2 | 0.076 | 15/40 (A-427, C32, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.625×** | -3.2 | 0.080 | 12/44 (HCT15, HepG2/C3A, …) | top dose only | position effect removed |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.609×** | -3.1 | 0.097 | 11/44 (RKO, LS 180, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8351. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 4.18 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0507× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0952× (z -9.2) |
| [[HOP62 (line)]] | alt | 5.11 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0546× (z -10.6) |
| [[HT-29 (line)]] | alt | 8.98 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.3) |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 5.26 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 6.10 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -11.9) |
| [[A-172 (line)]] | wt | 11.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0360× (z -13.8) |
| [[A498 (line)]] | wt | 10.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0779× (z -12.5) |
| [[BT-474 (line)]] | alt | 9.59 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.0) |
| [[CFPAC-1 (line)]] | alt | 3.78 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0992× (z -11.1) |
| [[COLO 205 (line)]] | alt | 9.06 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0570× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 7.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -9.4) |
| [[J82 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0919× (z -14.6) |
| [[LoVo (line)]] | wt | 3.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0637× (z -9.9) |
| [[Panc 03.27 (line)]] | alt | 10.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.2) |
| [[A-427 (line)]] | wt | 6.27 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.69 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.35 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.65 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8351), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 6 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNRNP25]] | +0.73 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CENPW]] | +0.70 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[TMEM276]] | +0.68 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[NUDT1]] | +0.68 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ANAPC11]] | +0.67 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[AP2S1]] | +0.66 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[TRAPPC1]] | +0.66 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[BLOC1S1]] | +0.66 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[PAFAH1B3]] | +0.65 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[SLC25A1]] | +0.62 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[MICOS13]] | +0.62 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[NRM]] | +0.62 | +0.64 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTO1]] | -0.64 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CROCC]] | -0.62 | -0.39 / -0.60 | both halves | 6e-05 |  |
| [[ZNF621]] | -0.59 | -0.57 / -0.28 | both halves | 3e-04 |  |
| [[WDR74]] | -0.57 | -0.50 / -0.36 | both halves | 9e-05 |  |
| [[RYR2]] | -0.56 | -0.40 / -0.50 | both halves | 4e-05 |  |
| [[KRR1]] | -0.56 | -0.48 / -0.26 | both halves | 4e-04 |  |
| [[SMIM15-AS1]] | -0.55 | -0.40 / -0.31 | both halves | 2e-04 |  |
| [[CDKL1]] | -0.54 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[MSTO1]] | -0.53 | -0.38 / -0.38 | both halves | 7e-05 |  |
| [[DPH5-DT]] | -0.53 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[PCBP1-AS1]] | -0.53 | -0.36 / -0.22 | both halves | 6e-04 |  |
| [[ADSS2]] | -0.52 | -0.39 / -0.42 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRDX2]] | B | PRDX2 activity lowers ZDHHC12's level | lines that do not express PRDX2 (9) vs lines expressing it (41) | 1.26× higher at baseline in the lines without PRDX2 | 0.043 | ⚠ within organs, on part of the lines; also absent: RAB20 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 048]] — Aerobic respiration and respiratory electron transport; 93 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (-47.8, -17.5); signed map (-37.3, 13.8). **Vector** length 61.8, 12.4% of its response variance represented; |z| ≥ 3 in 670 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +4.0 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | +3.8 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.5 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +1.8 | -0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.7 | +1.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.6 | +2.9 |
|  | [[Thymol (drug)]] 5 µM |  | +1.1 | +2.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.1 | +1.6 |
|  | [[Arbutin (drug)]] 5 µM |  | +1.1 | +2.6 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.0 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.4 | -11.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -10.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.0 | -3.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.5 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | zDHHC palmitoyltransferase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,720,870-128,724,127 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF400, FLJ14524 |
| Gene groups (HGNC) | Zinc fingers DHHC-type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96GR4](https://www.uniprot.org/uniprotkb/Q96GR4) (Palmitoyltransferase ZDHHC12):

> Palmitoyltransferase that catalyzes the addition of palmitate onto various protein substrates. Has a palmitoyltransferase activity toward gephyrin/GPHN, regulating its clustering at synapses and its function in gamma-aminobutyric acid receptor clustering (By similarity). Thereby, indirectly regulates GABAergic synaptic transmission (By similarity). Negatively regulates NLRP3-driven inflammation. Catalyzes NLRP3 palmitoylation, leading to its degradation via the chaperone-mediated autophagy …

**Summary**, from NCBI Gene [84885](https://www.ncbi.nlm.nih.gov/gene/84885):

> Enables protein-cysteine S-palmitoyltransferase activity. Involved in gephyrin clustering involved in postsynaptic density assembly and negative regulation of NLRP3 inflammasome complex assembly. Located in Golgi apparatus and endoplasmic reticulum. Is active in dendritic spine. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19159](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19159) · Entrez [84885](https://www.ncbi.nlm.nih.gov/gene/84885) · UniProt [Q96GR4](https://www.uniprot.org/uniprotkb/Q96GR4) · Ensembl [ENSG00000160446](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160446)

## Data

Gene col 8351: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8351); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8351, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8351]; `tensor/DDL_lfc|DDL_z.npy` [8351]; `embed/gene_vectors.npy` [8351]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8351 or target_col == 8351). Every well: [[ZDHHC12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZDHHC12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
