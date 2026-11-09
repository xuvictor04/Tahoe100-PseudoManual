---
symbol: "ARRDC4"
type: "gene"
col: 6409
ensembl_id: "ENSG00000140450"
name: "arrestin domain containing 4"
location: "15q26.2"
module: 20
arm: "-"
pooled_cpm: 24.85
n_lines_expressing: 42
n_dd_up: 41
n_dd_down: 11
n_dd_up_clean: 31
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ARRDC4

*arrestin domain containing 4* — 15q26.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 14.5× (z +57.8, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Belumosudil (drug)]] 5 µM: 0.395× (z -13.9, q 3e-41, down in 35 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KCTD11]] (+0.58, fdr 2e-05), [[DYNLL1]] (+0.57, fdr 1e-05), [[ARL14]] (+0.56, fdr 2e-05); moves opposite to [[XPOT]] (-0.48, fdr 1e-04), [[DFFB]] (-0.48, fdr 3e-05), [[MTHFD2]] (-0.47, fdr 5e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MSX2]] → it (grade B ⚠); 2 go from it, the strongest it → [[MSX2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6409.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **14.5×** | +57.8 | 0e+00 | 38/38 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **10.3×** | +36.2 | 0e+00 | 37/37 (C32, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **9.43×** | +33.5 | 0e+00 | 40/40 (C32, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **5.71×** | +27.1 | 0e+00 | 40/40 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.48×** | +23.3 | 0e+00 | 40/40 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.40×** | +23.0 | 0e+00 | 40/40 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.90×** | +21.1 | 0e+00 | 38/38 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.30×** | +18.6 | 0e+00 | 39/40 (C32, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.09×** | +17.5 | 0e+00 | 40/40 (SW480, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.96×** | +16.9 | 0e+00 | 37/40 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.93×** | +16.7 | 0e+00 | 37/39 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **6.16×** | +14.8 | 0e+00 | 40/41 (LS 180, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +11.4 | 1e-28 | 28/38 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.06×** | +11.2 | 2e-27 | 36/40 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.73×** | +10.7 | 4e-25 | 31/39 (LS 180, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.78×** | +8.9 | 2e-17 | 31/40 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6409.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belumosudil (drug)]] 5 µM |  | **0.395×** | -13.9 | 3e-41 | 35/40 (HOP62, RKO, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.559×** | -9.1 | 4e-17 | 24/32 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.562×** | -8.6 | 1e-15 | 24/30 (PANC-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.600×** | -7.6 | 3e-12 | 25/37 (HCT15, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.461×** | -6.3 | 3e-08 | 24/39 (NCI-H460, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.669×** | -6.3 | 3e-08 | 24/40 (HOP62, HCT15, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | **0.806×** | -4.7 | 2e-04 | 18/40 (RKO, NCI-H23, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.589×** | -4.3 | 0.001 | 16/38 (HCT15, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.779×** | -3.9 | 0.006 | 11/40 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.059 | 8/40 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.863× | -3.2 | 0.075 | 8/40 (NCI-H1573, BT-474, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.821×** | -3.1 | 0.099 | 11/39 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 0.5 µM |  | 0.825× | -3.0 | 0.11 | 6/41 (LoVo, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6409. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 57.0 | 13 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +33.0) | [[Niclosamide (olamine) (drug)]] 5 µM 0.364× (z -9.1) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.382× (z -8.7) |
| [[SW480 (line)]] | alt | 25.8 | 15 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +34.3) | — |
| [[SW48 (line)]] | wt | 82.9 | 12 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 12.6× (z +22.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.0) ⚠ cell-cycle shift, explains ~55% of this change |
| [[CFPAC-1 (line)]] | alt | 34.1 | 12 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +30.9) | — |
| [[H4 (line)]] | wt | 30.9 | 11 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +18.7) | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -10.0) ⚠ toxic |
| [[NCI-H460 (line)]] | wt | 22.9 | 10 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +30.0) | [[Pralsetinib (drug)]] 5 µM 0.101× (z -9.3) |
| [[RKO (line)]] | wt | 35.3 | 9 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +27.0) | [[Belumosudil (drug)]] 5 µM 0.158× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 23.3 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +28.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.211× (z -9.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 75.2 | 6 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.18× (z +18.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0887× (z -15.7) ⚠ toxic · without an alert: [[Belumosudil (drug)]] 5 µM 0.249× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 40.7 | 10 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 24.7× (z +17.4) | — |
| [[HOP62 (line)]] | alt | 22.7 | 5 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +17.8) | [[Belumosudil (drug)]] 5 µM 0.118× (z -14.7) |
| [[LS 180 (line)]] | wt | 71.4 | 9 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.24× (z +28.8) | [[Belumosudil (drug)]] 5 µM 0.364× (z -9.7) |
| [[PANC-1 (line)]] | alt | 13.1 | 9 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +28.8) | [[Dinaciclib (drug)]] 5 µM 0.0707× (z -18.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 22.0 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 34.3× (z +25.5) | — |
| [[BT-474 (line)]] | alt | 30.7 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 25.1× (z +26.3) | — |
| [[HT-29 (line)]] | alt | 43.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.9× (z +25.8) | — |
| [[LoVo (line)]] | wt | 23.9 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +28.9) | — |
| [[NCI-H2030 (line)]] | alt | 18.9 | 8 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 21.0× (z +19.1) | [[Dinaciclib (drug)]] 5 µM 0.112× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.2 | 7 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +18.3) | [[Adagrasib (drug)]] 0.05 µM 0.644× (z -9.7) ⚠ position not correctable · without an alert: [[Belumosudil (drug)]] 5 µM 0.196× (z -9.7) |
| [[SK-MEL-2 (line)]] | alt | 39.4 | 6 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.8× (z +28.0) | [[Belumosudil (drug)]] 5 µM 0.226× (z -10.7) |
| [[SW1417 (line)]] | alt | 58.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.6× (z +28.2) | — |
| [[A-172 (line)]] | wt | 20.1 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +20.9) | [[Dinaciclib (drug)]] 5 µM 0.210× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 18.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +31.5) | — |
| [[C32 (line)]] | wt | 51.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 45.6× (z +38.4) | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.1× (z +23.6) | — |
| [[A-427 (line)]] | wt | 9.46 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +13.8) | — |
| [[COLO 205 (line)]] | alt | 22.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 92.5× (z +29.1) | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +23.6) | — |
| [[Panc 03.27 (line)]] | alt | 49.0 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 14.2× (z +27.2) | [[Dinaciclib (drug)]] 5 µM 0.136× (z -14.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 33.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.73× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -13.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 22.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +18.7) | — |
| [[C-33 A (line)]] | alt | 13.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +11.3) | — |
| [[Hs 766T (line)]] | wt | 12.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 21.4× (z +20.7) | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H1573 (line)]] | alt | 32.6 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +18.3) | [[Dinaciclib (drug)]] 5 µM 0.282× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.310× (z -8.7) |
| [[J82 (line)]] | alt | 15.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.24× (z +15.6) | — |
| [[SNU-1 (line)]] | wt | 6.55 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 31.8× (z +10.1) | — |
| [[AN3 CA (line)]] | alt | 40.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 10.0× (z +9.2) | — |
| [[CHP-212 (line)]] | wt | 14.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +9.9) | — |
| [[SW 1088 (line)]] | alt | 28.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.7× (z +8.7) | — |
| [[SW 1271 (line)]] | alt | 25.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +9.7) | — |
| [[A549 (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.68 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 75.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6409), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCTD11]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[DYNLL1]] | +0.57 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[ARL14]] | +0.56 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[RSPH3]] | +0.55 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[CDKN2AIP]] | +0.53 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[BTG1]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[IFT88]] | +0.52 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[CMTR2]] | +0.52 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[MARCKS]] | +0.52 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[TOPORS]] | +0.51 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[KIAA1217]] | +0.51 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[KLF10]] | +0.50 | +0.49 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XPOT]] | -0.48 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[DFFB]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[MTHFD2]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[AHCTF1]] | -0.46 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[URI1]] | -0.45 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[NARS1]] | -0.45 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[UTP18]] | -0.44 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[MFSD14B]] | -0.44 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[MIA2]] | -0.44 | -0.56 / -0.28 | both halves | 3e-04 |  |
| [[PSAT1]] | -0.44 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[SACM1L]] | -0.44 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[GMPS]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX2]] | B | MSX2 activity raises ARRDC4's level | lines that do not express MSX2 (11) vs lines expressing it (39) | 2.42× lower at baseline in the lines without MSX2 | 0.012 | ⚠ within organs, on part of the lines; also absent: CD9, ABCC3, CDCP1 |
| [[ARL14]] | B | ARL14 activity raises ARRDC4's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without ARL14 | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSX2]] | B | ARRDC4 activity raises MSX2's level | lines that do not express ARRDC4 (8) vs lines expressing it (42) | 2.55× lower at baseline in the lines without ARRDC4 | 0.012 | ⚠ within organs, on part of the lines; also absent: C2orf72, ADAP1, BACH2; maybe low, not absent |
| [[URI1]] | B | ARRDC4 activity lowers URI1's level | lines that do not express ARRDC4 (8) vs lines expressing it (42) | 1.46× higher at baseline in the lines without ARRDC4 | 0.070 | ⚠ within organs, on part of the lines; also absent: C2orf72, ADAP1, BACH2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.347). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-2.2, -23.2); signed map (-2.2, 10.6). **Vector** length 95.1, 24.5% of its response variance represented; |z| ≥ 3 in 1,441 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.1 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.8 | +11.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.3 | +36.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.1 | +16.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.5 | +27.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.9 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.1 | +0.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.0 | +2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +2.9 | +2.9 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.6 | -7.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.8 | -6.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.2 | -2.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.7 | -2.2 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.6 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | arrestin domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.2 — chr15:97,960,703-97,973,833 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36045 |
| Gene groups (HGNC) | Alpha arrestins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCT1](https://www.uniprot.org/uniprotkb/Q8NCT1) (Arrestin domain-containing protein 4):

> Functions as an adapter recruiting ubiquitin-protein ligases to their specific substrates (By similarity). Plays a role in endocytosis of activated G protein-coupled receptors (GPCRs) (Probable). Through an ubiquitination-dependent mechanism also plays a role in the incorporation of SLC11A2 into extracellular vesicles (By similarity). May play a role in glucose uptake. Participates in innate immune response by promoting IFIH1/MDA5 activation through interaction with TRIM65.

**Summary**, from NCBI Gene [91947](https://www.ncbi.nlm.nih.gov/gene/91947):

> Enables ubiquitin-like ligase-substrate adaptor activity. Involved in positive regulation of interferon-beta production and protein K63-linked ubiquitination. Acts upstream of or within positive regulation of ubiquitin-protein transferase activity. Located in endosome and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28087) · Entrez [91947](https://www.ncbi.nlm.nih.gov/gene/91947) · UniProt [Q8NCT1](https://www.uniprot.org/uniprotkb/Q8NCT1) · Ensembl [ENSG00000140450](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140450)

## Data

Gene col 6409: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6409); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6409, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6409]; `tensor/DDL_lfc|DDL_z.npy` [6409]; `embed/gene_vectors.npy` [6409]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6409 or target_col == 6409). Every well: [[ARRDC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRDC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
