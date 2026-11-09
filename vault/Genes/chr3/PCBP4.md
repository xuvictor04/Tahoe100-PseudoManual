---
symbol: "PCBP4"
type: "gene"
col: 1612
ensembl_id: "ENSG00000090097"
name: "poly(rC) binding protein 4"
location: "3p21.2"
module: 2
arm: "+"
pooled_cpm: 10.05
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 11
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# PCBP4

*poly(rC) binding protein 4* — 3p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.43× (z +12.3, q 7e-32, up in 18 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 1.49× (z +4.1, q 0.004, up in 10 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.651× (z -8.7, q 2e-15, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM219B]] (+0.64, fdr 7e-06), [[ZDHHC8]] (+0.61, fdr 7e-06), [[LLGL1]] (+0.61, fdr 1e-05); moves opposite to [[HES1]] (-0.50, fdr 4e-05), [[FOS]] (-0.49, fdr 2e-05), [[CWC22]] (-0.47, fdr 4e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NCS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.43×** | +12.3 | 7e-32 | 18/18 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.15×** | +11.0 | 1e-25 | 32/35 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +8.5 | 3e-15 | 20/26 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.2 | 0.004 | 14/39 (NCI-H1573, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +4.1 | 0.004 | 10/42 (SW480, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.004 | 14/46 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.005 | 8/44 (MIA PaCa-2, SW48, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.7 | 0.019 | 15/38 (HS-578T, SNU-423, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.5 | 0.034 | 5/25 (LoVo, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.086 | 3/47 (LS 180, NCI-H2030, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.35× | +3.0 | 0.12 | 6/41 (MIA PaCa-2, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.651×** | -8.7 | 2e-15 | 29/45 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.591×** | -7.6 | 1e-11 | 25/45 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.685×** | -5.2 | 3e-05 | 19/45 (LOX-IMVI, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.717×** | -4.8 | 3e-04 | 19/47 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.548×** | -4.5 | 6e-04 | 15/45 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.549×** | -4.5 | 6e-04 | 17/47 (J82, HT-29, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.749×** | -4.1 | 0.003 | 17/47 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.768×** | -3.8 | 0.011 | 15/46 (HT-29, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.776×** | -3.4 | 0.038 | 10/46 (SW480, A-172, …) | inconsistent across doses |  |
| [[Pyridoxine (drug)]] 5 µM |  | 0.846× | -3.4 | 0.038 | 13/48 (J82, AN3 CA, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.780×** | -3.4 | 0.038 | 14/47 (PANC-1, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.800×** | -3.2 | 0.063 | 13/46 (COLO 205, NCI-H460, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 0.670× | -3.0 | 0.12 | 7/46 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.8) |
| [[NCI-H2030 (line)]] | alt | 16.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -11.6) |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.123× (z -12.0) |
| [[RKO (line)]] | wt | 14.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -10.5) |
| [[NCI-H460 (line)]] | wt | 6.76 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.185× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 18.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -14.1) |
| [[SW480 (line)]] | alt | 11.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.142× (z -8.5) |
| [[A-172 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.48 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.19 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.71 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.48 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.16 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM219B]] | +0.64 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[ZDHHC8]] | +0.61 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[LLGL1]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[CAPN1]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[KIF1C]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PIP4K2C]] | +0.58 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[KIFC2]] | +0.57 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[DUSP22]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[IRGQ]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.55 | +0.51 / +0.59 | both halves | 1e-05 |  |
| [[UBE2F]] | +0.55 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[AMFR]] | +0.55 | +0.60 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HES1]] | -0.50 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[FOS]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CWC22]] | -0.47 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[GOLGB1]] | -0.45 | -0.49 / -0.38 | both halves | 7e-05 |  |
| [[KIAA0586]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCS1]] | B | NCS1 activity raises PCBP4's level | lines that do not express NCS1 (6) vs lines expressing it (44) | 1.64× lower at baseline in the lines without NCS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: SH3BP5, ZNF618, PBK; maybe low, not absent |
| [[LRP3]] | B | LRP3 activity raises PCBP4's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.47× lower at baseline in the lines without LRP3 | 0.070 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.584). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-7.5, -22.2); signed map (-46.9, -10.1). **Vector** length 54.5, 7.52% of its response variance represented; |z| ≥ 3 in 739 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.9 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.4 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +4.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -7.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -1.9 | -8.7 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -2.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.6 | -5.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -2.2 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | -1.0 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -3.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | poly(rC) binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.2 — chr3:51,957,454-51,974,016 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MCG10, LIP4 |
| Reactome | 12 pathways, smallest: Transcriptional  activation of  cell cycle inhibitor p21; Transcriptional activation of p53 responsive genes; TP53 Regulates Transcription of Genes Involved in G1 Cell Cycle Arrest |
| Matched by | ensembl_id |

**Function**, from UniProt [P57723](https://www.uniprot.org/uniprotkb/P57723) (Poly(rC)-binding protein 4):

> Single-stranded nucleic acid binding protein that binds preferentially to oligo dC.

**Summary**, from NCBI Gene [57060](https://www.ncbi.nlm.nih.gov/gene/57060):

> This gene encodes a member of the KH-domain protein subfamily. Proteins of this subfamily, also referred to as alpha-CPs, bind to RNA with a specificity for C-rich pyrimidine regions. Alpha-CPs play important roles in post-transcriptional activities and have different cellular distributions. This gene is induced by the p53 tumor suppressor, and the encoded protein can suppress cell proliferation by inducing apoptosis and cell cycle arrest in G(2)-M. This gene's protein is found in the …

**Accessions** — [HGNC:8652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8652) · Entrez [57060](https://www.ncbi.nlm.nih.gov/gene/57060) · UniProt [P57723](https://www.uniprot.org/uniprotkb/P57723) · Ensembl [ENSG00000090097](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090097)

## Data

Gene col 1612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1612); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1612]; `tensor/DDL_lfc|DDL_z.npy` [1612]; `embed/gene_vectors.npy` [1612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1612 or target_col == 1612). Every well: [[PCBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
