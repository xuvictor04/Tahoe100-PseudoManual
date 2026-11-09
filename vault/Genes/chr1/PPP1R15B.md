---
symbol: "PPP1R15B"
type: "gene"
col: 8176
ensembl_id: "ENSG00000158615"
name: "protein phosphatase 1 regulatory subunit 15B"
location: "1q32.1"
module: 14
arm: "+"
pooled_cpm: 106.0
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 2
n_dd_up_clean: 17
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# PPP1R15B

*protein phosphatase 1 regulatory subunit 15B* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.85× (z +28.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Estrone sulfate (potassium) (drug)]] 5 µM: 0.725× (z -4.1, q 0.024, down in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.207×, NCI-H2347 0.290×, KATO III 0.306×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.268×, NCI-H2347 0.332×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (AsPC-1 0.0436×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL5B]] (+0.67, fdr 7e-06), [[ATF3]] (+0.58, fdr 1e-05), [[IRF1]] (+0.57, fdr 1e-05); moves opposite to [[PARGP1]] (-0.54, fdr 4e-05), [[DNAJC17]] (-0.50, fdr 5e-05), [[ABCC5]] (-0.50, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.85×** | +28.4 | 0e+00 | 47/48 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.07×** | +14.3 | 8e-44 | 48/48 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.91×** | +13.1 | 1e-36 | 44/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.99×** | +12.9 | 4e-36 | 48/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.61×** | +12.2 | 3e-32 | 47/48 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +10.0 | 1e-21 | 44/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.02×** | +9.0 | 2e-17 | 46/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.91×** | +8.2 | 1e-14 | 45/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.80×** | +7.5 | 4e-12 | 43/48 (HS-578T, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.79×** | +7.1 | 6e-11 | 41/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.70×** | +6.8 | 6e-10 | 44/48 (SNU-423, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.34×** | +5.7 | 7e-07 | 32/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +5.5 | 1e-06 | 32/48 (BT-474, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.52×** | +5.3 | 5e-06 | 38/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.51×** | +5.3 | 6e-06 | 38/48 (NCI-H2030, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.50×** | +5.2 | 7e-06 | 37/48 (HS-578T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +5.2 | 8e-06 | 34/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.033 | 25/47 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8176.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (C-33 A 0.207×, NCI-H2347 0.290×, KATO III 0.306×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.268×, NCI-H2347 0.332×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (AsPC-1 0.0436×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **0.725×** | -4.1 | 0.024 | 32/48 (CFPAC-1, CHP-212, …) | top dose only | position effect removed |
| [[Carbamazepine (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.064 | 33/47 (C-33 A, SW48, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 0.763× | -3.4 | 0.11 | 31/48 (A549, NCI-H1792, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.775× | -3.2 | 0.14 | 22/49 (HEC-1-A, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.776× | -3.2 | 0.14 | 24/48 (RKO, AN3 CA, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 13 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.67× (z +24.4) | — |
| [[BT-474 (line)]] | alt | 66.5 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +17.3) | — |
| [[HEC-1-A (line)]] | alt | 73.9 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +22.2) | — |
| [[NCI-H2347 (line)]] | alt | 145 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.290× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 108 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.38× (z +23.2) | — |
| [[SW480 (line)]] | alt | 69.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.4) | — |
| [[A549 (line)]] | wt | 136 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +23.8) | — |
| [[HOP62 (line)]] | alt | 56.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.85× (z +28.3) | — |
| [[A-172 (line)]] | wt | 74.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.41× (z +22.2) | — |
| [[LoVo (line)]] | wt | 113 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +20.9) | — |
| [[LOX-IMVI (line)]] | wt | 68.0 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +16.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 59.8 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.65× (z +18.2) | — |
| [[NCI-H1792 (line)]] | alt | 123 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.48× (z +18.7) | — |
| [[AsPC-1 (line)]] | alt | 123 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +24.8) | [[Lonafarnib (drug)]] 5 µM 0.0436× (z -16.0) ⚠ toxic |
| [[C32 (line)]] | wt | 97.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.1× (z +27.6) | — |
| [[HepG2_C3A (line)]] | wt | 72.1 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +16.5) | — |
| [[HS-578T (line)]] | alt | 47.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +21.1) | — |
| [[hTERT-HPNE (line)]] | wt | 71.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.93× (z +21.3) | — |
| [[J82 (line)]] | alt | 130 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.75× (z +22.2) | — |
| [[LS 180 (line)]] | wt | 82.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +16.0) | — |
| [[Panc 03.27 (line)]] | alt | 91.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.25× (z +22.3) | — |
| [[SK-MEL-2 (line)]] | alt | 88.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 75.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.75× (z +16.1) | — |
| [[SNU-423 (line)]] | alt | 70.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +24.6) | — |
| [[COLO 205 (line)]] | alt | 107 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +17.3) | — |
| [[RPMI-7951 (line)]] | alt | 79.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.14× (z +18.6) | — |
| [[A498 (line)]] | wt | 283 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.34× (z +17.2) | — |
| [[CFPAC-1 (line)]] | alt | 156 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +23.3) | — |
| [[H4 (line)]] | wt | 70.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +12.4) | — |
| [[HCT15 (line)]] | alt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +14.4) | — |
| [[KATO III (line)]] | alt | 97.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 183 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.6) | — |
| [[RKO (line)]] | wt | 105 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 188 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +15.9) | — |
| [[SW48 (line)]] | wt | 88.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +12.6) | — |
| [[A-427 (line)]] | wt | 61.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.48× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 71.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 177 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 135 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +17.2) | — |
| [[HT-29 (line)]] | alt | 150 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +13.2) | — |
| [[NCI-H2030 (line)]] | alt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +15.2) | — |
| [[NCI-H23 (line)]] | alt | 63.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 65.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.07× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 78.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +12.7) | — |
| [[NCI-H2122 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 98.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 74.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL5B]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ATF3]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IRF1]] | +0.57 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[BHLHE40]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[REL]] | +0.54 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[NFKB2]] | +0.53 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SLC50A1]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.52 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[TNFAIP2]] | +0.50 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC30A1]] | +0.50 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[IQCN]] | +0.49 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CD83]] | +0.49 | +0.50 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARGP1]] | -0.54 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[DNAJC17]] | -0.50 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[ABCC5]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[UBE2D2]] | -0.50 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[INVS]] | -0.49 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[POP1]] | -0.49 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[RNF8]] | -0.48 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[RAB11FIP3]] | -0.47 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[ZNF708]] | -0.47 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[PPP1R26-AS1]] | -0.47 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[PTPN9]] | -0.47 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[TBCE]] | -0.46 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises PPP1R15B's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.40× lower at baseline in the lines without AGR2 | 0.005 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises PPP1R15B's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 1.21× lower at baseline in the lines without TNFAIP2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[ARCN1]] | C | ARCN1's natural level weakens PPP1R15B's drug response | ARCN1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.16; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.437). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.0, 4.5); signed map (44.7, 6.0). **Vector** length 88.9, 30.9% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.3 | -0.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.2 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.7 | +2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.2 | +2.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | -0.1 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +2.1 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.1 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -8.5 | +0.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -7.2 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.4 | -0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.7 | -0.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.9 | +0.2 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.2 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.2 | -2.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | protein phosphatase 1 regulatory subunit 15B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:204,396,492-204,411,887 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14744 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits |
| Hallmark sets | ADIPOGENESIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5SWA1](https://www.uniprot.org/uniprotkb/Q5SWA1) (Protein phosphatase 1 regulatory subunit 15B):

> Maintains low levels of EIF2S1 phosphorylation in unstressed cells by promoting its dephosphorylation by PP1.

**Summary**, from NCBI Gene [84919](https://www.ncbi.nlm.nih.gov/gene/84919):

> This gene encodes a protein phosphatase I-interacting protein that promotes the dephosphorylation of eukaryotic translation initiation factor 2A to regulate translation under conditions of cellular stress. The transcribed messenger RNA contains two upstream open reading frames (ORFs) that repress translation of the main protein coding ORF under normal conditions, while the protein coding ORF is expressed at high levels in response to stress. Continual translation of the mRNA under conditions of …

**Accessions** — [HGNC:14951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14951) · Entrez [84919](https://www.ncbi.nlm.nih.gov/gene/84919) · UniProt [Q5SWA1](https://www.uniprot.org/uniprotkb/Q5SWA1) · Ensembl [ENSG00000158615](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158615)

## Data

Gene col 8176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8176); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8176]; `tensor/DDL_lfc|DDL_z.npy` [8176]; `embed/gene_vectors.npy` [8176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8176 or target_col == 8176). Every well: [[PPP1R15B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1R15B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
