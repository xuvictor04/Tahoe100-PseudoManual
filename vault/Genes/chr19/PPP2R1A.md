---
symbol: "PPP2R1A"
type: "gene"
col: 2621
ensembl_id: "ENSG00000105568"
name: "protein phosphatase 2 scaffold subunit Aalpha"
location: "19q13.41"
module: 153
arm: "+"
pooled_cpm: 69.47
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 8
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# PPP2R1A

*protein phosphatase 2 scaffold subunit Aalpha* — 19q13.41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.55× (z +11.6, q 3e-28, up in 38 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.28× (z +11.4, q 7e-28, up in 40 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.512× (z -17.8, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB1B]] (+0.71, fdr 2e-05), [[ATP13A1]] (+0.70, fdr 3e-05), [[WIZ]] (+0.69, fdr 3e-05); moves opposite to [[TMEM191A-1]] (-0.54, fdr 0.002, ⚠ one half only (not replicated)), [[CAMLG]] (-0.53, fdr 3e-04), [[RHEBL1]] (-0.52, fdr 6e-05), [[DNAJC1]] (-0.51, fdr 9e-05).
> It is in [[Module 153]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2621.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +11.6 | 3e-28 | 38/48 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.28×** | +11.4 | 7e-28 | 40/49 (LoVo, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +10.6 | 4e-24 | 32/43 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.40×** | +8.2 | 3e-14 | 30/45 (Panc 03.27, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +7.8 | 5e-13 | 36/48 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.69×** | +7.3 | 3e-11 | 31/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.24×** | +5.8 | 6e-07 | 22/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +5.4 | 5e-06 | 0/49 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.4 | 5e-06 | 26/48 (C-33 A, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.20×** | +4.5 | 3e-04 | 23/47 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.0 | 0.003 | 15/37 (HEC-1-A, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.021 | 14/47 (HEC-1-A, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 1.14× | +3.5 | 0.022 | 14/48 (HEC-1-A, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.16× | +3.3 | 0.039 | 9/48 (A549, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | 1.13× | +3.3 | 0.039 | 10/49 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.041 | 11/47 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.17× | +3.0 | 0.090 | 10/48 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2621.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.512×** | -17.8 | 0e+00 | 48/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.533×** | -16.7 | 0e+00 | 47/48 (NCI-H460, H4, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.619×** | -12.7 | 9e-35 | 43/48 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.660×** | -11.0 | 4e-26 | 42/48 (SW1417, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.666×** | -10.8 | 4e-25 | 44/48 (Panc 03.27, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -8.6 | 7e-16 | 34/48 (SW 1271, HT-29, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.545×** | -8.4 | 3e-15 | 42/49 (HEC-1-A, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.730×** | -8.0 | 6e-14 | 35/48 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.840× | -6.6 | 3e-09 | 22/48 (LOX-IMVI, CHP-212, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | **0.829×** | -4.8 | 1e-04 | 20/47 (H4, C-33 A, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.841× | -4.4 | 5e-04 | 20/49 (A498, NCI-H2030, …) | top dose only |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.823×** | -4.3 | 9e-04 | 15/48 (C-33 A, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Alpelisib (drug)]] 5 µM |  | **0.750×** | -4.0 | 0.003 | 21/47 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 0.864× | -3.9 | 0.004 | 12/48 (SNU-1, BT-474, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.865× | -3.9 | 0.004 | 15/48 (NCI-H2030, SW48, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.876× | -3.5 | 0.014 | 10/48 (KATO III, NCI-H2030, …) | rises with dose |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.917× | -3.2 | 0.035 | 4/48 (COLO 205, Hs 766T, …) | top dose only |  |
| [[Sulfatinib (drug)]] 0.05 µM |  | 0.889× | -2.9 | 0.098 | 13/48 (SW1417, HepG2/C3A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2621. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 50.1 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.57× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.87× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.512× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 55.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.06× (z +9.4) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.391× (z -12.8) |
| [[A549 (line)]] | wt | 83.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.481× (z -9.6) |
| [[C-33 A (line)]] | alt | 91.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.414× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 98.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 1.86× (z +9.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.553× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 65.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.383× (z -12.2) |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.409× (z -12.2) |
| [[SW480 (line)]] | alt | 68.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.78× (z +9.1) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.487× (z -11.4) |
| [[H4 (line)]] | wt | 130 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.301× (z -12.3) |
| [[HOP62 (line)]] | alt | 49.5 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.444× (z -9.3) |
| [[HT-29 (line)]] | alt | 72.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -10.0) |
| [[KATO III (line)]] | alt | 85.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.473× (z -9.8) |
| [[MIA PaCa-2 (line)]] | alt | 90.5 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.59× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 71.8 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.343× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 59.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.40× (z +8.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.345× (z -11.3) |
| [[SW 900 (line)]] | alt | 77.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.390× (z -9.6) |
| [[A-427 (line)]] | wt | 58.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.55× (z +10.2) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 51.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.473× (z -8.6) |
| [[BT-474 (line)]] | alt | 71.8 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.203× (z -9.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 62.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 41.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.377× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 53.8 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -21.3) |
| [[NCI-H596 (line)]] | alt | 63.6 | 1 | 0 | [[Methylthiouracil (drug)]] 5 µM 2.25× (z +9.2) | — |
| [[RKO (line)]] | wt | 83.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -10.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 90.9 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.509× (z -9.8) |
| [[A-172 (line)]] | wt | 80.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 84.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 56.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 59.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 74.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 75.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 98.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 75.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 54.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2621), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB1B]] | +0.71 | +0.48 / +0.75 | both halves | 2e-05 | pathway: Mitotic Prophase |
| [[ATP13A1]] | +0.70 | +0.46 / +0.72 | both halves | 3e-05 |  |
| [[WIZ]] | +0.69 | +0.43 / +0.71 | both halves | 3e-05 |  |
| [[RAB11B]] | +0.68 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[PIGT]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | same gene group |
| [[RBM4]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SZRD1]] | +0.65 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SRRM2]] | +0.65 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[NCSTN]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[VPS52]] | +0.64 | +0.41 / +0.70 | both halves | 4e-05 |  |
| [[HNRNPL]] | +0.63 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[U2AF2]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM191A-1]] | -0.54 | -0.13 / -0.60 | ⚠ one half (not replicated) | 0.002 |  |
| [[CAMLG]] | -0.53 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[RHEBL1]] | -0.52 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[DNAJC1]] | -0.51 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[GPR157]] | -0.51 | -0.26 / -0.47 | both halves | 3e-04 |  |
| [[TRAPPC4]] | -0.50 | -0.17 / -0.55 | ⚠ one half (not replicated) | 0.001 | same gene group |
| [[CARD19]] | -0.49 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[MPG]] | -0.49 | -0.03 / -0.48 | ⚠ not reproduced | 0.006 |  |
| [[PDCD5]] | -0.49 | -0.41 / -0.44 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.714). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.4, -23.8); signed map (-14.4, -34.4). **Vector** length 94.0, 22.0% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +11.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +8.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +11.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +7.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.0 | +4.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.7 | +1.3 |
|  | [[Folic acid (drug)]] 5 µM |  | +2.3 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +0.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~3% of this change | -4.8 | -4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -8.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.4 | -11.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.4 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.0 | -10.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.2 | -8.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | -0.8 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 2 scaffold subunit Aalpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.41 — chr19:52,170,936-52,229,518 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PR65A, PP2A-Aalpha, PP2AA |
| Gene groups (HGNC) | Protein phosphatase 2 scaffold subunits; STRIPAK complex; Armadillo like helical domain containing; MicroRNA protein coding host genes |
| Reactome | 139 pathways, smallest: PP2A-mediated dephosphorylation of key metabolic factors; MASTL Facilitates Mitotic Progression; Regulation of glycolysis by fructose 2,6-bisphosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P30153](https://www.uniprot.org/uniprotkb/P30153) (Serine/threonine-protein phosphatase 2A 65 kDa regulatory subunit A alpha isoform):

> The PR65 subunit of protein phosphatase 2A serves as a scaffolding molecule to coordinate the assembly of the catalytic subunit and a variable regulatory B subunit. Upon interaction with GNA12 promotes dephosphorylation of microtubule associated protein TAU/MAPT. Required for proper chromosome segregation and for centromeric localization of SGO1 in mitosis. Together with RACK1 adapter, mediates dephosphorylation of AKT1 at 'Ser-473', preventing AKT1 activation and AKT-mTOR signaling pathway (By …

**Summary**, from NCBI Gene [5518](https://www.ncbi.nlm.nih.gov/gene/5518):

> This gene encodes a constant regulatory subunit of protein phosphatase 2. Protein phosphatase 2 is one of the four major Ser/Thr phosphatases, and it is implicated in the negative control of cell growth and division. It consists of a common heteromeric core enzyme, which is composed of a catalytic subunit and a constant regulatory subunit, that associates with a variety of regulatory subunits. The constant regulatory subunit A serves as a scaffolding molecule to coordinate the assembly of the …

**Accessions** — [HGNC:9302](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9302) · Entrez [5518](https://www.ncbi.nlm.nih.gov/gene/5518) · UniProt [P30153](https://www.uniprot.org/uniprotkb/P30153) · Ensembl [ENSG00000105568](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105568)

## Data

Gene col 2621: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2621); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2621, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2621]; `tensor/DDL_lfc|DDL_z.npy` [2621]; `embed/gene_vectors.npy` [2621]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2621 or target_col == 2621). Every well: [[PPP2R1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP2R1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
