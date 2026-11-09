---
symbol: "MKRN1"
type: "gene"
col: 5455
ensembl_id: "ENSG00000133606"
name: "makorin ring finger protein 1"
location: "7q34"
module: 69
arm: "+"
pooled_cpm: 110.25
n_lines_expressing: 50
n_dd_up: 1
n_dd_down: 18
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# MKRN1

*makorin ring finger protein 1* — 7q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.25× (z +7.0, q 2e-09, up in 28 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.52×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.11×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.497× (z -15.7, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.715× (z -10.5, q 3e-23, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM59]] (+0.75, fdr 7e-06), [[PCMTD1]] (+0.75, fdr 7e-06), [[CCDC28A]] (+0.73, fdr 7e-06); moves opposite to [[SMARCA4]] (-0.67, fdr 7e-06), [[ANAPC7]] (-0.64, fdr 7e-06), [[DDX10]] (-0.64, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5455.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[PH-797804 (drug)]] 5 µM in 1 line (C32 4.52×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.11×); [[Dinaciclib (drug)]] 5 µM in 1 line (A-427 2.12×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.25×** | +7.0 | 2e-09 | 28/49 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.17× | +5.0 | 1e-04 | 19/48 (J82, HS-578T, …) | top dose only | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~1% of this change | 1.17× | +3.5 | 0.081 | 16/48 (SW 1271, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 1.14× | +3.0 | 0.37 | 10/48 (LOX-IMVI, A-427, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5455.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.497×** | -15.7 | 0e+00 | 48/48 (NCI-H2347, AsPC-1, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.715×** | -10.5 | 3e-23 | 36/48 (AN3 CA, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.705×** | -7.5 | 1e-11 | 40/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.734×** | -6.9 | 6e-10 | 33/48 (AsPC-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[EX229 (drug)]] 5 µM |  | **0.559×** | -6.8 | 1e-09 | 33/48 (SW1417, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.564×** | -6.7 | 2e-09 | 44/48 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.565×** | -6.7 | 2e-09 | 35/48 (A498, NCI-H2347, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.580×** | -6.4 | 1e-08 | 37/48 (NCI-H2347, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.697×** | -5.8 | 5e-07 | 33/48 (PANC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.761×** | -5.6 | 9e-07 | 29/45 (hTERT-HPNE, C32, …) | inconsistent across doses | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.621×** | -5.6 | 1e-06 | 32/48 (MIA PaCa-2, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.780×** | -5.6 | 1e-06 | 35/49 (BT-474, NCI-H23, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.937× | -5.0 | 3e-05 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.804×** | -4.9 | 5e-05 | 28/48 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.816×** | -4.6 | 2e-04 | 24/48 (AsPC-1, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.761×** | -4.4 | 5e-04 | 26/49 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.732×** | -3.6 | 0.009 | 21/47 (PANC-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.796×** | -3.6 | 0.009 | 22/48 (PANC-1, hTERT-HPNE, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.854× | -3.4 | 0.020 | 14/48 (NCI-H2347, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.903× | -3.1 | 0.044 | 12/48 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.867× | -3.0 | 0.067 | 12/47 (SW 900, MIA PaCa-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5455. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 130 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -17.1) |
| [[NCI-H2347 (line)]] | alt | 196 | 0 | 5 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.398× (z -14.3) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.578× (z -11.9) |
| [[PANC-1 (line)]] | alt | 97.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.525× (z -14.8) |
| [[C32 (line)]] | wt | 227 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.52× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.492× (z -9.1) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 96.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -11.0) |
| [[KATO III (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.451× (z -11.1) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 111 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -13.1) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.483× (z -12.3) |
| [[COLO 205 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.404× (z -10.1) ⚠ cell-cycle shift, explains ~55% of this change |
| [[NCI-H23 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.412× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.454× (z -9.9) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.587× (z -9.3) |
| [[SW 900 (line)]] | alt | 126 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -8.7) |
| [[SW48 (line)]] | wt | 154 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.310× (z -12.0) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 57.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.8) |
| [[A-427 (line)]] | wt | 77.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.12× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[A498 (line)]] | wt | 145 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.451× (z -10.9) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 97.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.463× (z -9.2) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -18.2) |
| [[BT-474 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.125× (z -12.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 126 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -10.1) |
| [[HCT15 (line)]] | alt | 141 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 86.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.506× (z -9.2) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.490× (z -10.2) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.476× (z -9.6) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 74.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 98.4 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.449× (z -9.9) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 74.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.457× (z -10.9) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 65.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -8.9) |
| [[SNU-423 (line)]] | alt | 96.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.6) |
| [[SW1417 (line)]] | alt | 216 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.493× (z -11.7) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.505× (z -11.1) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 92.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 78.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 84.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 69.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 111 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 85.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 120 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 80.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 92.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5455), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM59]] | +0.75 | +0.64 / +0.83 | both halves | 7e-06 |  |
| [[PCMTD1]] | +0.75 | +0.66 / +0.81 | both halves | 7e-06 |  |
| [[CCDC28A]] | +0.73 | +0.74 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[WIPI2]] | +0.73 | +0.68 / +0.77 | both halves | 7e-06 |  |
| [[KLHDC3]] | +0.71 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[TCP11L2]] | +0.70 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.70 | +0.59 / +0.74 | both halves | 7e-06 |  |
| [[SERINC1]] | +0.69 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.69 | +0.56 / +0.78 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[RALBP1]] | +0.66 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[YPEL5]] | +0.65 | +0.56 / +0.76 | both halves | 1e-05 | pathway: HALLMARK_HEME_METABOLISM |
| [[CPEB3]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMARCA4]] | -0.67 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.64 | -0.69 / -0.61 | both halves | 7e-06 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[DDX10]] | -0.64 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[CEP83]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[NAA15]] | -0.62 | -0.44 / -0.65 | both halves | 3e-05 |  |
| [[NOC3L]] | -0.62 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[UQCC2]] | -0.60 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.60 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[ABCE1]] | -0.60 | -0.62 / -0.58 | both halves | 7e-06 |  |
| [[THOP1]] | -0.60 | -0.57 / -0.57 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[MPHOSPH6]] | -0.59 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.0, -45.0); signed map (-18.5, 9.5). **Vector** length 130, 37.9% of its response variance represented; |z| ≥ 3 in 915 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +7.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | +5.7 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~1% of this change | +3.7 | +3.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +1.5 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +2.6 | +1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.5 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.9 | -15.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.9 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.4 | -6.7 |
|  | [[EX229 (drug)]] 5 µM |  | -7.3 | -6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.7 | -6.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.5 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | makorin ring finger protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q34 — chr7:140,453,033-140,479,536 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNF61 |
| Gene groups (HGNC) | Ring finger proteins; Zinc fingers CCCH-type; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 8 pathways, smallest: AKT phosphorylates targets in the cytosol; Regulation of PTEN stability and activity; PTEN Regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UHC7](https://www.uniprot.org/uniprotkb/Q9UHC7) (E3 ubiquitin-protein ligase makorin-1):

> E3 ubiquitin ligase catalyzing the covalent attachment of ubiquitin moieties onto substrate proteins. These substrates include FILIP1, p53/TP53, CDKN1A and TERT. Keeps cells alive by suppressing p53/TP53 under normal conditions, but stimulates apoptosis by repressing CDKN1A under stress conditions. Acts as a negative regulator of telomerase. Has negative and positive effects on RNA polymerase II-dependent transcription.

**Summary**, from NCBI Gene [23608](https://www.ncbi.nlm.nih.gov/gene/23608):

> This gene encodes a protein that belongs to a novel class of zinc finger proteins. The encoded protein functions as a transcriptional co-regulator, and as an E3 ubiquitin ligase that promotes the ubiquitination and proteasomal degradation of target proteins. The protein encoded by this gene is thought to regulate RNA polymerase II-catalyzed transcription. Substrates for this protein's E3 ubiquitin ligase activity include the capsid protein of the West Nile virus and the catalytic subunit of the …

**Accessions** — [HGNC:7112](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7112) · Entrez [23608](https://www.ncbi.nlm.nih.gov/gene/23608) · UniProt [Q9UHC7](https://www.uniprot.org/uniprotkb/Q9UHC7) · Ensembl [ENSG00000133606](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133606)

## Data

Gene col 5455: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5455); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5455, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5455]; `tensor/DDL_lfc|DDL_z.npy` [5455]; `embed/gene_vectors.npy` [5455]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5455 or target_col == 5455). Every well: [[MKRN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MKRN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
