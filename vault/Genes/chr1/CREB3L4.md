---
symbol: "CREB3L4"
type: "gene"
col: 6775
ensembl_id: "ENSG00000143578"
name: "cAMP responsive element binding protein 3 like 4"
location: "1q21.3"
module: 35
arm: "+"
pooled_cpm: 4.82
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# CREB3L4

*cAMP responsive element binding protein 3 like 4* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.12× (z +14.5, q 4e-45, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.456× (z -7.1, q 8e-10, down in 26 of 44 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC2HC1C]] (+0.73, fdr 1e-05), [[C11orf71]] (+0.72, fdr 1e-05), [[TCEAL1]] (+0.70, fdr 1e-05); moves opposite to [[GTF2E2]] (-0.64, fdr 6e-05), [[FBXW2]] (-0.61, fdr 7e-05), [[ABCC10]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SYCP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6775.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.12×** | +14.5 | 4e-45 | 36/37 (NCI-H2347, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +9.7 | 8e-20 | 23/37 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.90×** | +9.3 | 4e-18 | 6/8 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +6.5 | 1e-08 | 6/11 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.99×** | +6.2 | 6e-08 | 16/23 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +5.1 | 3e-05 | 17/36 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.42×** | +4.5 | 5e-04 | 14/46 (A-172, HOP62, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.54×** | +3.9 | 0.006 | 17/44 (NCI-H1573, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.029 | 15/43 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +3.5 | 0.029 | 10/40 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.4 | 0.034 | 3/20 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.054 | 9/45 (NCI-H23, A-427, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.43×** | +3.2 | 0.054 | 8/46 (NCI-H23, A-172, …) | two highest doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.2 | 0.054 | 9/28 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~20% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.054 | 7/45 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6775.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -7.1 | 8e-10 | 26/44 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.474×** | -6.7 | 5e-09 | 26/45 (NCI-H2030, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.513×** | -6.0 | 3e-07 | 22/45 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -5.6 | 4e-06 | 23/46 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.543×** | -5.5 | 4e-06 | 25/44 (SK-MEL-2, HT-29, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.549×** | -5.4 | 6e-06 | 23/45 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.591×** | -4.7 | 2e-04 | 20/46 (HCT15, COLO 205, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.615×** | -4.3 | 0.001 | 21/43 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.438×** | -3.9 | 0.006 | 16/38 (A-427, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.464×** | -3.6 | 0.017 | 8/33 (C32, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.677×** | -3.5 | 0.023 | 10/46 (A-427, MIA PaCa-2, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.503×** | -3.2 | 0.056 | 11/42 (A-427, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Gallic acid (drug)]] 5 µM |  | **0.776×** | -3.2 | 0.056 | 9/47 (SNU-1, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6775. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.38 | 0 | 2 (1 ⚠) | — | [[Pimozide (drug)]] 0.05 µM 0.0840× (z -10.7) |
| [[A498 (line)]] | wt | 6.39 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -9.0) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 3.51 | 0 | 1 | — | [[Thymopentin (drug)]] 5 µM 0.0700× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 10.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +8.9) | — |
| [[NCI-H460 (line)]] | wt | 4.02 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 7.99 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.190× (z -9.6) |
| [[A-172 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.95 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.20 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.02 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.31 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.59 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6775), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC2HC1C]] | +0.73 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[C11orf71]] | +0.72 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[TCEAL1]] | +0.70 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[LINC02307]] | +0.69 | +0.71 / +0.49 | both halves | 1e-05 |  |
| [[SIX5]] | +0.69 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[ZCWPW1]] | +0.67 | +0.70 / +0.35 | both halves | 1e-04 |  |
| [[SPEN-AS1]] | +0.67 | +0.75 / +0.39 | both halves | 6e-05 |  |
| [[C19orf54]] | +0.67 | +0.71 / +0.40 | both halves | 4e-05 |  |
| [[PLS3-AS1]] | +0.66 | +0.69 / +0.35 | both halves | 1e-04 |  |
| [[ZBTB2]] | +0.66 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[PJVK]] | +0.66 | +0.68 / +0.43 | both halves | 3e-05 |  |
| [[TMEM202-AS1]] | +0.65 | +0.68 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.64 | -0.65 / -0.38 | both halves | 6e-05 |  |
| [[FBXW2]] | -0.61 | -0.65 / -0.38 | both halves | 7e-05 |  |
| [[ABCC10]] | -0.61 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[NOMO1]] | -0.61 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[PCMT1]] | -0.60 | -0.66 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[ACTR5]] | -0.60 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[RSU1]] | -0.59 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[MTG1]] | -0.59 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[ARPC1A]] | -0.59 | -0.62 / -0.32 | both halves | 1e-04 |  |
| [[AP3M2]] | -0.59 | -0.58 / -0.30 | both halves | 2e-04 |  |
| [[PIP4K2A]] | -0.59 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[NOMO3]] | -0.58 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[STX2]] | -0.58 | -0.56 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYCP2]] | B | SYCP2 activity raises CREB3L4's level | lines that do not express SYCP2 (15) vs lines expressing it (35) | 1.42× lower at baseline in the lines without SYCP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: AMOT, LINC00937, DMBX1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CREB3L4's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM111A-DT]] | C | FAM111A-DT's natural level strengthens CREB3L4's drug response | FAM111A-DT's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.15; direction not clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-2.3, 15.2); signed map (19.8, -13.5). **Vector** length 69.5, 12.2% of its response variance represented; |z| ≥ 3 in 893 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +14.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +9.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.0 | +3.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +3.2 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -6.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -7.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.0 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.6 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | cAMP responsive element binding protein 3 like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:153,967,534-153,974,361 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIbZIP, CREB4, CREB3, hJAL, ATCE1 |
| Gene groups (HGNC) | CREB3 transcription factor family |
| Reactome | 4 pathways, smallest: CREB3 factors activate genes; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TEY5](https://www.uniprot.org/uniprotkb/Q8TEY5) (Cyclic AMP-responsive element-binding protein 3-like protein 4):

> Transcriptional activator that may play a role in the unfolded protein response. Binds to the UPR element (UPRE) but not to CRE element. Preferentially binds DNA with to the consensus sequence 5'-T[GT]ACGT[GA][GT]-3' and has transcriptional activation activity from UPRE. Binds to NF-kappa-B site and has transcriptional activation activity from NF-kappa-B-containing regulatory elements (By similarity).

**Summary**, from NCBI Gene [148327](https://www.ncbi.nlm.nih.gov/gene/148327):

> This gene encodes a CREB (cAMP responsive element binding) protein with a transmembrane domain which localizes it to the ER membrane. The encoded protein is a transcriptional activator which contains a dimerization domain, and this protein may function in a number of processing pathways including protein processing. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:18854](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18854) · Entrez [148327](https://www.ncbi.nlm.nih.gov/gene/148327) · UniProt [Q8TEY5](https://www.uniprot.org/uniprotkb/Q8TEY5) · Ensembl [ENSG00000143578](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143578)

## Data

Gene col 6775: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6775); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6775, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6775]; `tensor/DDL_lfc|DDL_z.npy` [6775]; `embed/gene_vectors.npy` [6775]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6775 or target_col == 6775). Every well: [[CREB3L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREB3L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
