---
symbol: "PTGFRN"
type: "gene"
col: 5528
ensembl_id: "ENSG00000134247"
name: "prostaglandin F2 receptor inhibitor"
location: "1p13.1"
module: 29
arm: "+"
pooled_cpm: 25.45
n_lines_expressing: 42
n_dd_up: 4
n_dd_down: 20
n_dd_up_clean: 0
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 11
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# PTGFRN

*prostaglandin F2 receptor inhibitor* — 1p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.95× (z +9.5, q 1e-18, up in 21 of 29 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HS-578T 3.45×, HEC-1-A 2.18×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 3.56×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 10.3×).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.410× (z -18.7, q 0e+00, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPSA]] (+0.68, fdr 7e-06), [[FKBP9]] (+0.67, fdr 7e-06), [[CAPRIN1]] (+0.66, fdr 7e-06); moves opposite to [[INAFM1]] (-0.69, fdr 7e-06), [[UBE2B]] (-0.63, fdr 2e-05), [[CROCCP2-1]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PDE3B]] → it (grade B ⚠); 11 go from it, the strongest it → [[TMEM64]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5528.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (HS-578T 3.45×, HEC-1-A 2.18×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HS-578T 3.56×; ⚠ toxic; transcription drop); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 10.3×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.95×** | +9.5 | 1e-18 | 21/29 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.9 | 1e-12 | 26/34 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.55×** | +6.0 | 3e-07 | 19/32 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.5 | 0.060 | 17/38 (HS-578T, RPMI-7951, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.4 | 0.070 | 12/40 (SW480, Panc 03.27, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.4 | 0.070 | 11/40 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | 1.49× | +3.1 | 0.16 | 14/40 (BT-474, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5528.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.410×** | -18.7 | 0e+00 | 34/40 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.365×** | -15.0 | 0e+00 | 32/40 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.397×** | -13.7 | 2e-40 | 33/40 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.411×** | -13.2 | 1e-37 | 33/39 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -12.3 | 6e-33 | 31/39 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.548×** | -8.9 | 4e-17 | 30/40 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.556×** | -8.7 | 2e-16 | 29/40 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.619×** | -7.1 | 8e-11 | 24/39 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -7.0 | 1e-10 | 26/40 (LoVo, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.628×** | -6.9 | 3e-10 | 27/40 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.623×** | -6.8 | 7e-10 | 29/40 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.891× | -5.7 | 6e-07 | 4/40 (A549, HepG2/C3A, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.720×** | -4.7 | 1e-04 | 20/39 (A-172, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -4.6 | 1e-04 | 20/39 (HepG2/C3A, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.737×** | -4.5 | 2e-04 | 20/40 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.747×** | -4.3 | 6e-04 | 20/40 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.796×** | -3.4 | 0.024 | 17/40 (NCI-H460, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5528. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 32.0 | 0 | 15 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0671× (z -31.8) |
| [[C32 (line)]] | wt | 72.4 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0469× (z -26.1) |
| [[RKO (line)]] | wt | 51.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0252× (z -30.0) |
| [[SW480 (line)]] | alt | 25.9 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -15.4) |
| [[A-172 (line)]] | wt | 21.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.6) |
| [[C-33 A (line)]] | alt | 25.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.147× (z -10.8) |
| [[LoVo (line)]] | wt | 26.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -20.9) |
| [[LS 180 (line)]] | wt | 47.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -11.2) |
| [[A498 (line)]] | wt | 76.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -12.6) |
| [[HepG2_C3A (line)]] | wt | 27.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.167× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.1) |
| [[HOP62 (line)]] | alt | 13.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 23.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -9.2) |
| [[SHP-77 (line)]] | alt | 47.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.123× (z -15.2) |
| [[A549 (line)]] | wt | 16.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -10.3) |
| [[COLO 205 (line)]] | alt | 21.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 53.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.333× (z -12.4) |
| [[HS-578T (line)]] | alt | 72.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0583× (z -14.6) |
| [[SW48 (line)]] | wt | 45.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.209× (z -10.2) |
| [[A-427 (line)]] | wt | 11.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.0) |
| [[AN3 CA (line)]] | alt | 63.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0973× (z -11.7) |
| [[BT-474 (line)]] | alt | 38.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +8.8) | — |
| [[KATO III (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.155× (z -12.9) |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0994× (z -10.6) |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -9.0) |
| [[SNU-423 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -10.3) |
| [[SW1417 (line)]] | alt | 22.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.258× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.96 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.26 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.34 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5528), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPSA]] | +0.68 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[FKBP9]] | +0.67 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CAPRIN1]] | +0.66 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SEPHS1]] | +0.65 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[NUP205]] | +0.64 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[PAICS]] | +0.64 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[GMPS]] | +0.63 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[MACROH2A1]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[IPO5]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[GPC4]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.62 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[CELSR2]] | +0.62 | +0.63 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INAFM1]] | -0.69 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[UBE2B]] | -0.63 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[CROCCP2-1]] | -0.62 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[ATF4]] | -0.62 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[JUND]] | -0.59 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.59 | -0.48 / -0.61 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RSPH3]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.59 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[GGNBP2]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[KRT10]] ⚠ | -0.58 | -0.53 / -0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[GABARAPL2]] | -0.58 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[POLR2J4]] | -0.58 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SAT2]] | -0.58 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[SIRT6]] | -0.58 | -0.45 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE3B]] | B | PDE3B activity strengthens PTGFRN's drug response | lines that do not express PDE3B (16) vs lines expressing it (24) | the lines without PDE3B respond 0.75× as strongly (z diff +1.48); strongest at Homoharringtonine 5 µM: 0.55x vs 0.32x (z diff +3.8) | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4; target measured in part of the lines; artifact flags |
| [[TRABD2B]] | B | TRABD2B activity raises PTGFRN's level | lines that do not express TRABD2B (19) vs lines expressing it (31) | 1.85× lower at baseline in the lines without TRABD2B | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM110B, ULK2, COL4A4 |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM64]] | B | PTGFRN activity lowers TMEM64's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.27× higher at baseline in the lines without PTGFRN | 0.031 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[IPO5]] | B | PTGFRN activity lowers IPO5's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.19× higher at baseline in the lines without PTGFRN | 0.051 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[TRABD2B]] | B | PTGFRN activity raises TRABD2B's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 3.06× lower at baseline in the lines without PTGFRN | 0.064 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[POGLUT3]] | B | PTGFRN activity lowers POGLUT3's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.91× higher at baseline in the lines without PTGFRN | 0.071 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[TMEM19]] | B | PTGFRN activity lowers TMEM19's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.35× higher at baseline in the lines without PTGFRN | 0.071 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | PTGFRN activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express PTGFRN (8) vs lines expressing it (40) | the lines without PTGFRN: 0.84× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[RPL6]] | B | PTGFRN activity lowers RPL6's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.12× higher at baseline in the lines without PTGFRN | 0.076 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[FRAS1]] | B | PTGFRN activity raises FRAS1's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 3.07× lower at baseline in the lines without PTGFRN | 0.091 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| cells under [[Torkinib (drug)]] 5 µM | B | PTGFRN activity raises the cells' numbers under Torkinib 5 µM (protects the cells) | lines that do not express PTGFRN (8) vs lines expressing it (40) | the lines without PTGFRN: 0.81× the cells of the other lines | 0.093 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[PPP2R1B]] | B | PTGFRN activity lowers PPP2R1B's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.23× higher at baseline in the lines without PTGFRN | 0.095 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |
| [[DUSP18]] | B | PTGFRN activity lowers DUSP18's level | lines that do not express PTGFRN (8) vs lines expressing it (42) | 1.24× higher at baseline in the lines without PTGFRN | 0.098 | ⚠ within organs, on part of the lines; also absent: MLLT3, FHIT |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-25.9, -25.7); signed map (-21.6, -42.4). **Vector** length 104, 26.0% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | +8.1 | +3.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.7 | +3.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | +1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | -0.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -13.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.0 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -1.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | prostaglandin F2 receptor inhibitor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p13.1 — chr1:116,909,916-116,990,353 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FPRP, EWI-F, CD9P-1, FLJ11001, KIAA1436, SMAP-6, CD315 |
| Gene groups (HGNC) | CD molecules; V-set domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2B2](https://www.uniprot.org/uniprotkb/Q9P2B2) (Prostaglandin F2 receptor negative regulator):

> Inhibits the binding of prostaglandin F2-alpha (PGF2-alpha) to its specific FP receptor, by decreasing the receptor number rather than the affinity constant. Functional coupling with the prostaglandin F2-alpha receptor seems to occur (By similarity). In myoblasts, associates with tetraspanins CD9 and CD81 to prevent myotube fusion during muscle regeneration (By similarity).

**Summary**, from NCBI Gene [5738](https://www.ncbi.nlm.nih.gov/gene/5738):

> Predicted to be involved in myoblast fusion involved in skeletal muscle regeneration. Predicted to act upstream of or within lipid droplet organization. Located in cell surface. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9601](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9601) · Entrez [5738](https://www.ncbi.nlm.nih.gov/gene/5738) · UniProt [Q9P2B2](https://www.uniprot.org/uniprotkb/Q9P2B2) · Ensembl [ENSG00000134247](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134247)

## Data

Gene col 5528: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5528); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5528, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5528]; `tensor/DDL_lfc|DDL_z.npy` [5528]; `embed/gene_vectors.npy` [5528]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5528 or target_col == 5528). Every well: [[PTGFRN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTGFRN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
