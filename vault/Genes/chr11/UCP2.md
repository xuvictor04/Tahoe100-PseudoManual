---
symbol: "UCP2"
type: "gene"
col: 10622
ensembl_id: "ENSG00000175567"
name: "uncoupling protein 2"
location: "11q13.4"
module: 29
arm: "+"
pooled_cpm: 4.24
n_lines_expressing: 32
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 6
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# UCP2

*uncoupling protein 2* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.61× (z +15.2, q 0e+00, up in 10 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 2.73× (z +10.0, q 3e-21, up in 23 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.542× (z -6.1, q 5e-07, down in 14 of 20 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.558× (z -5.8, q 2e-06, down in 13 of 25 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (BT-474 0.248×, RKO 0.0680×); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 0.253×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.278×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSPAN6]] (+0.59, fdr 2e-05), [[RBBP9]] (+0.57, fdr 1e-05), [[JMJD8]] (+0.56, fdr 1e-05); moves opposite to [[GUCA1B]] (-0.55, fdr 4e-05), [[KCNJ14]] (-0.52, fdr 8e-05), [[EIF3J]] (-0.48, fdr 2e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 6 go from it, the strongest it → [[ROGDI]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10622.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.61×** | +15.2 | 0e+00 | 10/10 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.19×** | +13.7 | 2e-40 | 7/7 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.70×** | +12.0 | 5e-31 | 6/8 (J82, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.73×** | +10.0 | 3e-21 | 23/27 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.70×** | +9.9 | 6e-21 | 24/30 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.79×** | +8.2 | 3e-14 | 17/28 (A498, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.95×** | +6.6 | 3e-09 | 15/27 (J82, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.8 | 5e-07 | 12/20 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +4.8 | 1e-04 | 8/16 (SHP-77, J82, …) | top dose only | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.6 | 2e-04 | 6/28 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.4 | 4e-04 | 4/13 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 4e-04 | 9/19 (SHP-77, BT-474, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.07×** | +3.8 | 0.007 | 1/9 (PANC-1) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.5 | 0.017 | 4/17 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~17% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.72×** | +3.4 | 0.024 | 1/12 (PANC-1) | two highest doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10622.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (BT-474 0.248×, RKO 0.0680×); [[Digitoxin (drug)]] 0.5 µM in 1 line (BT-474 0.253×); [[Digitoxin (drug)]] 5 µM in 1 line (BT-474 0.278×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.542×** | -6.1 | 5e-07 | 14/20 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.558×** | -5.8 | 2e-06 | 13/25 (BT-474, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -4.5 | 0.001 | 13/26 (BT-474, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.698× | -3.2 | 0.18 | 6/18 (SHP-77, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[EX229 (drug)]] 5 µM |  | 0.559× | -3.0 | 0.27 | 10/19 (BT-474, SW480, …) | rises with dose | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 40.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.248× (z -9.5) |
| [[J82 (line)]] | alt | 15.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.10× (z +11.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 8.81 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.55× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 4.94 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0680× (z -9.0) |
| [[A-172 (line)]] | wt | 1.99 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.36 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.371 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.671 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.354 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.838 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.50 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.501 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.507 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.735 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.984 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.96 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSPAN6]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[RBBP9]] | +0.57 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[JMJD8]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[GSTM4]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ZMYM3]] | +0.54 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[FAM210B]] | +0.53 | +0.41 / +0.50 | both halves | 4e-05 |  |
| [[CYB5A]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SLC25A30]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 | same gene group |
| [[TMEM106C]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CENPS]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[ECHS1]] | +0.51 | +0.41 / +0.36 | both halves | 9e-05 | pathway: HALLMARK_ADIPOGENESIS |
| [[OAZ2]] | +0.51 | +0.51 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUCA1B]] | -0.55 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.52 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[EIF3J]] | -0.48 | -0.31 / -0.48 | both halves | 2e-04 |  |
| [[GON4L]] | -0.48 | -0.57 / -0.37 | both halves | 7e-05 |  |
| [[FBXO10]] | -0.48 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[BMS1P4-1]] | -0.48 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[DCAF10]] | -0.48 | -0.44 / -0.37 | both halves | 8e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[MRPL33]] | -0.48 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[AGAP5]] | -0.48 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ZNF586]] | -0.47 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[KIF9-AS1]] | -0.47 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[UBE2CP5]] | -0.47 | -0.37 / -0.39 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROGDI]] | B | UCP2 activity raises ROGDI's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.29× lower at baseline in the lines without UCP2 | 0.013 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[PCYT2]] | B | UCP2 activity raises PCYT2's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without UCP2 | 0.029 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[ANAPC15]] | B | UCP2 activity raises ANAPC15's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without UCP2 | 0.074 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[SNRNP25]] | B | UCP2 activity raises SNRNP25's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.32× lower at baseline in the lines without UCP2 | 0.079 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[ATP6V0E2]] | B | UCP2 activity raises ATP6V0E2's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.63× lower at baseline in the lines without UCP2 | 0.083 | ⚠ within organs, on part of the lines; also absent: WNK2 |
| [[THYN1]] | B | UCP2 activity raises THYN1's level | lines that do not express UCP2 (18) vs lines expressing it (32) | 1.39× lower at baseline in the lines without UCP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: WNK2 |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.384). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.7, -42.4); signed map (-32.1, -38.8). **Vector** length 40.2, 6.49% of its response variance represented; |z| ≥ 3 in 646 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +15.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.9 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.1 | +2.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +0.8 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.7 | -5.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -2.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.0 | -3.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -0.9 | -0.1 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -0.9 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.9 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | uncoupling protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:73,974,672-73,982,843 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SLC25A8; previously BMIQ4 |
| Gene groups (HGNC) | Solute carrier family 25 |
| Hallmark sets | HEME_METABOLISM, ADIPOGENESIS |
| Reactome | 3 pathways, smallest: The fatty acid cycling model; Mitochondrial Uncoupling; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [P55851](https://www.uniprot.org/uniprotkb/P55851) (Dicarboxylate carrier SLC25A8):

> Antiporter that exports dicarboxylate intermediates of the Krebs cycle in exchange for phosphate plus a proton across the inner membrane of mitochondria, a process driven by mitochondrial motive force with an overall impact on glycolysis, glutaminolysis and glutathione-dependent redox balance. Continuous export of oxaloacetate and related four-carbon dicarboxylates from mitochondrial matrix into the cytosol negatively regulates the oxidation of acetyl-CoA substrates via the Krebs cycle, …

**Summary**, from NCBI Gene [7351](https://www.ncbi.nlm.nih.gov/gene/7351):

> Mitochondrial uncoupling proteins (UCP) are members of the larger family of mitochondrial anion carrier proteins (MACP). UCPs separate oxidative phosphorylation from ATP synthesis with energy dissipated as heat, also referred to as the mitochondrial proton leak. UCPs facilitate the transfer of anions from the inner to the outer mitochondrial membrane and the return transfer of protons from the outer to the inner mitochondrial membrane. They also reduce the mitochondrial membrane potential in …

**Accessions** — [HGNC:12518](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12518) · Entrez [7351](https://www.ncbi.nlm.nih.gov/gene/7351) · UniProt [P55851](https://www.uniprot.org/uniprotkb/P55851) · Ensembl [ENSG00000175567](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175567)

## Data

Gene col 10622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10622); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10622]; `tensor/DDL_lfc|DDL_z.npy` [10622]; `embed/gene_vectors.npy` [10622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10622 or target_col == 10622). Every well: [[UCP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UCP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
