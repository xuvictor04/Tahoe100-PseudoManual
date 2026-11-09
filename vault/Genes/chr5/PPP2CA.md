---
symbol: "PPP2CA"
type: "gene"
col: 3474
ensembl_id: "ENSG00000113575"
name: "protein phosphatase 2 catalytic subunit alpha"
location: "5q31.1"
module: 3
arm: "-"
pooled_cpm: 130.29
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# PPP2CA

*protein phosphatase 2 catalytic subunit alpha* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.14× (z +19.6, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.714× (z -5.7, q 3e-06, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD11]] (+0.74, fdr 7e-06), [[CENPBD1P]] (+0.71, fdr 7e-06), [[ZNF518B]] (+0.69, fdr 1e-05); moves opposite to [[MINDY2]] (-0.70, fdr 7e-06), [[GUK1]] (-0.67, fdr 1e-05), [[COMMD6]] (-0.65, fdr 7e-06).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3474.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.14×** | +19.6 | 0e+00 | 48/49 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +16.3 | 0e+00 | 46/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.44×** | +15.1 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.46×** | +13.2 | 7e-38 | 47/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.00×** | +11.7 | 9e-30 | 48/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.98×** | +11.5 | 8e-29 | 45/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.96×** | +11.4 | 3e-28 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.81×** | +10.0 | 7e-22 | 46/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.68×** | +8.8 | 1e-16 | 47/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 2e-14 | 43/48 (HT-29, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +8.0 | 7e-14 | 44/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +7.7 | 5e-13 | 44/47 (COLO 205, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.49×** | +6.4 | 8e-09 | 43/48 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.41×** | +5.8 | 2e-07 | 33/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +5.3 | 5e-06 | 30/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.2 | 8e-06 | 34/48 (HT-29, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.1 | 1e-05 | 30/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3474.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.714×** | -5.7 | 3e-06 | 40/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.715×** | -5.7 | 3e-06 | 35/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.770×** | -4.4 | 0.002 | 33/48 (A498, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.768×** | -4.3 | 0.002 | 26/44 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.782×** | -4.2 | 0.003 | 31/48 (LoVo, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.803×** | -3.7 | 0.018 | 26/48 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.805×** | -3.7 | 0.018 | 26/49 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.809×** | -3.5 | 0.035 | 27/48 (HOP62, H4, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.035 | 27/50 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.826×** | -3.2 | 0.065 | 25/48 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -3.1 | 0.090 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.778× | -3.0 | 0.11 | 22/48 (NCI-H460, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3474. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 116 | 13 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 4.83× (z +20.5) | — |
| [[PANC-1 (line)]] | alt | 112 | 13 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +18.9) | — |
| [[LoVo (line)]] | wt | 178 | 8 (2 ⚠) | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.520× (z -9.2) |
| [[LS 180 (line)]] | wt | 143 | 9 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.18× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.353× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 139 | 10 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 14.3× (z +19.4) | — |
| [[HOP62 (line)]] | alt | 129 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +14.9) | — |
| [[LOX-IMVI (line)]] | wt | 110 | 9 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 10.6× (z +14.5) | — |
| [[NCI-H1573 (line)]] | alt | 132 | 9 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 17.2× (z +18.2) | — |
| [[COLO 205 (line)]] | alt | 109 | 7 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 15.5× (z +13.8) | — |
| [[hTERT-HPNE (line)]] | wt | 98.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.6) | — |
| [[KATO III (line)]] | alt | 99.6 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.61× (z +15.7) | — |
| [[NCI-H23 (line)]] | alt | 132 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +14.2) | — |
| [[SW48 (line)]] | wt | 137 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.39× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 162 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 6.43× (z +11.7) | — |
| [[H4 (line)]] | wt | 122 | 6 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.24× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 129 | 6 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +15.7) | — |
| [[NCI-H1792 (line)]] | alt | 95.0 | 6 (2 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.14× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 113 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.9) | — |
| [[A549 (line)]] | wt | 115 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +20.7) | — |
| [[Hs 766T (line)]] | wt | 92.3 | 5 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +14.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 146 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +13.9) | — |
| [[NCI-H2030 (line)]] | alt | 129 | 5 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +12.7) | — |
| [[SNU-423 (line)]] | alt | 101 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +16.1) | — |
| [[A-172 (line)]] | wt | 119 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.4) | — |
| [[A498 (line)]] | wt | 107 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +19.4) | — |
| [[HEC-1-A (line)]] | alt | 177 | 4 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +13.7) | — |
| [[HS-578T (line)]] | alt | 124 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.1) | — |
| [[A-427 (line)]] | wt | 157 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.07× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -9.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 157 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +14.7) | — |
| [[C32 (line)]] | wt | 108 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 19.8× (z +13.0) | — |
| [[CFPAC-1 (line)]] | alt | 163 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.473× (z -8.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 150 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.15× (z +12.0) | — |
| [[HepG2_C3A (line)]] | wt | 138 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 6.26× (z +10.0) | — |
| [[J82 (line)]] | alt | 112 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.26× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 160 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.58× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -10.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 144 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 11.3× (z +14.6) | — |
| [[SK-MEL-2 (line)]] | alt | 169 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.14× (z +13.2) | — |
| [[SNU-1 (line)]] | wt | 132 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 11.4× (z +11.4) | — |
| [[SW1417 (line)]] | alt | 108 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 7.98× (z +11.0) | — |
| [[C-33 A (line)]] | alt | 152 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 5.96× (z +10.0) | — |
| [[RKO (line)]] | wt | 150 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 13.8× (z +14.9) | — |
| [[RPMI-7951 (line)]] | alt | 93.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.6× (z +11.9) | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.119× (z -9.1) |
| [[AN3 CA (line)]] | alt | 191 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 163 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3474), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD11]] | +0.74 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[CENPBD1P]] | +0.71 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[ZNF518B]] | +0.69 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[EWSR1]] | +0.68 | +0.73 / +0.67 | both halves | 7e-06 |  |
| [[SF3B4]] | +0.67 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[SNX19]] | +0.66 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[CEP41]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | pathway: G2/M Transition |
| [[DHX9]] | +0.64 | +0.74 / +0.68 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[C7orf25]] | +0.63 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PSMD1]] | +0.63 | +0.63 / +0.69 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[DCLRE1A]] | +0.63 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CAPRIN1]] | +0.62 | +0.53 / +0.68 | both halves | 1e-05 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MINDY2]] | -0.70 | -0.58 / -0.67 | both halves | 7e-06 |  |
| [[GUK1]] | -0.67 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[PI4KAP2]] | -0.65 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[AFMID]] | -0.64 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[SEC22A]] | -0.63 | -0.57 / -0.62 | both halves | 1e-05 |  |
| [[CBFA2T2]] | -0.62 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[B3GAT3]] | -0.62 | -0.55 / -0.55 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[ARID3A]] | -0.62 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[PGPEP1]] | -0.61 | -0.46 / -0.59 | both halves | 3e-05 |  |
| [[RPL36]] | -0.61 | -0.55 / -0.62 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC) |
| [[RPL37A]] ⚠ | -0.60 | -0.53 / -0.64 | both halves | 1e-05 | pathway: Nonsense Mediated Decay (NMD) enhanced by the Exon Junction Complex (EJC); ⚠ in the vector space only through flagged drug-doses |
| [[NARF]] | -0.60 | -0.67 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises PPP2CA's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.632). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-23.3, -10.6); signed map (3.4, -34.4). **Vector** length 79.8, 27.8% of its response variance represented; |z| ≥ 3 in 1,321 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.0 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | -4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.1 | -0.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.3 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +8.1 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +3.0 | +1.3 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +2.8 | +0.3 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | +15.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.3 | +11.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.1 | +0.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.8 | -2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.3 | -3.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.9 | -2.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.9 | -2.4 |
|  | [[ULK-101 (drug)]] 0.05 µM |  | -1.9 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 catalytic subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:134,194,035-134,226,073 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PP2Calpha, PP2AC |
| Gene groups (HGNC) | Protein phosphatase catalytic subunits; STRIPAK complex |
| Reactome | 128 pathways, smallest: PP2A-mediated dephosphorylation of key metabolic factors; MASTL Facilitates Mitotic Progression; Regulation of glycolysis by fructose 2,6-bisphosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P67775](https://www.uniprot.org/uniprotkb/P67775) (Serine/threonine-protein phosphatase 2A catalytic subunit alpha isoform):

> Catalytic subunit of protein phosphatase 2A (PP2A), a serine/threonine phosphatase involved in the regulation of a wide variety of enzymes, signal transduction pathways, and cellular events. PP2A is the major phosphatase for microtubule-associated proteins (MAPs). PP2A can modulate the activity of phosphorylase B kinase casein kinase 2, mitogen-stimulated S6 kinase, and MAP-2 kinase. Cooperates with SGO2 to protect centromeric cohesin from separase-mediated cleavage in oocytes specifically …

**Summary**, from NCBI Gene [5515](https://www.ncbi.nlm.nih.gov/gene/5515):

> This gene encodes the phosphatase 2A catalytic subunit. Protein phosphatase 2A is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. This gene encodes an alpha isoform of the catalytic subunit. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9299](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9299) · Entrez [5515](https://www.ncbi.nlm.nih.gov/gene/5515) · UniProt [P67775](https://www.uniprot.org/uniprotkb/P67775) · Ensembl [ENSG00000113575](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113575)

## Data

Gene col 3474: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3474); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3474, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3474]; `tensor/DDL_lfc|DDL_z.npy` [3474]; `embed/gene_vectors.npy` [3474]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3474 or target_col == 3474). Every well: [[PPP2CA — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2CA.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
