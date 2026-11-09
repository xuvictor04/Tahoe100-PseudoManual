---
symbol: "DUSP10"
type: "gene"
col: 6760
ensembl_id: "ENSG00000143507"
name: "dual specificity phosphatase 10"
location: "1q41"
module: 112
arm: "+"
pooled_cpm: 58.93
n_lines_expressing: 39
n_dd_up: 19
n_dd_down: 29
n_dd_up_clean: 15
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 25
direction_downstream: 43
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# DUSP10

*dual specificity phosphatase 10* — 1q41

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.34× (z +15.2, q 0e+00, up in 31 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.422× (z -10.9, q 6e-25, down in 33 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 0.619× (z -6.1, q 2e-07, down in 27 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GEM]] (+0.77, fdr 7e-06), [[SOX9]] (+0.66, fdr 9e-06), [[INHBA]] (+0.62, fdr 1e-05); moves opposite to [[MTRR]] (-0.50, fdr 3e-05), [[LTBR]] (-0.50, fdr 3e-05), [[VSTM2L]] (-0.49, fdr 3e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[LINC01705]] → it (grade B ⚠); 43 go from it, the strongest it → [[PMAIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.34×** | +15.2 | 0e+00 | 31/36 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.12×** | +13.9 | 4e-41 | 34/36 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.42×** | +11.2 | 1e-26 | 31/36 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.80×** | +7.5 | 1e-11 | 26/37 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.66×** | +6.4 | 2e-08 | 27/37 (NCI-H460, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.59×** | +5.9 | 4e-07 | 26/37 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.39×** | +5.8 | 7e-07 | 22/38 (NCI-H460, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +5.3 | 9e-06 | 24/35 (SNU-423, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.51×** | +5.2 | 1e-05 | 25/37 (C32, SW 900, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +5.0 | 4e-05 | 21/36 (NCI-H460, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.47×** | +4.9 | 6e-05 | 24/37 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +4.8 | 8e-05 | 21/37 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.3 | 9e-04 | 17/36 (NCI-H1573, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.012 | 14/37 (KATO III, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.017 | 16/37 (Panc 03.27, C32, …) | rises with dose |  |
| [[Malotilate (drug)]] 0.05 µM |  | **1.29×** | +3.2 | 0.047 | 14/37 (AsPC-1, HepG2/C3A, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.2 | 0.049 | 16/37 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.066 | 9/37 (NCI-H1573, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.422×** | -10.9 | 6e-25 | 33/37 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.420×** | -10.5 | 2e-23 | 28/31 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.594×** | -6.1 | 2e-07 | 20/33 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.619×** | -6.1 | 2e-07 | 27/37 (NCI-H2347, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.720×** | -5.9 | 5e-07 | 23/37 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.633×** | -5.8 | 7e-07 | 24/37 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -4.9 | 8e-05 | 21/38 (NCI-H2347, SNU-423, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.679×** | -4.9 | 8e-05 | 24/37 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.704×** | -4.4 | 6e-04 | 19/37 (A549, SW 900, …) | all doses, flat | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.697×** | -4.4 | 6e-04 | 23/36 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.707×** | -4.4 | 6e-04 | 22/37 (KATO III, Panc 03.27, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.710×** | -4.3 | 7e-04 | 20/37 (NCI-H2347, A549, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **0.710×** | -4.3 | 7e-04 | 20/37 (NCI-H2347, SW 900, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.711×** | -4.1 | 0.001 | 20/38 (NCI-H2347, NCI-H1573, …) | all doses, flat |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **0.724×** | -4.1 | 0.002 | 22/37 (LS 180, KATO III, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.728×** | -4.0 | 0.002 | 23/37 (NCI-H2347, A549, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.713×** | -3.9 | 0.003 | 20/36 (NCI-H2347, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.732×** | -3.9 | 0.003 | 20/37 (NCI-H2347, SNU-423, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.810×** | -3.8 | 0.005 | 15/37 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 42.4 | 14 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.50× (z +21.9) | — |
| [[NCI-H2347 (line)]] | alt | 349 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.200× (z -22.6) |
| [[A-172 (line)]] | wt | 55.9 | 5 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.14× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.159× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 27.8 | 6 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.5 µM 5.44× (z +12.5) | [[Clobetasol propionate (drug)]] 0.05 µM 0.316× (z -8.5) |
| [[SNU-423 (line)]] | alt | 235 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.174× (z -19.9) |
| [[HOP62 (line)]] | alt | 60.3 | 3 | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 3.91× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.236× (z -9.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 166 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0667× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.114× (z -11.2) |
| [[A498 (line)]] | wt | 42.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.3× (z +21.6) | — |
| [[A549 (line)]] | wt | 31.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +15.8) | — |
| [[C32 (line)]] | wt | 47.1 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +12.5) | — |
| [[CHP-212 (line)]] | wt | 165 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0865× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.158× (z -10.4) |
| [[HS-578T (line)]] | alt | 60.1 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -13.5) |
| [[Panc 03.27 (line)]] | alt | 200 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0921× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -13.3) |
| [[AsPC-1 (line)]] | alt | 30.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.20× (z +19.7) | — |
| [[CFPAC-1 (line)]] | alt | 71.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -9.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 21.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +10.0) | — |
| [[NCI-H1792 (line)]] | alt | 60.4 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.30× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.242× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 107 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0784× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -9.2) |
| [[J82 (line)]] | alt | 41.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.04× (z +17.2) | — |
| [[KATO III (line)]] | alt | 30.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.208× (z -11.2) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 32.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +12.7) | — |
| [[LS 180 (line)]] | wt | 59.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.192× (z -12.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 80.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.121× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -8.5) |
| [[BT-474 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 202 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 6.49× (z +9.5) | — |
| [[HEC-1-A (line)]] | alt | 35.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 30.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 86.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -10.2) |
| [[SW 900 (line)]] | alt | 99.7 | 0 | 1 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.259× (z -9.0) |
| [[SW1417 (line)]] | alt | 69.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +11.7) | — |
| [[A-427 (line)]] | wt | 12.8 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.95 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 64.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 13.5 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.02 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.60 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 9.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GEM]] | +0.77 | +0.77 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SOX9]] | +0.66 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[INHBA]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CADM1]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[HDAC9]] | +0.61 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[KIAA1217]] | +0.61 | +0.57 / +0.64 | both halves | 1e-05 |  |
| [[IER3]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[BMP2]] | +0.61 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.61 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[RND1]] | +0.59 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[NR3C1]] | +0.59 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[RASGRP3]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 | pathway: MAPK family signaling cascades |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTRR]] | -0.50 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[LTBR]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[VSTM2L]] | -0.49 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[ARMC8]] | -0.49 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[PHKA1]] | -0.48 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[ABCB10]] | -0.48 | -0.42 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 24, C 1. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01705]] | B | LINC01705 activity raises DUSP10's level | lines that do not express LINC01705 (27) vs lines expressing it (23) | 3.51× lower at baseline in the lines without LINC01705 | 1e-03 | ⚠ within organs, on part of the lines; also absent: ROR1-AS1, TIMP3, ENSG00000250137 |
| [[BDKRB2]] | B | BDKRB2 activity raises DUSP10's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 3.45× lower at baseline in the lines without BDKRB2 | 0.002 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[BMP2]] | B | BMP2 activity raises DUSP10's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without BMP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[CSF1R]] | B | CSF1R activity raises DUSP10's level | lines that do not express CSF1R (26) vs lines expressing it (24) | 3.21× lower at baseline in the lines without CSF1R | 0.006 | ⚠ within organs, on part of the lines; also absent: FKBP9P1-1, TIMP3, GDNF; maybe low, not absent |
| [[PLAU]] | B | PLAU activity raises DUSP10's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.62× lower at baseline in the lines without PLAU | 0.008 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[RRAD]] | B | RRAD activity raises DUSP10's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.83× lower at baseline in the lines without RRAD | 0.009 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[CSF2]] | B | CSF2 activity raises DUSP10's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 2.72× lower at baseline in the lines without CSF2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2 |
| [[GEM]] | B | GEM activity raises DUSP10's level | lines that do not express GEM (9) vs lines expressing it (41) | 3.51× lower at baseline in the lines without GEM | 0.015 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[RASGRP3]] | B | RASGRP3 activity raises DUSP10's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.43× lower at baseline in the lines without RASGRP3 | 0.017 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[AHR]] | B | AHR activity raises DUSP10's level | lines that do not express AHR (7) vs lines expressing it (43) | 3.96× lower at baseline in the lines without AHR | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000283321, VDR, GPR39 |
| [[MIR3142HG]] | B | MIR3142HG activity raises DUSP10's level | lines that do not express MIR3142HG (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without MIR3142HG | 0.020 | ⚠ within organs, on part of the lines; also absent: CTHRC1, IL6, ENSG00000291130 |
| [[CXCL8]] | B | CXCL8 activity raises DUSP10's level | lines that do not express CXCL8 (20) vs lines expressing it (30) | 2.99× lower at baseline in the lines without CXCL8 | 0.026 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, IL1R1, C15orf48 |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 42, C 1. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMAIP1]] | B | DUSP10 activity raises PMAIP1's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without DUSP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[BDKRB2]] | B | DUSP10 activity raises BDKRB2's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 4.82× lower at baseline in the lines without DUSP10 | 0.003 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[BTG1]] | B | DUSP10 activity raises BTG1's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.02× lower at baseline in the lines without DUSP10 | 0.004 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[RND3]] | B | DUSP10 activity raises RND3's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.46× lower at baseline in the lines without DUSP10 | 0.006 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[AHR]] | B | DUSP10 activity raises AHR's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.42× lower at baseline in the lines without DUSP10 | 0.006 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[NR3C1]] | B | DUSP10 activity raises NR3C1's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 4.32× lower at baseline in the lines without DUSP10 | 0.012 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[KIAA1217]] | B | DUSP10 activity raises KIAA1217's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.99× lower at baseline in the lines without DUSP10 | 0.021 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[FAM107B]] | B | DUSP10 activity raises FAM107B's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 2.95× lower at baseline in the lines without DUSP10 | 0.028 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[IL1A]] | B | DUSP10 activity raises IL1A's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.50× lower at baseline in the lines without DUSP10 | 0.030 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[BHLHE40]] | B | DUSP10 activity raises BHLHE40's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 1.85× lower at baseline in the lines without DUSP10 | 0.032 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[CXCL8]] | B | DUSP10 activity raises CXCL8's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 4.88× lower at baseline in the lines without DUSP10 | 0.035 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[TLE4]] | B | DUSP10 activity raises TLE4's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.62× lower at baseline in the lines without DUSP10 | 0.035 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.708). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.2, 3.0); signed map (44.8, 12.5). **Vector** length 122, 37.6% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.55 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.51 to 5); *KRAS signaling up* (hallmark, mean cos +0.54 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +13.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.6 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.7 | +1.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.5 | +2.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.3 | -0.3 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -5.2 | -4.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -5.2 | -5.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -5.0 | -6.1 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.5 | -3.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.5 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q41 — chr1:221,701,424-221,742,089 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MKP-5, MKP5 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Reactome | 8 pathways, smallest: Signaling by MAPK mutants; RAF-independent MAPK1/3 activation; Negative regulation of MAPK pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6W6](https://www.uniprot.org/uniprotkb/Q9Y6W6) (Dual specificity protein phosphatase 10):

> Protein phosphatase involved in the inactivation of MAP kinases. Has a specificity for the MAPK11/MAPK12/MAPK13/MAPK14 subfamily. It preferably dephosphorylates p38.

**Summary**, from NCBI Gene [11221](https://www.ncbi.nlm.nih.gov/gene/11221):

> Dual specificity protein phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the MAP kinase superfamily, which is associated with cellular proliferation and differentiation. Different members of this family of dual specificity phosphatases show distinct substrate specificities for MAP kinases, different tissue distribution and subcellular localization, and different modes of …

**Accessions** — [HGNC:3065](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3065) · Entrez [11221](https://www.ncbi.nlm.nih.gov/gene/11221) · UniProt [Q9Y6W6](https://www.uniprot.org/uniprotkb/Q9Y6W6) · Ensembl [ENSG00000143507](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143507)

## Data

Gene col 6760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6760); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6760]; `tensor/DDL_lfc|DDL_z.npy` [6760]; `embed/gene_vectors.npy` [6760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6760 or target_col == 6760). Every well: [[DUSP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
