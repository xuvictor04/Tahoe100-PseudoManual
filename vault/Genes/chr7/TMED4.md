---
symbol: "TMED4"
type: "gene"
col: 8175
ensembl_id: "ENSG00000158604"
name: "transmembrane p24 trafficking protein 4"
location: "7p13"
module: 11
arm: "-"
pooled_cpm: 68.53
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# TMED4

*transmembrane p24 trafficking protein 4* — 7p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.94× (z +14.3, q 7e-44, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.36× (z +5.8, q 9e-07, up in 33 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H23 4.78×, NCI-H1573 5.91×, HEC-1-A 3.24×, SW480 3.14×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 4.62×, SK-MEL-2 4.89×, NCI-H23 3.56×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 1.99×, LOX-IMVI 2.10×).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.319× (z -21.5, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MLEC]] (+0.78, fdr 7e-06), [[PCYOX1]] (+0.76, fdr 7e-06), [[ATP6AP2]] (+0.72, fdr 7e-06); moves opposite to [[MRPL58]] (-0.73, fdr 7e-06), [[SURF6]] (-0.68, fdr 7e-06), [[ERCC4]] (-0.67, fdr 7e-06).
> It sits in the **-** arm of [[Module 011]] (Mitochondrial translation elongation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GSPT2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8175.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H23 4.78×, NCI-H1573 5.91×, HEC-1-A 3.24×, SW480 3.14×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (AsPC-1 4.62×, SK-MEL-2 4.89×, NCI-H23 3.56×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 1.99×, LOX-IMVI 2.10×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.94×** | +14.3 | 7e-44 | 47/49 (NCI-H23, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +11.3 | 3e-27 | 40/43 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.79×** | +7.1 | 2e-10 | 39/45 (Panc 03.27, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +5.8 | 9e-07 | 33/48 (NCI-H2347, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.36×** | +3.9 | 0.010 | 29/49 (HEC-1-A, LS 180, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~57% of this change | **1.34×** | +3.9 | 0.010 | 30/48 (HOP62, HT-29, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.319×** | -21.5 | 0e+00 | 47/48 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.339×** | -14.4 | 3e-44 | 47/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.384×** | -12.2 | 4e-32 | 48/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.519×** | -8.7 | 4e-16 | 46/48 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.533×** | -8.3 | 8e-15 | 46/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **0.647×** | -5.5 | 3e-06 | 40/48 (SHP-77, SNU-1, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.4 | 9e-04 | 1/49 (AN3 CA) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.703×** | -4.3 | 0.001 | 34/47 (A-172, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.746×** | -3.7 | 0.015 | 24/47 (SW48, NCI-H2347, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.565×** | -3.6 | 0.015 | 28/48 (A549, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.781×** | -3.3 | 0.055 | 26/47 (PANC-1, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 88.6 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.0) |
| [[A-427 (line)]] | wt | 77.6 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 53.8 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 4.62× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 82.4 | 1 | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -21.7) |
| [[KATO III (line)]] | alt | 107 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.16× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -15.7) |
| [[LS 180 (line)]] | wt | 73.5 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.86× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 76.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -24.9) |
| [[NCI-H460 (line)]] | wt | 71.5 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -24.6) |
| [[SK-MEL-2 (line)]] | alt | 52.6 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.89× (z +12.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -19.6) |
| [[CFPAC-1 (line)]] | alt | 48.8 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -18.8) |
| [[H4 (line)]] | wt | 101 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -20.8) |
| [[HT-29 (line)]] | alt | 71.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 40.8 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.7) |
| [[NCI-H23 (line)]] | alt | 60.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -29.7) |
| [[SNU-1 (line)]] | wt | 74.1 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.101× (z -15.6) |
| [[SW 900 (line)]] | alt | 84.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -17.5) |
| [[BT-474 (line)]] | alt | 62.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -16.6) |
| [[C-33 A (line)]] | alt | 76.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.89× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.2) |
| [[HCT15 (line)]] | alt | 78.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 78.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -11.1) |
| [[HOP62 (line)]] | alt | 50.3 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -13.8) |
| [[HS-578T (line)]] | alt | 61.1 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.2) |
| [[J82 (line)]] | alt | 57.4 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.7) |
| [[LoVo (line)]] | wt | 74.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -14.6) |
| [[NCI-H1792 (line)]] | alt | 40.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.03× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -18.6) |
| [[RKO (line)]] | wt | 66.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.59× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -11.9) |
| [[SW480 (line)]] | alt | 63.7 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -10.7) |
| [[A498 (line)]] | wt | 90.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -10.1) |
| [[A549 (line)]] | wt | 48.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.374× (z -11.3) |
| [[C32 (line)]] | wt | 40.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -16.3) |
| [[COLO 205 (line)]] | alt | 40.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.7) |
| [[Hs 766T (line)]] | wt | 72.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 24.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 58.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.84× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 71.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -12.1) |
| [[SHP-77 (line)]] | alt | 63.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -12.4) |
| [[SNU-423 (line)]] | alt | 50.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -12.0) |
| [[SW 1088 (line)]] | alt | 136 | 0 | 2 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0678× (z -12.2) |
| [[SW1417 (line)]] | alt | 97.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -16.7) |
| [[A-172 (line)]] | wt | 76.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +8.5) ⚠ toxic; transcription drop | — |
| [[CHP-212 (line)]] | wt | 48.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 44.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 40.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 98.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -20.2) |
| [[SW 1271 (line)]] | alt | 66.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -9.5) |
| [[AN3 CA (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 97.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MLEC]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[PCYOX1]] | +0.76 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[ATP6AP2]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LAPTM4A]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TMBIM6]] | +0.69 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[P3H1]] | +0.69 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[GNB2]] | +0.68 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[BSG]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[RCN2]] | +0.68 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[TMEM30A]] | +0.68 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[GRN]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[EFCAB14]] | +0.66 | +0.66 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MRPL58]] | -0.73 | -0.72 / -0.69 | both halves | 7e-06 |  |
| [[SURF6]] | -0.68 | -0.70 / -0.65 | both halves | 7e-06 |  |
| [[ERCC4]] | -0.67 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[NSRP1]] | -0.66 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[NT5C]] | -0.64 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[ZNF480]] | -0.63 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[TRMT10B]] | -0.63 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[GLRX2]] | -0.63 | -0.66 / -0.58 | both halves | 7e-06 |  |
| [[NOL8]] | -0.62 | -0.67 / -0.55 | both halves | 1e-05 |  |
| [[CRCP]] | -0.62 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.62 | -0.62 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GSPT2]] | B | GSPT2 activity raises TMED4's level | lines that do not express GSPT2 (14) vs lines expressing it (36) | 1.10× lower at baseline in the lines without GSPT2 | 0.084 | ⚠ within organs, on part of the lines; also absent: PALM2AKAP2, KCNN4, MDFIC |
| [[P3H1]] | C | P3H1 activity raises TMED4's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without P3H1 | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **-** arm (projection on the module's main direction -0.689). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.4, -19.4); signed map (-51.4, -7.2). **Vector** length 104, 33.5% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.7 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | +3.6 | +3.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | -1.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.2 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | -0.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | +1.8 | -1.5 |
|  | [[Relugolix (drug)]] 0.5 µM |  | +1.8 | +0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.8 | -0.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -11.0 | -8.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -10.1 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.8 | -14.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.9 | -8.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -21.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.7 | -4.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.0 | -5.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane p24 trafficking protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p13 — chr7:44,577,894-44,582,287 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HNLF, p24alpha3, p24a3 |
| Gene groups (HGNC) | Transmembrane p24 trafficking proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7H5](https://www.uniprot.org/uniprotkb/Q7Z7H5) (Transmembrane emp24 domain-containing protein 4):

> Involved in vesicular protein trafficking, mainly in the early secretory pathway. targeting. Involved in the maintenance of the Golgi apparatus. Appears to play a role in the biosynthesis of secreted cargo including processing. Involved in endoplasmic reticulum stress response. May play a role in the regulation of heat-shock response and apoptosis (By similarity).

**Summary**, from NCBI Gene [222068](https://www.ncbi.nlm.nih.gov/gene/222068):

> Involved in positive regulation of canonical NF-kappaB signal transduction. Predicted to be located in endoplasmic reticulum membrane. Predicted to be active in several cellular components, including COPII-coated ER to Golgi transport vesicle; Golgi apparatus; and endoplasmic reticulum-Golgi intermediate compartment. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22301](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22301) · Entrez [222068](https://www.ncbi.nlm.nih.gov/gene/222068) · UniProt [Q7Z7H5](https://www.uniprot.org/uniprotkb/Q7Z7H5) · Ensembl [ENSG00000158604](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158604)

## Data

Gene col 8175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8175); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8175]; `tensor/DDL_lfc|DDL_z.npy` [8175]; `embed/gene_vectors.npy` [8175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8175 or target_col == 8175). Every well: [[TMED4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMED4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
