---
symbol: "UBQLN1"
type: "gene"
col: 5636
ensembl_id: "ENSG00000135018"
name: "ubiquilin 1"
location: "9q21.32"
module: 25
arm: "+"
pooled_cpm: 143.15
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# UBQLN1

*ubiquilin 1* — 9q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.85× (z +15.1, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.864× (z -7.4, q 7e-11, down in 7 of 50 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.846× (z -3.4, q 0.062, down in 19 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.761×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.269×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAD23B]] (+0.82, fdr 7e-06), [[GPN1]] (+0.79, fdr 7e-06), [[NCKAP1]] (+0.79, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.69, fdr 7e-06), [[INAFM1]] (-0.67, fdr 7e-06), [[MIDN]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.85×** | +15.1 | 0e+00 | 48/48 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.61×** | +13.9 | 2e-41 | 48/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.60×** | +13.0 | 2e-36 | 48/48 (KATO III, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.02×** | +10.1 | 6e-22 | 46/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.77×** | +10.0 | 1e-21 | 48/49 (C32, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.54×** | +9.5 | 1e-19 | 48/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +7.7 | 1e-12 | 44/48 (LoVo, A-427, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +7.4 | 1e-11 | 37/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +6.8 | 7e-10 | 43/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +6.4 | 1e-08 | 42/47 (LoVo, COLO 205, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.36×** | +6.2 | 2e-08 | 35/48 (A549, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.81×** | +6.1 | 5e-08 | 46/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +6.0 | 9e-08 | 41/45 (PANC-1, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.9 | 1e-07 | 35/49 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.51×** | +5.5 | 2e-06 | 34/45 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 8e-06 | 34/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.8 | 4e-05 | 32/48 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 2e-04 | 31/48 (LS 180, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.33×** | +4.1 | 0.001 | 28/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.028 | 17/49 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.53×** | +3.2 | 0.035 | 26/47 (C32, SW480, …) | top dose only | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5636.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Adagrasib (drug)]] 0.05 µM in 1 line (NCI-H23 0.761×; ⚠ position not correctable); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (AN3 CA 0.269×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.864× | -7.4 | 7e-11 | 7/50 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.812×** | -4.3 | 0.006 | 27/49 (A549, HOP62, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.784×** | -3.5 | 0.062 | 27/48 (A-172, SW 900, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~23% of this change | **0.777×** | -3.5 | 0.062 | 29/47 (HEC-1-A, KATO III, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.846× | -3.4 | 0.062 | 19/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.719×** | -3.4 | 0.062 | 34/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.793×** | -3.3 | 0.066 | 27/48 (C-33 A, LS 180, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.798×** | -3.3 | 0.081 | 27/48 (SW1417, SW 900, …) | all doses, stronger at high dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.741× | -3.1 | 0.12 | 26/49 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 157 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.64× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 88.1 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.41× (z +14.7) | — |
| [[SW480 (line)]] | alt | 143 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.93× (z +13.9) | — |
| [[LoVo (line)]] | wt | 118 | 8 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.68× (z +15.2) | — |
| [[LS 180 (line)]] | wt | 156 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.52× (z +15.5) | — |
| [[KATO III (line)]] | alt | 147 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.36× (z +17.2) | — |
| [[NCI-H1573 (line)]] | alt | 85.4 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.40× (z +12.0) | — |
| [[SW48 (line)]] | wt | 149 | 7 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 4.32× (z +12.4) | — |
| [[C32 (line)]] | wt | 124 | 6 | 0 | [[PH-797804 (drug)]] 5 µM 14.2× (z +13.4) | — |
| [[COLO 205 (line)]] | alt | 81.5 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.34× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 126 | 6 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.72× (z +14.1) | — |
| [[NCI-H1792 (line)]] | alt | 100 | 6 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +10.3) | — |
| [[A549 (line)]] | wt | 154 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +9.3) | — |
| [[A-427 (line)]] | wt | 114 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.87× (z +11.4) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.57× (z +11.0) | — |
| [[NCI-H23 (line)]] | alt | 137 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.29× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 129 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.25× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 83.0 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.52× (z +11.8) | — |
| [[H4 (line)]] | wt | 131 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.30× (z +9.4) | — |
| [[HCT15 (line)]] | alt | 122 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.91× (z +10.3) | — |
| [[HEC-1-A (line)]] | alt | 185 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +12.8) | — |
| [[HOP62 (line)]] | alt | 121 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +12.0) | — |
| [[Hs 766T (line)]] | wt | 143 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.17× (z +11.7) | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.40× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 163 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.83× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 117 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.60× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 140 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.21× (z +11.3) | — |
| [[A-172 (line)]] | wt | 229 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.23× (z +9.1) | — |
| [[A498 (line)]] | wt | 247 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.49× (z +9.2) | — |
| [[AsPC-1 (line)]] | alt | 130 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 143 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.71× (z +9.9) | — |
| [[HS-578T (line)]] | alt | 119 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.01× (z +9.6) | — |
| [[RKO (line)]] | wt | 168 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.54× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 138 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.61× (z +10.7) | — |
| [[AN3 CA (line)]] | alt | 184 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -8.8) |
| [[J82 (line)]] | alt | 226 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 107 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.48× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 184 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.07× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 153 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 98.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 200 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAD23B]] | +0.82 | +0.80 / +0.85 | both halves | 7e-06 | STRING 881 |
| [[GPN1]] | +0.79 | +0.73 / +0.78 | both halves | 7e-06 |  |
| [[NCKAP1]] | +0.79 | +0.76 / +0.84 | both halves | 7e-06 |  |
| [[FECH]] | +0.75 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[PAPOLA]] | +0.74 | +0.64 / +0.82 | both halves | 7e-06 |  |
| [[CRYZ]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[STX16]] | +0.72 | +0.59 / +0.78 | both halves | 7e-06 |  |
| [[GSR]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[API5]] | +0.72 | +0.64 / +0.79 | both halves | 7e-06 |  |
| [[USP14]] | +0.71 | +0.74 / +0.82 | both halves | 7e-06 | STRING 689 |
| [[PSMD11]] | +0.71 | +0.60 / +0.73 | both halves | 7e-06 | STRING 594 |
| [[TCP1]] | +0.70 | +0.72 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.69 | -0.72 / -0.67 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.67 | -0.62 / -0.69 | both halves | 7e-06 |  |
| [[MIDN]] | -0.66 | -0.70 / -0.59 | both halves | 7e-06 |  |
| [[ZBTB7A]] | -0.66 | -0.62 / -0.66 | both halves | 7e-06 |  |
| [[IMP3]] | -0.63 | -0.33 / -0.77 | both halves | 1e-04 | STRING 449 |
| [[ISG20L2]] | -0.63 | -0.55 / -0.71 | both halves | 1e-05 |  |
| [[HIC2]] | -0.63 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[TPRN]] | -0.62 | -0.46 / -0.76 | both halves | 2e-05 |  |
| [[PPP1R35]] ⚠ | -0.62 | -0.50 / -0.66 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[FOXA2]] | -0.62 | -0.46 / -0.73 | both halves | 3e-05 |  |
| [[TMEM258]] | -0.62 | -0.47 / -0.69 | both halves | 2e-05 |  |
| [[RPL36AL]] ⚠ | -0.61 | -0.48 / -0.68 | both halves | 2e-05 | STRING 463; ⚠ in the vector space only through flagged drug-doses |
| [[RBX1]] | -0.60 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[RBM38]] | -0.60 | -0.49 / -0.63 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.816). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-24.2, -14.4); signed map (-16.3, -41.3). **Vector** length 103, 41.6% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.9 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.2 | +13.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +13.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.7 | +1.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | -1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +2.7 | +2.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.2 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.0 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -5.0 | +10.1 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.7 | +6.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -2.6 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.2 | -2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ubiquilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.32 — chr9:83,659,968-83,707,958 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DSK2, PLIC-1, XDRP1, DA41 |
| Gene groups (HGNC) | Ubiquilin family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 4 pathways, smallest: Cargo recognition for clathrin-mediated endocytosis; Clathrin-mediated endocytosis; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMX0](https://www.uniprot.org/uniprotkb/Q9UMX0) (Ubiquilin-1):

> Plays an important role in the regulation of different protein degradation mechanisms and pathways including ubiquitin-proteasome system (UPS), autophagy and endoplasmic reticulum-associated protein degradation (ERAD) pathway. Mediates the proteasomal targeting of misfolded or accumulated proteins for degradation by binding (via UBA domain) to their polyubiquitin chains and by interacting (via ubiquitin-like domain) with the subunits of the proteasome. Plays a role in the ERAD pathway via its …

**Summary**, from NCBI Gene [29979](https://www.ncbi.nlm.nih.gov/gene/29979):

> This gene encodes an ubiquitin-like protein (ubiquilin) that shares a high degree of similarity with related products in yeast, rat and frog. Ubiquilins contain an N-terminal ubiquitin-like domain and a C-terminal ubiquitin-associated domain. They physically associate with both proteasomes and ubiquitin ligases, and thus are thought to functionally link the ubiquitination machinery to the proteasome to affect in vivo protein degradation. This ubiquilin has also been shown to modulate …

**Accessions** — [HGNC:12508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12508) · Entrez [29979](https://www.ncbi.nlm.nih.gov/gene/29979) · UniProt [Q9UMX0](https://www.uniprot.org/uniprotkb/Q9UMX0) · Ensembl [ENSG00000135018](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135018)

## Data

Gene col 5636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5636); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5636]; `tensor/DDL_lfc|DDL_z.npy` [5636]; `embed/gene_vectors.npy` [5636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5636 or target_col == 5636). Every well: [[UBQLN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UBQLN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
