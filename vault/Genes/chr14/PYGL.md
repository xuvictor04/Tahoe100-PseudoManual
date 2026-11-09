---
symbol: "PYGL"
type: "gene"
col: 1975
ensembl_id: "ENSG00000100504"
name: "glycogen phosphorylase L"
location: "14q22.1"
module: 84
arm: "+"
pooled_cpm: 175.06
n_lines_expressing: 43
n_dd_up: 0
n_dd_down: 36
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 4
direction_downstream: 4
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# PYGL

*glycogen phosphorylase L* — 14q22.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 2.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.279× (z -35.6, q 0e+00, down in 40 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHD1L]] (+0.68, fdr 7e-06), [[TMEM255B]] (+0.65, fdr 7e-06), [[LRRC8C]] (+0.62, fdr 7e-06); moves opposite to [[ALDH3B1]] (-0.53, fdr 3e-05), [[TNS3]] (-0.48, fdr 4e-05), [[FIGN]] (-0.47, fdr 6e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TMEM158]] → it (grade B ⚠); 4 go from it, the strongest it → [[LRRC8C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1975.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 2.96×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | 1.17× | +4.5 | 0.005 | 12/41 (SW480, HepG2/C3A, …) | inconsistent across doses | position effect removed |
| [[Roxadustat (drug)]] 5 µM |  | 1.17× | +3.1 | 0.63 | 14/41 (PANC-1, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.279×** | -35.6 | 0e+00 | 40/41 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.298×** | -23.0 | 0e+00 | 40/41 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.327×** | -22.0 | 0e+00 | 40/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.358×** | -20.2 | 0e+00 | 39/41 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.374×** | -19.4 | 0e+00 | 40/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.403×** | -17.9 | 0e+00 | 36/41 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.417×** | -17.2 | 0e+00 | 38/41 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.423×** | -16.3 | 0e+00 | 37/40 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.439×** | -16.2 | 0e+00 | 40/41 (NCI-H460, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.472×** | -14.8 | 0e+00 | 38/41 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.494×** | -13.9 | 3e-42 | 36/41 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.552×** | -11.7 | 5e-30 | 29/41 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.641×** | -8.8 | 9e-17 | 33/41 (H4, PANC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -8.4 | 1e-15 | 28/42 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.741×** | -8.3 | 3e-15 | 28/41 (PANC-1, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.658×** | -8.2 | 7e-15 | 31/41 (SK-MEL-2, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.346×** | -8.1 | 2e-14 | 37/42 (NCI-H460, A-427, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 596 | 0 | 23 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0887× (z -41.5) |
| [[MIA PaCa-2 (line)]] | alt | 408 | 0 | 22 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -25.1) |
| [[C32 (line)]] | wt | 277 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -21.5) |
| [[PANC-1 (line)]] | alt | 148 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -29.4) |
| [[H4 (line)]] | wt | 244 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0775× (z -25.5) |
| [[A-172 (line)]] | wt | 146 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -25.9) |
| [[A549 (line)]] | wt | 305 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0897× (z -30.8) |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -19.7) |
| [[HOP62 (line)]] | alt | 189 | 0 | 14 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -20.8) |
| [[HS-578T (line)]] | alt | 146 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -18.9) |
| [[C-33 A (line)]] | alt | 270 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -24.2) |
| [[NCI-H1792 (line)]] | alt | 323 | 0 | 12 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 468 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -35.1) |
| [[Hs 766T (line)]] | wt | 281 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -29.3) |
| [[LOX-IMVI (line)]] | wt | 66.7 | 0 | 11 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -14.8) |
| [[NCI-H1573 (line)]] | alt | 304 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -24.0) |
| [[CFPAC-1 (line)]] | alt | 96.1 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.4) |
| [[SK-MEL-2 (line)]] | alt | 209 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -18.4) |
| [[SW480 (line)]] | alt | 128 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.353× (z -18.5) |
| [[RKO (line)]] | wt | 101 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -28.1) |
| [[SNU-1 (line)]] | wt | 94.6 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.0) |
| [[SNU-423 (line)]] | alt | 118 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -18.3) |
| [[SW48 (line)]] | wt | 179 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -23.2) |
| [[HEC-1-A (line)]] | alt | 55.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -15.4) |
| [[LoVo (line)]] | wt | 97.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -22.6) |
| [[NCI-H2030 (line)]] | alt | 475 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -23.7) |
| [[A-427 (line)]] | wt | 107 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -23.5) |
| [[SHP-77 (line)]] | alt | 114 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -13.3) |
| [[J82 (line)]] | alt | 141 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -20.2) |
| [[RPMI-7951 (line)]] | alt | 71.5 | 0 | 4 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -13.0) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.207× (z -11.7) |
| [[A498 (line)]] | wt | 105 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -18.3) |
| [[HT-29 (line)]] | alt | 57.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.96× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 97.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -14.9) |
| [[AN3 CA (line)]] | alt | 135 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -14.1) |
| [[NCI-H2347 (line)]] | alt | 81.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 72.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.5) |
| [[CHP-212 (line)]] | wt | 122 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.256× (z -8.8) |
| [[SW 1088 (line)]] | alt | 205 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -9.9) |
| [[SW 1271 (line)]] | alt | 335 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0423× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 61.2 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.324× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 20.7 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 38.1 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 41.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 31.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 41.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1L]] | +0.68 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[TMEM255B]] | +0.65 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[LRRC8C]] | +0.62 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CSNK1E]] | +0.61 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[PARVB]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[GALNT18]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[SNX14]] | +0.58 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[PNP]] | +0.58 | +0.57 / +0.57 | both halves | 1e-05 | STRING 481 |
| [[CPNE5]] | +0.57 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[APBA2]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ARHGAP22]] | +0.57 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[SMYD2]] | +0.57 | +0.63 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH3B1]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[TNS3]] | -0.48 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[FIGN]] | -0.47 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[MUC20]] | -0.47 | -0.55 / -0.26 | both halves | 4e-04 |  |
| [[SETD2]] | -0.46 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[MTUS1]] | -0.46 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM158]] | B | TMEM158 activity raises PYGL's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 2.28× lower at baseline in the lines without TMEM158 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[NPAS2]] | B | NPAS2 activity raises PYGL's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without NPAS2 | 0.074 | ⚠ within organs, on part of the lines |
| [[KCNMA1]] | B | KCNMA1 activity raises PYGL's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.41× lower at baseline in the lines without KCNMA1 | 0.087 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[PDE10A]] | B | PDE10A activity raises PYGL's level | lines that do not express PDE10A (24) vs lines expressing it (26) | 1.72× lower at baseline in the lines without PDE10A | 0.089 | ⚠ within organs, on part of the lines; also absent: ZMAT4, UBE2QL1, C10orf90 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRRC8C]] | B | PYGL activity raises LRRC8C's level | lines that do not express PYGL (7) vs lines expressing it (43) | 3.83× lower at baseline in the lines without PYGL | 0.075 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |
| [[SLC4A7]] | B | PYGL activity raises SLC4A7's level | lines that do not express PYGL (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without PYGL | 0.079 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |
| [[ITPR1]] | B | PYGL activity raises ITPR1's level | lines that do not express PYGL (7) vs lines expressing it (43) | 4.22× lower at baseline in the lines without PYGL | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |
| [[CPNE5]] | B | PYGL activity raises CPNE5's level | lines that do not express PYGL (7) vs lines expressing it (43) | 2.09× lower at baseline in the lines without PYGL | 0.094 | ⚠ within organs, on part of the lines; also absent: FAM229B, ANKRD44, WHAMMP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (50.1, 4.1); signed map (1.3, 50.4). **Vector** length 103, 34.2% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +1.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.7 | -35.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.0 | -2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.8 | +0.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.7 | -0.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -5.3 | -3.3 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -4.6 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.5 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -2.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.3 | -2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | glycogen phosphorylase L |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,857,891-50,944,483 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GSD6 |
| Gene groups (HGNC) | Glycogen phosphorylases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 5 pathways, smallest: Glycogen breakdown (glycogenolysis); Glycogen metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P06737](https://www.uniprot.org/uniprotkb/P06737) (Glycogen phosphorylase, liver form):

> Allosteric enzyme that catalyzes the rate-limiting step in glycogen catabolism, the phosphorolytic cleavage of glycogen to produce glucose-1-phosphate, and plays a central role in maintaining cellular and organismal glucose homeostasis.

**Summary**, from NCBI Gene [5836](https://www.ncbi.nlm.nih.gov/gene/5836):

> This gene encodes a homodimeric protein that catalyses the cleavage of alpha-1,4-glucosidic bonds to release glucose-1-phosphate from liver glycogen stores. This protein switches from inactive phosphorylase B to active phosphorylase A by phosphorylation of serine residue 15. Activity of this enzyme is further regulated by multiple allosteric effectors and hormonal controls. Humans have three glycogen phosphorylase genes that encode distinct isozymes that are primarily expressed in liver, brain …

**Accessions** — [HGNC:9725](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9725) · Entrez [5836](https://www.ncbi.nlm.nih.gov/gene/5836) · UniProt [P06737](https://www.uniprot.org/uniprotkb/P06737) · Ensembl [ENSG00000100504](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100504)

## Data

Gene col 1975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1975); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1975]; `tensor/DDL_lfc|DDL_z.npy` [1975]; `embed/gene_vectors.npy` [1975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1975 or target_col == 1975). Every well: [[PYGL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PYGL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
