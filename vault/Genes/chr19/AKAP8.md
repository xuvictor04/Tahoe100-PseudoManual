---
symbol: "AKAP8"
type: "gene"
col: 2548
ensembl_id: "ENSG00000105127"
name: "A-kinase anchoring protein 8"
location: "19p13.12"
module: 156
arm: "+"
pooled_cpm: 35.54
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# AKAP8

*A-kinase anchoring protein 8* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 3.17× (z +16.4, q 0e+00, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.388× (z -25.7, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRCC]] (+0.74, fdr 7e-06), [[ZNF263]] (+0.69, fdr 7e-06), [[MIEF1]] (+0.68, fdr 7e-06); moves opposite to [[SPAG9]] (-0.63, fdr 7e-05), [[PICALM]] (-0.63, fdr 4e-05), [[AFDN]] (-0.61, fdr 1e-04).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2548.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **3.17×** | +16.4 | 0e+00 | 40/48 (SW480, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.82×** | +14.8 | 0e+00 | 45/49 (SW480, LoVo, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.68×** | +7.4 | 3e-11 | 29/43 (SW480, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.30×** | +6.8 | 1e-09 | 27/48 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +6.2 | 5e-08 | 21/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +6.0 | 2e-07 | 21/48 (J82, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.24×** | +5.8 | 6e-07 | 20/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.22×** | +5.4 | 5e-06 | 20/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +5.0 | 4e-05 | 14/48 (HOP62, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.8 | 1e-04 | 18/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.7 | 1e-04 | 17/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~16% of this change | 1.19× | +4.6 | 2e-04 | 18/46 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.4 | 4e-04 | 10/36 (PANC-1, C32, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +4.3 | 6e-04 | 18/48 (SW480, HS-578T, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +3.9 | 0.003 | 8/47 (NCI-H1573, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.060 | 6/48 (HT-29, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2548.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.388×** | -25.7 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.414×** | -24.0 | 0e+00 | 46/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.444×** | -22.1 | 0e+00 | 45/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.589×** | -14.4 | 8e-45 | 45/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.592×** | -14.3 | 3e-44 | 36/46 (C-33 A, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.742×** | -11.4 | 2e-28 | 40/48 (A498, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.686×** | -10.3 | 9e-23 | 36/48 (hTERT-HPNE, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.521×** | -9.3 | 1e-18 | 36/48 (A498, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.710×** | -9.0 | 2e-17 | 21/37 (HS-578T, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.765×** | -7.3 | 2e-11 | 23/47 (LoVo, SW 900, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.819×** | -5.2 | 1e-05 | 22/48 (A-427, NCI-H23, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.831×** | -4.9 | 6e-05 | 19/47 (SW 900, A-172, …) | top dose only |  |
| [[Terfenadine (drug)]] 0.5 µM |  | 0.847× | -4.5 | 3e-04 | 13/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | 0.844× | -4.3 | 8e-04 | 20/44 (LoVo, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.895× | -3.0 | 0.097 | 8/48 (SW 1271, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2548. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 44.9 | 1 | 7 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.32× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -18.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.288× (z -12.5) |
| [[SW480 (line)]] | alt | 42.7 | 2 | 5 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.21× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.393× (z -13.7) |
| [[A498 (line)]] | wt | 45.1 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -20.7) |
| [[H4 (line)]] | wt | 64.3 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.248× (z -10.2) |
| [[LoVo (line)]] | wt | 35.9 | 1 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.81× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.305× (z -14.5) |
| [[LS 180 (line)]] | wt | 45.7 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 4.67× (z +8.9) | [[Belinostat (drug)]] 5 µM 0.357× (z -11.3) |
| [[PANC-1 (line)]] | alt | 30.7 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 4.69× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.275× (z -15.7) |
| [[SW 900 (line)]] | alt | 31.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.324× (z -9.7) |
| [[A-172 (line)]] | wt | 34.2 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.339× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 34.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.319× (z -10.4) |
| [[HOP62 (line)]] | alt | 26.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.292× (z -13.3) |
| [[HS-578T (line)]] | alt | 47.4 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.308× (z -11.5) |
| [[J82 (line)]] | alt | 27.9 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.344× (z -9.7) |
| [[KATO III (line)]] | alt | 29.2 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.227× (z -14.1) |
| [[NCI-H23 (line)]] | alt | 31.7 | 0 | 3 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -10.8) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.318× (z -10.0) |
| [[NCI-H2347 (line)]] | alt | 31.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.379× (z -11.2) |
| [[NCI-H460 (line)]] | wt | 25.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.415× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 47.0 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.385× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 37.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.296× (z -10.2) |
| [[SNU-1 (line)]] | wt | 43.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 39.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.318× (z -11.6) |
| [[BT-474 (line)]] | alt | 79.4 | 1 | 1 | [[TAK-901 (drug)]] 0.05 µM 2.22× (z +9.4) | [[Panobinostat (drug)]] 0.5 µM 0.397× (z -11.6) |
| [[COLO 205 (line)]] | alt | 45.2 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.266× (z -10.5) |
| [[HT-29 (line)]] | alt | 29.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.288× (z -11.1) |
| [[A-427 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -11.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[C-33 A (line)]] | alt | 42.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.1000× (z -17.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 25.5 | 0 | 1 | — | [[OTS514 (drug)]] 5 µM 0.0713× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.412× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 28.5 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.158× (z -11.6) |
| [[NCI-H2030 (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -10.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -12.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 39.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -12.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 33.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -9.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 43.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.258× (z -9.0) |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2548), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRCC]] | +0.74 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[ZNF263]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[MIEF1]] | +0.68 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[SART3]] | +0.67 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[GTF3C4]] | +0.66 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[QRICH1]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[NGDN]] | +0.65 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.64 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[WDR81]] | +0.63 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[PTCD1]] | +0.63 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[LRRC41]] | +0.63 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[KEAP1]] | +0.63 | +0.49 / +0.59 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPAG9]] | -0.63 | -0.37 / -0.54 | both halves | 7e-05 |  |
| [[PICALM]] | -0.63 | -0.41 / -0.60 | both halves | 4e-05 |  |
| [[AFDN]] | -0.61 | -0.34 / -0.57 | both halves | 1e-04 |  |
| [[NPTN]] | -0.56 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[ZFAND6]] | -0.54 | -0.43 / -0.52 | both halves | 3e-05 |  |
| [[CAST]] | -0.54 | -0.29 / -0.40 | both halves | 3e-04 |  |
| [[NCAM1]] | -0.53 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[DIAPH1]] | -0.53 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ATP11B]] | -0.53 | -0.32 / -0.50 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises AKAP8's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises AKAP8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.730). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.1, 10.0); signed map (-5.7, -18.1). **Vector** length 87.8, 19.3% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.9 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.7 | +16.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.1 | -0.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.1 | +14.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.6 | +1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -11.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.7 | -14.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.5 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -24.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.0 | -14.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -9.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,353,385-15,379,815 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AKAP95, DKFZp586B1222 |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O43823](https://www.uniprot.org/uniprotkb/O43823) (A-kinase anchor protein 8):

> Anchoring protein that mediates the subcellular compartmentation of cAMP-dependent protein kinase (PKA type II). Acts as an anchor for a PKA-signaling complex onto mitotic chromosomes, which is required for maintenance of chromosomes in a condensed form throughout mitosis. Recruits condensin complex subunit NCAPD2 to chromosomes required for chromatin condensation; the function appears to be independent from PKA-anchoring. May help to deliver cyclin D/E to CDK4 to facilitate cell cycle …

**Summary**, from NCBI Gene [10270](https://www.ncbi.nlm.nih.gov/gene/10270):

> This gene encodes a member of the A-kinase anchor protein family. A-kinase anchor proteins are scaffold proteins that contain a binding domain for the RI/RII subunit of protein kinase A (PKA) and recruit PKA and other signaling molecules to specific subcellular locations. This gene encodes a nuclear A-kinase anchor protein that binds to the RII alpha subunit of PKA and may play a role in chromosome condensation during mitosis by targeting PKA and the condensin complex to chromatin. A pseudogene …

**Accessions** — [HGNC:378](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:378) · Entrez [10270](https://www.ncbi.nlm.nih.gov/gene/10270) · UniProt [O43823](https://www.uniprot.org/uniprotkb/O43823) · Ensembl [ENSG00000105127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105127)

## Data

Gene col 2548: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2548); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2548, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2548]; `tensor/DDL_lfc|DDL_z.npy` [2548]; `embed/gene_vectors.npy` [2548]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2548 or target_col == 2548). Every well: [[AKAP8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
