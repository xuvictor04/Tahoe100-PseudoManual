---
symbol: "LIFR"
type: "gene"
col: 3479
ensembl_id: "ENSG00000113594"
name: "LIF receptor subunit alpha"
location: "5p13.1"
module: 167
arm: "+"
pooled_cpm: 96.69
n_lines_expressing: 38
n_dd_up: 13
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 28
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# LIFR

*LIF receptor subunit alpha* — 5p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.06× (z +17.1, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.751× (z -9.5, q 1e-18, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RALGAPA2]] (+0.66, fdr 4e-05), [[RNF24]] (+0.63, fdr 2e-05), [[UGCG]] (+0.63, fdr 2e-05); moves opposite to [[DNAAF10]] (-0.63, fdr 3e-05), [[ANKAR]] (-0.61, fdr 5e-05), [[ACAD9]] (-0.59, fdr 4e-05).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[BIRC3]] → it (grade B ⚠); 28 go from it, the strongest it → cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.06×** | +17.1 | 0e+00 | 35/36 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.03×** | +16.7 | 0e+00 | 34/36 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +15.4 | 0e+00 | 33/36 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.90×** | +15.1 | 0e+00 | 34/36 (J82, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.58×** | +10.7 | 7e-25 | 32/36 (J82, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +9.2 | 3e-18 | 30/37 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.43×** | +8.4 | 4e-15 | 26/36 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +8.1 | 3e-14 | 29/37 (A498, C32, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +6.7 | 2e-09 | 20/36 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.31×** | +6.5 | 5e-09 | 23/36 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.26×** | +5.5 | 2e-06 | 21/36 (BT-474, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.003 | 12/36 (Panc 03.27, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.14× | +3.7 | 0.010 | 12/38 (SW 900, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.4 | 0.027 | 12/35 (BT-474, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.3 | 0.041 | 10/36 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.057 | 9/38 (SW 900, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.11× | +3.0 | 0.076 | 11/36 (Panc 03.27, NCI-H2347, …) | two highest doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.09× | +3.0 | 0.093 | 1/37 (AN3 CA) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -9.5 | 1e-18 | 21/37 (Panc 03.27, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -7.6 | 9e-12 | 23/36 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | **0.736×** | -7.2 | 1e-10 | 22/37 (BT-474, J82, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.733×** | -7.0 | 4e-10 | 19/33 (Panc 03.27, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.568×** | -7.0 | 4e-10 | 18/37 (A498, Panc 03.27, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.771×** | -5.9 | 4e-07 | 19/35 (CFPAC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change | **0.776×** | -5.5 | 3e-06 | 20/34 (A549, J82, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.796×** | -5.3 | 6e-06 | 18/36 (HOP62, C32, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.837× | -4.2 | 0.002 | 14/36 (C32, A-172, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.717×** | -4.1 | 0.003 | 14/34 (HS-578T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.722×** | -4.0 | 0.003 | 14/36 (C32, A-172, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.734×** | -3.8 | 0.007 | 14/36 (C32, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.850× | -3.7 | 0.011 | 15/36 (NCI-H23, BT-474, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.857× | -3.6 | 0.013 | 10/37 (CFPAC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.862× | -3.4 | 0.021 | 12/36 (C32, NCI-H1573, …) | two highest doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.875× | -3.1 | 0.056 | 3/37 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.780×** | -3.0 | 0.063 | 9/36 (C32, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | 0.879× | -3.0 | 0.071 | 13/36 (Hs 766T, CHP-212, …) | inconsistent across doses |  |
| [[Naproxen (drug)]] 0.05 µM |  | 0.874× | -2.9 | 0.091 | 5/36 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.792×** | -2.8 | 0.099 | 7/36 (C32, CFPAC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 80.4 | 5 (2 ⚠) | 4 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 5.10× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.87× (z +11.5) | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[NCI-H2347 (line)]] | alt | 72.7 | 9 (2 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.10× (z +16.7) | — |
| [[J82 (line)]] | alt | 138 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.74× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.3) |
| [[A498 (line)]] | wt | 74.0 | 5 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.82× (z +12.8) | [[TAK-901 (drug)]] 5 µM 0.250× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 254 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -12.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -11.7) |
| [[SNU-423 (line)]] | alt | 96.9 | 4 | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.21× (z +9.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.532× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 244 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -10.2) |
| [[NCI-H2030 (line)]] | alt | 99.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +14.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.25× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 116 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.19× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.224× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -13.6) |
| [[LOX-IMVI (line)]] | wt | 27.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.36× (z +11.0) | — |
| [[PANC-1 (line)]] | alt | 152 | 4 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +15.4) | — |
| [[SW 900 (line)]] | alt | 350 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.372× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.450× (z -9.4) |
| [[C32 (line)]] | wt | 216 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.82× (z +9.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -12.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 266 | 1 | 2 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.13× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.254× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 176 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change |
| [[A549 (line)]] | wt | 88.9 | 1 | 1 (1 ⚠) | [[Cobimetinib (drug)]] 5 µM 2.59× (z +9.7) | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[AsPC-1 (line)]] | alt | 35.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.27× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 51.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.40× (z +9.2) | — |
| [[NCI-H1573 (line)]] | alt | 33.1 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 2.25× (z +9.4) | — |
| [[SHP-77 (line)]] | alt | 377 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -9.8) |
| [[A-172 (line)]] | wt | 120 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.7) | — |
| [[A-427 (line)]] | wt | 84.7 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.70× (z +8.8) | — |
| [[AN3 CA (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -10.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[H4 (line)]] | wt | 123 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.139× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 102 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.6) | — |
| [[KATO III (line)]] | alt | 27.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.79× (z +8.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 60.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.4) |
| [[C-33 A (line)]] | alt | 76.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 141 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.22 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 6.63 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.71 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 91.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.43 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.64 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.98 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.74 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*38 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RALGAPA2]] | +0.66 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[RNF24]] | +0.63 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[UGCG]] | +0.63 | +0.46 / +0.54 | both halves | 2e-05 | same gene group |
| [[SLC44A1]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 | same gene group |
| [[PLD1]] | +0.59 | +0.36 / +0.62 | both halves | 1e-04 |  |
| [[SPTSSA]] | +0.58 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[SAA2]] | +0.56 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[CFD]] | +0.56 | +0.37 / +0.38 | both halves | 8e-05 |  |
| [[CLMN]] | +0.56 | +0.44 / +0.38 | both halves | 6e-05 |  |
| [[USP2]] | +0.55 | +0.46 / +0.40 | both halves | 5e-05 |  |
| [[PTGES]] | +0.53 | +0.46 / +0.49 | both halves | 3e-05 |  |
| [[SKAP2]] | +0.53 | +0.34 / +0.51 | both halves | 1e-04 |  |

## Genes that move opposite

*62 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF10]] | -0.63 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[ANKAR]] | -0.61 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ACAD9]] | -0.59 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SMIM15-AS1]] | -0.59 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[MAPKAPK5]] | -0.58 | -0.55 / -0.35 | both halves | 1e-04 |  |
| [[CSTF3]] | -0.58 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[LINC01355]] | -0.58 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[PCBD2]] | -0.56 | -0.34 / -0.42 | both halves | 1e-04 | same gene group |
| [[PCBP1-AS1]] | -0.56 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[PRC1-AS1]] | -0.56 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[SMC5-DT]] | -0.55 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[ZNF213-AS1]] | -0.55 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIRC3]] | B | BIRC3 activity lowers LIFR's level | lines that do not express BIRC3 (5) vs lines expressing it (45) | 1.50× higher at baseline in the lines without BIRC3 | 0.078 | ⚠ within organs, on part of the lines; also absent: LRRC8E, TRIM34, IFI35 |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 0, C 28. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Gallic acid (hydrate) (drug)]] 0.05 µM | C | LIFR activity raises the cells' numbers under Gallic acid (hydrate) 0.05 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.83× the cells of the other lines | 0.009 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Mifepristone (drug)]] 0.5 µM | C | LIFR activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.84× the cells of the other lines | 0.014 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[MK-3903 (drug)]] 5 µM | C | LIFR activity raises the cells' numbers under MK-3903 5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.76× the cells of the other lines | 0.015 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[9-ING-41 (drug)]] 0.5 µM | C | LIFR activity raises the cells' numbers under 9-ING-41 0.5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.80× the cells of the other lines | 0.020 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Almonertinib (hydrochloride) (drug)]] 0.5 µM | C | LIFR activity raises the cells' numbers under Almonertinib (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.84× the cells of the other lines | 0.028 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Erlotinib (drug)]] 0.05 µM | C | LIFR activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.24× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Ixazomib (drug)]] 0.05 µM | C | LIFR activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.25× the cells of the other lines | 0.030 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Lonafarnib (drug)]] 5 µM | C | LIFR activity raises the cells' numbers under Lonafarnib 5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.30× the cells of the other lines | 0.034 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Furosemide (drug)]] 0.5 µM | C | LIFR activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.17× the cells of the other lines | 0.041 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[HI-TOPK-032 (drug)]] 0.05 µM | C | LIFR activity lowers the cells' numbers under HI-TOPK-032 0.05 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.34× the cells of the other lines | 0.046 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[BAY1125976 (drug)]] 0.5 µM | C | LIFR activity raises the cells' numbers under BAY1125976 0.5 µM (protects the cells) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 0.79× the cells of the other lines | 0.048 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |
| cells under [[Erdafitinib (drug)]] 5 µM | C | LIFR activity lowers the cells' numbers under Erdafitinib 5 µM (makes them more sensitive) | lines that do not express LIFR (12) vs lines expressing it (36) | the lines without LIFR: 1.15× the cells of the other lines | 0.056 | ⚠ tissue-confounded; across organs; co-occurs with APC, BRAF; also absent: WHAMMP2, ENSG00000286964, OSMR-DT |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.0, 6.3); signed map (-9.1, 18.6). **Vector** length 103, 24.6% of its response variance represented; |z| ≥ 3 in 1,168 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.9 | +15.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.6 | +9.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.7 | +15.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +16.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +1.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.1 | +1.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.4 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -3.3 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -5.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | -2.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | LIF receptor subunit alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p13.1 — chr5:38,474,668-38,608,354 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD118 |
| Gene groups (HGNC) | CD molecules; Fibronectin type III domain containing; MicroRNA protein coding host genes |
| Hallmark sets | ANDROGEN_RESPONSE, ADIPOGENESIS |
| Reactome | 6 pathways, smallest: RUNX1 regulates transcription of genes involved in interleukin signaling; IL-6-type cytokine receptor ligand interactions; Interleukin-6 family signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P42702](https://www.uniprot.org/uniprotkb/P42702) (Leukemia inhibitory factor receptor):

> [Isoform 1]: Functions as a membrane-bound signal-transducing subunit either in complex with IL6ST/gp130 or as part of the ciliary neurotrophic factor receptor (CNTFR) complex composed by CNTFR, IL6ST/gp130 and LIFR. Signal transmission is initiated either by binding directly to cytokines, such as OSM or LIF or CTF1, or through the binding of other cytokines, like CNTF, CLCF1 or the heterodimeric complex CRLF1-CLCF1 to the non-signaling receptor CNTFR; ligand binding induces heterodimerization …

**Summary**, from NCBI Gene [3977](https://www.ncbi.nlm.nih.gov/gene/3977):

> This gene encodes a protein that belongs to the type I cytokine receptor family. This protein combines with a high-affinity converter subunit, gp130, to form a receptor complex that mediates the action of the leukemia inhibitory factor, a polyfunctional cytokine that is involved in cellular differentiation, proliferation and survival in the adult and the embryo. Mutations in this gene cause Schwartz-Jampel syndrome type 2, a disease belonging to the group of the bent-bone dysplasias. A …

**Accessions** — [HGNC:6597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6597) · Entrez [3977](https://www.ncbi.nlm.nih.gov/gene/3977) · UniProt [P42702](https://www.uniprot.org/uniprotkb/P42702) · Ensembl [ENSG00000113594](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113594)

## Data

Gene col 3479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3479); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3479]; `tensor/DDL_lfc|DDL_z.npy` [3479]; `embed/gene_vectors.npy` [3479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3479 or target_col == 3479). Every well: [[LIFR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LIFR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
