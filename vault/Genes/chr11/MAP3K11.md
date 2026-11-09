---
symbol: "MAP3K11"
type: "gene"
col: 10373
ensembl_id: "ENSG00000173327"
name: "mitogen-activated protein kinase kinase kinase 11"
location: "11q13.1"
module: 38
arm: "+"
pooled_cpm: 33.46
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 20
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# MAP3K11

*mitogen-activated protein kinase kinase kinase 11* — 11q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.42× (z +8.5, q 7e-15, up in 32 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 1.85×, SW480 1.79×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.07×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.553× (z -10.6, q 2e-23, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IRF3]] (+0.62, fdr 2e-05), [[MON1B]] (+0.59, fdr 1e-05), [[BRPF1]] (+0.58, fdr 1e-05); moves opposite to [[GFM1]] (-0.58, fdr 2e-05), [[MRPL42]] (-0.57, fdr 3e-05), [[CMSS1]] (-0.53, fdr 2e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[USF3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10373.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (PANC-1 1.85×, SW480 1.79×); [[Dinaciclib (drug)]] 5 µM in 1 line (LoVo 3.30×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SK-MEL-2 3.07×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +8.5 | 7e-15 | 32/47 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.041 | 15/46 (RPMI-7951, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.21× | +3.4 | 0.14 | 16/45 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 1.20× | +3.2 | 0.19 | 3/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 1.21× | +3.1 | 0.19 | 14/46 (SW480, LS 180, …) | inconsistent across doses | position effect removed |
| [[Posaconazole (drug)]] 5 µM |  | 1.19× | +3.1 | 0.19 | 12/48 (CFPAC-1, HOP62, …) | top dose only | plate-row cell shift; position effect removed |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 1.19× | +3.0 | 0.19 | 9/47 (SW1417, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10373.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.553×** | -10.6 | 2e-23 | 37/48 (HS-578T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.582×** | -8.9 | 1e-16 | 40/48 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.620×** | -8.5 | 3e-15 | 36/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.641×** | -8.0 | 2e-13 | 34/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.643×** | -7.9 | 3e-13 | 36/48 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.676×** | -7.0 | 3e-10 | 33/48 (HOP62, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -6.8 | 9e-10 | 31/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -6.3 | 2e-08 | 29/47 (HT-29, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.690×** | -6.1 | 5e-08 | 25/39 (HOP62, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -5.6 | 1e-06 | 28/48 (HS-578T, A549, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.740×** | -5.4 | 4e-06 | 28/47 (RPMI-7951, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.750×** | -4.9 | 4e-05 | 23/47 (SW 900, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.762×** | -4.9 | 5e-05 | 26/48 (SW 900, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.757×** | -4.6 | 2e-04 | 24/44 (NCI-H1573, SW48, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.777×** | -4.5 | 3e-04 | 24/48 (SW 900, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.801×** | -4.0 | 0.003 | 17/47 (NCI-H1573, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.800×** | -3.7 | 0.007 | 14/47 (NCI-H661, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.883× | -3.1 | 0.058 | 11/48 (HOP62, RPMI-7951, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10373. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 48.5 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -12.5) |
| [[HOP62 (line)]] | alt | 35.3 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.259× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.371× (z -9.5) |
| [[HT-29 (line)]] | alt | 59.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.324× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.339× (z -8.5) |
| [[PANC-1 (line)]] | alt | 35.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.432× (z -9.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 29.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.79× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 37.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.311× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~23% of this change |
| [[AN3 CA (line)]] | alt | 23.8 | 0 | 1 | — | [[Ponatinib (drug)]] 0.5 µM 0.0677× (z -9.4) |
| [[Hs 766T (line)]] | wt | 62.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -11.2) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 27.7 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -10.2) |
| [[LoVo (line)]] | wt | 38.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | — |
| [[LS 180 (line)]] | wt | 36.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -17.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[NCI-H2030 (line)]] | alt | 22.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.290× (z -8.6) |
| [[NCI-H2122 (line)]] | alt | 28.3 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.610× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 42.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.346× (z -8.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 22.3 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.180× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 33.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.217× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW48 (line)]] | wt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 46.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 42.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 51.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10373), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IRF3]] | +0.62 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[MON1B]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[BRPF1]] | +0.58 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[GPANK1]] | +0.57 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[ZSWIM8]] | +0.57 | +0.48 / +0.69 | both halves | 2e-05 |  |
| [[FBRS]] | +0.57 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[RNF31]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[SPACDR]] | +0.56 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[TSC22D4]] | +0.56 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[TTLL3]] | +0.55 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SPAG4]] | +0.55 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[IKZF4]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GFM1]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[MRPL42]] | -0.57 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[CMSS1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[DTD2]] | -0.53 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[SUCLG2]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TNPO1]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[EFR3A]] | -0.51 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[DPH6]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[VPS36]] | -0.50 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[MBTPS2]] | -0.50 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[NAE1]] | -0.50 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[ZDHHC21]] | -0.50 | -0.31 / -0.61 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USF3]] | C | USF3's natural level strengthens MAP3K11's drug response | USF3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.27; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.466). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.2, -28.8); signed map (4.8, 9.8). **Vector** length 97.8, 22.3% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.9 | +8.5 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.1 | +0.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +1.6 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.3 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +1.1 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.5 | +3.4 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.2 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.0 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -3.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.0 | -8.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -3.3 | -4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.6 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.1 — chr11:65,597,756-65,615,382 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SPRK, MEKK11; previously MLK3, PTK1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family; SH3 domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 16 pathways, smallest: RAF activation; RHOV GTPase cycle; Paradoxical activation of RAF signaling by kinase inactive BRAF |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16584](https://www.uniprot.org/uniprotkb/Q16584) (Mitogen-activated protein kinase kinase kinase 11):

> Activates the JUN N-terminal pathway. Required for serum-stimulated cell proliferation and for mitogen and cytokine activation of MAPK14 (p38), MAPK3 (ERK) and MAPK8 (JNK1) through phosphorylation and activation of MAP2K4/MKK4 and MAP2K7/MKK7. Plays a role in mitogen-stimulated phosphorylation and activation of BRAF, but does not phosphorylate BRAF directly. Influences microtubule organization during the cell cycle.

**Summary**, from NCBI Gene [4296](https://www.ncbi.nlm.nih.gov/gene/4296):

> The protein encoded by this gene is a member of the serine/threonine kinase family. This kinase contains a SH3 domain and a leucine zipper-basic motif. This kinase preferentially activates MAPK8/JNK kinase, and functions as a positive regulator of JNK signaling pathway. This kinase can directly phosphorylate, and activates IkappaB kinase alpha and beta, and is found to be involved in the transcription activity of NF-kappaB mediated by Rho family GTPases and CDC42. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:6850](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6850) · Entrez [4296](https://www.ncbi.nlm.nih.gov/gene/4296) · UniProt [Q16584](https://www.uniprot.org/uniprotkb/Q16584) · Ensembl [ENSG00000173327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173327)

## Data

Gene col 10373: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10373); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10373, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10373]; `tensor/DDL_lfc|DDL_z.npy` [10373]; `embed/gene_vectors.npy` [10373]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10373 or target_col == 10373). Every well: [[MAP3K11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
