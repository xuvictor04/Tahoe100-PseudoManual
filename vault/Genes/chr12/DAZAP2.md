---
symbol: "DAZAP2"
type: "gene"
col: 11387
ensembl_id: "ENSG00000183283"
name: "DAZ associated protein 2"
location: "12q13.13"
module: 23
arm: "+"
pooled_cpm: 58.7
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# DAZAP2

*DAZ associated protein 2* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.77× (z +12.4, q 1e-32, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.547× (z -13.2, q 9e-37, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UFC1]] (+0.72, fdr 1e-05), [[SLC25A53]] (+0.67, fdr 2e-05), [[CELF6]] (+0.65, fdr 1e-05); moves opposite to [[PPM1G]] (-0.62, fdr 1e-04), [[BOLA3]] (-0.56, fdr 1e-04), [[NPM3]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +12.4 | 1e-32 | 39/48 (A-427, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.75×** | +12.1 | 2e-31 | 40/49 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.69×** | +11.0 | 1e-25 | 29/40 (NCI-H23, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +10.2 | 2e-22 | 33/44 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +9.7 | 4e-20 | 42/47 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +7.9 | 3e-13 | 40/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +7.6 | 2e-12 | 35/47 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.28×** | +7.6 | 2e-12 | 31/48 (PANC-1, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.0 | 2e-07 | 31/48 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.9 | 4e-05 | 21/49 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 9e-05 | 25/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **1.22×** | +4.4 | 5e-04 | 22/48 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.008 | 18/48 (LoVo, HS-578T, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.36×** | +3.5 | 0.018 | 14/47 (Hs 766T, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.17× | +3.4 | 0.028 | 10/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 1.16× | +3.0 | 0.097 | 11/48 (C-33 A, RPMI-7951, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11387.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.547×** | -13.2 | 9e-37 | 45/48 (LoVo, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.573×** | -12.2 | 1e-31 | 44/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.641×** | -9.7 | 5e-20 | 39/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.672×** | -8.7 | 6e-16 | 37/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.800×** | -6.9 | 5e-10 | 31/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.574×** | -6.3 | 2e-08 | 35/49 (HT-29, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.785×** | -5.3 | 1e-05 | 24/48 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.802×** | -4.8 | 9e-05 | 23/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.817×** | -4.3 | 0.001 | 20/48 (SW48, hTERT-HPNE, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -3.5 | 0.028 | 19/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -3.4 | 0.029 | 19/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.858× | -3.3 | 0.053 | 6/48 (KATO III, A498, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.085 | 9/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.868× | -3.0 | 0.11 | 15/48 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 55.3 | 8 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +19.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +11.3) | — |
| [[PANC-1 (line)]] | alt | 61.3 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.81× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 1.66× (z +9.6) | [[Belinostat (drug)]] 5 µM 0.514× (z -8.8) |
| [[A-172 (line)]] | wt | 36.5 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.90× (z +9.3) | — |
| [[LoVo (line)]] | wt | 82.3 | 3 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 2.46× (z +12.2) | [[Belinostat (drug)]] 5 µM 0.435× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 77.1 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.399× (z -10.6) |
| [[COLO 205 (line)]] | alt | 83.0 | 2 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.40× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.366× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 50.9 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.52× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 33.8 | 3 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.77× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 74.3 | 1 | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.63× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -11.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.453× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 84.8 | 2 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.29× (z +13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 2.34× (z +10.3) | [[Belinostat (drug)]] 5 µM 0.490× (z -8.7) |
| [[A-427 (line)]] | wt | 75.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.84× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.412× (z -10.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +10.9) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 40.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.5) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 49.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.42× (z +11.9) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 97.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.471× (z -9.7) |
| [[LS 180 (line)]] | wt | 68.5 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +8.7) | — |
| [[NCI-H1573 (line)]] | alt | 75.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -10.9) |
| [[SW480 (line)]] | alt | 91.9 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.12× (z +12.2) | — |
| [[A498 (line)]] | wt | 40.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +11.4) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HepG2_C3A (line)]] | wt | 65.1 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.358× (z -8.9) |
| [[NCI-H661 (line)]] | alt | 52.1 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0933× (z -9.4) |
| [[RKO (line)]] | wt | 42.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.97× (z +9.4) | — |
| [[SW48 (line)]] | wt | 60.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -11.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[AN3 CA (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 55.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 81.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 59.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 58.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 58.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UFC1]] | +0.72 | +0.50 / +0.73 | both halves | 1e-05 |  |
| [[SLC25A53]] | +0.67 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[CELF6]] | +0.65 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[ATP6V0C]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[MED28]] | +0.64 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[HEXA]] | +0.63 | +0.41 / +0.67 | both halves | 4e-05 |  |
| [[ATP6V1G1]] | +0.63 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[RRAGC-DT]] | +0.63 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[KMT2E-AS1]] | +0.62 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[FBXL19-AS1]] | +0.62 | +0.40 / +0.55 | both halves | 4e-05 |  |
| [[STX17-DT]] | +0.62 | +0.44 / +0.41 | both halves | 4e-05 |  |
| [[CAB39L]] | +0.61 | +0.42 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1G]] | -0.62 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[BOLA3]] | -0.56 | -0.59 / -0.35 | both halves | 1e-04 |  |
| [[NPM3]] | -0.55 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[NSMCE4A]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[HEATR3]] | -0.55 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[NUP93]] | -0.55 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PDSS1]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[TFB1M]] | -0.54 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[FAR1]] | -0.54 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[WASF3]] | -0.53 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[TRIM35]] | -0.53 | -0.49 / -0.37 | both halves | 8e-05 |  |
| [[HAUS7]] | -0.53 | -0.32 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises DAZAP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises DAZAP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HAUS7]] | C | HAUS7's natural level strengthens DAZAP2's drug response | HAUS7's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.62, reverse -0.13; direction not clear | 0.075 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (12.0, 13.1); signed map (19.1, -3.2). **Vector** length 104, 28.1% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.2 | +7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.8 | +12.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +6.0 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.9 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.7 | +7.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.8 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +1.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.9 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -4.9 | -9.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -4.5 | -4.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.4 | -13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -6.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -1.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | DAZ associated protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:51,238,724-51,271,362 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0058 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15038](https://www.uniprot.org/uniprotkb/Q15038) (DAZ-associated protein 2):

> In unstressed cells, promotes SIAH1-mediated polyubiquitination and degradation of the serine/threonine-protein kinase HIPK2, probably by acting as a loading factor that potentiates complex formation between HIPK2 and ubiquitin ligase SIAH1. In response to DNA damage, localizes to the nucleus following phosphorylation by HIPK2 and modulates the expression of a subset of TP53/p53 target genes by binding to TP53 at target gene promoters. This limits the expression of a number of cell …

**Summary**, from NCBI Gene [9802](https://www.ncbi.nlm.nih.gov/gene/9802):

> This gene encodes a proline-rich protein which interacts with the deleted in azoospermia (DAZ) and the deleted in azoospermia-like gene through the DAZ-like repeats. This protein also interacts with the transforming growth factor-beta signaling molecule SARA (Smad anchor for receptor activation), eukaryotic initiation factor 4G, and an E3 ubiquitinase that regulates its stability in splicing factor containing nuclear speckles. The encoded protein may function in various biological and …

**Accessions** — [HGNC:2684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2684) · Entrez [9802](https://www.ncbi.nlm.nih.gov/gene/9802) · UniProt [Q15038](https://www.uniprot.org/uniprotkb/Q15038) · Ensembl [ENSG00000183283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183283)

## Data

Gene col 11387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11387); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11387]; `tensor/DDL_lfc|DDL_z.npy` [11387]; `embed/gene_vectors.npy` [11387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11387 or target_col == 11387). Every well: [[DAZAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DAZAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
