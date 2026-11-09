---
symbol: "SERPINB9"
type: "gene"
col: 9972
ensembl_id: "ENSG00000170542"
name: "serpin family B member 9"
location: "6p25.2"
module: 101
arm: "+"
pooled_cpm: 53.38
n_lines_expressing: 26
n_dd_up: 30
n_dd_down: 32
n_dd_up_clean: 15
n_dd_down_clean: 31
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# SERPINB9

*serpin family B member 9* — 6p25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.27× (z +24.9, q 0e+00, up in 20 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.58× (z +20.1, q 0e+00, up in 19 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (1 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 0.607× (z -7.6, q 2e-11, down in 20 of 24 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IER3]] (+0.62, fdr 8e-06), [[GNG4]] (+0.59, fdr 2e-05), [[JUNB]] (+0.57, fdr 2e-05); moves opposite to [[TRAPPC13]] (-0.51, fdr 4e-05), [[GTF3C2]] (-0.50, fdr 4e-05), [[C8orf76]] (-0.48, fdr 4e-05).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PKIA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9972.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.27×** | +24.9 | 0e+00 | 20/22 (HOP62, LoVo, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.36×** | +21.2 | 0e+00 | 18/21 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.59×** | +21.1 | 0e+00 | 18/22 (LoVo, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.58×** | +20.1 | 0e+00 | 19/24 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.29×** | +11.9 | 1e-30 | 19/24 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.61×** | +10.0 | 2e-21 | 15/24 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **1.94×** | +9.9 | 4e-21 | 14/24 (PANC-1, SW480, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.22×** | +9.2 | 4e-18 | 13/19 (HOP62, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.85×** | +9.2 | 4e-18 | 18/24 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.81×** | +8.9 | 4e-17 | 15/24 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.79×** | +8.7 | 1e-16 | 16/24 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +8.6 | 3e-16 | 17/24 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.69×** | +7.8 | 2e-13 | 16/24 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.9 | 2e-10 | 16/24 (HCT15, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +6.8 | 3e-10 | 15/24 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 1e-06 | 11/24 (SW480, CFPAC-1, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.002 | 8/24 (HEC-1-A, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bexarotene (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.004 | 10/24 (AsPC-1, HCT15, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.17× | +3.3 | 0.023 | 10/24 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.024 | 9/24 (SNU-423, Hs 766T, …) | rises with dose |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.031 | 3/24 (RKO, LoVo, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.46×** | +3.0 | 0.056 | 10/24 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9972.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **0.607×** | -7.6 | 2e-11 | 20/24 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.700×** | -5.4 | 2e-05 | 13/24 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.708×** | -5.2 | 3e-05 | 17/24 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.721×** | -5.0 | 1e-04 | 15/24 (A549, HOP62, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.730×** | -4.8 | 2e-04 | 11/24 (RKO, NCI-H460, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.730×** | -4.8 | 2e-04 | 16/24 (A549, HOP62, …) | rises with dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.725×** | -4.5 | 5e-04 | 13/24 (A549, HOP62, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.746×** | -4.4 | 6e-04 | 12/24 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -4.2 | 0.001 | 11/24 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.760×** | -4.2 | 0.002 | 14/24 (Hs 766T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.762×** | -4.1 | 0.002 | 15/24 (SNU-423, NCI-H23, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.828×** | -4.1 | 0.002 | 11/24 (NCI-H1792, A549, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.829×** | -4.1 | 0.002 | 17/24 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.767×** | -4.0 | 0.002 | 11/24 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.748×** | -3.9 | 0.004 | 9/24 (NCI-H460, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.738×** | -3.8 | 0.004 | 14/24 (NCI-H460, RKO, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9972. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 75.8 | 12 (7 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.08× (z +13.7) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.3) | — |
| [[SW480 (line)]] | alt | 15.7 | 11 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +16.4) | — |
| [[HOP62 (line)]] | alt | 53.1 | 8 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 12.6× (z +19.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.6) | — |
| [[HEC-1-A (line)]] | alt | 54.8 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +16.7) | — |
| [[LoVo (line)]] | wt | 57.7 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.80× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.78× (z +12.9) | — |
| [[HepG2_C3A (line)]] | wt | 55.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +11.9) | — |
| [[J82 (line)]] | alt | 28.3 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.3× (z +15.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 5.51× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 213 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -9.2) ⚠ cell-cycle shift, explains ~45% of this change |
| [[PANC-1 (line)]] | alt | 16.7 | 6 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.30× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 323 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -14.6) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.367× (z -10.4) |
| [[SW1417 (line)]] | alt | 78.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.51× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.53× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 155 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +15.2) | — |
| [[HCT15 (line)]] | alt | 67.2 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.00× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 28.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +14.1) | — |
| [[RKO (line)]] | wt | 49.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +9.1) ⚠ toxic; transcription drop | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.194× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.328× (z -9.4) |
| [[A549 (line)]] | wt | 196 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -12.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.327× (z -9.3) |
| [[CFPAC-1 (line)]] | alt | 265 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 200 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -13.7) ⚠ cell-cycle shift, explains ~45% of this change |
| [[SNU-423 (line)]] | alt | 62.1 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.65× (z +9.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.6) | — |
| [[Hs 766T (line)]] | wt | 77.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.346× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 36.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.00× (z +8.8) | — |
| [[A-172 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.46 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.94 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.54 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.54 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.61 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.29 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.98 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.65 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9972), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER3]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[GNG4]] | +0.59 | +0.47 / +0.64 | both halves | 2e-05 |  |
| [[JUNB]] | +0.57 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[CSRNP1]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FGD6]] | +0.56 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PTGS2]] | +0.54 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[SLC9A7]] | +0.53 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[ZMIZ2]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[AGPAT4]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[NOCT]] | +0.52 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[UXS1]] | +0.52 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[CACNG8]] | +0.52 | +0.44 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAPPC13]] | -0.51 | -0.47 / -0.42 | both halves | 4e-05 |  |
| [[GTF3C2]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[C8orf76]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[LIN9]] | -0.48 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[TMEM267]] | -0.47 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[TDRD3]] | -0.47 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[BFAR]] | -0.47 | -0.29 / -0.53 | both halves | 3e-04 |  |
| [[TMEM101]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[TCEANC2]] | -0.46 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[MRPL37]] | -0.46 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[GAPVD1]] | -0.46 | -0.36 / -0.46 | both halves | 9e-05 |  |
| [[DHX35]] | -0.46 | -0.39 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers SERPINB9's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[CA2]] | C | CA2 activity raises SERPINB9's level | lines that do not express CA2 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without CA2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CCDC68, SCEL, MUC4; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKIA]] | B | SERPINB9 activity lowers PKIA's level | lines that do not express SERPINB9 (24) vs lines expressing it (26) | 2.07× higher at baseline in the lines without SERPINB9 | 0.042 | ⚠ within organs, on part of the lines; also absent: MT1A, SHH, LINC02086 |
| [[BMAL2]] | B | SERPINB9 activity raises BMAL2's level | lines that do not express SERPINB9 (24) vs lines expressing it (26) | 2.17× lower at baseline in the lines without SERPINB9 | 0.069 | ⚠ within organs, on part of the lines; also absent: MT1A, SHH, LINC02086 |

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.463). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.6, -2.7); signed map (8.5, 27.2). **Vector** length 95.7, 27.6% of its response variance represented; |z| ≥ 3 in 924 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.2 | +24.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.1 | +21.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.9 | +21.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +6.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.0 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.5 | +1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +1.7 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -4.2 | -7.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -5.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.8 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p25.2 — chr6:2,887,270-2,903,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CAP3; previously PI9 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Matched by | ensembl_id |

**Function**, from UniProt [P50453](https://www.uniprot.org/uniprotkb/P50453) (Serpin B9):

> Granzyme B inhibitor.

**Summary**, from NCBI Gene [5272](https://www.ncbi.nlm.nih.gov/gene/5272):

> This gene encodes a member of the serine protease inhibitor family which are also known as serpins. The encoded protein belongs to a subfamily of intracellular serpins. This protein inhibits the activity of the effector molecule granzyme B. Overexpression of this protein may prevent cytotoxic T-lymphocytes from eliminating certain tumor cells. A pseudogene of this gene is found on chromosome 6. [provided by RefSeq, Mar 2012]

**Accessions** — [HGNC:8955](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8955) · Entrez [5272](https://www.ncbi.nlm.nih.gov/gene/5272) · UniProt [P50453](https://www.uniprot.org/uniprotkb/P50453) · Ensembl [ENSG00000170542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170542)

## Data

Gene col 9972: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9972); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9972, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9972]; `tensor/DDL_lfc|DDL_z.npy` [9972]; `embed/gene_vectors.npy` [9972]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9972 or target_col == 9972). Every well: [[SERPINB9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
