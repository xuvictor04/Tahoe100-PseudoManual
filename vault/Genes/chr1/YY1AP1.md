---
symbol: "YY1AP1"
type: "gene"
col: 8678
ensembl_id: "ENSG00000163374"
name: "YY1 associated protein 1"
location: "1q22"
module: 60
arm: "-"
pooled_cpm: 91.48
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# YY1AP1

*YY1 associated protein 1* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.01× (z +28.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.615× (z -8.0, q 8e-13, down in 34 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.778× (z -4.1, q 0.007, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PER1]] (+0.70, fdr 7e-06), [[ABCA5]] (+0.63, fdr 1e-05), [[KMT2E]] (+0.62, fdr 7e-06); moves opposite to [[CCT4]] (-0.67, fdr 7e-06), [[ARPC5]] (-0.66, fdr 7e-06), [[PRDX1]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[NFIX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8678.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.01×** | +28.8 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.64×** | +21.1 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **2.85×** | +16.5 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.70×** | +16.2 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.26×** | +13.3 | 2e-38 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.24×** | +13.2 | 1e-37 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.15×** | +12.2 | 4e-32 | 48/49 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +11.5 | 1e-28 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +9.6 | 7e-20 | 45/48 (NCI-H1573, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +6.1 | 4e-08 | 31/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.40×** | +5.4 | 3e-06 | 32/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.36×** | +5.0 | 3e-05 | 27/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.1 | 0.001 | 28/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.078 | 19/48 (NCI-H1573, CHP-212, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8678.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.615×** | -8.0 | 8e-13 | 34/49 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.606×** | -7.9 | 8e-13 | 32/44 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.778×** | -4.1 | 0.007 | 29/48 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.801×** | -3.7 | 0.035 | 25/48 (LOX-IMVI, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.805×** | -3.6 | 0.039 | 25/48 (J82, HT-29, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.077 | 22/49 (NCI-H2347, RPMI-7951, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.819×** | -3.3 | 0.077 | 18/48 (NCI-H1573, Panc 03.27, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.822×** | -3.2 | 0.085 | 22/48 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.826×** | -3.2 | 0.099 | 18/47 (hTERT-HPNE, J82, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.824× | -3.1 | 0.11 | 21/48 (RKO, SW480, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | 0.830× | -3.1 | 0.11 | 19/49 (J82, SW1417, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.832× | -3.0 | 0.11 | 20/48 (COLO 205, J82, …) | inconsistent across doses |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.833× | -3.0 | 0.11 | 17/49 (RKO, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8678. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 107 | 13 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +25.9) | [[Dinaciclib (drug)]] 5 µM 0.463× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 73.9 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +31.5) | — |
| [[NCI-H1573 (line)]] | alt | 110 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +19.1) | — |
| [[SW 900 (line)]] | alt | 137 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.0) | [[Dinaciclib (drug)]] 0.5 µM 0.360× (z -10.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 74.1 | 9 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.50× (z +19.3) | — |
| [[LoVo (line)]] | wt | 49.8 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.06× (z +20.0) | — |
| [[NCI-H23 (line)]] | alt | 146 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +19.2) | — |
| [[AsPC-1 (line)]] | alt | 84.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -9.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 95.9 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +17.1) | — |
| [[NCI-H2347 (line)]] | alt | 133 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.52× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.495× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 95.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.05× (z +25.0) | — |
| [[KATO III (line)]] | alt | 60.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.39× (z +17.4) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 90.0 | 6 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.30× (z +17.2) | — |
| [[NCI-H2030 (line)]] | alt | 129 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +20.3) | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 135 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.19× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.238× (z -15.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 63.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.7) | — |
| [[H4 (line)]] | wt | 68.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 65.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +17.8) | — |
| [[hTERT-HPNE (line)]] | wt | 71.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +15.8) | — |
| [[RPMI-7951 (line)]] | alt | 98.5 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -9.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 96.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.44× (z +25.0) | — |
| [[COLO 205 (line)]] | alt | 101 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +13.7) | — |
| [[HEC-1-A (line)]] | alt | 87.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +22.9) | — |
| [[Hs 766T (line)]] | wt | 87.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +17.0) | — |
| [[HT-29 (line)]] | alt | 71.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +18.8) | — |
| [[LS 180 (line)]] | wt | 67.7 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.55× (z +16.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 93.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +18.8) | — |
| [[Panc 03.27 (line)]] | alt | 96.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.47× (z +20.1) | — |
| [[RKO (line)]] | wt | 76.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.03× (z +20.1) | — |
| [[SNU-1 (line)]] | wt | 86.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 67.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +18.9) | — |
| [[SW1417 (line)]] | alt | 85.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +18.6) | — |
| [[SW48 (line)]] | wt | 65.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.32× (z +13.2) | — |
| [[A-427 (line)]] | wt | 72.5 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +14.6) | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +12.4) | — |
| [[J82 (line)]] | alt | 82.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +16.5) | — |
| [[LOX-IMVI (line)]] | wt | 77.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +15.2) | — |
| [[SK-MEL-2 (line)]] | alt | 84.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.107× (z -19.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 71.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 124 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +16.1) | — |
| [[CHP-212 (line)]] | wt | 129 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.6) | — |
| [[SHP-77 (line)]] | alt | 172 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.82× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 91.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 77.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 112 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[NCI-H661 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0633× (z -11.9) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 76.8 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0744× (z -8.9) |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 95.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8678), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER1]] | +0.70 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[ABCA5]] | +0.63 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[KMT2E]] | +0.62 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[SPACA9]] | +0.62 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[PATL1]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[LRRC27]] | +0.60 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[GALT]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[CLK4]] | +0.60 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[RCOR3]] | +0.60 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LSM14B]] | +0.59 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[DNAJC27]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PEX13]] | +0.59 | +0.57 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCT4]] | -0.67 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[ARPC5]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PRDX1]] | -0.65 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[CCT6A]] | -0.65 | -0.56 / -0.64 | both halves | 1e-05 |  |
| [[HSP90AA1]] | -0.64 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[CCT3]] | -0.64 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[HSPA8]] | -0.64 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[RAP1GDS1]] | -0.64 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[UTP11]] | -0.61 | -0.59 / -0.57 | both halves | 9e-06 |  |
| [[MTAP]] | -0.61 | -0.67 / -0.48 | both halves | 2e-05 |  |
| [[ACOT7]] | -0.60 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[HSP90AA2P]] | -0.58 | -0.52 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NFIX]] | B | NFIX activity lowers YY1AP1's level | lines that do not express NFIX (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without NFIX | 0.038 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **-** arm (projection on the module's main direction -0.642). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-20.9, -11.0); signed map (-9.4, 3.2). **Vector** length 67.4, 19.3% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.4 | +28.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.2 | -1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +0.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | -7.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +16.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | -1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.6 | -2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.2 | -0.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.2 | +1.0 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.4 | +0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | +2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -2.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.0 | -0.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.0 | -1.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | +0.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | YY1 associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:155,659,446-155,689,334 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YY1AP, HCCA2, YAP |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H869](https://www.uniprot.org/uniprotkb/Q9H869) (YY1-associated protein 1):

> Associates with the INO80 chromatin remodeling complex, which is responsible for transcriptional regulation, DNA repair, and replication. Enhances transcription activation by YY1. Plays a role in cell cycle regulation.

**Summary**, from NCBI Gene [55249](https://www.ncbi.nlm.nih.gov/gene/55249):

> Involved in cell differentiation; cell population proliferation; and regulation of cell cycle. Located in Ino80 complex; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30935) · Entrez [55249](https://www.ncbi.nlm.nih.gov/gene/55249) · UniProt [Q9H869](https://www.uniprot.org/uniprotkb/Q9H869) · Ensembl [ENSG00000163374](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163374)

## Data

Gene col 8678: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8678); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8678, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8678]; `tensor/DDL_lfc|DDL_z.npy` [8678]; `embed/gene_vectors.npy` [8678]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8678 or target_col == 8678). Every well: [[YY1AP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YY1AP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
