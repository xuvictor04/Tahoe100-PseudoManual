---
symbol: "LRCH3"
type: "gene"
col: 11764
ensembl_id: "ENSG00000186001"
name: "leucine rich repeats and calponin homology domain containing 3"
location: "3q29"
module: 20
arm: "-"
pooled_cpm: 237.88
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 19
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# LRCH3

*leucine rich repeats and calponin homology domain containing 3* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.63× (z +20.7, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.355× (z -29.8, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.427× (z -25.4, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XIAP]] (+0.72, fdr 9e-06), [[RBX1]] (+0.71, fdr 7e-06), [[UNK]] (+0.71, fdr 7e-06); moves opposite to [[TCP1]] (-0.68, fdr 7e-06), [[BLTP2]] (-0.65, fdr 1e-05), [[CDK9]] (-0.63, fdr 1e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[EMP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11764.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +20.7 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.73×** | +16.5 | 0e+00 | 47/48 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +14.6 | 0e+00 | 45/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +11.0 | 4e-26 | 43/48 (BT-474, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +10.6 | 4e-24 | 37/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.35×** | +8.9 | 6e-17 | 39/48 (BT-474, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.25×** | +6.7 | 1e-09 | 25/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.8 | 0.012 | 13/47 (BT-474, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.14× | +3.7 | 0.016 | 10/49 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.09× | +3.5 | 0.026 | 8/49 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.047 | 14/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | 1.21× | +3.0 | 0.12 | 14/48 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11764.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.355×** | -29.8 | 0e+00 | 40/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.395×** | -27.8 | 0e+00 | 48/49 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.382×** | -26.6 | 0e+00 | 44/45 (MIA PaCa-2, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.427×** | -25.4 | 0e+00 | 47/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.452×** | -23.7 | 0e+00 | 48/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.471×** | -22.5 | 0e+00 | 48/48 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.541×** | -18.4 | 0e+00 | 44/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.634×** | -13.6 | 3e-40 | 47/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.643×** | -13.2 | 7e-38 | 45/48 (RPMI-7951, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.676×** | -11.7 | 1e-29 | 43/48 (PANC-1, hTERT-HPNE, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | 0.849× | -6.9 | 2e-10 | 24/49 (A549, RPMI-7951, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.662×** | -6.4 | 6e-09 | 40/49 (A549, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.820×** | -5.7 | 6e-07 | 25/47 (SNU-423, A-172, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.847× | -4.9 | 3e-05 | 23/48 (J82, CFPAC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.738×** | -4.7 | 8e-05 | 28/49 (HS-578T, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.869× | -4.2 | 0.001 | 16/48 (CFPAC-1, J82, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.866× | -4.1 | 0.001 | 18/48 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.806×** | -3.4 | 0.018 | 21/48 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.808×** | -3.3 | 0.019 | 17/48 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.05 µM |  | 0.895× | -3.3 | 0.021 | 2/48 (RKO, SW48) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.816×** | -3.2 | 0.032 | 17/48 (MIA PaCa-2, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.824×** | -3.0 | 0.049 | 20/49 (NCI-H23, PANC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11764. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 284 | 2 (1 ⚠) | 14 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.203× (z -30.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.333× (z -20.9) |
| [[PANC-1 (line)]] | alt | 322 | 7 (2 ⚠) | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +36.8) | [[Dinaciclib (drug)]] 5 µM 0.329× (z -24.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.417× (z -19.6) |
| [[NCI-H23 (line)]] | alt | 274 | 5 (1 ⚠) | 9 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +13.3) | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -20.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.322× (z -19.6) |
| [[HEC-1-A (line)]] | alt | 370 | 2 | 11 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.406× (z -17.4) |
| [[HepG2_C3A (line)]] | wt | 197 | 5 (1 ⚠) | 8 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 2.25× (z +11.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.21× (z +11.1) | [[Dinaciclib (drug)]] 0.05 µM 0.249× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 0.5 µM 0.370× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 228 | 4 (1 ⚠) | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.01× (z +11.7) | [[Dinaciclib (drug)]] 5 µM 0.141× (z -31.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -17.0) |
| [[HS-578T (line)]] | alt | 269 | 1 | 11 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -17.0) |
| [[LoVo (line)]] | wt | 181 | 6 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +20.4) | [[Panobinostat (drug)]] 5 µM 0.452× (z -15.4) |
| [[SNU-1 (line)]] | wt | 225 | 6 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.394× (z -12.7) |
| [[SW1417 (line)]] | alt | 201 | 4 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.443× (z -15.0) |
| [[SW480 (line)]] | alt | 304 | 4 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +17.2) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -28.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -21.5) |
| [[MIA PaCa-2 (line)]] | alt | 368 | 1 | 10 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +13.3) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -25.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.283× (z -24.8) |
| [[NCI-H460 (line)]] | wt | 158 | 4 (2 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +22.1) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -14.9) |
| [[SNU-423 (line)]] | alt | 259 | 0 | 11 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.348× (z -18.6) |
| [[A549 (line)]] | wt | 239 | 1 | 9 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.395× (z -22.8) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.296× (z -21.1) |
| [[HOP62 (line)]] | alt | 328 | 1 | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -22.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.323× (z -16.2) |
| [[Hs 766T (line)]] | wt | 164 | 3 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +11.9) | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -14.8) |
| [[J82 (line)]] | alt | 275 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.317× (z -19.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.431× (z -14.9) |
| [[NCI-H2347 (line)]] | alt | 217 | 2 | 8 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.395× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.406× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 342 | 2 (1 ⚠) | 8 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.422× (z -14.7) |
| [[RKO (line)]] | wt | 230 | 3 (1 ⚠) | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +15.1) | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -27.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.368× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 309 | 1 | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.369× (z -16.2) |
| [[AsPC-1 (line)]] | alt | 190 | 4 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 254 | 1 (1 ⚠) | 8 (3 ⚠) | [[Digitoxin (drug)]] 5 µM 1.71× (z +8.8) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.384× (z -15.7) |
| [[hTERT-HPNE (line)]] | wt | 244 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.413× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 281 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 371 | 2 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.133× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.259× (z -16.7) |
| [[SK-MEL-2 (line)]] | alt | 261 | 2 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.319× (z -18.1) |
| [[A498 (line)]] | wt | 133 | 2 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.507× (z -11.0) |
| [[H4 (line)]] | wt | 276 | 0 | 8 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.315× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -12.4) |
| [[SW 900 (line)]] | alt | 168 | 1 | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.96× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.341× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.438× (z -11.8) |
| [[A-427 (line)]] | wt | 194 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.369× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.498× (z -11.2) |
| [[BT-474 (line)]] | alt | 183 | 6 (2 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 4.49× (z +21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.90× (z +19.8) | [[Panobinostat (drug)]] 5 µM 0.559× (z -8.5) |
| [[C32 (line)]] | wt | 186 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.445× (z -10.3) |
| [[COLO 205 (line)]] | alt | 188 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.419× (z -12.1) |
| [[HCT15 (line)]] | alt | 269 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.363× (z -14.7) |
| [[LS 180 (line)]] | wt | 151 | 2 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.459× (z -10.0) |
| [[HT-29 (line)]] | alt | 139 | 3 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.0) | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -12.3) |
| [[NCI-H2030 (line)]] | alt | 222 | 1 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.459× (z -12.9) |
| [[SW48 (line)]] | wt | 190 | 3 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.307× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -10.0) |
| [[CHP-212 (line)]] | wt | 213 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -11.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 112 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.19× (z +10.9) | [[Docetaxel (drug)]] 0.05 µM 0.502× (z -9.5) ⚠ transcription drop |
| [[AN3 CA (line)]] | alt | 225 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.394× (z -8.7) |
| [[C-33 A (line)]] | alt | 137 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 377 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.257× (z -11.3) |
| [[NCI-H2122 (line)]] | alt | 239 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 234 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11764), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XIAP]] | +0.72 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[RBX1]] | +0.71 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[UNK]] | +0.71 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[EIF1B]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[TNRC6C]] | +0.69 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[WBP4]] | +0.67 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[FAM193A]] | +0.67 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[OFD1]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[AK6]] | +0.65 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[CROCCP2-1]] | +0.65 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[COX17]] | +0.64 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[CYP20A1]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCP1]] | -0.68 | -0.67 / -0.60 | both halves | 7e-06 |  |
| [[BLTP2]] | -0.65 | -0.61 / -0.54 | both halves | 1e-05 |  |
| [[CDK9]] | -0.63 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[SKP2]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[FTSJ1]] | -0.60 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[TMED7]] | -0.60 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[USP5]] | -0.60 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[AHSA1]] | -0.60 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[MINPP1]] | -0.60 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[STRAP]] | -0.59 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[PGAM1]] | -0.59 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[TSKU]] | -0.58 | -0.57 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EMP3]] | B | EMP3 activity raises LRCH3's level | lines that do not express EMP3 (9) vs lines expressing it (41) | 1.59× lower at baseline in the lines without EMP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: LGALS1, SYDE1, SPAG17 |
| [[FOXD1]] | B | FOXD1 activity raises LRCH3's level | lines that do not express FOXD1 (10) vs lines expressing it (40) | 1.34× lower at baseline in the lines without FOXD1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ZIC2, SCD5, FGF2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.687). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-22.2, -14.6); signed map (-1.7, -8.2). **Vector** length 126, 48.1% of its response variance represented; |z| ≥ 3 in 1,534 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.8 | +20.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +10.0 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +8.4 | +6.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.2 | +14.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +7.7 | +16.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | -1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.2 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | +2.9 | +1.7 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -8.5 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.3 | -3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.3 | -18.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.2 | -13.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.6 | -26.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -4.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.0 | -6.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeats and calponin homology domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,791,226-197,888,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC4126 |
| Gene groups (HGNC) | Leucine rich repeats and calponin homology domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96II8](https://www.uniprot.org/uniprotkb/Q96II8) (DISP complex protein LRCH3):

> As part of the DISP complex, may regulate the association of septins with actin and thereby regulate the actin cytoskeleton.

**Summary**, from NCBI Gene [84859](https://www.ncbi.nlm.nih.gov/gene/84859):

> Involved in septin cytoskeleton organization. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28637](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28637) · Entrez [84859](https://www.ncbi.nlm.nih.gov/gene/84859) · UniProt [Q96II8](https://www.uniprot.org/uniprotkb/Q96II8) · Ensembl [ENSG00000186001](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186001)

## Data

Gene col 11764: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11764); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11764, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11764]; `tensor/DDL_lfc|DDL_z.npy` [11764]; `embed/gene_vectors.npy` [11764]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11764 or target_col == 11764). Every well: [[LRCH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRCH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
