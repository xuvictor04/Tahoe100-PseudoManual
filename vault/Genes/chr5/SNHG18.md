---
symbol: "SNHG18"
type: "gene"
col: 14713
ensembl_id: "ENSG00000250786"
name: "small nucleolar RNA host gene 18"
location: "5p15.31"
module: 40
arm: "+"
pooled_cpm: 5.3
n_lines_expressing: 21
n_dd_up: 9
n_dd_down: 4
n_dd_up_clean: 4
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 29
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# SNHG18

*small nucleolar RNA host gene 18* — 5p15.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.62× (z +11.1, q 8e-26, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.47× (z +4.0, q 0.007, up in 3 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.550× (z -4.5, q 0.002, down in 15 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ISOC2]] (+0.70, fdr 7e-06), [[PDXDC2P]] (+0.68, fdr 7e-06), [[YIPF2]] (+0.67, fdr 7e-06); moves opposite to [[CPSF2]] (-0.56, fdr 2e-05), [[PRRC2B]] (-0.55, fdr 2e-05), [[ATE1]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SEMA5A]] → it (grade C ⚠); 29 go from it, the strongest it → [[NPRL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 5 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14713.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.62×** | +11.1 | 8e-26 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.17×** | +5.8 | 2e-06 | 1/14 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +4.1 | 0.007 | 4/12 (J82, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.007 | 3/19 (KATO III, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.73×** | +3.8 | 0.016 | 0/11 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.02×** | +3.8 | 0.016 | 1/13 (Hs 766T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.98×** | +3.7 | 0.019 | 2/13 (J82, SW1417) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.85×** | +3.3 | 0.067 | 1/16 (HS-578T) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.067 | 2/19 (LS 180, NCI-H2347) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.77× | +3.1 | 0.13 | 4/14 (SW 900, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14713.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -4.5 | 0.002 | 15/17 (RPMI-7951, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.540×** | -4.5 | 0.002 | 11/18 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.603×** | -3.8 | 0.023 | 14/19 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.613×** | -3.7 | 0.028 | 16/18 (A498, RPMI-7951, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.647× | -3.3 | 0.10 | 3/18 (NCI-H2347, C32, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.651× | -3.3 | 0.10 | 5/18 (SW 900, Hs 766T, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.39 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14713. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.108× (z -14.2) |
| [[A498 (line)]] | wt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -10.2) |
| [[KATO III (line)]] | alt | 17.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -15.8) |
| [[A-172 (line)]] | wt | 34.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -9.6) |
| [[Hs 766T (line)]] | wt | 9.02 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -10.6) |
| [[HS-578T (line)]] | alt | 37.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.247× (z -9.1) ⚠ cell-cycle shift, explains ~83% of this change |
| [[LS 180 (line)]] | wt | 4.51 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 3.64 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.120× (z -8.6) |
| [[SW1417 (line)]] | alt | 15.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0675× (z -21.6) |
| [[A-427 (line)]] | wt | 0.308 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.332 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.405 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.387 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.401 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.386 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.893 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.471 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.359 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.414 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.452 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.907 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.362 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.416 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.513 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.986 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.333 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.485 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.62 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.534 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14713), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ISOC2]] | +0.70 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[PDXDC2P]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[YIPF2]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[COG6]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PDXDC2P-NPIPB14P]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[SDHAP1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TMEM243]] | +0.63 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[CYB561D2]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[IER3IP1]] | +0.63 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[AKR1A1]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPSF2]] | -0.56 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[PRRC2B]] | -0.55 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[ATE1]] | -0.54 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEMA5A]] | C | SEMA5A activity raises SNHG18's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 4.77× lower at baseline in the lines without SEMA5A | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 27, C 2. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NPRL2]] | B | SNHG18 activity raises NPRL2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.36× lower at baseline in the lines without SNHG18 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[YIPF2]] | B | SNHG18 activity raises YIPF2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without SNHG18 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[COG6]] | B | SNHG18 activity raises COG6's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.42× lower at baseline in the lines without SNHG18 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[OSBPL7]] | B | SNHG18 activity raises OSBPL7's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.78× lower at baseline in the lines without SNHG18 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[SMIM3]] | B | SNHG18 activity raises SMIM3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 2.29× lower at baseline in the lines without SNHG18 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[CYB561D2]] | B | SNHG18 activity raises CYB561D2's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.45× lower at baseline in the lines without SNHG18 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[COG3]] | B | SNHG18 activity raises COG3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.37× lower at baseline in the lines without SNHG18 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[MOSPD3]] | B | SNHG18 activity raises MOSPD3's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.32× lower at baseline in the lines without SNHG18 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[LMAN1]] | B | SNHG18 activity strengthens LMAN1's drug response | lines that do not express SNHG18 (29) vs lines expressing it (20) | the lines without SNHG18 respond 0.71× as strongly (z diff +1.89); strongest at Homoharringtonine 0.5 µM: 0.64x vs 0.39x (z diff +3.9) | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930; target measured in part of the lines; artifact flags |
| [[SEC61B]] | B | SNHG18 activity raises SEC61B's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.32× lower at baseline in the lines without SNHG18 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[RAB3A]] | B | SNHG18 activity raises RAB3A's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.40× lower at baseline in the lines without SNHG18 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |
| [[SEC24D]] | B | SNHG18 activity raises SEC24D's level | lines that do not express SNHG18 (29) vs lines expressing it (21) | 1.74× lower at baseline in the lines without SNHG18 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SEMA5A, AMPH, LINC02930 |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.675). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (15.7, -34.7); signed map (-48.5, 10.0). **Vector** length 45.4, 11.9% of its response variance represented; |z| ≥ 3 in 355 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +1.8 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +4.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.4 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.8 | +3.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +0.8 | +1.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.8 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.1 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.0 | -3.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.9 | -0.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -4.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.1 | -0.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.9 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | small nucleolar RNA host gene 18 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p15.31 — chr5:9,546,170-9,550,725 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100505806](https://www.ncbi.nlm.nih.gov/gene/100505806):

> Predicted to be involved in RNA processing. Predicted to be located in nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:49007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:49007) · Entrez [100505806](https://www.ncbi.nlm.nih.gov/gene/100505806) · Ensembl [ENSG00000250786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250786)

## Data

Gene col 14713: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14713); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14713, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14713]; `tensor/DDL_lfc|DDL_z.npy` [14713]; `embed/gene_vectors.npy` [14713]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14713 or target_col == 14713). Every well: [[SNHG18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNHG18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
