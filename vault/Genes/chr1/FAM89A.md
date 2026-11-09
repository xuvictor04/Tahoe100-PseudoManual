---
symbol: "FAM89A"
type: "gene"
col: 11242
ensembl_id: "ENSG00000182118"
name: "family with sequence similarity 89 member A"
location: "1q42.2"
module: 18
arm: "+"
pooled_cpm: 8.33
n_lines_expressing: 45
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# FAM89A

*family with sequence similarity 89 member A* — 1q42.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.87× (z +15.9, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.657× (z -6.3, q 2e-07, down in 24 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAGP]] (+0.64, fdr 1e-05), [[ARMC10]] (+0.64, fdr 1e-05), [[GSTO1]] (+0.63, fdr 1e-05); moves opposite to [[PBRM1]] (-0.59, fdr 8e-05), [[COQ7]] (-0.58, fdr 1e-05), [[IFT81]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[BACE2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11242.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +15.9 | 0e+00 | 37/38 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **2.01×** | +7.5 | 2e-11 | 31/42 (PANC-1, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.74×** | +5.9 | 7e-07 | 25/42 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +5.6 | 3e-06 | 25/42 (NCI-H2347, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.67×** | +5.5 | 4e-06 | 24/42 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +5.2 | 2e-05 | 21/41 (SW480, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.65×** | +5.1 | 2e-05 | 22/40 (NCI-H460, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **1.62×** | +5.1 | 2e-05 | 22/42 (PANC-1, LoVo, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.54×** | +4.4 | 6e-04 | 18/37 (AsPC-1, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.7 | 0.011 | 16/41 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.41×** | +3.7 | 0.011 | 18/41 (SW1417, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.43×** | +3.7 | 0.011 | 13/39 (NCI-H460, Panc 03.27, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.3 | 0.036 | 4/39 (A-172, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11242.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.657×** | -6.3 | 2e-07 | 24/38 (SK-MEL-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~22% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.365×** | -5.6 | 6e-06 | 23/41 (NCI-H460, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.650×** | -4.6 | 7e-04 | 23/42 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.651×** | -4.6 | 7e-04 | 19/41 (CHP-212, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.477×** | -4.1 | 0.004 | 19/40 (C32, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.708×** | -3.7 | 0.023 | 14/42 (AsPC-1, C32, …) | all doses, flat | position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | 0.740× | -3.2 | 0.11 | 11/41 (HCT15, NCI-H1792, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.816× | -3.0 | 0.16 | 14/41 (SNU-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11242. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 24.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0332× (z -20.5) ⚠ cell-cycle shift, explains ~82% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.362× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 12.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +8.6) | — |
| [[LoVo (line)]] | wt | 8.83 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 6.50 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 8.24 | 0 | 1 | — | [[Ivermectin (drug)]] 0.5 µM 0.128× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 20.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -11.3) |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0615× (z -10.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.108× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 16.1 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.107× (z -9.2) |
| [[SW480 (line)]] | alt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.8) | — |
| [[A-172 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.96 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.625 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.41 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11242), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAGP]] | +0.64 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[ARMC10]] | +0.64 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[GSTO1]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TNFRSF10A]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[ESRRA]] | +0.63 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[KLHL29]] | +0.62 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ANKRD13B]] | +0.60 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[NBPF9]] | +0.59 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[PALS2]] | +0.59 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[RGS10]] | +0.58 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[NBPF15]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBRM1]] | -0.59 | -0.37 / -0.64 | both halves | 8e-05 |  |
| [[COQ7]] | -0.58 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[IFT81]] | -0.58 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[RAB1B]] | -0.56 | -0.36 / -0.65 | both halves | 9e-05 |  |
| [[ARAF]] | -0.54 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[THRAP3]] | -0.53 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[BCLAF1]] | -0.53 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[HP1BP3]] | -0.52 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[SF3B1]] | -0.52 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[NDUFA5]] | -0.51 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[MORF4L1]] | -0.51 | -0.36 / -0.54 | both halves | 1e-04 |  |
| [[BACE1-AS]] | -0.51 | -0.37 / -0.52 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers FAM89A's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BACE2]] | B | FAM89A activity raises BACE2's level | lines that do not express FAM89A (5) vs lines expressing it (45) | 4.73× lower at baseline in the lines without FAM89A | 0.089 | ⚠ within organs, on part of the lines; also absent: DPP7, IL17RD, B3GNT5; maybe low, not absent |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.433). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-15.2, 3.6); signed map (-18.4, 45.3). **Vector** length 77.9, 16.7% of its response variance represented; |z| ≥ 3 in 690 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +15.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +5.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.3 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.2 | +5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +3.3 |
| fall | [[Trametinib (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.3 | -6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -2.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.6 | -2.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 89 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q42.2 — chr1:231,018,958-231,040,254 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15887; previously C1orf153 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q96GI7](https://www.uniprot.org/uniprotkb/Q96GI7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25057) · Entrez [375061](https://www.ncbi.nlm.nih.gov/gene/375061) · UniProt [Q96GI7](https://www.uniprot.org/uniprotkb/Q96GI7) · Ensembl [ENSG00000182118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182118)

## Data

Gene col 11242: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11242); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11242, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11242]; `tensor/DDL_lfc|DDL_z.npy` [11242]; `embed/gene_vectors.npy` [11242]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11242 or target_col == 11242). Every well: [[FAM89A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM89A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
