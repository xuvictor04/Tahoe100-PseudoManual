---
symbol: "CXADR"
type: "gene"
col: 7820
ensembl_id: "ENSG00000154639"
name: "CXADR cell adhesion molecule"
location: "21q21.1"
module: 45
arm: "+"
pooled_cpm: 73.89
n_lines_expressing: 34
n_dd_up: 29
n_dd_down: 10
n_dd_up_clean: 24
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 22
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# CXADR

*CXADR cell adhesion molecule* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.90× (z +17.0, q 0e+00, up in 28 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.735× (z -8.2, q 1e-13, down in 18 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP7]] (+0.69, fdr 1e-05), [[HMGN3]] (+0.68, fdr 1e-05), [[AMOT]] (+0.67, fdr 3e-05); moves opposite to [[FAM120B]] (-0.62, fdr 1e-05), [[E2F3]] (-0.60, fdr 1e-05), [[PHF5A]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[HOOK1]] → it (grade B ⚠); 22 go from it, the strongest it → [[SORL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +17.0 | 0e+00 | 28/32 (HOP62, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.07×** | +13.7 | 5e-40 | 26/32 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +12.0 | 6e-31 | 27/32 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.81×** | +11.1 | 1e-26 | 28/32 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +11.0 | 6e-26 | 27/32 (SW480, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.73×** | +10.3 | 6e-23 | 29/32 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.38×** | +9.2 | 2e-18 | 27/33 (NCI-H1573, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.62×** | +9.1 | 9e-18 | 25/32 (SW48, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +7.9 | 2e-13 | 24/32 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.33×** | +7.4 | 6e-12 | 17/32 (SNU-423, HOP62, …) | rises with dose | composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +6.9 | 3e-10 | 21/32 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +6.7 | 9e-10 | 22/32 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +5.9 | 2e-07 | 15/32 (LS 180, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +5.3 | 4e-06 | 21/32 (LoVo, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.00×** | +5.3 | 5e-06 | 24/33 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 2e-05 | 16/32 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +4.6 | 1e-04 | 16/32 (SW48, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -8.2 | 1e-13 | 18/32 (NCI-H23, LoVo, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.676×** | -7.0 | 1e-09 | 24/32 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.693×** | -6.9 | 1e-09 | 22/32 (LoVo, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -6.4 | 2e-08 | 18/32 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.751×** | -5.4 | 8e-06 | 17/32 (LoVo, NCI-H1573, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.800×** | -4.0 | 0.005 | 15/32 (A-427, SW480, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.606×** | -3.8 | 0.010 | 15/29 (LoVo, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.010 | 14/32 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.813×** | -3.8 | 0.011 | 17/34 (HEC-1-A, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.817×** | -3.5 | 0.031 | 12/32 (NCI-H1573, HepG2/C3A, …) | rises with dose |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 0.792× | -3.0 | 0.14 | 9/32 (NCI-H1573, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 80.4 | 7 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +12.2) | [[Auranofin (drug)]] 5 µM 0.444× (z -9.9) |
| [[LoVo (line)]] | wt | 233 | 1 | 7 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.60× (z +8.5) | [[Auranofin (drug)]] 5 µM 0.346× (z -13.9) |
| [[NCI-H460 (line)]] | wt | 48.1 | 8 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.30× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 2.07× (z +10.8) | — |
| [[SW48 (line)]] | wt | 114 | 6 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 22.5 | 5 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 5.70× (z +13.5) | — |
| [[A-427 (line)]] | wt | 393 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.469× (z -11.0) |
| [[LS 180 (line)]] | wt | 164 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.431× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change |
| [[NCI-H23 (line)]] | alt | 143 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -12.6) |
| [[SK-MEL-2 (line)]] | alt | 42.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +10.7) | — |
| [[AsPC-1 (line)]] | alt | 76.6 | 2 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.7) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Radotinib (drug)]] 5 µM 1.99× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.447× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 69.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.15× (z +11.2) | — |
| [[NCI-H1573 (line)]] | alt | 118 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.14× (z +9.2) | [[Ixazomib citrate (drug)]] 5 µM 0.415× (z -9.5) |
| [[PANC-1 (line)]] | alt | 25.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.02× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 82.6 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.60× (z +8.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.90× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 147 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.04× (z +9.0) | [[Ixazomib citrate (drug)]] 5 µM 0.382× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 93.8 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.611× (z -8.5) |
| [[SNU-423 (line)]] | alt | 77.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +13.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.28× (z +9.2) | — |
| [[A549 (line)]] | wt | 39.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.10× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 29.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.78× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 85.8 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.11× (z +10.8) | — |
| [[KATO III (line)]] | alt | 113 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.92× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.70× (z +9.3) | — |
| [[SW 900 (line)]] | alt | 30.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.40× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 144 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.6) | — |
| [[A-172 (line)]] | wt | 8.39 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 49.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 133 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.1 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.54 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.8 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 73.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 367 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.55 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.07 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP7]] | +0.69 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[HMGN3]] | +0.68 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[AMOT]] | +0.67 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[MAPRE2]] | +0.67 | +0.49 / +0.71 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.66 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[CAT]] | +0.65 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[TSPAN15]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TMEM14A]] | +0.64 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.64 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[SNX2]] | +0.62 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ARHGAP12]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CGN]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM120B]] | -0.62 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[E2F3]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[PHF5A]] | -0.59 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[EMG1]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH2L]] | -0.59 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TRAPPC12]] | -0.59 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[MAP3K7]] | -0.58 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ACAD9]] | -0.57 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[TMEM11-DT]] | -0.57 | -0.39 / -0.60 | both halves | 5e-05 |  |
| [[RECQL5]] | -0.57 | -0.34 / -0.63 | both halves | 1e-04 |  |
| [[MOSMO]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[SLC30A6]] | -0.56 | -0.51 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOOK1]] | B | HOOK1 activity raises CXADR's level | lines that do not express HOOK1 (22) vs lines expressing it (28) | 3.75× lower at baseline in the lines without HOOK1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SMPDL3B, BSPRY, SPINT1-AS1 |
| [[IL18]] | B | IL18 activity raises CXADR's level | lines that do not express IL18 (18) vs lines expressing it (32) | 4.00× lower at baseline in the lines without IL18 | 0.008 | ⚠ within organs, on part of the lines; also absent: LSR, SPINT2, LAMA3 |
| [[CGN]] | B | CGN activity raises CXADR's level | lines that do not express CGN (21) vs lines expressing it (29) | 4.52× lower at baseline in the lines without CGN | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[MPP7]] | B | MPP7 activity raises CXADR's level | lines that do not express MPP7 (19) vs lines expressing it (31) | 2.68× lower at baseline in the lines without MPP7 | 0.031 | ⚠ within organs, on part of the lines; also absent: TTC9, BSPRY, HOOK1; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises CXADR's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 3.58× lower at baseline in the lines without SORL1 | 0.039 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[AMOT]] | B | AMOT activity raises CXADR's level | lines that do not express AMOT (12) vs lines expressing it (38) | 2.79× lower at baseline in the lines without AMOT | 0.048 | ⚠ within organs, on part of the lines; also absent: SYCP2, ENSG00000289956, ENSG00000132832 |
| [[SH3BGRL2]] | B | SH3BGRL2 activity raises CXADR's level | lines that do not express SH3BGRL2 (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without SH3BGRL2 | 0.059 | ⚠ within organs, on part of the lines; also absent: LSR, HOOK1, SMPDL3B; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises CXADR's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CDS1]] | B | CDS1 activity raises CXADR's level | lines that do not express CDS1 (19) vs lines expressing it (31) | 2.89× lower at baseline in the lines without CDS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, C6orf132; maybe low, not absent |
| [[CRIP1]] | B | CRIP1 activity raises CXADR's level | lines that do not express CRIP1 (27) vs lines expressing it (23) | 3.18× lower at baseline in the lines without CRIP1 | 0.085 | ⚠ within organs, on part of the lines; also absent: SPINT2, POF1B, S100P |
| [[SLAIN1]] | B | SLAIN1 activity raises CXADR's level | lines that do not express SLAIN1 (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without SLAIN1 | 0.089 | ⚠ within organs, on part of the lines; also absent: RBM11, NELL2, LHX2 |
| [[VWA1]] | B | VWA1 activity raises CXADR's level | lines that do not express VWA1 (10) vs lines expressing it (40) | 4.08× lower at baseline in the lines without VWA1 | 0.097 | ⚠ within organs, on part of the lines; also absent: ATAD3C, KLC3, GPRC5C |

### Downstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 21, C 1. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SORL1]] | B | CXADR activity raises SORL1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 4.54× lower at baseline in the lines without CXADR | 0.001 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[IL18]] | B | CXADR activity raises IL18's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.46× lower at baseline in the lines without CXADR | 0.003 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[TSPAN15]] | B | CXADR activity raises TSPAN15's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.74× lower at baseline in the lines without CXADR | 0.006 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[CTSH]] | B | CXADR activity raises CTSH's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.73× lower at baseline in the lines without CXADR | 0.008 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[CGN]] | B | CXADR activity raises CGN's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without CXADR | 0.011 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[KRT80]] | B | CXADR activity raises KRT80's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.68× lower at baseline in the lines without CXADR | 0.020 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[CDS1]] | B | CXADR activity raises CDS1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.09× lower at baseline in the lines without CXADR | 0.021 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[LPAR2]] | B | CXADR activity raises LPAR2's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.23× lower at baseline in the lines without CXADR | 0.028 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[HOOK1]] | B | CXADR activity raises HOOK1's level | lines that do not express CXADR (16) vs lines expressing it (34) | 3.44× lower at baseline in the lines without CXADR | 0.033 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[MPP7]] | B | CXADR activity raises MPP7's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.54× lower at baseline in the lines without CXADR | 0.034 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[GALM]] | B | CXADR activity raises GALM's level | lines that do not express CXADR (16) vs lines expressing it (34) | 2.27× lower at baseline in the lines without CXADR | 0.040 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |
| [[ZNF778]] | B | CXADR activity lowers ZNF778's level | lines that do not express CXADR (16) vs lines expressing it (34) | 1.28× higher at baseline in the lines without CXADR | 0.056 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, LMTK3 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.709). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (18.9, 1.4); signed map (48.2, 5.0). **Vector** length 110, 30.9% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +17.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.0 | +11.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | -1.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~13% of this change | +5.3 | -1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.5 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +5.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +3.7 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -5.3 | -7.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.3 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | -4.3 | -4.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.0 | -5.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | CXADR cell adhesion molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.1 — chr21:17,513,043-17,593,579 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CAR |
| Gene groups (HGNC) | V-set domain containing; IgCAM CXADR-related subfamily |
| Reactome | 4 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Cell surface interactions at the vascular wall; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [P78310](https://www.uniprot.org/uniprotkb/P78310) (Coxsackievirus and adenovirus receptor):

> Component of the epithelial apical junction complex that may function as a homophilic cell adhesion molecule and is essential for tight junction integrity. Also involved in transepithelial migration of leukocytes through adhesive interactions with JAML a transmembrane protein of the plasma membrane of leukocytes. The interaction between both receptors also mediates the activation of gamma-delta T-cells, a subpopulation of T-cells residing in epithelia and involved in tissue homeostasis and …

**Summary**, from NCBI Gene [1525](https://www.ncbi.nlm.nih.gov/gene/1525):

> The protein encoded by this gene is a type I membrane receptor for group B coxsackieviruses and subgroup C adenoviruses. Several transcript variants encoding different isoforms have been found for this gene. Pseudogenes of this gene are found on chromosomes 15, 18, and 21. [provided by RefSeq, May 2011]

**Accessions** — [HGNC:2559](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2559) · Entrez [1525](https://www.ncbi.nlm.nih.gov/gene/1525) · UniProt [P78310](https://www.uniprot.org/uniprotkb/P78310) · Ensembl [ENSG00000154639](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154639)

## Data

Gene col 7820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7820); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7820]; `tensor/DDL_lfc|DDL_z.npy` [7820]; `embed/gene_vectors.npy` [7820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7820 or target_col == 7820). Every well: [[CXADR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CXADR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
