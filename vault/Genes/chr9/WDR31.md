---
symbol: "WDR31"
type: "gene"
col: 7254
ensembl_id: "ENSG00000148225"
name: "WD repeat domain 31"
location: "9q32"
module: 10
arm: "+"
pooled_cpm: 7.8
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 23
n_dd_up_clean: 23
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# WDR31

*WD repeat domain 31* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.68× (z +13.9, q 2e-41, up in 10 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 2.36× (z +9.6, q 2e-19, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.300× (z -13.4, q 2e-38, down in 37 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARF]] (+0.62, fdr 1e-05), [[SCRN3]] (+0.60, fdr 7e-06), [[LYRM9]] (+0.59, fdr 1e-05); moves opposite to [[MAD1L1]] (-0.47, fdr 4e-05), [[PDCD6]] (-0.47, fdr 4e-05), [[SLC25A44]] (-0.45, fdr 2e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7254.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.68×** | +13.9 | 2e-41 | 10/13 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.22×** | +13.0 | 3e-36 | 25/28 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.36×** | +9.6 | 2e-19 | 38/47 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +7.9 | 3e-13 | 32/46 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.9 | 3e-13 | 17/22 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.92×** | +7.3 | 3e-11 | 27/47 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.76×** | +6.3 | 3e-08 | 26/47 (A498, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.75×** | +5.9 | 3e-07 | 22/44 (HEC-1-A, KATO III, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.60×** | +5.2 | 1e-05 | 19/46 (KATO III, LS 180, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.58×** | +5.1 | 2e-05 | 19/47 (KATO III, A549, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.7 | 2e-04 | 13/37 (NCI-H460, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 3e-04 | 16/44 (KATO III, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.32×** | +4.4 | 5e-04 | 14/47 (HEC-1-A, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +4.3 | 7e-04 | 13/41 (SK-MEL-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.002 | 14/44 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 13/46 (SW480, C32, …) | two highest doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 13/48 (SW480, SK-MEL-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +3.6 | 0.010 | 10/45 (NCI-H23, SW480, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.011 | 10/46 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7254.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.300×** | -13.4 | 2e-38 | 37/47 (COLO 205, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.347×** | -11.8 | 1e-29 | 37/45 (COLO 205, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.388×** | -10.6 | 9e-24 | 29/43 (A-427, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.401×** | -10.2 | 3e-22 | 34/45 (COLO 205, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.493×** | -7.9 | 4e-13 | 29/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.264×** | -7.8 | 8e-13 | 30/41 (KATO III, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.565×** | -6.0 | 1e-07 | 22/43 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.376×** | -5.7 | 8e-07 | 21/46 (HT-29, NCI-H23, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.601×** | -5.7 | 8e-07 | 21/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.634×** | -5.1 | 2e-05 | 20/48 (NCI-H23, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.636×** | -5.0 | 2e-05 | 20/46 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.486×** | -4.2 | 0.001 | 16/37 (COLO 205, SHP-77, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.672×** | -4.2 | 0.001 | 18/46 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -4.0 | 0.003 | 15/45 (LoVo, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.707×** | -3.9 | 0.004 | 14/42 (COLO 205, RKO, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.711×** | -3.8 | 0.005 | 20/44 (COLO 205, C-33 A, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.537×** | -3.6 | 0.010 | 9/39 (NCI-H460, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7254. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 19.2 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0131× (z -21.1) |
| [[A-427 (line)]] | wt | 9.65 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0411× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Cyclosporin A (drug)]] 0.5 µM 0.126× (z -10.8) |
| [[A-172 (line)]] | wt | 9.66 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -9.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 6.97 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.12× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 17.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.75× (z +12.4) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.151× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0331× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -11.7) |
| [[NCI-H460 (line)]] | wt | 9.72 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 4.72× (z +8.6) ⚠ toxic | [[Ixazomib citrate (drug)]] 5 µM 0.223× (z -8.7) |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 2 | — | [[Canagliflozin (drug)]] 5 µM 0.0750× (z -11.5) |
| [[SW1417 (line)]] | alt | 9.47 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.04× (z +8.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.160× (z -9.0) |
| [[HCT15 (line)]] | alt | 8.66 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0359× (z -10.9) |
| [[HOP62 (line)]] | alt | 10.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.179× (z -9.3) |
| [[HS-578T (line)]] | alt | 5.73 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0561× (z -10.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -9.6) |
| [[J82 (line)]] | alt | 10.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.55× (z +9.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 6.21 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -8.7) |
| [[LS 180 (line)]] | wt | 7.86 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 10.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -8.8) |
| [[RKO (line)]] | wt | 9.28 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -8.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 13.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.25× (z +9.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -8.5) |
| [[A549 (line)]] | wt | 9.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.42 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.29 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.63 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7254), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARF]] | +0.62 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[SCRN3]] | +0.60 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[LYRM9]] | +0.59 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[ARPIN]] | +0.59 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[UROS]] | +0.59 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[MTMR3]] | +0.58 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[CCDC191]] | +0.57 | +0.71 / +0.34 | both halves | 1e-04 |  |
| [[C11orf65]] | +0.57 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[IFTAP]] | +0.56 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[ARMH1]] | +0.55 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[TTC12]] | +0.55 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[ZMAT1]] | +0.55 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAD1L1]] | -0.47 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[PDCD6]] | -0.47 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[SLC25A44]] | -0.45 | -0.32 / -0.33 | both halves | 2e-04 |  |
| [[TOP3A]] | -0.45 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[IL20RB]] | -0.45 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[CCDC168]] | -0.44 | -0.31 / -0.34 | both halves | 2e-04 |  |
| [[TNFRSF10A]] | -0.43 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[GPRC5D-AS1]] | -0.43 | -0.37 / -0.36 | both halves | 1e-04 |  |
| [[TMEM181]] | -0.43 | -0.40 / -0.41 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers WDR31's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |
| [[SIRT5]] | C | SIRT5's natural level strengthens WDR31's drug response | SIRT5's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.49; direction not clear | 0.054 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.378). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-28.4, 22.7); signed map (16.8, -42.2). **Vector** length 60.3, 9.87% of its response variance represented; |z| ≥ 3 in 1,080 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.6 | +13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +13.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +1.9 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.7 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +5.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.5 | +1.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.4 | +3.8 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -2.6 | -6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.5 | -4.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.7 | +2.1 |
|  | [[Hesperidin (drug)]] 0.05 µM |  | -1.2 | -1.8 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 31 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,313,222-113,340,298 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35921 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q8NA23](https://www.uniprot.org/uniprotkb/Q8NA23) carries no function annotation.

**Summary**, from NCBI Gene [114987](https://www.ncbi.nlm.nih.gov/gene/114987):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD), which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes, including cell cycle progression, signal transduction, apoptosis, and gene regulation. Multiple alternatively spliced transcript variants encoding distinct isoforms …

**Accessions** — [HGNC:21421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21421) · Entrez [114987](https://www.ncbi.nlm.nih.gov/gene/114987) · UniProt [Q8NA23](https://www.uniprot.org/uniprotkb/Q8NA23) · Ensembl [ENSG00000148225](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148225)

## Data

Gene col 7254: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7254); `tables/drug_effects.parquet` (54 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7254, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7254]; `tensor/DDL_lfc|DDL_z.npy` [7254]; `embed/gene_vectors.npy` [7254]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7254 or target_col == 7254). Every well: [[WDR31 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR31.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
