---
symbol: "MAPRE1"
type: "gene"
col: 2127
ensembl_id: "ENSG00000101367"
name: "microtubule associated protein RP/EB family member 1"
location: "20q11.21"
module: 24
arm: "-"
pooled_cpm: 81.66
n_lines_expressing: 50
n_dd_up: 35
n_dd_down: 2
n_dd_up_clean: 21
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# MAPRE1

*microtubule associated protein RP/EB family member 1* — 20q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.95× (z +16.7, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 0.5 µM: 0.808× (z -3.8, q 0.045, down in 24 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR1]] (+0.74, fdr 7e-06), [[LIN7C]] (+0.71, fdr 1e-05), [[TARDBP]] (+0.71, fdr 7e-06); moves opposite to [[MALSU1]] (-0.76, fdr 1e-05), [[LAMTOR5]] (-0.74, fdr 1e-05), [[SMIM26]] (-0.74, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[NSUN5P1-1]] (-0.70, fdr 1e-05).
> It sits in the **-** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DSG2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2127.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.95×** | +16.7 | 0e+00 | 40/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.55×** | +15.9 | 0e+00 | 41/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **2.43×** | +15.7 | 0e+00 | 43/49 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.37×** | +15.2 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.78×** | +14.5 | 3e-45 | 48/49 (SW480, NCI-H2030, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.05×** | +11.7 | 1e-29 | 42/45 (SNU-423, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +11.6 | 2e-29 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.93×** | +11.2 | 3e-27 | 42/48 (NCI-H1792, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +10.8 | 1e-25 | 42/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.79×** | +10.3 | 4e-23 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **1.77×** | +10.1 | 3e-22 | 39/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +8.9 | 2e-17 | 39/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +8.9 | 4e-17 | 35/49 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.51×** | +8.5 | 8e-16 | 45/48 (SW480, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +8.2 | 1e-14 | 41/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +6.3 | 1e-08 | 38/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +6.2 | 2e-08 | 37/48 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.003 | 21/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.003 | 23/47 (HT-29, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2127.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 0.5 µM |  | **0.808×** | -3.8 | 0.045 | 24/48 (KATO III, SW 1088, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.810×** | -3.8 | 0.045 | 20/48 (HOP62, NCI-H2030, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.5 µM |  | 0.832× | -3.3 | 0.17 | 17/48 (KATO III, Panc 03.27, …) | all doses, flat |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.780× | -3.2 | 0.17 | 16/48 (HEC-1-A, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.840× | -3.1 | 0.17 | 20/48 (HOP62, NCI-H460, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.17 | 15/48 (NCI-H2030, C32, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2127. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 64.4 | 15 (6 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.70× (z +19.2) | — |
| [[NCI-H1792 (line)]] | alt | 76.0 | 11 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +21.0) | — |
| [[LoVo (line)]] | wt | 64.9 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.99× (z +15.5) | — |
| [[SW480 (line)]] | alt | 99.8 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.28× (z +14.7) | — |
| [[LOX-IMVI (line)]] | wt | 73.9 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +14.2) | — |
| [[KATO III (line)]] | alt | 92.2 | 7 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.68× (z +14.4) | — |
| [[A-172 (line)]] | wt | 61.3 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.40× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.84× (z +9.6) | — |
| [[A549 (line)]] | wt | 83.1 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.83× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 96.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 79.8 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.03× (z +11.8) | — |
| [[A498 (line)]] | wt | 50.1 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 84.2 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.57× (z +15.3) | — |
| [[CFPAC-1 (line)]] | alt | 57.5 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +12.6) | — |
| [[COLO 205 (line)]] | alt | 68.6 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +13.3) | — |
| [[Hs 766T (line)]] | wt | 103 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.16× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.65× (z +9.3) | — |
| [[J82 (line)]] | alt | 166 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.24× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 67.7 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +14.0) | — |
| [[SW 900 (line)]] | alt | 48.7 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 57.5 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 76.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.41× (z +14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.56× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 74.9 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +13.1) | — |
| [[SW1417 (line)]] | alt | 172 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.6) | — |
| [[HEC-1-A (line)]] | alt | 82.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 48.0 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 75.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 134 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.05× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 103 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.45× (z +12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[Panc 03.27 (line)]] | alt | 64.6 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.62× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.60× (z +8.8) | — |
| [[RKO (line)]] | wt | 78.4 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.36× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 95.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[SW48 (line)]] | wt | 97.5 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 55.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.80× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.59× (z +8.5) | — |
| [[HepG2_C3A (line)]] | wt | 113 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 47.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 56.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +8.5) | — |
| [[SNU-1 (line)]] | wt | 111 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.5× (z +9.2) | — |
| [[A-427 (line)]] | wt | 125 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 45.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +13.1) | — |
| [[HS-578T (line)]] | alt | 73.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +10.2) | — |
| [[SHP-77 (line)]] | alt | 68.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AN3 CA (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 84.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 157 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 129 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2127), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*36 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | +0.74 | +0.63 / +0.77 | both halves | 7e-06 | STRING 457 |
| [[LIN7C]] | +0.71 | +0.53 / +0.75 | both halves | 1e-05 |  |
| [[TARDBP]] | +0.71 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[NRAS]] | +0.70 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[TUG1]] | +0.69 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[YWHAZ]] | +0.69 | +0.55 / +0.72 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints; STRING 417 |
| [[SF3B4]] | +0.68 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[DDX3X]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CDC42]] | +0.68 | +0.49 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE; STRING 417 |
| [[EIF4G2]] | +0.68 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[PSME3]] | +0.67 | +0.57 / +0.70 | both halves | 9e-06 |  |
| [[DARS2]] | +0.67 | +0.59 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*64 of its nearest partners move opposite, 8 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MALSU1]] | -0.76 | -0.55 / -0.81 | both halves | 1e-05 |  |
| [[LAMTOR5]] | -0.74 | -0.53 / -0.80 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.74 | -0.55 / -0.77 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[NSUN5P1-1]] | -0.70 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[COMMD6]] | -0.70 | -0.51 / -0.78 | both halves | 1e-05 |  |
| [[NSUN5P2-1]] ⚠ | -0.70 | -0.40 / -0.72 | both halves | 5e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SELENOH]] | -0.70 | -0.44 / -0.79 | both halves | 3e-05 |  |
| [[ATP5MJ]] | -0.70 | -0.43 / -0.81 | both halves | 3e-05 | pathway: Organelle biogenesis and maintenance |
| [[MRPL23]] | -0.69 | -0.52 / -0.70 | both halves | 1e-05 |  |
| [[ELP2]] | -0.68 | -0.56 / -0.69 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.68 | -0.50 / -0.74 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.68 | -0.52 / -0.72 | both halves | 1e-05 |  |
| [[RPAIN]] | -0.67 | -0.38 / -0.71 | both halves | 6e-05 |  |
| [[EMC2]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DSG2]] | B | DSG2 activity lowers MAPRE1's level | lines that do not express DSG2 (11) vs lines expressing it (39) | 1.18× higher at baseline in the lines without DSG2 | 0.064 | ⚠ within organs, on part of the lines; also absent: KITLG, COBLL1, ETS2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **-** arm (projection on the module's main direction -0.761). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-36.8, -20.4); signed map (-14.9, -36.3). **Vector** length 104, 35.2% of its response variance represented; |z| ≥ 3 in 1,281 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +12.7 | +15.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +11.7 | +15.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +11.5 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +10.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | +6.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.0 | +1.1 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.7 | -2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -2.0 |
|  | [[Sunitinib (drug)]] 5 µM | ⚠ toxic | -2.7 | -3.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.4 | -2.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.4 | -2.1 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -2.4 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein RP/EB family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q11.21 — chr20:32,819,954-32,850,405 (+) |
| Ensembl biotype | protein_coding |
| Also known as | EB1 |
| Gene groups (HGNC) | Microtubule associated protein RP/EB family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 31 pathways, smallest: The role of GTSE1 in G2/M progression after G2 checkpoint; Loss of Nlp from mitotic centrosomes; Loss of proteins required for interphase microtubule organization from the centrosome |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15691](https://www.uniprot.org/uniprotkb/Q15691) (Microtubule-associated protein RP/EB family member 1):

> Plus-end tracking protein (+TIP) that binds to the plus-end of microtubules and regulates the dynamics of the microtubule cytoskeleton. Recruits other +TIP proteins to microtubules by binding to a conserved Ser-Xaa-Leu-Pro (SXLP) motif in their polypeptide chains. Promotes cytoplasmic microtubule nucleation and elongation. Involved in mitotic spindle positioning by stabilizing microtubules and promoting dynamic connection between astral microtubules and the cortex during mitotic chromosome …

**Summary**, from NCBI Gene [22919](https://www.ncbi.nlm.nih.gov/gene/22919):

> The protein encoded by this gene was first identified by its binding to the APC protein which is often mutated in familial and sporadic forms of colorectal cancer. This protein localizes to microtubules, especially the growing ends, in interphase cells. During mitosis, the protein is associated with the centrosomes and spindle microtubules. The protein also associates with components of the dynactin complex and the intermediate chain of cytoplasmic dynein. Because of these associations, it is …

**Accessions** — [HGNC:6890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6890) · Entrez [22919](https://www.ncbi.nlm.nih.gov/gene/22919) · UniProt [Q15691](https://www.uniprot.org/uniprotkb/Q15691) · Ensembl [ENSG00000101367](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101367)

## Data

Gene col 2127: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2127); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2127, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2127]; `tensor/DDL_lfc|DDL_z.npy` [2127]; `embed/gene_vectors.npy` [2127]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2127 or target_col == 2127). Every well: [[MAPRE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPRE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
