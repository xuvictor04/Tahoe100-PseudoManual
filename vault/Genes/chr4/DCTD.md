---
symbol: "DCTD"
type: "gene"
col: 4953
ensembl_id: "ENSG00000129187"
name: "dCMP deaminase"
location: "4q35.1"
module: 5
arm: "+"
pooled_cpm: 32.02
n_lines_expressing: 49
n_dd_up: 5
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DCTD

*dCMP deaminase* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.79× (z +12.3, q 3e-32, up in 34 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 2.18×, RKO 2.60×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 2.99×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.314× (z -24.6, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF239]] (+0.69, fdr 9e-06), [[WDR4]] (+0.68, fdr 7e-06), [[GNL3L]] (+0.67, fdr 1e-05); moves opposite to [[NPEPPS]] (-0.68, fdr 3e-05), [[GPBP1]] (-0.64, fdr 7e-06), [[GABARAP]] (-0.62, fdr 1e-05, ⚠ GABARAP in the vector space only through flagged drug-doses), [[PLEKHH3]] (-0.62, fdr 5e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EFNA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 6 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4953.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SW480 2.18×, RKO 2.60×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (LS 180 2.99×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.3 | 3e-32 | 34/43 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +9.6 | 2e-19 | 27/37 (LS 180, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +8.1 | 9e-14 | 25/41 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +5.5 | 5e-06 | 0/47 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.23×** | +4.3 | 0.002 | 17/44 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +3.5 | 0.043 | 9/33 (NCI-H2347, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4953.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.314×** | -24.6 | 0e+00 | 45/47 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.465×** | -23.0 | 0e+00 | 40/46 (SK-MEL-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.357×** | -21.8 | 0e+00 | 44/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.371×** | -20.8 | 0e+00 | 44/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.628×** | -13.9 | 5e-42 | 37/47 (RKO, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.567×** | -12.0 | 3e-31 | 41/47 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.652×** | -8.7 | 2e-16 | 35/46 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.681×** | -8.1 | 5e-14 | 29/47 (J82, RKO, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.799×** | -6.7 | 1e-09 | 24/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.722×** | -6.6 | 2e-09 | 26/46 (C32, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.534×** | -6.6 | 3e-09 | 27/47 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -6.5 | 5e-09 | 26/47 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.743×** | -6.3 | 1e-08 | 26/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.781×** | -6.2 | 2e-08 | 23/47 (C32, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.761×** | -6.2 | 2e-08 | 25/47 (AsPC-1, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4953. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 30.7 | 0 | 9 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.216× (z -17.2) |
| [[RKO (line)]] | wt | 78.7 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.164× (z -17.1) |
| [[SW480 (line)]] | alt | 37.4 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.18× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.176× (z -22.2) |
| [[AsPC-1 (line)]] | alt | 34.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.6) |
| [[HEC-1-A (line)]] | alt | 47.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -14.8) |
| [[J82 (line)]] | alt | 37.2 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -21.2) |
| [[LoVo (line)]] | wt | 43.4 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -21.5) |
| [[LS 180 (line)]] | wt | 31.6 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -10.1) |
| [[PANC-1 (line)]] | alt | 31.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -14.5) |
| [[SW48 (line)]] | wt | 59.1 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.130× (z -14.2) |
| [[C-33 A (line)]] | alt | 54.9 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.266× (z -10.1) |
| [[HOP62 (line)]] | alt | 41.5 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.248× (z -14.1) |
| [[HS-578T (line)]] | alt | 24.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.101× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 34.9 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -11.8) |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 31.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.3) |
| [[A-427 (line)]] | wt | 35.7 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.267× (z -12.2) |
| [[A498 (line)]] | wt | 41.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.348× (z -12.2) |
| [[A549 (line)]] | wt | 28.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -11.8) |
| [[A-172 (line)]] | wt | 39.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.326× (z -11.6) |
| [[C32 (line)]] | wt | 36.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -11.5) |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.260× (z -8.6) |
| [[KATO III (line)]] | alt | 22.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 27.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.213× (z -11.1) |
| [[SK-MEL-2 (line)]] | alt | 31.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -22.8) |
| [[SNU-1 (line)]] | wt | 33.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -10.3) |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -11.0) |
| [[H4 (line)]] | wt | 46.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.257× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 33.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -21.5) |
| [[NCI-H2347 (line)]] | alt | 29.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.3) |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.238× (z -9.2) |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 7.30 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4953), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF239]] | +0.69 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[WDR4]] | +0.68 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[GNL3L]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[TRNT1]] | +0.66 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[ZNF202]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ZNF121]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[PPIL1]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ALG8]] | +0.65 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[MAK16]] | +0.64 | +0.51 / +0.63 | both halves | 1e-05 |  |
| [[PUS1]] | +0.64 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[ZNF783]] ⚠ | +0.63 | +0.53 / +0.56 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ABCF2]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SLC25A15]] | +0.62 | +0.60 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPEPPS]] | -0.68 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[GPBP1]] | -0.64 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[GABARAP]] ⚠ | -0.62 | -0.58 / -0.55 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[PLEKHH3]] | -0.62 | -0.40 / -0.70 | both halves | 5e-05 |  |
| [[SIRT2]] | -0.61 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[CXXC5]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[ELF2]] | -0.59 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RNASE4]] | -0.59 | -0.28 / -0.61 | both halves | 3e-04 |  |
| [[STK38]] | -0.59 | -0.47 / -0.60 | both halves | 2e-05 |  |
| [[ARID4A]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[DAAM1]] | -0.58 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[KMT2C]] | -0.58 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[BLVRB]] | -0.58 | -0.45 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EFNA1]] | B | EFNA1 activity lowers DCTD's level | lines that do not express EFNA1 (13) vs lines expressing it (37) | 1.28× higher at baseline in the lines without EFNA1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ELF3-AS1, ANO9, GPRC5A; maybe low, not absent |
| [[KIAA1549]] | C | KIAA1549 activity raises DCTD's level | lines that do not express KIAA1549 (4) vs lines expressing it (46) | 1.78× lower at baseline in the lines without KIAA1549 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HHAT, WHRN, GNAL; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.7, -33.3); signed map (-0.8, -47.6). **Vector** length 89.4, 21.0% of its response variance represented; |z| ≥ 3 in 1,104 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.51 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.2 | -0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.5 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.9 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.9 | -0.9 |
|  | [[Gallic acid (drug)]] 0.05 µM |  | +1.8 | +1.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +2.7 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -6.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.2 | -6.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.8 | -5.8 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.8 | -6.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | dCMP deaminase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:182,890,060-182,917,936 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 2 pathways, smallest: Interconversion of nucleotide di- and triphosphates; Metabolism of nucleotides |
| Matched by | ensembl_id |

**Function**, from UniProt [P32321](https://www.uniprot.org/uniprotkb/P32321) (Deoxycytidylate deaminase):

> Catalyzes the deamination of dCMP to dUMP, providing the nucleoside monophosphate substrate for the thymidylate synthase/TYMS. Also, part of a nucleotide salvage pathway that eliminates epigenetically modified 5-hydroxymethyl-dCMP (hmdCMP) in a two-step process entailing deamination to cytotoxic 5-hydroxymethyl-dUMP (hmdUMP), followed by its hydrolysis into 5-hydroxymethyluracil (hmU) and 2-deoxy-D-ribose 5-phosphate (deoxyribosephosphate). Catalyzes the first step in that pathway, the …

**Summary**, from NCBI Gene [1635](https://www.ncbi.nlm.nih.gov/gene/1635):

> The protein encoded by this gene catalyzes the deamination of dCMP to dUMP, the nucleotide substrate for thymidylate synthase. The encoded protein is allosterically activated by dCTP and inhibited by dTTP, and is found as a homohexamer. This protein uses zinc as a cofactor for its activity. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2710](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2710) · Entrez [1635](https://www.ncbi.nlm.nih.gov/gene/1635) · UniProt [P32321](https://www.uniprot.org/uniprotkb/P32321) · Ensembl [ENSG00000129187](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129187)

## Data

Gene col 4953: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4953); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4953, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4953]; `tensor/DDL_lfc|DDL_z.npy` [4953]; `embed/gene_vectors.npy` [4953]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4953 or target_col == 4953). Every well: [[DCTD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCTD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
