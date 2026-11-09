---
symbol: "CHST12"
type: "gene"
col: 5835
ensembl_id: "ENSG00000136213"
name: "carbohydrate sulfotransferase 12"
location: "7p22.3"
module: 40
arm: "+"
pooled_cpm: 16.78
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 28
n_dd_up_clean: 9
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CHST12

*carbohydrate sulfotransferase 12* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.08× (z +10.9, q 5e-25, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.293× (z -17.5, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF41]] (+0.65, fdr 3e-05), [[CLASRP]] (+0.65, fdr 1e-05), [[ESS2]] (+0.65, fdr 1e-05); moves opposite to [[VPS13C]] (-0.58, fdr 2e-05), [[RAP2C]] (-0.57, fdr 7e-05), [[CRPPA]] (-0.56, fdr 1e-04).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5835.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.08×** | +10.9 | 5e-25 | 42/47 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +10.8 | 7e-25 | 42/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.67×** | +7.7 | 3e-12 | 39/47 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.48×** | +5.9 | 5e-07 | 32/47 (AsPC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 4e-06 | 26/46 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +3.6 | 0.033 | 12/47 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +3.4 | 0.055 | 8/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.073 | 7/47 (A-427, CFPAC-1, …) | two highest doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.085 | 9/47 (NCI-H23, Hs 766T, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.090 | 6/47 (NCI-H460, Panc 03.27, …) | top dose only | plate-row cell shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5835.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.293×** | -17.5 | 0e+00 | 45/47 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.323×** | -16.8 | 0e+00 | 43/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.342×** | -16.0 | 0e+00 | 44/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.351×** | -15.5 | 0e+00 | 42/47 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.428×** | -12.6 | 2e-34 | 40/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.464×** | -11.4 | 3e-28 | 39/47 (PANC-1, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.484×** | -10.8 | 4e-25 | 41/47 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.519×** | -9.7 | 1e-20 | 36/46 (A-427, HT-29, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.557×** | -8.4 | 4e-15 | 27/46 (SNU-423, A-427, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.571×** | -8.0 | 7e-14 | 28/46 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.593×** | -7.4 | 5e-12 | 32/47 (A-172, H4, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.596×** | -7.1 | 6e-11 | 19/33 (PANC-1, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.643×** | -6.6 | 2e-09 | 30/47 (A-172, A498, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.743×** | -6.2 | 2e-08 | 26/46 (A-172, A549, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.660×** | -6.2 | 3e-08 | 26/40 (NCI-H1792, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[EX229 (drug)]] 0.05 µM |  | **0.698×** | -5.0 | 2e-05 | 20/47 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.697×** | -4.9 | 3e-05 | 23/46 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.645×** | -4.6 | 1e-04 | 24/47 (HT-29, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.555×** | -4.6 | 1e-04 | 20/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -4.6 | 1e-04 | 22/47 (NCI-H460, HS-578T, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.005 | 20/47 (A-427, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5835. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 20.0 | 0 | 9 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0808× (z -24.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.134× (z -18.9) |
| [[A-172 (line)]] | wt | 20.5 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0705× (z -18.0) |
| [[H4 (line)]] | wt | 42.6 | 0 | 7 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0444× (z -19.3) |
| [[NCI-H460 (line)]] | wt | 15.9 | 0 | 7 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.117× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.165× (z -14.6) |
| [[HT-29 (line)]] | alt | 17.6 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0242× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -11.0) |
| [[LoVo (line)]] | wt | 20.8 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +9.5) ⚠ cell-cycle shift, explains ~73% of this change | [[Harringtonine (drug)]] 5 µM 0.131× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 25.0 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.110× (z -15.8) |
| [[SW480 (line)]] | alt | 15.6 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -15.2) |
| [[HOP62 (line)]] | alt | 15.8 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.157× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 15.2 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.106× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.196× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 48.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.56× (z +18.7) ⚠ cell-cycle shift, explains ~73% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.260× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[RPMI-7951 (line)]] | alt | 17.2 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 5.59× (z +12.4) ⚠ cell-cycle shift, explains ~73% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.112× (z -10.7) |
| [[A-427 (line)]] | wt | 21.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.191× (z -11.3) |
| [[A498 (line)]] | wt | 22.9 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.166× (z -15.7) |
| [[A549 (line)]] | wt | 13.7 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 13.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0628× (z -13.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.7) ⚠ cell-cycle shift, explains ~73% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -8.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0973× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.247× (z -8.5) |
| [[SNU-423 (line)]] | alt | 17.1 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.199× (z -9.9) |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.103× (z -12.5) |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.165× (z -8.7) |
| [[COLO 205 (line)]] | alt | 9.35 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0462× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.188× (z -10.4) |
| [[J82 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.111× (z -14.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 15.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 18.9 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.116× (z -14.2) |
| [[NCI-H2347 (line)]] | alt | 10.6 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -9.2) |
| [[RKO (line)]] | wt | 11.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.124× (z -9.4) |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.155× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.79 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5835), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF41]] | +0.65 | +0.45 / +0.59 | both halves | 3e-05 |  |
| [[CLASRP]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[ESS2]] | +0.65 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[SLC27A1]] | +0.65 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[RBAK-RBAKDN]] | +0.64 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[SEZ6L2]] | +0.64 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[DRG1]] | +0.63 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[TBC1D25]] | +0.63 | +0.54 / +0.39 | both halves | 5e-05 |  |
| [[PDPR2P]] | +0.62 | +0.35 / +0.67 | both halves | 1e-04 |  |
| [[MYPOP]] | +0.61 | +0.41 / +0.65 | both halves | 4e-05 |  |
| [[SGSM3]] | +0.61 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[ADIPOR1]] | +0.60 | +0.35 / +0.63 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS13C]] | -0.58 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[RAP2C]] | -0.57 | -0.38 / -0.53 | both halves | 7e-05 |  |
| [[CRPPA]] | -0.56 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[RWDD2B]] | -0.55 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[DECR1]] | -0.54 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[MBNL3]] | -0.54 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[ANKRD18A]] | -0.54 | -0.26 / -0.46 | both halves | 4e-04 |  |
| [[ELK4]] | -0.54 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[SCRN1]] | -0.53 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[ARRDC3-AS1]] | -0.53 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[RAB11FIP2]] | -0.53 | -0.44 / -0.33 | both halves | 1e-04 |  |
| [[GSTCD]] | -0.52 | -0.57 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CHST12's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.540). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-33.2, -6.1); signed map (-34.6, 0.8). **Vector** length 82.0, 17.7% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.3 | +7.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.5 | +2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | -0.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +3.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.5 | -15.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -7.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -8.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -17.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.8 | -0.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.3 | -4.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.2 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:2,403,588-2,448,484 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C4S-2, C4ST2 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRB3](https://www.uniprot.org/uniprotkb/Q9NRB3) (Carbohydrate sulfotransferase 12):

> Catalyzes the transfer of sulfate to position 4 of the N-acetylgalactosamine (GalNAc) residue of chondroitin and desulfated dermatan sulfate. Chondroitin sulfate constitutes the predominant proteoglycan present in cartilage and is distributed on the surfaces of many cells and extracellular matrices. Activity toward partially desulfated dermatan sulfate is however lower. Does not form 4, 6-di-O-sulfated GalNAc when chondroitin sulfate C is used as an acceptor.

**Summary**, from NCBI Gene [55501](https://www.ncbi.nlm.nih.gov/gene/55501):

> The protein encoded by this gene belongs to the sulfotransferase 2 family. It is localized to the golgi membrane, and catalyzes the transfer of sulfate to position 4 of the N-acetylgalactosamine (GalNAc) residue of chondroitin and desulfated dermatan sulfate. Chondroitin sulfate constitutes the predominant proteoglycan present in cartilage, and is distributed on the surfaces of many cells and extracellular matrices. Alternatively spliced transcript variants differing only in their 5' UTRs have …

**Accessions** — [HGNC:17423](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17423) · Entrez [55501](https://www.ncbi.nlm.nih.gov/gene/55501) · UniProt [Q9NRB3](https://www.uniprot.org/uniprotkb/Q9NRB3) · Ensembl [ENSG00000136213](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136213)

## Data

Gene col 5835: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5835); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5835, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5835]; `tensor/DDL_lfc|DDL_z.npy` [5835]; `embed/gene_vectors.npy` [5835]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5835 or target_col == 5835). Every well: [[CHST12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
