---
symbol: "NKRF"
type: "gene"
col: 11812
ensembl_id: "ENSG00000186416"
name: "NFKB repressing factor"
location: "Xq24"
module: 33
arm: "+"
pooled_cpm: 17.88
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 3
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NKRF

*NFKB repressing factor* — Xq24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.69× (z +10.2, q 1e-21, up in 38 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.65× (z +9.8, q 3e-20, up in 32 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.629× (z -9.1, q 5e-17, down in 30 of 42 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 0.1000×, PANC-1 0.220×, KATO III 0.155×, SW480 0.348×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.189×, HEC-1-A 0.202×, MIA PaCa-2 0.260×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HT-29 0.0894×, SW480 0.326×; ⚠ toxic; transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HS-578T 0.0676×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SNU-1 0.0784×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0834×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NLE1]] (+0.72, fdr 7e-06), [[WDR3]] (+0.70, fdr 7e-06), [[RRP1B]] (+0.69, fdr 7e-06); moves opposite to [[SMIM14]] (-0.59, fdr 1e-05), [[SPPL2A]] (-0.59, fdr 1e-05), [[HLA-A]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DUXAP8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11812.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.69×** | +10.2 | 1e-21 | 38/47 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +9.8 | 3e-20 | 32/47 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.61×** | +9.3 | 3e-18 | 28/47 (A498, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +9.0 | 2e-17 | 25/46 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +8.9 | 4e-17 | 32/47 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.27×** | +8.4 | 5e-15 | 27/38 (LoVo, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +8.0 | 8e-14 | 27/47 (NCI-H1573, SNU-423, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.18×** | +8.0 | 9e-14 | 26/45 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.53×** | +7.8 | 4e-13 | 26/47 (SW1417, J82, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.30×** | +7.3 | 2e-11 | 20/48 (SK-MEL-2, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +7.2 | 2e-11 | 24/47 (HOP62, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +6.6 | 2e-09 | 23/46 (HOP62, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +5.5 | 1e-06 | 18/46 (SNU-423, A498, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +5.5 | 1e-06 | 17/47 (LOX-IMVI, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +5.2 | 6e-06 | 18/45 (A498, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.2 | 6e-06 | 16/46 (LOX-IMVI, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +4.9 | 3e-05 | 12/45 (SK-MEL-2, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +4.0 | 0.002 | 9/47 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.23×** | +4.0 | 0.002 | 10/46 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.002 | 9/48 (SW1417, HOP62, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11812.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (NCI-H460 0.1000×, PANC-1 0.220×, KATO III 0.155×, SW480 0.348×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (PANC-1 0.189×, HEC-1-A 0.202×, MIA PaCa-2 0.260×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (HT-29 0.0894×, SW480 0.326×; ⚠ toxic; transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (HS-578T 0.0676×); [[Cepharanthine (drug)]] 0.5 µM in 1 line (SNU-1 0.0784×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (H4 0.0834×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.629×** | -9.1 | 5e-17 | 30/42 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -8.3 | 4e-14 | 15/25 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.734×** | -5.0 | 1e-04 | 15/33 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.2 | 0.16 | 16/46 (HOP62, RKO, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.850× | -3.2 | 0.16 | 15/46 (BT-474, NCI-H661, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11812. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 23.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.155× (z -14.1) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 29.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.229× (z -11.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 29.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -18.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 41.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.348× (z -12.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -10.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.85 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -8.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 15.6 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0834× (z -10.6) |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -11.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -12.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 7.90 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0676× (z -12.8) |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0894× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.1000× (z -22.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -10.7) ⚠ cell-cycle shift, explains ~82% of this change |
| [[RPMI-7951 (line)]] | alt | 11.5 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.114× (z -9.8) |
| [[SHP-77 (line)]] | alt | 16.0 | 0 | 1 | — | [[PF-06260933 (drug)]] 0.5 µM 0.0950× (z -9.6) |
| [[SNU-1 (line)]] | wt | 16.5 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0784× (z -10.8) |
| [[A-172 (line)]] | wt | 6.78 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11812), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NLE1]] | +0.72 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[WDR3]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[RRP1B]] | +0.69 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[POP1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[BYSL]] | +0.67 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[MRPS23]] | +0.65 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MRPS27]] | +0.65 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.65 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[NOB1]] | +0.65 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PHB1]] | +0.64 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[STARD7]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[SPPL2A]] | -0.59 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[HLA-A]] | -0.58 | -0.63 / -0.49 | both halves | 1e-05 |  |
| [[TP53INP2]] | -0.57 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[WBP1]] | -0.56 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[DLEU2]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CYLD]] | -0.55 | -0.36 / -0.64 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUXAP8]] | B | DUXAP8 activity raises NKRF's level | lines that do not express DUXAP8 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without DUXAP8 | 0.083 | ⚠ within organs, on part of the lines; also absent: DUXAP10, DUXAP9, TTYH2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.769). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.8, -39.9); signed map (-9.8, -50.8). **Vector** length 80.9, 14.8% of its response variance represented; |z| ≥ 3 in 1,028 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.56 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.9 | +10.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.5 | +7.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.4 | +8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.7 | +4.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.5 | +4.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | -3.9 | -2.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.6 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | -9.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | +1.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.1 | -1.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -1.9 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -1.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | NFKB repressing factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq24 — chrX:119,588,337-119,606,443 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XTBD3, ITBA4, NRF |
| Gene groups (HGNC) | G-patch domain containing; XTBD family |
| Matched by | ensembl_id |

**Function**, from UniProt [O15226](https://www.uniprot.org/uniprotkb/O15226) (NF-kappa-B-repressing factor):

> Enhances the ATPase activity of DHX15 by acting like a brace that tethers mobile sections of DHX15 together, stabilizing a functional conformation with high RNA affinity of DHX15. Involved in the constitutive silencing of the interferon beta promoter, independently of the virus-induced signals, and in the inhibition of the basal and cytokine-induced iNOS promoter activity. Also involved in the regulation of IL-8 transcription. May also act as a DNA-binding transcription regulator: interacts …

**Summary**, from NCBI Gene [55922](https://www.ncbi.nlm.nih.gov/gene/55922):

> This gene encodes a transcriptional repressor that interacts with specific negative regulatory elements to mediate transcriptional repression of certain nuclear factor kappa B responsive genes. The protein localizes predominantly to the nucleolus with a small fraction found in the nucleoplasm and cytoplasm. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:19374](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19374) · Entrez [55922](https://www.ncbi.nlm.nih.gov/gene/55922) · UniProt [O15226](https://www.uniprot.org/uniprotkb/O15226) · Ensembl [ENSG00000186416](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186416)

## Data

Gene col 11812: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11812); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11812, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11812]; `tensor/DDL_lfc|DDL_z.npy` [11812]; `embed/gene_vectors.npy` [11812]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11812 or target_col == 11812). Every well: [[NKRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NKRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
