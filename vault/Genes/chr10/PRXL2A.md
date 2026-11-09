---
symbol: "PRXL2A"
type: "gene"
col: 4331
ensembl_id: "ENSG00000122378"
name: "peroxiredoxin like 2A"
location: "10q23.1"
module: 45
arm: "+"
pooled_cpm: 26.55
n_lines_expressing: 41
n_dd_up: 13
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PRXL2A

*peroxiredoxin like 2A* — 10q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.17× (z +15.0, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Entrectinib (drug)]] 5 µM: 1.56× (z +4.7, q 3e-04, up in 29 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.315× (z -17.0, q 0e+00, down in 37 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QPRT]] (+0.68, fdr 7e-06), [[SLC25A23]] (+0.66, fdr 1e-05), [[C20orf96]] (+0.62, fdr 1e-05); moves opposite to [[ATRIP]] (-0.55, fdr 3e-05), [[CHTF8]] (-0.51, fdr 1e-04), [[MTG2]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CTSH]] → it (grade B ⚠); 1 goes from it, the strongest it → [[CTSH]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4331.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.17×** | +15.0 | 0e+00 | 35/36 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.05×** | +14.1 | 1e-42 | 26/28 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.59×** | +9.3 | 4e-18 | 32/33 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.56×** | +4.7 | 3e-04 | 29/38 (A549, COLO 205, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **1.36×** | +4.6 | 4e-04 | 26/40 (A549, C32, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | **1.31×** | +4.1 | 0.004 | 22/39 (A549, C32, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.012 | 22/39 (AsPC-1, SK-MEL-2, …) | top dose only |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.41×** | +3.5 | 0.031 | 20/38 (HOP62, NCI-H460, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.035 | 22/38 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.035 | 15/38 (HOP62, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~22% of this change | **1.37×** | +3.4 | 0.041 | 17/36 (SW1417, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.062 | 15/38 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.35×** | +3.1 | 0.098 | 16/38 (J82, SW1417, …) | top dose only |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.22× | +3.0 | 0.10 | 14/38 (C32, A498, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4331.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.315×** | -17.0 | 0e+00 | 37/39 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.257×** | -14.1 | 7e-43 | 36/38 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.482×** | -7.3 | 6e-11 | 27/38 (Panc 03.27, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.499×** | -7.2 | 8e-11 | 31/38 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.592×** | -5.4 | 6e-06 | 26/38 (SW 900, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.598×** | -5.3 | 1e-05 | 26/38 (RKO, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.617×** | -5.0 | 5e-05 | 22/37 (Panc 03.27, BT-474, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -4.5 | 4e-04 | 22/37 (A-427, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.651×** | -4.4 | 6e-04 | 22/38 (SW 900, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.656×** | -4.3 | 8e-04 | 25/38 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.004 | 21/39 (NCI-H1792, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.702×** | -3.6 | 0.013 | 19/39 (CHP-212, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Isocorydine (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.070 | 15/39 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -3.1 | 0.075 | 16/38 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4331. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 47.5 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.16× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -14.7) |
| [[NCI-H1792 (line)]] | alt | 40.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -13.7) |
| [[NCI-H2347 (line)]] | alt | 42.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -14.2) |
| [[PANC-1 (line)]] | alt | 38.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.43× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -11.9) |
| [[A549 (line)]] | wt | 34.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -11.4) |
| [[HOP62 (line)]] | alt | 23.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.27× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -13.6) |
| [[Hs 766T (line)]] | wt | 84.1 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +9.3) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -10.8) |
| [[LS 180 (line)]] | wt | 58.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.41× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 23.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 11.9× (z +14.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -12.3) |
| [[Panc 03.27 (line)]] | alt | 20.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.5) |
| [[SW 900 (line)]] | alt | 32.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.2) |
| [[COLO 205 (line)]] | alt | 41.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.6) |
| [[HepG2_C3A (line)]] | wt | 93.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.308× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 59.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 17.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.76× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -11.2) |
| [[SW480 (line)]] | alt | 9.71 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 8.40× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -12.0) |
| [[A-427 (line)]] | wt | 61.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.17× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -18.9) |
| [[A498 (line)]] | wt | 9.74 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.75× (z +10.4) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 32.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +9.7) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 10.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -9.7) |
| [[J82 (line)]] | alt | 28.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +10.3) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 12.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -13.5) |
| [[RKO (line)]] | wt | 45.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.6) |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.2) |
| [[SW48 (line)]] | wt | 61.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -11.5) |
| [[A-172 (line)]] | wt | 8.63 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.82× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 18.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.6) |
| [[BT-474 (line)]] | alt | 46.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.151× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 25.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.7) |
| [[SHP-77 (line)]] | alt | 21.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.45 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 73.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.68 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.02 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.26 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4331), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QPRT]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[SLC25A23]] | +0.66 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[C20orf96]] | +0.62 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.62 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ATP8A1]] | +0.59 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[GSTM4]] | +0.58 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[HMGN3]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[ATP6V0E2]] | +0.56 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[PECR]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[GALM]] | +0.55 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CD46]] | +0.55 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[CMBL]] | +0.55 | +0.57 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATRIP]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[CHTF8]] | -0.51 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[MTG2]] | -0.50 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[SMIM12]] | -0.50 | -0.39 / -0.39 | both halves | 5e-05 |  |
| [[ANKRD17-DT]] | -0.50 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[ZNF689]] | -0.50 | -0.34 / -0.40 | both halves | 1e-04 |  |
| [[C14orf119]] | -0.49 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[RPAP1]] | -0.49 | -0.38 / -0.35 | both halves | 1e-04 |  |
| [[UBE3B]] | -0.48 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[ADPRHL1]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[PYCR2]] | -0.47 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[ZNF7]] | -0.47 | -0.42 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSH]] | B | CTSH activity raises PRXL2A's level | lines that do not express CTSH (8) vs lines expressing it (42) | 1.59× lower at baseline in the lines without CTSH | 0.039 | ⚠ within organs, on part of the lines; also absent: BCL2L1, ENSG00000234139, DAPK2; maybe low, not absent |
| [[ARMH1]] | C | ARMH1 activity raises PRXL2A's level | lines that do not express ARMH1 (3) vs lines expressing it (47) | 5.14× lower at baseline in the lines without ARMH1 | 0.057 | ⚠ few lines (3 vs 47); across organs; also absent: MCF2L2, KIAA1522, ENSG00000257489; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSH]] | B | PRXL2A activity raises CTSH's level | lines that do not express PRXL2A (9) vs lines expressing it (41) | 1.16× lower at baseline in the lines without PRXL2A | 0.067 | ⚠ within organs, on part of the lines; also absent: ACSS1, LONRF3, AP1G2 |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.643). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (6.0, -8.4); signed map (-29.2, -4.7). **Vector** length 76.0, 20.1% of its response variance represented; |z| ≥ 3 in 779 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.2 | +14.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.1 | +15.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +9.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.0 | +1.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +2.7 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Berbamine (drug)]] 5 µM |  | +2.9 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.8 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -14.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.3 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.8 | -17.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | peroxiredoxin like 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1 — chr10:80,407,829-80,437,115 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4248, PAMM, Adrx; previously C10orf58, FAM213A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BRX8](https://www.uniprot.org/uniprotkb/Q9BRX8) (Peroxiredoxin-like 2A):

> Involved in redox regulation of the cell. Acts as an antioxidant. Inhibits TNFSF11-induced NFKB1 and JUN activation and osteoclast differentiation. May affect bone resorption and help to maintain bone mass. Acts as a negative regulator of macrophage-mediated inflammation by inhibiting macrophage production of inflammatory cytokines, probably through suppression of the MAPK signaling pathway.

**Summary**, from NCBI Gene [84293](https://www.ncbi.nlm.nih.gov/gene/84293):

> Enables antioxidant activity. Involved in regulation of osteoclast differentiation. Located in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28651) · Entrez [84293](https://www.ncbi.nlm.nih.gov/gene/84293) · UniProt [Q9BRX8](https://www.uniprot.org/uniprotkb/Q9BRX8) · Ensembl [ENSG00000122378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122378)

## Data

Gene col 4331: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4331); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4331, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4331]; `tensor/DDL_lfc|DDL_z.npy` [4331]; `embed/gene_vectors.npy` [4331]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4331 or target_col == 4331). Every well: [[PRXL2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRXL2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
