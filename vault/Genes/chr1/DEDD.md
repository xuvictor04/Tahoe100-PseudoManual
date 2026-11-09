---
symbol: "DEDD"
type: "gene"
col: 8192
ensembl_id: "ENSG00000158796"
name: "death effector domain containing"
location: "1q23.3"
module: 16
arm: "+"
pooled_cpm: 20.52
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 10
n_dd_up_clean: 14
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# DEDD

*death effector domain containing* — 1q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +14.3, q 8e-44, up in 41 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.655× (z -10.8, q 3e-24, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF776]] (+0.72, fdr 7e-06), [[MYL5]] (+0.71, fdr 7e-06), [[ZFHX2]] (+0.69, fdr 7e-06); moves opposite to [[GOLT1B]] (-0.60, fdr 1e-05), [[PIGN]] (-0.59, fdr 3e-05), [[NME2]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +14.3 | 8e-44 | 41/47 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +12.6 | 4e-34 | 42/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +10.5 | 1e-23 | 33/48 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.61×** | +8.5 | 3e-15 | 28/46 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.33×** | +7.9 | 3e-13 | 35/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.30×** | +7.8 | 7e-13 | 29/44 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +5.9 | 3e-07 | 0/48 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +5.3 | 6e-06 | 21/47 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +5.1 | 2e-05 | 23/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +5.0 | 3e-05 | 18/46 (BT-474, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.004 | 13/47 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.007 | 7/46 (PANC-1, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.019 | 13/46 (J82, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.23×** | +3.5 | 0.019 | 11/48 (HOP62, A-172, …) | rises with dose | plate-row cell shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.5 | 0.019 | 9/46 (H4, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.20×** | +3.3 | 0.034 | 11/48 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.060 | 11/45 (PANC-1, HEC-1-A, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.655×** | -10.8 | 3e-24 | 33/48 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~19% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.551×** | -10.7 | 3e-24 | 43/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.605×** | -9.0 | 3e-17 | 36/47 (SNU-423, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.609×** | -8.9 | 7e-17 | 38/48 (A-172, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.718×** | -5.7 | 1e-06 | 24/46 (NCI-H23, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.733×** | -5.6 | 2e-06 | 24/48 (SW 1271, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.759×** | -4.8 | 1e-04 | 19/47 (SK-MEL-2, NCI-H23, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.625×** | -4.4 | 7e-04 | 17/48 (A-172, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.794×** | -4.2 | 0.002 | 22/46 (SW48, HT-29, …) | rises with dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.803×** | -3.9 | 0.004 | 17/47 (HepG2/C3A, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 26.8 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.0726× (z -26.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.8) |
| [[A-172 (line)]] | wt | 33.2 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.303× (z -11.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -8.5) |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.401× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 38.8 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.85× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +14.6) | — |
| [[RKO (line)]] | wt | 26.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -12.3) |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.193× (z -9.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +10.7) | — |
| [[A549 (line)]] | wt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 20.2 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 23.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 18.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 19.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -12.9) |
| [[HT-29 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.1 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.207× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 40.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -10.9) ⚠ cell-cycle shift, explains ~37% of this change |
| [[RPMI-7951 (line)]] | alt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 20.6 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.214× (z -9.2) |
| [[SW48 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0734× (z -11.3) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW480 (line)]] | alt | 17.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -8.8) |
| [[A-427 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 37.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF776]] | +0.72 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[MYL5]] | +0.71 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ZFHX2]] | +0.69 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PRR14]] | +0.69 | +0.58 / +0.73 | both halves | 8e-06 |  |
| [[ZNF780A]] | +0.69 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CHTOP]] | +0.68 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZNF554]] | +0.67 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[CLK4]] | +0.67 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[PBX2]] | +0.67 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[ZNF317]] | +0.66 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[POGZ]] | +0.66 | +0.58 / +0.66 | both halves | 8e-06 |  |
| [[ZNF620]] | +0.66 | +0.50 / +0.65 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOLT1B]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[PIGN]] | -0.59 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[NME2]] | -0.59 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[MTFR1]] | -0.58 | -0.57 / -0.53 | both halves | 1e-05 |  |
| [[MFN1]] | -0.58 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[PLEKHA8]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[COG5]] | -0.58 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[GRB2]] | -0.57 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[DYM]] | -0.56 | -0.56 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DEDD's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[THNSL2]] | B | THNSL2 activity raises DEDD's level | lines that do not express THNSL2 (19) vs lines expressing it (31) | 1.22× lower at baseline in the lines without THNSL2 | 0.081 | ⚠ within organs, on part of the lines; also absent: CRABP2, NPTX2, SULT4A1 |
| [[HDAC6]] | B | HDAC6 activity raises DEDD's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.700). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-12.6, 4.7); signed map (10.8, -18.5). **Vector** length 81.2, 15.4% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +7.5 | +12.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.0 | +14.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +5.0 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~81% of this change | +4.7 | -2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.8 | +3.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.7 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | +0.5 |

## What is on record

|  |  |
|---|---|
| Name | death effector domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q23.3 — chr1:161,120,974-161,132,688 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DEFT, FLDED1, CASP8IP1, KE05, DEDD1 |
| Gene groups (HGNC) | Death effector domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O75618](https://www.uniprot.org/uniprotkb/O75618) (Death effector domain-containing protein):

> A scaffold protein that directs CASP3 to certain substrates and facilitates their ordered degradation during apoptosis. May also play a role in mediating CASP3 cleavage of KRT18. Regulates degradation of intermediate filaments during apoptosis. May play a role in the general transcription machinery in the nucleus and might be an important regulator of the activity of GTF3C3. Inhibits DNA transcription in vitro (By similarity).

**Summary**, from NCBI Gene [9191](https://www.ncbi.nlm.nih.gov/gene/9191):

> This gene encodes a protein that contains a death effector domain (DED). DED is a protein-protein interaction domain shared by adaptors, regulators and executors of the programmed cell death pathway. Overexpression of this gene was shown to induce weak apoptosis. Upon stimulation, this protein was found to translocate from cytoplasm to nucleus and colocalize with UBTF, a basal factor required for RNA polymerase I transcription, in the nucleolus. At least three transcript variants encoding the …

**Accessions** — [HGNC:2755](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2755) · Entrez [9191](https://www.ncbi.nlm.nih.gov/gene/9191) · UniProt [O75618](https://www.uniprot.org/uniprotkb/O75618) · Ensembl [ENSG00000158796](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158796)

## Data

Gene col 8192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8192); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8192]; `tensor/DDL_lfc|DDL_z.npy` [8192]; `embed/gene_vectors.npy` [8192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8192 or target_col == 8192). Every well: [[DEDD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DEDD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
