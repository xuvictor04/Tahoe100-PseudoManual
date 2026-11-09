---
symbol: "FZR1"
type: "gene"
col: 2582
ensembl_id: "ENSG00000105325"
name: "fizzy and cell division cycle 20 related 1"
location: "19p13.3"
module: 3
arm: "+"
pooled_cpm: 30.46
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# FZR1

*fizzy and cell division cycle 20 related 1* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.71× (z +6.4, q 8e-08, up in 37 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.375× (z -12.0, q 1e-30, down in 38 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.769× (z -4.3, q 0.002, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAK4]] (+0.70, fdr 8e-06), [[MPND]] (+0.63, fdr 1e-05), [[HDGFL2]] (+0.62, fdr 1e-05); moves opposite to [[SRFBP1]] (-0.52, fdr 3e-05), [[MCTS1]] (-0.51, fdr 2e-04), [[IL6ST]] (-0.51, fdr 3e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2582.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +6.4 | 8e-08 | 37/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +6.2 | 1e-07 | 38/48 (HOP62, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.32×** | +5.4 | 1e-05 | 31/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.53×** | +5.2 | 2e-05 | 28/47 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.47×** | +4.7 | 3e-04 | 28/48 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.6 | 4e-04 | 7/48 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.002 | 25/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2582.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.375×** | -12.0 | 1e-30 | 38/44 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.425×** | -10.1 | 2e-21 | 27/35 (SW 900, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.527×** | -7.3 | 7e-11 | 36/42 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.714×** | -5.5 | 5e-06 | 32/48 (A-172, NCI-H1792, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.704×** | -4.3 | 0.002 | 31/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.769×** | -4.3 | 0.002 | 25/48 (NCI-H1792, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.703×** | -4.2 | 0.003 | 25/48 (A-172, C-33 A, …) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.726×** | -3.8 | 0.012 | 22/47 (SNU-423, AN3 CA, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.801×** | -3.7 | 0.012 | 29/48 (A-172, HS-578T, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.744×** | -3.6 | 0.017 | 24/48 (NCI-H23, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.747×** | -3.6 | 0.018 | 23/48 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.748×** | -3.5 | 0.018 | 25/47 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.754×** | -3.5 | 0.024 | 21/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.770×** | -3.2 | 0.056 | 20/48 (MIA PaCa-2, HEC-1-A, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -3.2 | 0.059 | 23/48 (SW 900, RPMI-7951, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2582. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 27.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.162× (z -12.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 30.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -14.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 31.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -11.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 33.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 31.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -10.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 45.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.191× (z -11.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.166× (z -11.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 24.8 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -9.6) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H460 (line)]] | wt | 22.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -11.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 42.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0752× (z -16.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -10.1) ⚠ cell-cycle shift, explains ~24% of this change |
| [[A-427 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -9.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 23.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.241× (z -8.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.140× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 43.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.136× (z -11.6) |
| [[HCT15 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0670× (z -15.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 34.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.210× (z -8.6) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 38.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -8.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -15.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 28.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.184× (z -11.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.347× (z -9.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 28.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +9.7) ⚠ cell-cycle shift, explains ~59% of this change | — |
| [[SNU-423 (line)]] | alt | 37.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -8.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2582), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAK4]] | +0.70 | +0.73 / +0.58 | both halves | 8e-06 |  |
| [[MPND]] | +0.63 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[HDGFL2]] | +0.62 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[CDAN1]] | +0.61 | +0.45 / +0.62 | both halves | 3e-05 |  |
| [[PIAS4]] | +0.60 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[MARK4]] | +0.60 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[PPP1R16A]] | +0.59 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[ESS2]] | +0.59 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[CLK2]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[TNFAIP8L1]] | +0.57 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[HSDL1]] | +0.57 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[VRK3]] | +0.56 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRFBP1]] | -0.52 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[MCTS1]] | -0.51 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[IL6ST]] | -0.51 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ADSS2]] | -0.51 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[RXYLT1]] | -0.50 | -0.64 / -0.26 | both halves | 4e-04 |  |
| [[SMIM15]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[GUF1]] | -0.49 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[CFAP97]] | -0.49 | -0.51 / -0.36 | both halves | 9e-05 |  |
| [[ATIC]] | -0.49 | -0.53 / -0.45 | both halves | 3e-05 |  |
| [[EREG]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |
| [[PHACTR2]] | -0.48 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[SEPTIN11]] | -0.48 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises FZR1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.561). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-12.4, -5.8); signed map (-35.4, 1.4). **Vector** length 85.9, 18.7% of its response variance represented; |z| ≥ 3 in 869 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.5 | +1.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.6 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | -2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.4 | +1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | -1.2 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +1.9 | +1.0 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.8 | +0.7 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.7 | +0.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.6 | -1.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.8 | -2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | -7.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -12.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.2 | -3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Lactate (calcium) (drug)]] 0.05 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | fizzy and cell division cycle 20 related 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:3,506,311-3,538,334 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCDH1, CDH1, HCDH, FZR, FZR2, KIAA1242, CDC20C |
| Gene groups (HGNC) | WD repeat domain containing |
| Reactome | 32 pathways, smallest: Phosphorylation of Emi1; Aberrant regulation of mitotic exit in cancer due to RB1 defects; Conversion from APC/C:Cdc20 to APC/C:Cdh1 in late anaphase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UM11](https://www.uniprot.org/uniprotkb/Q9UM11) (Fizzy-related protein homolog):

> Substrate-specific adapter for the anaphase promoting complex/cyclosome (APC/C) E3 ubiquitin-protein ligase complex. Associates with the APC/C in late mitosis, in replacement of CDC20, and activates the APC/C during anaphase and telophase. The APC/C remains active in degrading substrates to ensure that positive regulators of the cell cycle do not accumulate prematurely. At the G1/S transition FZR1 is phosphorylated, leading to its dissociation from the APC/C. Following DNA damage, it is …

**Summary**, from NCBI Gene [51343](https://www.ncbi.nlm.nih.gov/gene/51343):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in anaphase-promoting complex-dependent catabolic process; mitotic G2 DNA damage checkpoint signaling; and positive regulation of ubiquitin protein ligase activity. Located in nuclear membrane and nucleoplasm. Implicated in developmental and epileptic encephalopathy 109. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24824](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24824) · Entrez [51343](https://www.ncbi.nlm.nih.gov/gene/51343) · UniProt [Q9UM11](https://www.uniprot.org/uniprotkb/Q9UM11) · Ensembl [ENSG00000105325](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105325)

## Data

Gene col 2582: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2582); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2582, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2582]; `tensor/DDL_lfc|DDL_z.npy` [2582]; `embed/gene_vectors.npy` [2582]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2582 or target_col == 2582). Every well: [[FZR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FZR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
