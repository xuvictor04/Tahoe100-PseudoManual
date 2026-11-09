---
symbol: "ARHGAP22"
type: "gene"
col: 4922
ensembl_id: "ENSG00000128805"
name: "Rho GTPase activating protein 22"
location: "10q11.22-q11.23"
module: 110
arm: "+"
pooled_cpm: 69.76
n_lines_expressing: 29
n_dd_up: 13
n_dd_down: 39
n_dd_up_clean: 9
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 40
direction_downstream: 37
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ARHGAP22

*Rho GTPase activating protein 22* — 10q11.22-q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.46× (z +5.2, q 1e-04, up in 17 of 27 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM: 1.25× (z +4.3, q 0.004, up in 17 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 39 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.247× (z -26.4, q 0e+00, down in 27 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPSAP52]] (+0.76, fdr 7e-06), [[SHANK1]] (+0.74, fdr 7e-06), [[CORO2B]] (+0.70, fdr 7e-06); moves opposite to [[MBNL2]] (-0.54, fdr 2e-05), [[ALDH3B1]] (-0.52, fdr 3e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[ARHGAP31]] → it (grade B ⚠); 37 go from it, the strongest it → [[HMGA2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.46×** | +5.2 | 1e-04 | 17/27 (PANC-1, SW 900, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +4.9 | 3e-04 | 18/26 (SW 900, PANC-1, …) | rises with dose |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **1.25×** | +4.3 | 0.004 | 17/27 (A-172, NCI-H460, …) | all doses, flat | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.35×** | +4.1 | 0.005 | 17/27 (NCI-H1792, NCI-H23, …) | all doses, flat | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.005 | 17/26 (PANC-1, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.014 | 13/28 (PANC-1, SW 900, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.015 | 13/27 (PANC-1, A549, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.32×** | +3.6 | 0.020 | 14/27 (RKO, PANC-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.034 | 13/27 (PANC-1, SW 900, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.28×** | +3.4 | 0.040 | 7/27 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | **1.30×** | +3.3 | 0.048 | 10/27 (HEC-1-A, NCI-H460, …) | all doses, flat | position effect removed |
| [[Naproxen (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.068 | 11/27 (RPMI-7951, A549, …) | all doses, flat | position effect removed |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.094 | 12/27 (A498, CHP-212, …) | all doses, flat | position effect removed |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.10 | 11/27 (SNU-423, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 39 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.247×** | -26.4 | 0e+00 | 27/27 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.464×** | -14.5 | 6e-45 | 24/27 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.327×** | -13.9 | 8e-42 | 26/27 (RKO, A-427, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.388×** | -12.7 | 2e-34 | 26/27 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.392×** | -12.5 | 9e-34 | 23/27 (RKO, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.393×** | -12.5 | 9e-34 | 24/27 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -10.8 | 2e-25 | 23/27 (RKO, HS-578T, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -9.0 | 1e-17 | 23/26 (NCI-H23, HOP62, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.534×** | -8.4 | 4e-15 | 20/27 (RKO, HOP62, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.551×** | -7.9 | 1e-13 | 22/27 (RKO, HOP62, …) | rises with dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.566×** | -7.1 | 8e-11 | 21/27 (RKO, HOP62, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.606×** | -6.7 | 1e-09 | 21/27 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.627×** | -6.2 | 2e-08 | 17/27 (RKO, HOP62, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.382×** | -6.0 | 8e-08 | 20/26 (RKO, SW48, …) | top dose only | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.397×** | -5.8 | 3e-07 | 23/28 (RKO, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.668×** | -5.7 | 4e-07 | 20/29 (RKO, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.661×** | -5.5 | 1e-06 | 19/28 (RKO, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.720×** | -5.3 | 3e-06 | 16/27 (RKO, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.704×** | -5.0 | 1e-05 | 17/28 (RKO, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.675×** | -4.9 | 2e-05 | 16/27 (RKO, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 932 | 0 | 35 (13 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0280× (z -41.6) |
| [[HOP62 (line)]] | alt | 275 | 0 | 28 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0349× (z -35.7) |
| [[HS-578T (line)]] | alt | 201 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -26.4) |
| [[SNU-423 (line)]] | alt | 224 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -17.6) |
| [[H4 (line)]] | wt | 230 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -18.5) |
| [[NCI-H1792 (line)]] | alt | 174 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -24.7) |
| [[C32 (line)]] | wt | 40.9 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -16.7) |
| [[hTERT-HPNE (line)]] | wt | 307 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0594× (z -26.3) |
| [[RPMI-7951 (line)]] | alt | 134 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -22.5) |
| [[A549 (line)]] | wt | 66.3 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -22.6) |
| [[NCI-H23 (line)]] | alt | 70.8 | 0 | 7 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0384× (z -26.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.188× (z -20.7) |
| [[LOX-IMVI (line)]] | wt | 80.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -32.3) |
| [[NCI-H460 (line)]] | wt | 25.6 | 2 (1 ⚠) | 4 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.72× (z +10.2) ⚠ unreliable plate only · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -14.9) |
| [[SW48 (line)]] | wt | 95.1 | 1 (1 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.40× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~68% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~86% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.399× (z -10.3) |
| [[A-172 (line)]] | wt | 74.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.0) |
| [[A498 (line)]] | wt | 72.1 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -17.2) |
| [[PANC-1 (line)]] | alt | 37.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 50.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -17.2) |
| [[SW 1088 (line)]] | alt | 161 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0818× (z -13.0) |
| [[A-427 (line)]] | wt | 19.2 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0534× (z -18.4) |
| [[HEC-1-A (line)]] | alt | 36.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 61.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -20.5) |
| [[Panc 03.27 (line)]] | alt | 49.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -12.9) |
| [[SW 900 (line)]] | alt | 36.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -10.7) |
| [[CHP-212 (line)]] | wt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -13.0) |
| [[AN3 CA (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.33 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.25 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.89 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.09 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.63 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.93 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.26 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.58 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSAP52]] | +0.76 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[SHANK1]] | +0.74 | +0.75 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CORO2B]] | +0.70 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[RFX8]] | +0.69 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[KIAA1549L]] | +0.68 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[INSYN2B]] | +0.68 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LINC02454]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[TM4SF19]] | +0.67 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[SPOCD1]] | +0.66 | +0.68 / +0.57 | both halves | 1e-05 | STRING 415 |
| [[HS3ST3A1]] | +0.66 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[EFL1]] | +0.66 | +0.63 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL2]] | -0.54 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[ALDH3B1]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 14, C 26. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP31]] | B | ARHGAP31 activity raises ARHGAP22's level | lines that do not express ARHGAP31 (10) vs lines expressing it (40) | 5.92× lower at baseline in the lines without ARHGAP31 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000236230, ROBO3, KIRREL1 |
| [[SERPINE1]] | B | SERPINE1 activity raises ARHGAP22's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 3.48× lower at baseline in the lines without SERPINE1 | 0.026 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[CLDN14-AS1]] | B | CLDN14-AS1 activity raises ARHGAP22's level | lines that do not express CLDN14-AS1 (16) vs lines expressing it (34) | 3.72× lower at baseline in the lines without CLDN14-AS1 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, ENSG00000289526, TMEM158 |
| [[APCDD1L]] | B | APCDD1L activity raises ARHGAP22's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 4.24× lower at baseline in the lines without APCDD1L | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1 |
| [[GPR68]] | B | GPR68 activity raises ARHGAP22's level | lines that do not express GPR68 (16) vs lines expressing it (34) | 3.10× lower at baseline in the lines without GPR68 | 0.037 | ⚠ within organs, on part of the lines; also absent: ELOVL4, CPE, NOTCH3; maybe low, not absent |
| [[UBASH3B]] | B | UBASH3B activity raises ARHGAP22's level | lines that do not express UBASH3B (7) vs lines expressing it (43) | 3.71× lower at baseline in the lines without UBASH3B | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000284969, CD59, MAMLD1 |
| [[SYNDIG1]] | B | SYNDIG1 activity strengthens ARHGAP22's drug response | lines that do not express SYNDIG1 (14) vs lines expressing it (13) | the lines without SYNDIG1 respond 0.79× as strongly (z diff +1.75); strongest at Panobinostat 5 µM: 0.47x vs 0.24x (z diff +4.6) | 0.049 | ⚠ within organs, on part of the lines; also absent: PXDN, LINC01411, SPOCK1; target measured in part of the lines; artifact flags |
| [[C13orf46]] | B | C13orf46 activity raises ARHGAP22's level | lines that do not express C13orf46 (11) vs lines expressing it (39) | 3.16× lower at baseline in the lines without C13orf46 | 0.057 | ⚠ within organs, on part of the lines; also absent: RASA3, COL27A1, PRR5L |
| [[HRH1]] | B | HRH1 activity raises ARHGAP22's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.34× lower at baseline in the lines without HRH1 | 0.057 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[EVC2]] | B | EVC2 activity raises ARHGAP22's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 3.58× lower at baseline in the lines without EVC2 | 0.059 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7 |
| [[RAI14]] | B | RAI14 activity raises ARHGAP22's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 4.85× lower at baseline in the lines without RAI14 | 0.072 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[EVC]] | B | EVC activity raises ARHGAP22's level | lines that do not express EVC (13) vs lines expressing it (37) | 4.25× lower at baseline in the lines without EVC | 0.072 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: RNF150, PYGO1, EHD3 |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 16, C 21. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGA2]] | B | ARHGAP22 activity raises HMGA2's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 3.21× lower at baseline in the lines without ARHGAP22 | 0.022 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[HRH1]] | B | ARHGAP22 activity raises HRH1's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.34× lower at baseline in the lines without ARHGAP22 | 0.027 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[UBASH3B]] | B | ARHGAP22 activity raises UBASH3B's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without ARHGAP22 | 0.027 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[EVC]] | B | ARHGAP22 activity raises EVC's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 3.60× lower at baseline in the lines without ARHGAP22 | 0.034 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[RAI14]] | B | ARHGAP22 activity raises RAI14's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.92× lower at baseline in the lines without ARHGAP22 | 0.038 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[ARHGAP31]] | B | ARHGAP22 activity raises ARHGAP31's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 2.92× lower at baseline in the lines without ARHGAP22 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[GSTO1]] | B | ARHGAP22 activity raises GSTO1's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.48× lower at baseline in the lines without ARHGAP22 | 0.049 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[BLZF2P]] | B | ARHGAP22 activity raises BLZF2P's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without ARHGAP22 | 0.058 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[PHC2]] | B | ARHGAP22 activity raises PHC2's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.67× lower at baseline in the lines without ARHGAP22 | 0.074 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[ACP7]] | B | ARHGAP22 activity raises ACP7's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.63× lower at baseline in the lines without ARHGAP22 | 0.078 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[C13orf46]] | B | ARHGAP22 activity raises C13orf46's level | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | 1.53× lower at baseline in the lines without ARHGAP22 | 0.079 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2 |
| [[EFL1]] | B | ARHGAP22 activity strengthens EFL1's drug response | lines that do not express ARHGAP22 (21) vs lines expressing it (29) | the lines without ARHGAP22 respond 0.75× as strongly (z diff +1.51); strongest at Idarubicin (hydrochloride) 5 µM: 0.64x vs 0.44x (z diff +3.0) | 0.089 | ⚠ within organs, on part of the lines; also absent: FAT4, TSHZ3, COL4A2; artifact flags |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.8, 11.3); signed map (15.0, 49.5). **Vector** length 121, 39.7% of its response variance represented; |z| ≥ 3 in 1,128 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.0 | +3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.9 | +4.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +3.8 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.8 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.5 | +3.0 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.1 | +2.6 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.4 | -5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -5.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.3 | -4.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.1 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | Rho GTPase activating protein 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.22-q11.23 — chr10:48,446,036-48,656,265 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RhoGAP2 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Rho GTPase activating proteins |
| Reactome | 6 pathways, smallest: RHOA GTPase cycle; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z5H3](https://www.uniprot.org/uniprotkb/Q7Z5H3) (Rho GTPase-activating protein 22):

> Rho GTPase-activating protein involved in the signal transduction pathway that regulates endothelial cell capillary tube formation during angiogenesis. Acts as a GTPase activator for the RAC1 by converting it to an inactive GDP-bound state. Inhibits RAC1-dependent lamellipodia formation. May also play a role in transcription regulation via its interaction with VEZF1, by regulating activity of the endothelin-1 (EDN1) promoter (By similarity).

**Summary**, from NCBI Gene [58504](https://www.ncbi.nlm.nih.gov/gene/58504):

> This gene encodes a member of the GTPase activating protein family which activates a GTPase belonging to the RAS superfamily of small GTP-binding proteins. The encoded protein is insulin-responsive, is dependent on the kinase Akt and requires the Akt-dependent 14-3-3 binding protein which binds sequentially to two serine residues. The result of these interactions is regulation of cell motility. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:30320](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30320) · Entrez [58504](https://www.ncbi.nlm.nih.gov/gene/58504) · UniProt [Q7Z5H3](https://www.uniprot.org/uniprotkb/Q7Z5H3) · Ensembl [ENSG00000128805](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128805)

## Data

Gene col 4922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4922); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4922]; `tensor/DDL_lfc|DDL_z.npy` [4922]; `embed/gene_vectors.npy` [4922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4922 or target_col == 4922). Every well: [[ARHGAP22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGAP22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
