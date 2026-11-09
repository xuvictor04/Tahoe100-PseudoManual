---
symbol: "MINDY4"
type: "gene"
col: 2726
ensembl_id: "ENSG00000106125"
name: "MINDY lysine 48 deubiquitinase 4"
location: "7p14.3"
module: 4
arm: "+"
pooled_cpm: 12.43
n_lines_expressing: 45
n_dd_up: 16
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# MINDY4

*MINDY lysine 48 deubiquitinase 4* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.36× (z +10.9, q 4e-25, up in 35 of 42 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 2.08× (z +9.3, q 4e-18, up in 33 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.480× (z -13.2, q 6e-37, down in 38 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH8]] (+0.74, fdr 7e-06), [[CHCHD6]] (+0.72, fdr 7e-06), [[CSTPP1]] (+0.70, fdr 7e-06); moves opposite to [[SMIM14]] (-0.59, fdr 1e-05), [[HERPUD2]] (-0.59, fdr 2e-05), [[LNX2]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[SMO]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2726.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.36×** | +10.9 | 4e-25 | 35/42 (A-172, HOP62, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.08×** | +9.3 | 4e-18 | 33/43 (A-172, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.98×** | +8.7 | 8e-16 | 31/43 (A-172, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.89×** | +7.6 | 3e-12 | 30/42 (A-172, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.81×** | +7.5 | 6e-12 | 28/43 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.51×** | +5.2 | 2e-05 | 18/42 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.51×** | +5.1 | 3e-05 | 15/43 (A-172, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~65% of this change | **1.45×** | +4.6 | 4e-04 | 18/35 (SW480, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.0 | 0.004 | 19/41 (A-172, C32, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~94% of this change | **1.25×** | +4.0 | 0.004 | 18/43 (LoVo, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.005 | 9/40 (CFPAC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.46×** | +3.9 | 0.005 | 8/42 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.033 | 2/43 (A498, NCI-H2030) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.30×** | +3.3 | 0.035 | 6/43 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.038 | 5/41 (NCI-H460, HCT15, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.070 | 4/43 (A-172, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2726.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.480×** | -13.2 | 6e-37 | 38/41 (PANC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.573×** | -10.0 | 4e-21 | 28/42 (PANC-1, SK-MEL-2, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.507×** | -8.6 | 1e-15 | 25/40 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.527×** | -8.1 | 5e-14 | 29/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.623×** | -6.0 | 2e-07 | 21/41 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -5.8 | 7e-07 | 21/40 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.626×** | -5.7 | 8e-07 | 24/42 (LOX-IMVI, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.697×** | -4.6 | 3e-04 | 18/42 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~67% of this change | **0.720×** | -4.2 | 0.002 | 17/36 (NCI-H23, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.728×** | -3.9 | 0.006 | 12/21 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.739×** | -3.8 | 0.006 | 14/40 (COLO 205, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -3.5 | 0.023 | 17/43 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.767×** | -3.4 | 0.034 | 12/43 (KATO III, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.763×** | -3.3 | 0.039 | 17/40 (PANC-1, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.742×** | -3.1 | 0.080 | 7/43 (PANC-1, LS 180, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.64 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2726. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.7 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.8) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 25.3 | 0 | 4 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0685× (z -16.5) |
| [[LoVo (line)]] | wt | 8.47 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.154× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.1) |
| [[NCI-H2030 (line)]] | alt | 14.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.150× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.370× (z -8.9) |
| [[A-172 (line)]] | wt | 14.4 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.6× (z +13.0) | — |
| [[HEC-1-A (line)]] | alt | 18.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.0) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0749× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0550× (z -18.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.301× (z -9.5) |
| [[AN3 CA (line)]] | alt | 45.5 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0896× (z -10.1) |
| [[C-33 A (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -9.1) |
| [[H4 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -9.7) ⚠ cell-cycle shift, explains ~67% of this change |
| [[KATO III (line)]] | alt | 28.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.160× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 15.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.290× (z -10.8) |
| [[SW480 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.302× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.01 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2726), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH8]] | +0.74 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[CSTPP1]] | +0.70 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NAA25]] | +0.68 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SARS2]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[CDIN1]] | +0.67 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[TMEM161A]] | +0.66 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[SPATA5]] | +0.66 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[POP1]] | +0.65 | +0.67 / +0.59 | both halves | 7e-06 |  |
| [[VWA8]] | +0.65 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[HERC2]] | +0.64 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[HIBCH]] | +0.64 | +0.64 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[HERPUD2]] | -0.59 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[LNX2]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[CDK19]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[KPNB1-DT]] | -0.55 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[H2AZ1-DT]] | -0.54 | -0.41 / -0.35 | both halves | 1e-04 |  |
| [[UPK2]] | -0.54 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[RNF170]] | -0.53 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[TRAPPC6B]] | -0.53 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MINDY4's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMO]] | B | MINDY4 activity raises SMO's level | lines that do not express MINDY4 (5) vs lines expressing it (45) | 2.73× lower at baseline in the lines without MINDY4 | 0.068 | ⚠ within organs, on part of the lines; also absent: MPP4, DPH6-DT, CFAP58; maybe low, not absent |
| [[ANKRD23]] | B | MINDY4 activity raises ANKRD23's level | lines that do not express MINDY4 (5) vs lines expressing it (45) | 1.51× lower at baseline in the lines without MINDY4 | 0.072 | ⚠ within organs, on part of the lines; also absent: MPP4, DPH6-DT, CFAP58; maybe low, not absent |

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.635). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-9.3, -33.3); signed map (-12.6, -50.2). **Vector** length 88.9, 18.9% of its response variance represented; |z| ≥ 3 in 949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +8.5 | +10.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | +7.2 | +7.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.1 | +9.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | +1.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -13.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.6 | -5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | -4.2 | -10.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | MINDY lysine 48 deubiquitinase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,771,417-30,892,387 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22374; previously C7orf67, FAM188B |
| Gene groups (HGNC) | MINDY deubiquitinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4G0A6](https://www.uniprot.org/uniprotkb/Q4G0A6) (Probable ubiquitin carboxyl-terminal hydrolase MINDY-4):

> Probable hydrolase that can remove 'Lys-48'-linked conjugated ubiquitin from proteins.

**Summary**, from NCBI Gene [84182](https://www.ncbi.nlm.nih.gov/gene/84182):

> Predicted to enable K48-linked deubiquitinase activity. Predicted to be involved in protein K48-linked deubiquitination and proteolysis. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21916) · Entrez [84182](https://www.ncbi.nlm.nih.gov/gene/84182) · UniProt [Q4G0A6](https://www.uniprot.org/uniprotkb/Q4G0A6) · Ensembl [ENSG00000106125](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106125)

## Data

Gene col 2726: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2726); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2726, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2726]; `tensor/DDL_lfc|DDL_z.npy` [2726]; `embed/gene_vectors.npy` [2726]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2726 or target_col == 2726). Every well: [[MINDY4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINDY4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
