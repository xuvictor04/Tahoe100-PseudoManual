---
symbol: "ZFY"
type: "gene"
col: 866
ensembl_id: "ENSG00000067646"
name: "zinc finger protein Y-linked"
location: "Yp11.2"
module: 68
arm: "+"
pooled_cpm: 13.32
n_lines_expressing: 21
n_dd_up: 20
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 8
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# ZFY

*zinc finger protein Y-linked* — Yp11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.53× (z +12.7, q 5e-34, up in 0 of 17 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +12.3, q 2e-32, up in 19 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.277× (z -17.5, q 0e+00, down in 18 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFX]] (+0.76, fdr 7e-06), [[PCNX4-DT]] (+0.76, fdr 2e-05), [[INO80D]] (+0.74, fdr 7e-06); moves opposite to [[GMCL1]] (-0.68, fdr 1e-05), [[QSOX1]] (-0.64, fdr 1e-05), [[COG5]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 8 go from it, the strongest it → [[ZBED1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 866.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.53×** | +12.7 | 5e-34 | 0/17 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +12.3 | 2e-32 | 19/19 (NCI-H2030, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +11.9 | 3e-30 | 7/16 (NCI-H460, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.44×** | +11.7 | 2e-29 | 0/13 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +11.3 | 2e-27 | 17/18 (NCI-H2030, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.30×** | +10.9 | 1e-25 | 19/19 (A-172, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.72×** | +7.4 | 2e-11 | 18/19 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.64×** | +6.7 | 1e-09 | 0/19 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +6.4 | 7e-09 | 7/18 (C32, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +5.8 | 4e-07 | 15/19 (NCI-H2030, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.2 | 1e-05 | 3/13 (NCI-H2030, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 10/19 (A-427, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.7 | 1e-04 | 8/19 (LoVo, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.5 | 3e-04 | 7/17 (H4, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 3e-04 | 9/19 (LoVo, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.002 | 10/18 (NCI-H460, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 6/19 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.48×** | +3.8 | 0.004 | 0/19 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.68×** | +3.7 | 0.007 | 11/19 (C32, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.014 | 12/19 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 866.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.277×** | -17.5 | 0e+00 | 18/19 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.334×** | -15.0 | 0e+00 | 19/19 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.382×** | -13.1 | 4e-37 | 19/19 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.409×** | -12.2 | 4e-32 | 19/19 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.570×** | -7.7 | 2e-12 | 18/19 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.419×** | -6.2 | 5e-08 | 13/19 (SK-MEL-2, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.717×** | -4.5 | 5e-04 | 13/19 (CHP-212, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.842× | -3.3 | 0.062 | 18/19 (NCI-H2030, LoVo, …) | all doses, flat |  |
| [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM |  | **0.778×** | -3.2 | 0.075 | 2/19 (SK-MEL-2, HepG2/C3A) | inconsistent across doses |  |
| [[Tucatinib (drug)]] 0.5 µM |  | 0.732× | -3.0 | 0.13 | 0/19 | inconsistent across doses | noisy plate (z scaled) |
| [[Monocrotaline (drug)]] 5 µM |  | 0.795× | -3.0 | 0.13 | 0/18 | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 866. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 38.4 | 6 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.03× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.38× (z +11.7) | [[Panobinostat (drug)]] 5 µM 0.133× (z -19.1) |
| [[NCI-H2030 (line)]] | alt | 134 | 3 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +19.3) | [[Dinaciclib (drug)]] 5 µM 0.131× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.168× (z -17.1) |
| [[A-172 (line)]] | wt | 31.2 | 3 | 5 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.78× (z +11.6) | [[Panobinostat (drug)]] 5 µM 0.106× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0779× (z -20.4) |
| [[LoVo (line)]] | wt | 22.7 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +9.6) | [[Panobinostat (drug)]] 5 µM 0.0716× (z -17.3) |
| [[SNU-423 (line)]] | alt | 19.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0737× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.144× (z -11.7) |
| [[C32 (line)]] | wt | 22.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.140× (z -11.2) |
| [[H4 (line)]] | wt | 26.3 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 30.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0653× (z -15.8) |
| [[J82 (line)]] | alt | 35.4 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.117× (z -16.0) |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.134× (z -12.4) |
| [[A549 (line)]] | wt | 16.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.179× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0996× (z -11.7) |
| [[SNU-1 (line)]] | wt | 58.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0942× (z -14.1) |
| [[A-427 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0931× (z -11.9) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Esmolol (hydrochloride) (drug)]] 0.5 µM 0.168× (z -9.3) |
| [[HCT15 (line)]] | alt | 23.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0698× (z -12.5) |
| [[A498 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.781 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.939 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.972 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.865 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.731 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.825 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.768 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.25 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.874 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 866), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFX]] | +0.76 | +0.64 / +0.65 | both halves | 7e-06 | same gene group; STRING 726 |
| [[PCNX4-DT]] | +0.76 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[INO80D]] | +0.74 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LATS1]] | +0.73 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[ZNF407-AS1]] | +0.72 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[ZNF644]] | +0.72 | +0.61 / +0.64 | both halves | 7e-06 | same gene group |
| [[FAM200A]] | +0.72 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[VPS35L]] | +0.71 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[YJU2]] | +0.71 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[ZNF764]] | +0.70 | +0.59 / +0.64 | both halves | 7e-06 | same gene group |
| [[WARS2-AS1]] | +0.70 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[PPP3CB-AS1]] | +0.70 | +0.55 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GMCL1]] | -0.68 | -0.56 / -0.55 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.64 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[COG5]] | -0.63 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[TPD52]] | -0.63 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[WASF3]] | -0.63 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[LPCAT4]] | -0.63 | -0.58 / -0.39 | both halves | 5e-05 |  |
| [[POGLUT2]] | -0.62 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[PLA2G12A]] | -0.62 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[IGSF8]] | -0.62 | -0.42 / -0.39 | both halves | 6e-05 |  |
| [[TM9SF2]] | -0.62 | -0.58 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 2, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ZFY's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ZFY's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[UTY]] | C | UTY activity raises ZFY's level | lines that do not express UTY (31) vs lines expressing it (19) | 7.93× lower at baseline in the lines without UTY | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[BMPR1B]] | C | BMPR1B activity raises ZFY's level | lines that do not express BMPR1B (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without BMPR1B | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000286385, SLC6A17, EPHA5-AS1; co-absent with the target |
| [[PLAGL1]] | C | PLAGL1 activity raises ZFY's level | lines that do not express PLAGL1 (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without PLAGL1 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: C5orf46, GJA1, SOX5; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises ZFY's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 6.98× lower at baseline in the lines without NLGN4Y | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZBED1]] | B | ZFY activity raises ZBED1's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.62× lower at baseline in the lines without ZFY | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[FGF2]] | B | ZFY activity raises FGF2's level | lines that do not express ZFY (29) vs lines expressing it (21) | 2.48× lower at baseline in the lines without ZFY | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[TENM3-AS1]] | B | ZFY activity raises TENM3-AS1's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without ZFY | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[SOCS2]] | B | ZFY activity raises SOCS2's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without ZFY | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[UTY]] | C | ZFY activity raises UTY's level | lines that do not express ZFY (29) vs lines expressing it (21) | 14.74× lower at baseline in the lines without ZFY | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |
| [[BMPR1B]] | C | ZFY activity raises BMPR1B's level | lines that do not express ZFY (29) vs lines expressing it (21) | 2.78× lower at baseline in the lines without ZFY | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |
| [[NLGN4Y]] | C | ZFY activity raises NLGN4Y's level | lines that do not express ZFY (29) vs lines expressing it (21) | 6.51× lower at baseline in the lines without ZFY | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |
| [[UGT2B7]] | C | ZFY activity raises UGT2B7's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.33× lower at baseline in the lines without ZFY | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278; co-absent with the target |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (2.3, 8.8); signed map (19.0, -23.4). **Vector** length 60.1, 15.2% of its response variance represented; |z| ≥ 3 in 528 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.5 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.5 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +3.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.9 | +10.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.4 | +2.3 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -3.4 | -7.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.3 | -12.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -17.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -6.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -13.1 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.4 | -0.5 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.3 | -0.2 |
|  | [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.9 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein Y-linked |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Yp11.2 — chrY:2,935,281-2,982,506 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ZNF911 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZFX transcription factor family |
| Matched by | ensembl_id |

**Function**, from UniProt [P08048](https://www.uniprot.org/uniprotkb/P08048) (Zinc finger Y-chromosomal protein):

> Probable transcriptional activator. Binds to the consensus sequence 5'-AGGCCY-3'.

**Summary**, from NCBI Gene [7544](https://www.ncbi.nlm.nih.gov/gene/7544):

> This gene encodes a zinc finger-containing protein that may function as a transcription factor. This gene was once a candidate gene for the testis-determining factor (TDF) and was erroneously referred to as TDF. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12870](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12870) · Entrez [7544](https://www.ncbi.nlm.nih.gov/gene/7544) · UniProt [P08048](https://www.uniprot.org/uniprotkb/P08048) · Ensembl [ENSG00000067646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000067646)

## Data

Gene col 866: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 866); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 866, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 866]; `tensor/DDL_lfc|DDL_z.npy` [866]; `embed/gene_vectors.npy` [866]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 866 or target_col == 866). Every well: [[ZFY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
