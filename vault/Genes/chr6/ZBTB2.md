---
symbol: "ZBTB2"
type: "gene"
col: 11191
ensembl_id: "ENSG00000181472"
name: "zinc finger and BTB domain containing 2"
location: "6q25.1"
module: 95
arm: "+"
pooled_cpm: 21.38
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 8
n_dd_up_clean: 14
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/095"]
generated_by: "tahoemap"
---

# ZBTB2

*zinc finger and BTB domain containing 2* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.21× (z +34.7, q 0e+00, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.307× (z -24.9, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB1]] (+0.69, fdr 1e-05), [[PKN2-AS1]] (+0.68, fdr 7e-05), [[ZNF689]] (+0.68, fdr 3e-05); moves opposite to [[F11R]] (-0.63, fdr 3e-05), [[COG5]] (-0.61, fdr 5e-05), [[UBA6]] (-0.61, fdr 4e-04).
> It sits in the **+** arm of [[Module 095]] (Chromatin organization).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.21×** | +34.7 | 0e+00 | 43/47 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.36×** | +24.5 | 0e+00 | 43/48 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.87×** | +22.7 | 0e+00 | 48/48 (SW480, NCI-H2030, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **2.09×** | +15.5 | 0e+00 | 43/47 (A-172, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.09×** | +15.5 | 0e+00 | 36/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +12.2 | 2e-32 | 36/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.78×** | +12.2 | 4e-32 | 31/48 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +11.7 | 7e-30 | 35/47 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.72×** | +11.5 | 1e-28 | 33/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +10.9 | 5e-26 | 28/46 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.65×** | +10.5 | 5e-24 | 33/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.60×** | +9.9 | 3e-21 | 32/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.42×** | +9.7 | 9e-21 | 30/47 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.0 | 2e-05 | 12/29 (NCI-H2030, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +4.9 | 4e-05 | 16/48 (PANC-1, J82, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.004 | 9/47 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.005 | 8/48 (SW480, HEC-1-A, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 5 µM |  | 1.12× | +3.4 | 0.016 | 6/48 (PANC-1, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.307×** | -24.9 | 0e+00 | 48/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.316×** | -24.3 | 0e+00 | 47/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.349×** | -22.2 | 0e+00 | 46/47 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.614×** | -10.3 | 1e-22 | 35/48 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.572×** | -6.2 | 8e-08 | 19/48 (NCI-H23, SW1417, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.782×** | -5.2 | 2e-05 | 20/47 (LOX-IMVI, SW48, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.789×** | -5.0 | 4e-05 | 19/48 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.650×** | -4.7 | 1e-04 | 13/46 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -3.8 | 0.009 | 17/48 (A498, NCI-H23, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.846× | -3.5 | 0.022 | 12/47 (NCI-H23, HEC-1-A, …) | two highest doses |  |
| [[Ciclopirox (drug)]] 5 µM |  | 0.895× | -3.3 | 0.047 | 9/48 (SW48, NCI-H1573, …) | top dose only |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | 0.855× | -3.2 | 0.067 | 4/47 (RKO, LS 180, …) | all doses, flat |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.862× | -3.1 | 0.076 | 5/47 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Meloxicam (drug)]] 0.05 µM |  | 0.865× | -3.1 | 0.090 | 3/47 (BT-474, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 28.7 | 12 (2 ⚠) | 4 | [[TAK-901 (drug)]] 5 µM 16.3× (z +15.6) | [[Panobinostat (drug)]] 5 µM 0.178× (z -18.5) |
| [[NCI-H460 (line)]] | wt | 16.8 | 10 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.39× (z +17.9) | [[Panobinostat (drug)]] 0.5 µM 0.275× (z -11.1) |
| [[SW1417 (line)]] | alt | 31.0 | 4 | 4 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +19.0) | [[Panobinostat (drug)]] 5 µM 0.301× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 21.9 | 6 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.70× (z +26.1) | [[Panobinostat (drug)]] 0.5 µM 0.386× (z -8.7) |
| [[A498 (line)]] | wt | 28.7 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +20.3) | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -12.9) |
| [[J82 (line)]] | alt | 26.3 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 6.92× (z +23.1) | [[Panobinostat (drug)]] 0.5 µM 0.270× (z -11.0) |
| [[A-172 (line)]] | wt | 16.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.10× (z +18.2) | — |
| [[HOP62 (line)]] | alt | 16.7 | 3 | 2 | [[Homoharringtonine (drug)]] 5 µM 8.07× (z +21.4) | [[Belinostat (drug)]] 5 µM 0.258× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 30.1 | 2 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -12.6) |
| [[NCI-H2030 (line)]] | alt | 20.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +20.5) | — |
| [[SNU-423 (line)]] | alt | 37.4 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +27.3) | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -9.7) |
| [[A549 (line)]] | wt | 18.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +12.2) | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.145× (z -11.5) |
| [[LoVo (line)]] | wt | 12.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +11.2) | — |
| [[C32 (line)]] | wt | 25.9 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 15.8× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.199× (z -10.9) |
| [[HepG2_C3A (line)]] | wt | 26.6 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.75× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 15.6 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.0) | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -8.8) |
| [[LOX-IMVI (line)]] | wt | 29.0 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.134× (z -16.2) |
| [[NCI-H23 (line)]] | alt | 60.8 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.108× (z -16.8) |
| [[PANC-1 (line)]] | alt | 17.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +8.7) | [[Belinostat (drug)]] 5 µM 0.343× (z -10.6) |
| [[RKO (line)]] | wt | 26.3 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 4.63× (z +9.7) | [[Panobinostat (drug)]] 0.5 µM 0.261× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.6) | [[Belinostat (drug)]] 5 µM 0.200× (z -10.8) |
| [[AsPC-1 (line)]] | alt | 14.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -8.5) |
| [[Hs 766T (line)]] | wt | 13.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +11.3) | [[Belinostat (drug)]] 5 µM 0.214× (z -8.5) |
| [[KATO III (line)]] | alt | 19.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +15.1) | — |
| [[RPMI-7951 (line)]] | alt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 24.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -11.4) |
| [[SW 900 (line)]] | alt | 19.0 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.215× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 14.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +18.2) | — |
| [[H4 (line)]] | wt | 17.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +10.3) | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 15.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +13.0) | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.7) | — |
| [[SW48 (line)]] | wt | 19.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.165× (z -9.0) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB1]] | +0.69 | +0.53 / +0.53 | both halves | 1e-05 | same gene group; STRING 406 |
| [[PKN2-AS1]] | +0.68 | +0.52 / +0.38 | both halves | 7e-05 |  |
| [[ZNF689]] | +0.68 | +0.54 / +0.46 | both halves | 3e-05 | same gene group |
| [[ZFX]] | +0.68 | +0.48 / +0.51 | both halves | 2e-05 | same gene group |
| [[PCNX4-DT]] | +0.67 | +0.49 / +0.39 | both halves | 6e-05 |  |
| [[ANGPT2]] | +0.67 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[MAD2L1-DT]] | +0.67 | +0.50 / +0.36 | both halves | 9e-05 |  |
| [[CFAP418-AS1]] | +0.67 | +0.53 / +0.40 | both halves | 5e-05 |  |
| [[PATL2]] | +0.66 | +0.56 / +0.34 | both halves | 1e-04 |  |
| [[CREB3L4]] | +0.66 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[SIX5]] | +0.66 | +0.60 / +0.44 | both halves | 3e-05 |  |
| [[INO80D]] | +0.66 | +0.41 / +0.48 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[F11R]] | -0.63 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[COG5]] | -0.61 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[UBA6]] | -0.61 | -0.58 / -0.25 | both halves | 4e-04 |  |
| [[ARPC1A]] | -0.60 | -0.53 / -0.34 | both halves | 1e-04 |  |
| [[HSPA5]] | -0.59 | -0.61 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZBTB2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 095]] — Chromatin organization; 48 genes; this gene is in the **+** arm (projection on the module's main direction 0.727). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.36).
- **Nodal map** (x, y) = (4.1, 10.8); signed map (25.2, -17.4). **Vector** length 98.4, 24.1% of its response variance represented; |z| ≥ 3 in 1,186 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.3 | +15.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +24.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.1 | +34.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +11.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +15.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +9.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.8 | +0.3 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.9 | -24.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.7 | -24.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.8 | -22.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.1 | -1.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.1 | +2.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -4.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.6 | +2.3 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger and BTB domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:151,364,115-151,391,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1483, ZNF437, bA351K16.2 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N680](https://www.uniprot.org/uniprotkb/Q8N680) (Zinc finger and BTB domain-containing protein 2):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [57621](https://www.ncbi.nlm.nih.gov/gene/57621):

> Enables DNA-binding transcription repressor activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and identical protein binding activity. Involved in negative regulation of transcription by RNA polymerase II. Predicted to be located in nucleus. Predicted to be active in nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:20868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20868) · Entrez [57621](https://www.ncbi.nlm.nih.gov/gene/57621) · UniProt [Q8N680](https://www.uniprot.org/uniprotkb/Q8N680) · Ensembl [ENSG00000181472](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181472)

## Data

Gene col 11191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11191); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11191]; `tensor/DDL_lfc|DDL_z.npy` [11191]; `embed/gene_vectors.npy` [11191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11191 or target_col == 11191). Every well: [[ZBTB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
