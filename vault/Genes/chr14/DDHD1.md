---
symbol: "DDHD1"
type: "gene"
col: 1979
ensembl_id: "ENSG00000100523"
name: "DDHD domain containing 1"
location: "14q22.1"
module: 134
arm: "+"
pooled_cpm: 76.95
n_lines_expressing: 48
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/134"]
generated_by: "tahoemap"
---

# DDHD1

*DDHD domain containing 1* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Belinostat (drug)]] 0.5 µM: 1.53× (z +10.3, q 2e-22, up in 38 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.685× (z -8.9, q 4e-16, down in 28 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.769× (z -6.2, q 1e-07, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIAA1958]] (+0.61, fdr 1e-05), [[ADGRL1]] (+0.60, fdr 1e-05), [[PIAS2]] (+0.58, fdr 1e-05); moves opposite to [[MAU2]] (-0.46, fdr 6e-05), [[VPS39]] (-0.46, fdr 3e-05), [[PRMT2]] (-0.46, fdr 3e-05).
> It is in [[Module 134]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[SOBP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1979.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +10.3 | 2e-22 | 38/46 (SW1417, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.35×** | +10.3 | 2e-22 | 27/46 (SW48, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.25×** | +10.1 | 8e-22 | 34/47 (PANC-1, SW48, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.51×** | +10.1 | 9e-22 | 37/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +9.5 | 3e-19 | 34/46 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +9.2 | 3e-18 | 26/47 (NCI-H1573, A498, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.46×** | +9.1 | 6e-18 | 35/46 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.38×** | +7.9 | 3e-13 | 26/46 (H4, SW480, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.35×** | +7.3 | 2e-11 | 29/46 (PANC-1, NCI-H1573, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +6.8 | 7e-10 | 32/47 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +6.1 | 7e-08 | 20/46 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 1e-07 | 28/47 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.27×** | +5.8 | 2e-07 | 23/46 (PANC-1, CFPAC-1, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.20×** | +4.5 | 3e-04 | 24/46 (HOP62, CFPAC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.41×** | +4.3 | 6e-04 | 19/42 (RPMI-7951, LoVo, …) | top dose only | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.015 | 11/46 (LOX-IMVI, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.016 | 13/46 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.018 | 17/46 (NCI-H460, A549, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.029 | 11/46 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.13× | +2.9 | 0.083 | 10/47 (NCI-H1573, A549, …) | top dose only | plate-row cell shift |
| [[Lopinavir (drug)]] 5 µM |  | 1.13× | +2.9 | 0.091 | 8/45 (NCI-H1573, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1979.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -8.9 | 4e-16 | 28/42 (Panc 03.27, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.709×** | -8.4 | 1e-14 | 28/46 (SK-MEL-2, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.769×** | -6.2 | 1e-07 | 28/46 (SK-MEL-2, C32, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -5.9 | 5e-07 | 1/48 (MIA PaCa-2) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.846× | -5.8 | 8e-07 | 17/46 (C32, CHP-212, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.739×** | -5.0 | 5e-05 | 27/46 (SW 1271, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.849× | -4.4 | 0.001 | 13/46 (NCI-H23, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.768×** | -3.3 | 0.070 | 10/47 (AN3 CA, SK-MEL-2, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.823×** | -3.3 | 0.073 | 17/46 (Hs 766T, AN3 CA, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.825×** | -3.2 | 0.079 | 13/46 (RKO, SW480, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1979. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 67.0 | 7 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +17.0) | — |
| [[SW48 (line)]] | wt | 193 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +26.7) | — |
| [[PANC-1 (line)]] | alt | 56.9 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.7) | — |
| [[A498 (line)]] | wt | 25.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +23.5) | — |
| [[RKO (line)]] | wt | 163 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -16.8) |
| [[CFPAC-1 (line)]] | alt | 36.7 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +22.1) | — |
| [[NCI-H2030 (line)]] | alt | 144 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.325× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 45.2 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +21.7) | — |
| [[NCI-H460 (line)]] | wt | 89.9 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.491× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.543× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 101 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -23.7) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 65.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 93.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +11.7) ⚠ cell-cycle shift, explains ~21% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 71.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.198× (z -18.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 71.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.394× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 94.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +13.7) | — |
| [[A549 (line)]] | wt | 63.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +15.1) | — |
| [[C-33 A (line)]] | alt | 180 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -9.6) |
| [[CHP-212 (line)]] | wt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0813× (z -16.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 21.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 85.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.22× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 67.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 79.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -13.0) |
| [[SHP-77 (line)]] | alt | 194 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.509× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 170 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.102× (z -11.0) |
| [[SW 900 (line)]] | alt | 80.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +17.2) | — |
| [[SW1417 (line)]] | alt | 72.3 | 1 | 0 | [[Belinostat (drug)]] 0.5 µM 2.13× (z +9.1) | — |
| [[A-172 (line)]] | wt | 51.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 173 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 45.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 60.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.98 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 102 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 82.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 86.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 74.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 83.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1979), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIAA1958]] | +0.61 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[ADGRL1]] | +0.60 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PIAS2]] | +0.58 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[ASIC1]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[POLR3G]] | +0.57 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[FAM117B]] | +0.57 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[SERGEF]] | +0.56 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[CACNB4]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[RIMKLA]] | +0.55 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[LRP5L]] | +0.54 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[HK1]] | +0.54 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[UGT8]] | +0.54 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAU2]] | -0.46 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[VPS39]] | -0.46 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PRMT2]] | -0.46 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[N4BP2L2]] | -0.45 | -0.46 / -0.40 | both halves | 5e-05 |  |
| [[ATP6V1G1]] | -0.44 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[PSORS1C1]] | -0.44 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[PMF1]] | -0.43 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[NFX1]] | -0.42 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | SOBP activity raises DDHD1's level | lines that do not express SOBP (19) vs lines expressing it (31) | 2.08× lower at baseline in the lines without SOBP | 0.060 | ⚠ within organs, on part of the lines; also absent: ANK2, TMEM145, SYT11 |
| [[PALS2]] | C | PALS2 activity raises DDHD1's level | lines that do not express PALS2 (3) vs lines expressing it (47) | 3.63× lower at baseline in the lines without PALS2 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: TMCC2, SACS, ANKRD44; maybe low, not absent |
| [[ASIC1]] | C | ASIC1 activity raises DDHD1's level | lines that do not express ASIC1 (3) vs lines expressing it (47) | 3.76× lower at baseline in the lines without ASIC1 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: TBC1D19, C1orf216, ZNF391; co-absent with the target |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 134]]; 35 genes; every member is in the + arm (projection on the module's main direction 0.663). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.8, -12.5); signed map (-43.1, 25.2). **Vector** length 110, 30.0% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +8.4 | +10.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.1 | +9.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.1 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.8 | +9.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +3.2 | +2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +3.5 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.7 | -5.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.6 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | +0.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.8 | -6.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -5.0 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | DDHD domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:53,036,745-53,153,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1705, PA-PLA1, iPLA1alpha, PAPLA1, iPLA1α; previously SPG28 |
| Reactome | 4 pathways, smallest: Synthesis of PA; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NEL9](https://www.uniprot.org/uniprotkb/Q8NEL9) (Phospholipase DDHD1):

> Phospholipase A1 (PLA1) that hydrolyzes ester bonds at the sn-1 position of glycerophospholipids producing a free fatty acid and a lysophospholipid (Probable). Prefers phosphatidate (1,2-diacyl-sn-glycero-3-phosphate, PA) as substrate in vitro, but can efficiently hydrolyze phosphatidylinositol (1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol), PI), as well as a range of other glycerophospholipid substrates such as phosphatidylcholine (1,2-diacyl-sn-glycero-3-phosphocholine, PC), …

**Summary**, from NCBI Gene [80821](https://www.ncbi.nlm.nih.gov/gene/80821):

> This gene is a member of the intracellular phospholipase A1 gene family. The protein encoded by this gene preferentially hydrolyzes phosphatidic acid. It is a cytosolic protein with some mitochondrial localization, and is thought to be involved in the regulation of mitochondrial dynamics. Overexpression of this gene causes fragmentation of the tubular structures in mitochondria, while depletion of the gene results in mitochondrial tubule elongation. Deletion of this gene in male mice caused …

**Accessions** — [HGNC:19714](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19714) · Entrez [80821](https://www.ncbi.nlm.nih.gov/gene/80821) · UniProt [Q8NEL9](https://www.uniprot.org/uniprotkb/Q8NEL9) · Ensembl [ENSG00000100523](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100523)

## Data

Gene col 1979: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1979); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1979, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1979]; `tensor/DDL_lfc|DDL_z.npy` [1979]; `embed/gene_vectors.npy` [1979]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1979 or target_col == 1979). Every well: [[DDHD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDHD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
