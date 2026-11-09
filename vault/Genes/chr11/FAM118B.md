---
symbol: "FAM118B"
type: "gene"
col: 12466
ensembl_id: "ENSG00000197798"
name: "SIR2 antiphage like 1"
location: "11q24.2"
module: 129
arm: "+"
pooled_cpm: 16.14
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 2
n_dd_up_clean: 20
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# FAM118B

*SIR2 antiphage like 1* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.45× (z +28.9, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.773× (z -4.4, q 0.006, down in 16 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 0.05 µM: 0.789× (z -4.0, q 0.010, down in 10 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.262×, LoVo 0.246×, HepG2/C3A 0.122×; ⚠ toxic; transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.0863×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0702×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.100×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCSK7]] (+0.68, fdr 7e-06), [[RRP36]] (+0.63, fdr 7e-06), [[ZDHHC5]] (+0.60, fdr 3e-05); moves opposite to [[LSMEM1]] (-0.58, fdr 2e-04), [[CLK1]] (-0.52, fdr 3e-05), [[VAMP1]] (-0.51, fdr 4e-05).
> It is in [[Module 129]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12466.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.45×** | +28.9 | 0e+00 | 46/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.06×** | +27.6 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.56×** | +25.9 | 0e+00 | 46/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +13.2 | 2e-37 | 38/46 (CFPAC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +11.1 | 1e-26 | 41/47 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.94×** | +9.7 | 3e-20 | 34/46 (NCI-H23, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.68×** | +8.9 | 5e-17 | 35/47 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.71×** | +8.9 | 5e-17 | 31/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.41×** | +8.2 | 1e-14 | 25/47 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.74×** | +8.0 | 5e-14 | 27/42 (SW480, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.46×** | +8.0 | 5e-14 | 30/46 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.17×** | +6.9 | 3e-10 | 30/48 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.56×** | +6.5 | 4e-09 | 22/47 (PANC-1, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.4 | 6e-09 | 22/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.44×** | +6.2 | 3e-08 | 21/47 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +5.6 | 7e-07 | 18/48 (HOP62, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +5.2 | 7e-06 | 18/47 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +5.0 | 1e-05 | 14/47 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +4.7 | 7e-05 | 16/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12466.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SW480 0.262×, LoVo 0.246×, HepG2/C3A 0.122×; ⚠ toxic; transcription drop); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.0863×); [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM in 1 line (SW48 0.0702×); [[Cobimetinib (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.100×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.773×** | -4.4 | 0.006 | 16/38 (SW480, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -4.1 | 0.010 | 3/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **0.789×** | -4.0 | 0.010 | 10/48 (COLO 205, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.794× | -3.4 | 0.10 | 15/29 (PANC-1, SW 900, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.782× | -3.0 | 0.30 | 9/46 (NCI-H1573, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12466. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 26.5 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 4.98× (z +16.8) | — |
| [[SW480 (line)]] | alt | 21.1 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.85× (z +16.7) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -12.7) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 9.36 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.82× (z +11.1) | — |
| [[HEC-1-A (line)]] | alt | 11.8 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 6.57× (z +12.8) | [[Dinaciclib (drug)]] 0.05 µM 0.181× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 18.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.35× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -10.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 18.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.79× (z +11.0) | — |
| [[NCI-H460 (line)]] | wt | 11.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.53× (z +11.4) | — |
| [[A498 (line)]] | wt | 10.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +11.1) | — |
| [[A549 (line)]] | wt | 10.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.07× (z +9.6) | — |
| [[AsPC-1 (line)]] | alt | 14.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.41× (z +12.4) | — |
| [[HOP62 (line)]] | alt | 13.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.66× (z +13.9) | — |
| [[HS-578T (line)]] | alt | 15.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.64× (z +10.2) | — |
| [[HT-29 (line)]] | alt | 29.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.29× (z +10.4) | — |
| [[KATO III (line)]] | alt | 21.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.29× (z +13.7) | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.34× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 20.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.67× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 25.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +11.6) | — |
| [[NCI-H1792 (line)]] | alt | 10.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.89× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 13.0 | 3 | 0 | [[Belinostat (drug)]] 5 µM 4.90× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 22.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.51× (z +9.6) | — |
| [[SNU-423 (line)]] | alt | 10.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.02× (z +10.6) | — |
| [[SW1417 (line)]] | alt | 23.9 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.01× (z +12.3) | — |
| [[A-172 (line)]] | wt | 9.19 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 6.81× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 2 (1 ⚠) | — | [[Cobimetinib (drug)]] 0.05 µM 0.100× (z -9.3) |
| [[Hs 766T (line)]] | wt | 16.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.27× (z +10.8) | — |
| [[NCI-H2347 (line)]] | alt | 12.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +10.0) | — |
| [[RKO (line)]] | wt | 21.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.50× (z +9.1) | — |
| [[C32 (line)]] | wt | 16.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.45× (z +9.1) | — |
| [[COLO 205 (line)]] | alt | 17.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.27× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 15.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +9.0) | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0863× (z -11.6) |
| [[SW 900 (line)]] | alt | 15.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.83× (z +8.8) | — |
| [[SW48 (line)]] | wt | 14.5 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0702× (z -10.0) |
| [[A-427 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.39 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12466), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCSK7]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[RRP36]] | +0.63 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[ZDHHC5]] | +0.60 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[BMS1P4]] | +0.58 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[EMC8]] | +0.57 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NLK]] | +0.57 | +0.44 / +0.48 | both halves | 3e-05 |  |
| [[RMND5B]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[RNF34]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZNF16]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ZBED4]] | +0.55 | +0.33 / +0.48 | both halves | 1e-04 |  |
| [[ZGPAT]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[CIAPIN1]] | +0.55 | +0.63 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LSMEM1]] | -0.58 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[CLK1]] | -0.52 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[VAMP1]] | -0.51 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[KATNAL2]] | -0.50 | -0.23 / -0.33 | both halves | 5e-04 |  |
| [[STAG2]] | -0.50 | -0.37 / -0.51 | both halves | 8e-05 |  |
| [[HBP1]] | -0.50 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[GIPC2]] | -0.46 | -0.20 / -0.43 | both halves | 7e-04 |  |
| [[PCBP2]] | -0.46 | -0.35 / -0.38 | both halves | 1e-04 |  |
| [[CD27-AS1]] | -0.46 | -0.27 / -0.35 | both halves | 3e-04 |  |
| [[SPX]] | -0.46 | -0.37 / -0.38 | both halves | 9e-05 |  |
| [[TXNDC16]] | -0.46 | -0.29 / -0.22 | both halves | 6e-04 |  |
| [[MAP7D2]] | -0.46 | -0.30 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.398). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-48.8, 2.8); signed map (-11.9, -22.4). **Vector** length 62.4, 10.7% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.4 | +8.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.6 | +8.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | +1.9 | +8.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.4 | +1.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 0.5 µM |  | +1.3 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.7 | -1.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -3.4 |
|  | [[Selinexor (drug)]] 0.05 µM |  | -3.0 | -4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.6 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.4 | +0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Methylthiouracil (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.3 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | SIR2 antiphage like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:126,211,724-126,262,984 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SIRal, FLJ21103; previously FAM118B |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPY3](https://www.uniprot.org/uniprotkb/Q9BPY3) (SIR2 antiphage-like protein 1):

> Exhibits weak intrinsic NAD(+) nucleosidase activity, which is strongly stimulated upon interaction with its paralog SIRAL2 and the formation of SIRAL1-SIRAL2 filaments. Plays a key role in innate immunity by activating inflammation through the Toll-like receptor pathway probably through its NADase activity. May play a role in Cajal bodies formation.; (Microbial infection) Restricts the replication of herpes simplex virus 1 and Salmonella enterica in macrophages.

**Summary**, from NCBI Gene [79607](https://www.ncbi.nlm.nih.gov/gene/79607):

> Enables identical protein binding activity. Predicted to be located in Cajal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26110](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26110) · Entrez [79607](https://www.ncbi.nlm.nih.gov/gene/79607) · UniProt [Q9BPY3](https://www.uniprot.org/uniprotkb/Q9BPY3) · Ensembl [ENSG00000197798](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197798)

## Data

Gene col 12466: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12466); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12466, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12466]; `tensor/DDL_lfc|DDL_z.npy` [12466]; `embed/gene_vectors.npy` [12466]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12466 or target_col == 12466). Every well: [[FAM118B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM118B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
