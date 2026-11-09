---
symbol: "UAP1L1"
type: "gene"
col: 12387
ensembl_id: "ENSG00000197355"
name: "UDP-N-acetylglucosamine pyrophosphorylase 1 like 1"
location: "9q34.3"
module: 59
arm: "+"
pooled_cpm: 8.68
n_lines_expressing: 46
n_dd_up: 28
n_dd_down: 3
n_dd_up_clean: 25
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/059"]
generated_by: "tahoemap"
---

# UAP1L1

*UDP-N-acetylglucosamine pyrophosphorylase 1 like 1* — 9q34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.16× (z +25.5, q 0e+00, up in 39 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.657× (z -4.5, q 0.004, down in 18 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-423 0.188×, MIA PaCa-2 0.236×, hTERT-HPNE 0.182×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 0.179×, Hs 766T 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.155×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FLCN]] (+0.73, fdr 7e-06), [[SLC31A2]] (+0.70, fdr 7e-06), [[AMDHD2]] (+0.69, fdr 7e-06); moves opposite to [[ACTL6A]] (-0.61, fdr 1e-05), [[COP1]] (-0.59, fdr 1e-05), [[RECQL]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 059]] (Amino acids regulate mTORC1).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ZNF264]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.16×** | +25.5 | 0e+00 | 39/41 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.45×** | +9.8 | 3e-20 | 28/39 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.47×** | +9.5 | 4e-19 | 30/42 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.96×** | +7.3 | 3e-11 | 24/43 (NCI-H460, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.49×** | +6.2 | 8e-08 | 20/44 (A498, RKO, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.0 | 2e-07 | 23/40 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +5.5 | 4e-06 | 22/43 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.64×** | +5.4 | 4e-06 | 19/43 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +5.0 | 4e-05 | 18/43 (A-172, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.57×** | +4.9 | 6e-05 | 17/42 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +4.7 | 1e-04 | 18/36 (A-172, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.6 | 2e-04 | 16/43 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.006 | 7/44 (A-172, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.63×** | +3.8 | 0.006 | 9/30 (A498, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.6 | 0.011 | 12/32 (Hs 766T, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~9% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.39×** | +3.6 | 0.011 | 9/43 (A-172, A498, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +3.6 | 0.011 | 15/43 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12387.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SNU-423 0.188×, MIA PaCa-2 0.236×, hTERT-HPNE 0.182×; ⚠ cell-cycle shift, explains ~21% of this change); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SNU-423 0.179×, Hs 766T 0.118×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 0.155×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.657×** | -4.5 | 0.004 | 18/39 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.772×** | -4.1 | 0.012 | 19/40 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -3.8 | 0.029 | 17/39 (SNU-423, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | 0.581× | -3.1 | 0.24 | 9/37 (MIA PaCa-2, CFPAC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 2 (1 ⚠) | 3 (2 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.81× (z +10.9) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.236× (z -10.6) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.155× (z -9.3) |
| [[A-172 (line)]] | wt | 62.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.57× (z +21.6) | — |
| [[J82 (line)]] | alt | 19.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +22.1) | — |
| [[KATO III (line)]] | alt | 6.55 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.2× (z +16.0) | — |
| [[SNU-423 (line)]] | alt | 23.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +12.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.188× (z -14.6) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A498 (line)]] | wt | 10.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.87× (z +18.4) | — |
| [[Hs 766T (line)]] | wt | 11.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +16.2) | [[Dinaciclib (drug)]] 0.05 µM 0.118× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 9.30 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.28× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -8.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[H4 (line)]] | wt | 8.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.43× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 3.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.9× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 7.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +9.0) | — |
| [[HT-29 (line)]] | alt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.79× (z +12.5) | — |
| [[LoVo (line)]] | wt | 5.01 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.54× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 7.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.75× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 3.63 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.91× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 4.30 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 4.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +9.2) | — |
| [[RKO (line)]] | wt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +12.1) | — |
| [[RPMI-7951 (line)]] | alt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.49× (z +11.9) | — |
| [[SW1417 (line)]] | alt | 9.86 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +9.8) | — |
| [[SW48 (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +10.2) | — |
| [[SW480 (line)]] | alt | 7.87 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.17× (z +14.3) | — |
| [[A-427 (line)]] | wt | 3.07 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.08 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.59 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.949 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLCN]] | +0.73 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[SLC31A2]] | +0.70 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[AMDHD2]] | +0.69 | +0.73 / +0.65 | both halves | 7e-06 | STRING 440 |
| [[DUSP3]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[RRAGC]] | +0.64 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[PLD6]] | +0.62 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SAT2]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TSC1]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[ZBTB4]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[TOLLIP]] | +0.61 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[NUDT14]] | +0.61 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[ZNF316]] | +0.61 | +0.57 / +0.62 | both halves | 9e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACTL6A]] | -0.61 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[COP1]] | -0.59 | -0.65 / -0.52 | both halves | 1e-05 |  |
| [[RECQL]] | -0.54 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[POC1B]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[GMPS]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[CCT6A]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MTFR1]] | -0.51 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[NIPA2]] | -0.51 | -0.55 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises UAP1L1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 0.8% of all compounds | 0.010 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[NDRG4]] | B | NDRG4 activity raises UAP1L1's level | lines that do not express NDRG4 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without NDRG4 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000176593, SMARCA1, ZNF606; maybe low, not absent |
| [[GYPC]] | B | GYPC activity raises UAP1L1's level | lines that do not express GYPC (35) vs lines expressing it (15) | 1.82× lower at baseline in the lines without GYPC | 0.059 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PHACTR1, ANKRD30B, PLPP4 |
| [[TCEAL3]] | B | TCEAL3 activity raises UAP1L1's level | lines that do not express TCEAL3 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without TCEAL3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000281091, TTLL7, ENSG00000234405 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF264]] | C | UAP1L1 activity raises ZNF264's level | lines that do not express UAP1L1 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without UAP1L1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF516, POGLUT3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 059]] — Amino acids regulate mTORC1; 80 genes; this gene is in the **+** arm (projection on the module's main direction 0.645). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (0.0, -31.8); signed map (4.9, -9.4). **Vector** length 97.8, 22.5% of its response variance represented; |z| ≥ 3 in 839 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Amino acids regulate mTORC1* (reactome, mean cos +0.57 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +25.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +9.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.1 | +9.5 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.4 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.3 | +5.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +4.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.8 | -4.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.7 | -0.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.7 | -1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.7 | -1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | UDP-N-acetylglucosamine pyrophosphorylase 1 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.3 — chr9:137,077,517-137,084,539 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

UniProt [Q3KQV9](https://www.uniprot.org/uniprotkb/Q3KQV9) carries no function annotation.

**Summary**, from NCBI Gene [91373](https://www.ncbi.nlm.nih.gov/gene/91373):

> Predicted to enable UDP-N-acetylglucosamine diphosphorylase activity. Predicted to be involved in UDP-N-acetylglucosamine biosynthetic process. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28082](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28082) · Entrez [91373](https://www.ncbi.nlm.nih.gov/gene/91373) · UniProt [Q3KQV9](https://www.uniprot.org/uniprotkb/Q3KQV9) · Ensembl [ENSG00000197355](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197355)

## Data

Gene col 12387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12387); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12387]; `tensor/DDL_lfc|DDL_z.npy` [12387]; `embed/gene_vectors.npy` [12387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12387 or target_col == 12387). Every well: [[UAP1L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UAP1L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
