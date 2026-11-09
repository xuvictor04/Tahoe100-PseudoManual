---
symbol: "ATN1"
type: "gene"
col: 3260
ensembl_id: "ENSG00000111676"
name: "atrophin 1"
location: "12p13.31"
module: 126
arm: "+"
pooled_cpm: 65.36
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 18
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# ATN1

*atrophin 1* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.13× (z +13.4, q 3e-38, up in 42 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.69× (z +9.3, q 4e-18, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.255× (z -24.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[U2AF2]] (+0.75, fdr 1e-05), [[DVL3]] (+0.70, fdr 3e-05), [[INPPL1]] (+0.69, fdr 7e-06); moves opposite to [[PET117]] (-0.63, fdr 4e-04), [[ATP5MJ]] (-0.63, fdr 3e-05), [[POP7]] (-0.62, fdr 1e-04).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.13×** | +13.4 | 3e-38 | 42/49 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +10.5 | 2e-23 | 36/43 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +9.3 | 4e-18 | 40/48 (LoVo, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +8.4 | 8e-15 | 37/45 (HOP62, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.32×** | +4.9 | 1e-04 | 34/49 (SW480, Panc 03.27, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.012 | 25/48 (SNU-423, RPMI-7951, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.25×** | +3.6 | 0.022 | 21/48 (Panc 03.27, HOP62, …) | inconsistent across doses | position effect removed |
| [[Pentoxifylline (drug)]] 0.5 µM |  | **1.23×** | +3.6 | 0.022 | 23/48 (LS 180, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.06× | +3.6 | 0.022 | 0/49 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.20×** | +3.2 | 0.074 | 22/48 (AsPC-1, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.255×** | -24.3 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.291×** | -21.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.345×** | -18.9 | 0e+00 | 48/48 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.509×** | -12.0 | 4e-31 | 45/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.665×** | -10.0 | 2e-21 | 42/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.474×** | -6.9 | 4e-10 | 40/49 (SW480, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.713×** | -6.0 | 1e-07 | 37/48 (NCI-H23, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.731×** | -5.6 | 2e-06 | 32/48 (SNU-423, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -4.5 | 4e-04 | 24/48 (SNU-423, J82, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.787×** | -4.3 | 0.001 | 27/48 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.793×** | -4.1 | 0.002 | 21/48 (BT-474, C32, …) | two highest doses | position effect removed |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.786×** | -4.1 | 0.002 | 26/47 (SHP-77, NCI-H2347, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.796×** | -3.9 | 0.004 | 21/48 (H4, LOX-IMVI, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.804×** | -3.9 | 0.004 | 24/48 (AN3 CA, KATO III, …) | rises with dose |  |
| [[Cilostazol (drug)]] 5 µM |  | **0.798×** | -3.9 | 0.004 | 22/48 (NCI-H23, LoVo, …) | top dose only | position effect removed |
| [[Almonertinib (hydrochloride) (drug)]] 0.05 µM |  | **0.826×** | -3.4 | 0.020 | 21/48 (NCI-H661, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.827×** | -3.4 | 0.021 | 22/48 (NCI-H23, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 51.8 | 5 (5 ⚠) | 4 | [[Digitoxin (drug)]] 5 µM 2.67× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.187× (z -18.8) |
| [[SW480 (line)]] | alt | 72.1 | 3 (2 ⚠) | 5 | [[Auranofin (drug)]] 5 µM 2.46× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -21.0) |
| [[HOP62 (line)]] | alt | 74.7 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.05 µM 2.49× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.219× (z -17.1) |
| [[LoVo (line)]] | wt | 58.3 | 3 (2 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 3.60× (z +14.8) | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 90.3 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.36× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.193× (z -17.3) |
| [[PANC-1 (line)]] | alt | 43.7 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +12.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.207× (z -17.6) |
| [[A-427 (line)]] | wt | 88.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.79× (z +10.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.259× (z -14.1) |
| [[A549 (line)]] | wt | 44.9 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.291× (z -11.5) |
| [[J82 (line)]] | alt | 75.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.61× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -12.6) |
| [[LOX-IMVI (line)]] | wt | 84.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.273× (z -13.4) |
| [[LS 180 (line)]] | wt | 53.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.230× (z -15.4) |
| [[Panc 03.27 (line)]] | alt | 97.2 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -18.1) |
| [[SW 900 (line)]] | alt | 129 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -15.6) |
| [[SW48 (line)]] | wt | 62.2 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 3.29× (z +8.9) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.5) |
| [[A498 (line)]] | wt | 63.3 | 2 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +9.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.376× (z -10.0) |
| [[C32 (line)]] | wt | 74.4 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.83× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.241× (z -13.0) |
| [[H4 (line)]] | wt | 112 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.232× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 79.9 | 2 (1 ⚠) | 2 | [[Auranofin (drug)]] 5 µM 2.38× (z +9.9) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -12.5) |
| [[Hs 766T (line)]] | wt | 53.1 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.224× (z -12.9) |
| [[HT-29 (line)]] | alt | 60.4 | 1 | 3 | [[Auranofin (drug)]] 5 µM 2.85× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.235× (z -14.5) |
| [[KATO III (line)]] | alt | 52.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.199× (z -15.2) |
| [[MIA PaCa-2 (line)]] | alt | 118 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.53× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 67.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +8.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.224× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 43.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.383× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 70.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.239× (z -16.6) |
| [[SK-MEL-2 (line)]] | alt | 67.4 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -11.9) |
| [[AsPC-1 (line)]] | alt | 44.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -15.8) |
| [[C-33 A (line)]] | alt | 62.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -14.5) |
| [[COLO 205 (line)]] | alt | 51.1 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.223× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 51.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 81.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 58.9 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +12.7) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -14.7) |
| [[RKO (line)]] | wt | 95.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.251× (z -13.2) |
| [[SNU-423 (line)]] | alt | 50.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.288× (z -10.9) |
| [[SW1417 (line)]] | alt | 66.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.60× (z +9.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.228× (z -15.2) |
| [[A-172 (line)]] | wt | 45.0 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.84× (z +8.8) | [[Belinostat (drug)]] 5 µM 0.331× (z -9.4) |
| [[AN3 CA (line)]] | alt | 101 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -11.4) |
| [[BT-474 (line)]] | alt | 61.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.142× (z -16.0) |
| [[CFPAC-1 (line)]] | alt | 38.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.352× (z -10.1) |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.291× (z -10.5) |
| [[RPMI-7951 (line)]] | alt | 68.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -10.1) |
| [[SNU-1 (line)]] | wt | 103 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -11.9) |
| [[CHP-212 (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 75.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[U2AF2]] | +0.75 | +0.53 / +0.73 | both halves | 1e-05 |  |
| [[DVL3]] | +0.70 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[INPPL1]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[PHF8]] | +0.67 | +0.37 / +0.67 | both halves | 9e-05 |  |
| [[ATXN2L]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 |  |
| [[SORBS3]] | +0.67 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[AKT1S1]] | +0.66 | +0.47 / +0.62 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers |
| [[GPR137]] | +0.66 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[MTA2]] | +0.65 | +0.48 / +0.58 | both halves | 2e-05 | pathway: Intracellular signaling by second messengers; STRING 592 |
| [[UBQLN4]] | +0.64 | +0.46 / +0.54 | both halves | 3e-05 | STRING 509 |
| [[CHD3]] | +0.64 | +0.43 / +0.59 | both halves | 3e-05 | pathway: Intracellular signaling by second messengers; STRING 606 |
| [[BAG6]] | +0.64 | +0.58 / +0.66 | both halves | 8e-06 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 7 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PET117]] | -0.63 | -0.25 / -0.64 | both halves | 4e-04 |  |
| [[ATP5MJ]] | -0.63 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[POP7]] | -0.62 | -0.35 / -0.58 | both halves | 1e-04 |  |
| [[C4orf48]] | -0.61 | -0.29 / -0.59 | both halves | 2e-04 |  |
| [[ROMO1]] | -0.61 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ANAPC11]] | -0.61 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[UQCRQ]] ⚠ | -0.60 | -0.43 / -0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL41]] ⚠ | -0.60 | -0.23 / -0.56 | both halves | 5e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM256]] | -0.60 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[UQCR10]] ⚠ | -0.60 | -0.33 / -0.57 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[GTF2H2]] | -0.60 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[LSM2]] | -0.58 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[NDUFA12]] | -0.58 | -0.27 / -0.54 | both halves | 3e-04 |  |
| [[ELOB]] | -0.58 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[SF3B6]] | -0.58 | -0.26 / -0.55 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.3, -22.6); signed map (-11.6, -34.9). **Vector** length 117, 33.2% of its response variance represented; |z| ≥ 3 in 1,020 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +12.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.7 | +8.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.6 | +13.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +10.3 | +9.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +10.2 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +0.5 |
|  | [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | +2.2 | +0.5 |
|  | [[Pyridoxine (drug)]] 0.5 µM |  | +2.2 | +1.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -10.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.6 | -18.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.2 | -24.3 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -3.8 | -12.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.7 | -1.4 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.6 | -2.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.6 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | atrophin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,924,463-6,942,321 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B37; previously D12S755E, DRPLA |
| Gene groups (HGNC) | Atrophins |
| Reactome | 4 pathways, smallest: Regulation of PTEN gene transcription; PTEN Regulation; PIP3 activates AKT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P54259](https://www.uniprot.org/uniprotkb/P54259) (Atrophin-1):

> Transcriptional corepressor. Recruits NR2E1 to repress transcription. Promotes vascular smooth cell (VSMC) migration and orientation (By similarity). Corepressor of MTG8 transcriptional repression. Has some intrinsic repression activity which is independent of the number of poly-Gln (polyQ) repeats.

**Summary**, from NCBI Gene [1822](https://www.ncbi.nlm.nih.gov/gene/1822):

> Dentatorubral pallidoluysian atrophy (DRPLA) is a rare neurodegenerative disorder characterized by cerebellar ataxia, myoclonic epilepsy, choreoathetosis, and dementia. The disorder is related to the expansion from 7-35 copies to 49-93 copies of a trinucleotide repeat (CAG/CAA) within this gene. The encoded protein includes a serine repeat and a region of alternating acidic and basic amino acids, as well as the variable glutamine repeat. Alternative splicing results in two transcripts variants …

**Accessions** — [HGNC:3033](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3033) · Entrez [1822](https://www.ncbi.nlm.nih.gov/gene/1822) · UniProt [P54259](https://www.uniprot.org/uniprotkb/P54259) · Ensembl [ENSG00000111676](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111676)

## Data

Gene col 3260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3260); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3260]; `tensor/DDL_lfc|DDL_z.npy` [3260]; `embed/gene_vectors.npy` [3260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3260 or target_col == 3260). Every well: [[ATN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
