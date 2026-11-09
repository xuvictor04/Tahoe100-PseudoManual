---
symbol: "TMEM245"
type: "gene"
col: 2802
ensembl_id: "ENSG00000106771"
name: "transmembrane protein 245"
location: "9q31.3"
module: 57
arm: "+"
pooled_cpm: 134.65
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 18
n_dd_up_clean: 9
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# TMEM245

*transmembrane protein 245* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.54× (z +13.3, q 1e-37, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.602× (z -15.7, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUSB]] (+0.69, fdr 1e-05), [[SORT1]] (+0.68, fdr 1e-05), [[ALDH7A1]] (+0.67, fdr 3e-05); moves opposite to [[SPHK1]] (-0.64, fdr 3e-05), [[LRIF1]] (-0.60, fdr 3e-05), [[GCNT4]] (-0.59, fdr 5e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CDCA7L]] → it (grade B ⚠); 2 go from it, the strongest it → [[NHLRC3]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +13.3 | 1e-37 | 38/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.41×** | +10.6 | 7e-24 | 37/48 (A498, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +9.8 | 2e-20 | 31/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +8.6 | 1e-15 | 34/48 (HOP62, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +8.5 | 2e-15 | 26/44 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +8.2 | 3e-14 | 28/48 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +7.1 | 7e-11 | 25/49 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.52×** | +6.7 | 1e-09 | 36/47 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.43×** | +5.8 | 3e-07 | 31/49 (A498, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.14× | +5.7 | 6e-07 | 12/48 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.15× | +4.5 | 4e-04 | 14/49 (A498, Hs 766T, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.15× | +4.4 | 4e-04 | 15/48 (KATO III, LoVo, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.15× | +4.4 | 5e-04 | 16/48 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.09× | +4.0 | 0.003 | 4/49 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change | 1.15× | +3.9 | 0.003 | 17/45 (CFPAC-1, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.13× | +3.7 | 0.006 | 10/48 (KATO III, BT-474, …) | top dose only |  |
| [[Ipatasertib (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.006 | 11/48 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.12× | +3.5 | 0.014 | 14/48 (A549, SW 900, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.602×** | -15.7 | 0e+00 | 46/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.731×** | -13.7 | 2e-40 | 33/48 (Hs 766T, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -10.1 | 7e-22 | 27/49 (A549, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.736×** | -9.5 | 4e-19 | 28/48 (COLO 205, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -8.2 | 3e-14 | 28/48 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.776×** | -7.8 | 4e-13 | 26/48 (BT-474, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.776×** | -7.8 | 4e-13 | 33/48 (Panc 03.27, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.783×** | -7.3 | 3e-11 | 26/48 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -7.1 | 6e-11 | 31/48 (HCT15, A498, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.814×** | -6.4 | 1e-08 | 24/48 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.713×** | -5.5 | 3e-06 | 26/45 (NCI-H2030, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.838× | -5.4 | 3e-06 | 22/48 (Panc 03.27, COLO 205, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.831×** | -5.4 | 3e-06 | 21/48 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -5.2 | 7e-06 | 21/48 (SNU-1, HepG2/C3A, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.729×** | -5.1 | 1e-05 | 24/48 (Hs 766T, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.772×** | -4.2 | 1e-03 | 20/48 (PANC-1, Panc 03.27, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.777×** | -4.1 | 0.001 | 19/49 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 0.876× | -4.1 | 0.001 | 14/48 (SW1417, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 164 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.24× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -11.7) |
| [[A498 (line)]] | wt | 147 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +12.1) | — |
| [[HOP62 (line)]] | alt | 116 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 204 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.349× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 201 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.449× (z -12.5) |
| [[SNU-423 (line)]] | alt | 126 | 2 | 2 | [[Belinostat (drug)]] 5 µM 1.86× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -13.6) |
| [[A-427 (line)]] | wt | 98.3 | 0 | 3 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.412× (z -12.6) |
| [[CFPAC-1 (line)]] | alt | 74.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -13.0) |
| [[COLO 205 (line)]] | alt | 199 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -12.1) |
| [[Hs 766T (line)]] | wt | 193 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -21.5) |
| [[LoVo (line)]] | wt | 108 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 1.84× (z +10.2) | [[Auranofin (drug)]] 5 µM 0.554× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -11.0) |
| [[NCI-H2030 (line)]] | alt | 164 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -16.1) |
| [[AsPC-1 (line)]] | alt | 53.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.00× (z +10.3) | — |
| [[C32 (line)]] | wt | 104 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.32× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.526× (z -10.8) |
| [[HCT15 (line)]] | alt | 194 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.366× (z -12.5) |
| [[HT-29 (line)]] | alt | 87.9 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.499× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 84.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.580× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 83.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -15.6) |
| [[SW 900 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.489× (z -8.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -8.6) |
| [[SW1417 (line)]] | alt | 127 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.540× (z -10.1) |
| [[SW480 (line)]] | alt | 167 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 1.51× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.425× (z -20.8) |
| [[A549 (line)]] | wt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.486× (z -15.5) |
| [[BT-474 (line)]] | alt | 74.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.421× (z -8.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 267 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.537× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 104 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -8.5) |
| [[HS-578T (line)]] | alt | 70.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.08× (z +8.6) | — |
| [[KATO III (line)]] | alt | 131 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.540× (z -9.2) |
| [[LS 180 (line)]] | wt | 176 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.373× (z -14.9) |
| [[PANC-1 (line)]] | alt | 115 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.608× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.440× (z -12.7) |
| [[SNU-1 (line)]] | wt | 102 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -11.6) |
| [[AN3 CA (line)]] | alt | 121 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 175 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 83.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 170 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 123 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 281 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 140 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUSB]] | +0.69 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[SORT1]] | +0.68 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[ALDH7A1]] | +0.67 | +0.44 / +0.69 | both halves | 3e-05 |  |
| [[ALAD]] | +0.62 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[HLTF]] | +0.62 | +0.37 / +0.58 | both halves | 8e-05 |  |
| [[ATP5F1C]] | +0.61 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SKP2]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[NUDT21]] | +0.60 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[CASP2]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[HADH]] | +0.59 | +0.36 / +0.56 | both halves | 1e-04 |  |
| [[EHMT2]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[ERLIN1]] | +0.59 | +0.43 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPHK1]] | -0.64 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[LRIF1]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.59 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[MSX1]] | -0.58 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[SP140]] | -0.57 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[LINC00393]] | -0.57 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[ZNF341-AS1]] | -0.56 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[LINC01829]] | -0.56 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[NPHS1]] | -0.55 | -0.36 / -0.37 | both halves | 9e-05 |  |
| [[DNAH10]] | -0.55 | -0.39 / -0.40 | both halves | 5e-05 |  |
| [[MAPK6]] | -0.55 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[NIPAL1]] | -0.55 | -0.44 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCA7L]] | B | CDCA7L activity raises TMEM245's level | lines that do not express CDCA7L (8) vs lines expressing it (42) | 1.45× lower at baseline in the lines without CDCA7L | 0.024 | ⚠ within organs, on part of the lines |
| [[GGH]] | B | GGH activity raises TMEM245's level | lines that do not express GGH (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without GGH | 0.036 | ⚠ within organs, on part of the lines; also absent: AADAT, LINC01341, HHAT; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NHLRC3]] | C | TMEM245's natural level strengthens NHLRC3's drug response | TMEM245's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.23; direction not clear | 0.094 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | TMEM245's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | TMEM245's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.406 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (12.7, 5.5); signed map (-35.0, -35.6). **Vector** length 116, 33.1% of its response variance represented; |z| ≥ 3 in 1,399 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +6.4 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +10.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +5.0 | +5.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +8.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.2 | +13.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.1 | -1.0 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +4.1 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.3 | +5.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -14.5 | -10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -13.0 | -15.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.9 | -13.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -3.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.1 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 245 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:109,015,135-109,119,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CG-2; previously C9orf5 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q9H330](https://www.uniprot.org/uniprotkb/Q9H330) carries no function annotation.

**Summary**, from NCBI Gene [23731](https://www.ncbi.nlm.nih.gov/gene/23731):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:1363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1363) · Entrez [23731](https://www.ncbi.nlm.nih.gov/gene/23731) · UniProt [Q9H330](https://www.uniprot.org/uniprotkb/Q9H330) · Ensembl [ENSG00000106771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106771)

## Data

Gene col 2802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2802); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2802]; `tensor/DDL_lfc|DDL_z.npy` [2802]; `embed/gene_vectors.npy` [2802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2802 or target_col == 2802). Every well: [[TMEM245 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM245.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
