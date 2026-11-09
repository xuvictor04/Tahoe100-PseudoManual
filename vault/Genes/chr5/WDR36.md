---
symbol: "WDR36"
type: "gene"
col: 5633
ensembl_id: "ENSG00000134987"
name: "WD repeat domain 36"
location: "5q22.1"
module: 33
arm: "+"
pooled_cpm: 86.47
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 5
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# WDR36

*WD repeat domain 36* — 5q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (14 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.26× (z +10.8, q 2e-24, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.725× (z -6.5, q 5e-08, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR3]] (+0.79, fdr 7e-06), [[MRPL3]] (+0.79, fdr 7e-06), [[POLR1B]] (+0.77, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.62, fdr 7e-06), [[TP53INP2]] (-0.61, fdr 1e-05), [[ERF]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NBEAP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.26×** | +10.8 | 2e-24 | 48/49 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.10×** | +10.5 | 3e-23 | 46/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.67×** | +7.3 | 5e-11 | 36/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.1 | 1e-07 | 36/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +5.8 | 7e-07 | 39/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.10×** | +5.5 | 4e-06 | 27/37 (NCI-H1573, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.47×** | +5.5 | 4e-06 | 33/48 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.4 | 4e-06 | 36/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +5.4 | 4e-06 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.43×** | +5.0 | 3e-05 | 35/48 (HS-578T, COLO 205, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.42×** | +5.0 | 3e-05 | 32/48 (SNU-423, NCI-H1792, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.40×** | +4.8 | 6e-05 | 27/48 (NCI-H1573, LS 180, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +4.8 | 6e-05 | 32/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.27×** | +4.7 | 9e-05 | 25/48 (A549, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.41×** | +4.7 | 1e-04 | 29/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.001 | 26/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.61×** | +3.6 | 0.011 | 30/48 (NCI-H1792, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.021 | 22/48 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.023 | 22/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.55×** | +3.2 | 0.027 | 23/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.038 | 19/48 (A-172, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.044 | 21/48 (NCI-H460, NCI-H2030, …) | top dose only |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.0 | 0.056 | 21/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.074 | 17/48 (NCI-H1792, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | **1.23×** | +2.9 | 0.074 | 17/49 (HOP62, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.725×** | -6.5 | 5e-08 | 39/49 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.747×** | -4.0 | 0.017 | 23/44 (SK-MEL-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.766×** | -3.7 | 0.044 | 28/47 (HS-578T, LS 180, …) | rises with dose | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **0.777×** | -3.6 | 0.044 | 29/48 (KATO III, HEC-1-A, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.807×** | -3.3 | 0.093 | 19/48 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.739× | -3.1 | 0.19 | 20/48 (LS 180, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.810× | -3.0 | 0.21 | 18/47 (C32, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 90.5 | 6 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.45× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 102 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.53× (z +11.6) | — |
| [[SW480 (line)]] | alt | 101 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +9.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 4.12× (z +8.9) | — |
| [[NCI-H1573 (line)]] | alt | 54.3 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.23× (z +11.3) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 11.2× (z +9.9) | — |
| [[RKO (line)]] | wt | 151 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.24× (z +9.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -21.5) |
| [[A498 (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -12.7) |
| [[AsPC-1 (line)]] | alt | 64.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 69.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +11.8) | — |
| [[HOP62 (line)]] | alt | 69.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.78× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 41.3 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.60× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 93.1 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.6) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 124 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.60× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.202× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 96.2 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 4.57× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -9.1) |
| [[A-427 (line)]] | wt | 99.1 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.85× (z +8.5) | — |
| [[A549 (line)]] | wt | 72.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[C-33 A (line)]] | alt | 83.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | — |
| [[C32 (line)]] | wt | 63.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -10.2) |
| [[HS-578T (line)]] | alt | 129 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.33× (z +8.5) ⚠ cell-cycle shift, explains ~53% of this change | — |
| [[J82 (line)]] | alt | 97.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.89× (z +8.5) | — |
| [[LOX-IMVI (line)]] | wt | 78.3 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 3.36× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 111 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 6.76× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 99.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.66× (z +9.0) | — |
| [[NCI-H661 (line)]] | alt | 80.4 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0843× (z -11.9) |
| [[SW 1088 (line)]] | alt | 92.6 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.0670× (z -9.8) |
| [[SW1417 (line)]] | alt | 52.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -10.1) |
| [[A-172 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 151 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 114 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 74.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 46.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 70.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 69.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 52.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 81.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 85.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 59.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 83.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR3]] | +0.79 | +0.83 / +0.69 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[MRPL3]] | +0.79 | +0.82 / +0.79 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.77 | +0.79 / +0.67 | both halves | 7e-06 | STRING 951 |
| [[UTP18]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 | same gene group; pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 999 |
| [[DLAT]] | +0.71 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[NLE1]] | +0.70 | +0.71 / +0.61 | both halves | 7e-06 | same gene group; STRING 857 |
| [[EEF1E1]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ATIC]] | +0.69 | +0.63 / +0.75 | both halves | 7e-06 |  |
| [[PHB1]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[USP10]] | +0.69 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[CCT2]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MRPS35]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.62 | -0.60 / -0.60 | both halves | 7e-06 |  |
| [[TP53INP2]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[ERF]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[EIF1B]] | -0.58 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[CD63]] | -0.58 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[PDE6D]] | -0.58 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NBEAP2]] | B | NBEAP2 activity raises WDR36's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without NBEAP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.788). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.8, -39.5); signed map (-7.0, -50.9). **Vector** length 106, 36.0% of its response variance represented; |z| ≥ 3 in 1,154 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.57 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.3 | +3.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +4.2 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +4.1 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +10.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.0 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +0.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.6 | +2.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.6 | +4.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.6 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.5 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -4.1 | +4.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.5 | -2.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.4 | -0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 36 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q22.1 — chr5:111,092,321-111,130,502 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TA-WDRP, UTP21; previously GLC1G |
| Gene groups (HGNC) | WD repeat domain containing; UTPb subcomplex |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NI36](https://www.uniprot.org/uniprotkb/Q8NI36) (WD repeat-containing protein 36):

> Part of the small subunit (SSU) processome, first precursor of the small eukaryotic ribosomal subunit. During the assembly of the SSU processome in the nucleolus, many ribosome biogenesis factors, an RNA chaperone and ribosomal proteins associate with the nascent pre-rRNA and work in concert to generate RNA folding, modifications, rearrangements and cleavage as well as targeted degradation of pre-ribosomal RNA by the RNA exosome. Involved in the nucleolar processing of SSU 18S rRNA. Involved in …

**Summary**, from NCBI Gene [134430](https://www.ncbi.nlm.nih.gov/gene/134430):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Mutations in this gene have been associated with adult-onset primary …

**Accessions** — [HGNC:30696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30696) · Entrez [134430](https://www.ncbi.nlm.nih.gov/gene/134430) · UniProt [Q8NI36](https://www.uniprot.org/uniprotkb/Q8NI36) · Ensembl [ENSG00000134987](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134987)

## Data

Gene col 5633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5633); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5633]; `tensor/DDL_lfc|DDL_z.npy` [5633]; `embed/gene_vectors.npy` [5633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5633 or target_col == 5633). Every well: [[WDR36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
