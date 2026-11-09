---
symbol: "RASA3"
type: "gene"
col: 11763
ensembl_id: "ENSG00000185989"
name: "RAS p21 protein activator 3"
location: "13q34"
module: 84
arm: "+"
pooled_cpm: 111.11
n_lines_expressing: 41
n_dd_up: 0
n_dd_down: 57
n_dd_up_clean: 0
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 19
direction_downstream: 14
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# RASA3

*RAS p21 protein activator 3* — 13q34

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 7.39×, A-172 3.31×, CHP-212 3.58×, Panc 03.27 2.03×); [[Harringtonine (drug)]] 5 µM in 1 line (J82 4.65×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 2.64×; ⚠ cell-cycle shift, explains ~28% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 2.53×).
> Pooled over the cell lines (median), lowered significantly by 57 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.564× (z -12.3, q 8e-32, down in 34 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C13orf46]] (+0.79, fdr 7e-06, ⚠ read-through risk), [[RAC2]] (+0.78, fdr 7e-06), [[STX1A]] (+0.78, fdr 7e-06), [[KCNN4]] (+0.74, fdr 7e-06); moves opposite to [[C1RL]] (-0.60, fdr 4e-05), [[MR1]] (-0.55, fdr 3e-04).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[CDH13]] → it (grade B ⚠); 14 go from it, the strongest it → [[STK32B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11763.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 7.39×, A-172 3.31×, CHP-212 3.58×, Panc 03.27 2.03×); [[Harringtonine (drug)]] 5 µM in 1 line (J82 4.65×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (KATO III 2.64×; ⚠ cell-cycle shift, explains ~28% of this change); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (KATO III 2.53×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.25× | +3.4 | 0.35 | 17/39 (SW480, CHP-212, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | 1.59× | +3.1 | 0.49 | 17/39 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 58 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 57 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11763.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.564×** | -12.3 | 8e-32 | 34/40 (C32, HS-578T, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.435×** | -11.7 | 3e-29 | 28/34 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.473×** | -10.5 | 1e-23 | 34/39 (RPMI-7951, C32, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.513×** | -10.1 | 6e-22 | 32/40 (C32, HOP62, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.504×** | -9.6 | 8e-20 | 35/38 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.681×** | -8.2 | 2e-14 | 25/39 (RPMI-7951, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.584×** | -8.1 | 3e-14 | 32/40 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.587×** | -8.1 | 5e-14 | 26/39 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.565×** | -8.0 | 6e-14 | 30/41 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.568×** | -7.9 | 1e-13 | 31/39 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.561×** | -7.9 | 1e-13 | 28/36 (RKO, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.571×** | -7.9 | 2e-13 | 26/39 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.654×** | -7.7 | 6e-13 | 34/39 (AsPC-1, HEC-1-A, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.628×** | -7.4 | 4e-12 | 31/41 (HEC-1-A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.673×** | -7.1 | 5e-11 | 31/39 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.720×** | -6.8 | 4e-10 | 28/39 (AsPC-1, HEC-1-A, …) | all doses, flat | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.640×** | -6.8 | 5e-10 | 22/39 (SNU-1, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.653×** | -6.5 | 2e-09 | 33/40 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.634×** | -6.2 | 1e-08 | 31/39 (AsPC-1, C32, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11763. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 286 | 0 | 22 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -17.9) |
| [[HEC-1-A (line)]] | alt | 173 | 0 | 18 (2 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.259× (z -17.0) |
| [[NCI-H460 (line)]] | wt | 93.1 | 0 | 16 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.177× (z -18.3) |
| [[AsPC-1 (line)]] | alt | 232 | 0 | 15 (2 ⚠) | — | [[Trametinib (drug)]] 0.5 µM 0.233× (z -16.5) |
| [[HOP62 (line)]] | alt | 390 | 0 | 14 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -13.9) |
| [[A-172 (line)]] | wt | 164 | 1 | 10 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +15.9) | [[Trametinib (drug)]] 5 µM 0.233× (z -13.8) |
| [[H4 (line)]] | wt | 146 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -14.3) |
| [[J82 (line)]] | alt | 182 | 2 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.39× (z +29.5) | [[Dinaciclib (drug)]] 0.5 µM 0.342× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Trametinib (drug)]] 0.5 µM 0.442× (z -10.3) |
| [[SK-MEL-2 (line)]] | alt | 77.2 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.9) |
| [[HS-578T (line)]] | alt | 147 | 0 | 9 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.6) |
| [[LOX-IMVI (line)]] | wt | 183 | 0 | 9 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.236× (z -11.9) |
| [[RPMI-7951 (line)]] | alt | 201 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -20.2) |
| [[CFPAC-1 (line)]] | alt | 105 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -11.8) |
| [[KATO III (line)]] | alt | 85.6 | 2 (1 ⚠) | 4 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.64× (z +9.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.53× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -9.6) |
| [[SNU-1 (line)]] | wt | 134 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -12.9) |
| [[SW480 (line)]] | alt | 178 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.56× (z +8.8) | [[Harringtonine (drug)]] 5 µM 0.269× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 200 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.3) |
| [[PANC-1 (line)]] | alt | 150 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.2) |
| [[Hs 766T (line)]] | wt | 225 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.255× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.9) |
| [[LS 180 (line)]] | wt | 52.2 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -12.5) |
| [[RKO (line)]] | wt | 103 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.103× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -10.9) |
| [[LoVo (line)]] | wt | 42.5 | 1 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -11.4) |
| [[NCI-H23 (line)]] | alt | 33.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 89.8 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 70.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.4) |
| [[A498 (line)]] | wt | 83.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -14.0) |
| [[CHP-212 (line)]] | wt | 75.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 52.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -8.8) |
| [[SNU-423 (line)]] | alt | 146 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -9.9) |
| [[A-427 (line)]] | wt | 21.9 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 32.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 16.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 81.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 86.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 97.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.25 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 62.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 88.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11763), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C13orf46]] | +0.79 | +0.73 / +0.77 | both halves | 7e-06 | ⚠ **readthrough risk**: C13orf46 lies 3.7 kb 3′ of this gene on the same strand (can correlate by spillover, not regulation) |
| [[RAC2]] | +0.78 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[STX1A]] | +0.78 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[KCNN4]] | +0.74 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[ZFYVE28]] | +0.73 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.71 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[SEMA7A]] | +0.68 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[PHC2]] | +0.68 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[KIF21B]] | +0.68 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.67 | +0.65 / +0.55 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.67 | +0.67 / +0.55 | both halves | 1e-05 | same gene group; STRING 622 |
| [[COL13A1]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[SLCO4A1]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C1RL]] | -0.60 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[MR1]] | -0.55 | -0.57 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 18, C 1. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDH13]] | B | CDH13 activity raises RASA3's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without CDH13 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032 |
| [[RFX8]] | B | RFX8 activity raises RASA3's level | lines that do not express RFX8 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without RFX8 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS15, IRAG2, CARMN |
| [[NLRP1]] | B | NLRP1 activity raises RASA3's level | lines that do not express NLRP1 (21) vs lines expressing it (29) | 3.05× lower at baseline in the lines without NLRP1 | 0.008 | ⚠ within organs, on part of the lines; also absent: EVA1A, NRP2, SLFN12 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises RASA3's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.43× lower at baseline in the lines without HS3ST3A1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[RPSAP52]] | B | RPSAP52 activity raises RASA3's level | lines that do not express RPSAP52 (20) vs lines expressing it (30) | 2.72× lower at baseline in the lines without RPSAP52 | 0.010 | ⚠ within organs, on part of the lines; also absent: APOBEC3G, LINC00702, PLAT; maybe low, not absent |
| [[ZEB1]] | B | ZEB1 activity raises RASA3's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without ZEB1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[VAT1L]] | B | VAT1L activity raises RASA3's level | lines that do not express VAT1L (23) vs lines expressing it (27) | 1.18× lower at baseline in the lines without VAT1L | 0.040 | ⚠ within organs, on part of the lines; also absent: RBM20, ENSG00000242880, CHST8; maybe low, not absent |
| [[SERPINE1]] | B | SERPINE1 activity raises RASA3's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 2.13× lower at baseline in the lines without SERPINE1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[MGP]] | B | MGP activity raises RASA3's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without MGP | 0.054 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1 |
| [[STK32B]] | B | STK32B activity raises RASA3's level | lines that do not express STK32B (24) vs lines expressing it (26) | 1.63× lower at baseline in the lines without STK32B | 0.055 | ⚠ within organs, on part of the lines; also absent: HTR7, CA8, KCNJ6 |
| [[MAP2K1]] | B | MAP2K1 activity raises RASA3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 10.1% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds |
| [[STC1]] | B | STC1 activity raises RASA3's level | lines that do not express STC1 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without STC1 | 0.063 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 13, C 1. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK32B]] | B | RASA3 activity raises STK32B's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.00× lower at baseline in the lines without RASA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[PMP22]] | B | RASA3 activity raises PMP22's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.99× lower at baseline in the lines without RASA3 | 0.031 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[NLRP1]] | B | RASA3 activity raises NLRP1's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 4.60× lower at baseline in the lines without RASA3 | 0.041 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[STRN3]] | B | RASA3 activity lowers STRN3's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.61× higher at baseline in the lines without RASA3 | 0.044 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[CAPRIN2]] | B | RASA3 activity raises CAPRIN2's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.81× lower at baseline in the lines without RASA3 | 0.067 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[SHC3]] | B | RASA3 activity raises SHC3's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.72× lower at baseline in the lines without RASA3 | 0.070 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[PPFIBP1]] | B | RASA3 activity raises PPFIBP1's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.79× lower at baseline in the lines without RASA3 | 0.072 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[NAV2]] | B | RASA3 activity raises NAV2's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 3.81× lower at baseline in the lines without RASA3 | 0.074 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[MICAL2]] | B | RASA3 activity raises MICAL2's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.65× lower at baseline in the lines without RASA3 | 0.077 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[HIVEP3]] | B | RASA3 activity raises HIVEP3's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 2.46× lower at baseline in the lines without RASA3 | 0.078 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[PARVB]] | B | RASA3 activity raises PARVB's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.90× lower at baseline in the lines without RASA3 | 0.083 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |
| [[STX1A]] | B | RASA3 activity raises STX1A's level | lines that do not express RASA3 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without RASA3 | 0.086 | ⚠ within organs, on part of the lines; also absent: C13orf46, PRR5L, LINC02100; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.1, 2.1); signed map (1.3, 49.1). **Vector** length 141, 48.6% of its response variance represented; |z| ≥ 3 in 1,548 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.7 | +2.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +8.4 | +2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +8.2 | -0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.4 | +0.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.8 | +0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.8 | +0.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | +2.4 | +0.9 |
|  | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | +2.3 | -0.0 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -9.5 | -7.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.3 | -7.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.4 | -7.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.3 | -6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -7.9 | -8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.9 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | RAS p21 protein activator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:113,977,783-114,132,623 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAP1IP4BP, GAPIII |
| Gene groups (HGNC) | Pleckstrin homology domain containing; C2 and RasGAP domain containing |
| Reactome | 4 pathways, smallest: Regulation of RAS by GAPs; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14644](https://www.uniprot.org/uniprotkb/Q14644) (Ras GTPase-activating protein 3):

> Inhibitory regulator of the Ras-cyclic AMP pathway. Binds inositol tetrakisphosphate (IP4) with high affinity. Might be a specific IP4 receptor.

**Summary**, from NCBI Gene [22821](https://www.ncbi.nlm.nih.gov/gene/22821):

> This gene encodes a protein that binds inositol 1,3,4,5-tetrakisphosphate and stimulates the GTPase activity of Ras p21. This protein functions as a negative regulator of the Ras signalling pathway. It is localized to the cell membrane via a pleckstrin homology (PH) domain in the C-terminal region. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:20331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20331) · Entrez [22821](https://www.ncbi.nlm.nih.gov/gene/22821) · UniProt [Q14644](https://www.uniprot.org/uniprotkb/Q14644) · Ensembl [ENSG00000185989](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185989)

## Data

Gene col 11763: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11763); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11763, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11763]; `tensor/DDL_lfc|DDL_z.npy` [11763]; `embed/gene_vectors.npy` [11763]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11763 or target_col == 11763). Every well: [[RASA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RASA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
