---
symbol: "TEX10"
type: "gene"
col: 5933
ensembl_id: "ENSG00000136891"
name: "testis expressed 10"
location: "9q31.1"
module: 92
arm: "+"
pooled_cpm: 99.16
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 16
n_dd_up_clean: 17
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# TEX10

*testis expressed 10* — 9q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +11.1, q 6e-26, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.464× (z -10.3, q 4e-22, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Trametinib (drug)]] 0.5 µM: 0.722× (z -5.2, q 4e-05, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR17HG]] (+0.57, fdr 1e-05), [[SPRY4-AS1]] (+0.55, fdr 2e-05), [[LINC01844]] (+0.55, fdr 1e-05); moves opposite to [[GPKOW]] (-0.51, fdr 3e-05), [[CEP350]] (-0.50, fdr 1e-05), [[RHOB]] (-0.49, fdr 5e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5933.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +11.1 | 6e-26 | 39/48 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.18×** | +10.9 | 3e-25 | 44/48 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.09×** | +10.3 | 2e-22 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.03×** | +9.9 | 6e-21 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.14×** | +8.4 | 7e-15 | 47/49 (HT-29, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.11×** | +8.3 | 1e-14 | 43/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.68×** | +7.2 | 4e-11 | 38/48 (NCI-H460, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.66×** | +7.1 | 9e-11 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.67×** | +6.6 | 2e-09 | 29/45 (SHP-77, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.5 | 4e-09 | 38/48 (HT-29, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +6.0 | 9e-08 | 37/47 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +5.9 | 2e-07 | 33/37 (NCI-H1573, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +5.8 | 4e-07 | 34/48 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.0 | 3e-05 | 31/48 (COLO 205, A-427, …) | top dose only | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.001 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.005 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.008 | 27/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.44×** | +3.7 | 0.008 | 22/49 (C-33 A, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.6 | 0.011 | 21/49 (CFPAC-1, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5933.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -10.3 | 4e-22 | 43/44 (NCI-H23, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.548×** | -8.4 | 2e-14 | 40/49 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **0.722×** | -5.2 | 4e-05 | 37/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.703×** | -4.9 | 1e-04 | 37/49 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.756×** | -4.8 | 2e-04 | 34/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.702×** | -4.7 | 2e-04 | 31/47 (RKO, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.765×** | -4.2 | 0.002 | 28/50 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.743×** | -4.1 | 0.003 | 30/47 (A549, SNU-423, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.742×** | -4.0 | 0.004 | 30/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.817×** | -3.9 | 0.006 | 29/49 (SW480, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Carbamazepine (drug)]] 5 µM |  | **0.779×** | -3.5 | 0.027 | 24/47 (SW 1271, A-172, …) | top dose only |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.775×** | -3.3 | 0.038 | 27/48 (NCI-H23, C32, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.717×** | -3.3 | 0.041 | 24/48 (RKO, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.793×** | -3.2 | 0.052 | 24/49 (NCI-H23, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.850× | -3.1 | 0.067 | 21/48 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.802×** | -3.1 | 0.077 | 20/48 (NCI-H23, PANC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.05 µM |  | **0.792×** | -3.0 | 0.092 | 23/47 (NCI-H23, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5933. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 115 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.5) | — |
| [[SW480 (line)]] | alt | 120 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -11.4) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 85.5 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.448× (z -9.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 53.9 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 69.2 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.31× (z +13.7) | — |
| [[KATO III (line)]] | alt | 81.1 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +14.4) | — |
| [[LoVo (line)]] | wt | 78.4 | 5 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.80× (z +12.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +11.8) | — |
| [[NCI-H1573 (line)]] | alt | 47.0 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.46× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.22× (z +12.0) | — |
| [[NCI-H1792 (line)]] | alt | 71.4 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.85× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.62× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 94.7 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 140 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -12.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 73.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.401× (z -8.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 47.7 | 3 | 0 | [[Digitoxin (drug)]] 0.5 µM 3.13× (z +9.6) | — |
| [[LOX-IMVI (line)]] | wt | 191 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 3.43× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.174× (z -14.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 102 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.09× (z +10.9) ⚠ toxic; transcription drop | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0648× (z -14.9) ⚠ toxic |
| [[A549 (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.265× (z -12.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 65.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.61× (z +8.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.26× (z +8.5) | — |
| [[H4 (line)]] | wt | 102 | 0 | 2 (2 ⚠) | — | [[Elimusertib hydrochloride (drug)]] 5 µM 0.0750× (z -9.3) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -18.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 83.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.27× (z +11.1) | — |
| [[LS 180 (line)]] | wt | 62.7 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.41× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +11.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 153 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +11.3) ⚠ cell-cycle shift, explains ~18% of this change | [[Dinaciclib (drug)]] 5 µM 0.198× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 94.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.160× (z -14.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 301 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -15.4) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SK-MEL-2 (line)]] | alt | 119 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -14.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 139 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.158× (z -13.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 62.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.0) | — |
| [[SW48 (line)]] | wt | 93.2 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 0.05 µM 3.45× (z +9.7) | — |
| [[A-172 (line)]] | wt | 98.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +9.1) | — |
| [[A-427 (line)]] | wt | 85.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +10.9) | — |
| [[CHP-212 (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0543× (z -16.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 88.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 99.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -21.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 120 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -17.6) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 76.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 170 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 78.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 107 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 69.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5933), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR17HG]] | +0.57 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.55 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[LINC01844]] | +0.55 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CTTN-DT]] | +0.53 | +0.33 / +0.55 | both halves | 1e-04 |  |
| [[LINC01357]] | +0.51 | +0.40 / +0.50 | both halves | 5e-05 |  |
| [[GOLGA7B-DT]] | +0.50 | +0.43 / +0.50 | both halves | 4e-05 |  |
| [[WT1-AS]] | +0.50 | +0.46 / +0.42 | both halves | 4e-05 |  |
| [[ACY1]] | +0.49 | +0.46 / +0.38 | both halves | 7e-05 |  |
| [[STX6]] | +0.49 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[NBPF8]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ACP7]] | +0.49 | +0.53 / +0.42 | both halves | 4e-05 |  |
| [[ETV4]] | +0.48 | +0.55 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPKOW]] | -0.51 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[CEP350]] | -0.50 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[RHOB]] | -0.49 | -0.54 / -0.39 | both halves | 5e-05 |  |
| [[PDPK1]] | -0.46 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZZEF1]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[RAB8A]] | -0.45 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[MRFAP1]] | -0.45 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[RNF40]] | -0.44 | -0.42 / -0.37 | both halves | 8e-05 |  |
| [[NUDT16L1]] | -0.44 | -0.48 / -0.39 | both halves | 6e-05 |  |
| [[TRAFD1]] | -0.44 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[PPP1R37]] | -0.44 | -0.42 / -0.38 | both halves | 6e-05 |  |
| [[EXOC8]] | -0.44 | -0.46 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TEX10's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.2% of all compounds | 0.037 | ⚠ off-target possible; 3 compounds |
| [[MCOLN2]] | B | MCOLN2 activity raises TEX10's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.18× lower at baseline in the lines without MCOLN2 | 0.070 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.6, 7.2); signed map (8.9, 47.1). **Vector** length 85.2, 28.6% of its response variance represented; |z| ≥ 3 in 1,357 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +1.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +6.6 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.9 | +0.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +1.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | +10.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.7 | +1.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.2 | +5.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.1 | -5.2 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.1 | -4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.7 | -4.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.6 | -3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.5 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.1 — chr9:100,302,077-100,352,942 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20287, bA208F1.2, Ipi1 |
| Gene groups (HGNC) | Large ribosomal subunit biogenesis complex; Armadillo like helical domain containing |
| Reactome | 4 pathways, smallest: Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol; rRNA processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NXF1](https://www.uniprot.org/uniprotkb/Q9NXF1) (Testis-expressed protein 10):

> Functions as a component of the Five Friends of Methylated CHTOP (5FMC) complex; the 5FMC complex is recruited to ZNF148 by methylated CHTOP, leading to desumoylation of ZNF148 and subsequent transactivation of ZNF148 target genes. Component of the PELP1 complex involved in the nucleolar steps of 28S rRNA maturation and the subsequent nucleoplasmic transit of the pre-60S ribosomal subunit.

**Summary**, from NCBI Gene [54881](https://www.ncbi.nlm.nih.gov/gene/54881):

> Predicted to be involved in cleavage in ITS2 between 5.8S rRNA and LSU-rRNA of tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in nucleus. Part of MLL1 complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25988](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25988) · Entrez [54881](https://www.ncbi.nlm.nih.gov/gene/54881) · UniProt [Q9NXF1](https://www.uniprot.org/uniprotkb/Q9NXF1) · Ensembl [ENSG00000136891](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136891)

## Data

Gene col 5933: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5933); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5933, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5933]; `tensor/DDL_lfc|DDL_z.npy` [5933]; `embed/gene_vectors.npy` [5933]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5933 or target_col == 5933). Every well: [[TEX10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
