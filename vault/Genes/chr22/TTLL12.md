---
symbol: "TTLL12"
type: "gene"
col: 1920
ensembl_id: "ENSG00000100304"
name: "tubulin tyrosine ligase like 12"
location: "22q13.2"
module: 50
arm: "+"
pooled_cpm: 17.88
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# TTLL12

*tubulin tyrosine ligase like 12* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.22× (z +16.2, q 0e+00, up in 27 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.28× (z +3.4, q 0.037, up in 16 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 10.3×, A498 5.17×, LoVo 5.63×, SNU-423 6.76×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 5.92×, LoVo 7.56×, A498 5.57×, SW480 4.01×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 4.34×); [[Harringtonine (drug)]] 5 µM in 1 line (KATO III 6.21×).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.469× (z -15.4, q 0e+00, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APEH]] (+0.78, fdr 7e-06), [[BOP1]] (+0.72, fdr 7e-06), [[SLC25A39]] (+0.71, fdr 9e-06); moves opposite to [[SPATC1]] (-0.66, fdr 1e-05), [[ATE1OSP]] (-0.65, fdr 3e-05), [[TERF2IP]] (-0.65, fdr 1e-05).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PTPRU]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1920.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (NCI-H1792 10.3×, A498 5.17×, LoVo 5.63×, SNU-423 6.76×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (NCI-H460 5.92×, LoVo 7.56×, A498 5.57×, SW480 4.01×, …; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 4.34×); [[Harringtonine (drug)]] 5 µM in 1 line (KATO III 6.21×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.22×** | +16.2 | 0e+00 | 27/28 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **2.28×** | +11.8 | 6e-30 | 36/39 (NCI-H1792, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.23×** | +10.7 | 3e-24 | 29/35 (A498, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.02×** | +10.1 | 5e-22 | 39/47 (HOP62, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.84×** | +8.8 | 2e-16 | 38/47 (A498, HOP62, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.52×** | +6.0 | 2e-07 | 33/47 (A498, NCI-H1573, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.6 | 3e-04 | 20/43 (SW1417, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.33×** | +4.1 | 0.002 | 15/47 (HOP62, A498, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.33×** | +4.1 | 0.002 | 16/46 (A549, NCI-H1573, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.037 | 16/46 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.059 | 4/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.2 | 0.059 | 14/47 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.17× | +3.2 | 0.059 | 8/48 (SNU-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1920.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.469×** | -15.4 | 0e+00 | 40/47 (MIA PaCa-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.467×** | -11.0 | 1e-25 | 40/47 (COLO 205, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.547×** | -8.7 | 6e-16 | 30/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.557×** | -8.5 | 4e-15 | 32/46 (SNU-1, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.558×** | -8.4 | 4e-15 | 27/46 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -8.1 | 5e-14 | 30/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.350×** | -7.9 | 2e-13 | 36/46 (Hs 766T, HOP62, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.409×** | -6.8 | 1e-09 | 31/45 (C32, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.640×** | -6.4 | 7e-09 | 25/46 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -5.4 | 3e-06 | 26/47 (HS-578T, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.677×** | -5.4 | 3e-06 | 23/46 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.673×** | -5.4 | 3e-06 | 27/46 (LOX-IMVI, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.728×** | -4.4 | 4e-04 | 21/46 (NCI-H2030, SK-MEL-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.760×** | -4.0 | 0.003 | 19/46 (C32, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.764×** | -3.9 | 0.004 | 23/47 (HS-578T, LS 180, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.778×** | -3.6 | 0.009 | 14/48 (SNU-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1920. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 24.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.66× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -16.4) |
| [[MIA PaCa-2 (line)]] | alt | 36.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.74× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -24.5) |
| [[A498 (line)]] | wt | 15.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.57× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.209× (z -11.6) |
| [[SW480 (line)]] | alt | 24.1 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.01× (z +11.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.334× (z -9.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.343× (z -9.0) |
| [[LoVo (line)]] | wt | 18.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.56× (z +12.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 14.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0628× (z -23.2) |
| [[SNU-1 (line)]] | wt | 26.6 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0328× (z -17.3) |
| [[AsPC-1 (line)]] | alt | 17.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 23.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -15.9) |
| [[COLO 205 (line)]] | alt | 25.5 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0952× (z -12.3) |
| [[HOP62 (line)]] | alt | 20.2 | 1 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 3.56× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -8.9) |
| [[KATO III (line)]] | alt | 29.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.2) | — |
| [[NCI-H1792 (line)]] | alt | 17.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.3× (z +13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H23 (line)]] | alt | 15.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -15.9) |
| [[PANC-1 (line)]] | alt | 9.31 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.7) |
| [[RKO (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0453× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.202× (z -13.8) |
| [[A-427 (line)]] | wt | 14.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -10.1) |
| [[BT-474 (line)]] | alt | 18.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -8.5) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.96 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0411× (z -14.1) |
| [[HEC-1-A (line)]] | alt | 26.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +8.8) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -8.7) |
| [[HT-29 (line)]] | alt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +8.9) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 7.26 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.0760× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 8.85 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 16.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.8) |
| [[SNU-423 (line)]] | alt | 13.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SW1417 (line)]] | alt | 16.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -9.0) |
| [[SW48 (line)]] | wt | 29.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -8.8) |
| [[A-172 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1920), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APEH]] | +0.78 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[BOP1]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[SLC25A39]] | +0.71 | +0.71 / +0.57 | both halves | 9e-06 |  |
| [[SIGMAR1]] | +0.68 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[CS]] | +0.68 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[BCKDK]] | +0.68 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[MAPKAPK3]] | +0.68 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[POLD2]] | +0.67 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[PDHA1]] | +0.66 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PHB1]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[BLTP2]] | +0.65 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[MTHFD1]] | +0.64 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATC1]] | -0.66 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[ATE1OSP]] | -0.65 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[TERF2IP]] | -0.65 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[LINC02608]] | -0.65 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[LINC02951]] | -0.64 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[ZCCHC10]] | -0.63 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[GTF2IRD2B]] | -0.63 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MAFG]] | -0.63 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[NDUFC1]] | -0.63 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[ARID4B]] | -0.62 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[C1orf56]] | -0.61 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[ZMYM5]] | -0.60 | -0.66 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPRU]] | B | PTPRU activity raises TTLL12's level | lines that do not express PTPRU (7) vs lines expressing it (43) | 1.30× lower at baseline in the lines without PTPRU | 0.069 | ⚠ within organs, on part of the lines; also absent: FBXO16, RNF144A |
| [[HDAC6]] | B | HDAC6 activity lowers TTLL12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.497). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-22.2, -27.2); signed map (-27.2, -44.3). **Vector** length 92.7, 21.5% of its response variance represented; |z| ≥ 3 in 1,137 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.7 | +8.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.7 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +5.6 | +6.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +5.4 | +10.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +2.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.3 | +2.3 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.2 | +1.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +2.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.8 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -15.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -8.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.3 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -0.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -2.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:43,166,622-43,187,134 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0153 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14166](https://www.uniprot.org/uniprotkb/Q14166) (Tubulin--tyrosine ligase-like protein 12):

> Negatively regulates post-translational modifications of tubulin, including detyrosination of the C-terminus and polyglutamylation of glutamate residues. Also, indirectly promotes histone H4 trimethylation at 'Lys-20' (H4K20me3). Probably by controlling tubulin and/or histone H4 post-translational modifications, plays a role in mitosis and in maintaining chromosome number stability. During RNA virus-mediated infection, acts as a negative regulator of the RIG-I pathway by preventing MAVS binding …

**Summary**, from NCBI Gene [23170](https://www.ncbi.nlm.nih.gov/gene/23170):

> Enables histone H4K20me2 reader activity. Involved in negative regulation of type I interferon-mediated signaling pathway and regulation of mitotic cell cycle. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28974) · Entrez [23170](https://www.ncbi.nlm.nih.gov/gene/23170) · UniProt [Q14166](https://www.uniprot.org/uniprotkb/Q14166) · Ensembl [ENSG00000100304](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100304)

## Data

Gene col 1920: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1920); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1920, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1920]; `tensor/DDL_lfc|DDL_z.npy` [1920]; `embed/gene_vectors.npy` [1920]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1920 or target_col == 1920). Every well: [[TTLL12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
