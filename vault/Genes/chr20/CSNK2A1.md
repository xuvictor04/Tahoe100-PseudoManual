---
symbol: "CSNK2A1"
type: "gene"
col: 2107
ensembl_id: "ENSG00000101266"
name: "casein kinase 2 alpha 1"
location: "20p13"
module: 40
arm: "+"
pooled_cpm: 196.7
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 11
n_dd_up_clean: 12
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# CSNK2A1

*casein kinase 2 alpha 1* — 20p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.88× (z +11.3, q 1e-26, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.751× (z -8.0, q 7e-13, down in 38 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COG5]] (+0.73, fdr 1e-05), [[EIF4EBP1]] (+0.72, fdr 1e-05), [[SDHB]] (+0.71, fdr 1e-05); moves opposite to [[TIA1]] (-0.65, fdr 3e-05), [[BAZ2B]] (-0.64, fdr 4e-05), [[CFLAR]] (-0.62, fdr 2e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[C2orf27A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2107.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.88×** | +11.3 | 1e-26 | 46/49 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.80×** | +11.0 | 1e-25 | 45/48 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.39×** | +6.7 | 4e-09 | 36/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.31×** | +5.6 | 4e-06 | 37/49 (LOX-IMVI, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.32×** | +5.4 | 8e-06 | 38/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +5.3 | 1e-05 | 25/48 (LOX-IMVI, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +5.1 | 3e-05 | 31/48 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +4.9 | 5e-05 | 35/48 (HT-29, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.9 | 6e-05 | 36/45 (A-427, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.6 | 2e-04 | 27/47 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.5 | 3e-04 | 26/48 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 32/48 (A498, SHP-77, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.009 | 32/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.14× | +3.6 | 0.013 | 13/49 (SK-MEL-2, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.38×** | +3.4 | 0.022 | 24/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.029 | 22/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.053 | 17/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2107.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -8.0 | 7e-13 | 38/49 (RKO, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.659×** | -7.9 | 1e-12 | 37/45 (C-33 A, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -7.4 | 2e-11 | 35/44 (SNU-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.698×** | -6.8 | 2e-09 | 39/49 (SNU-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.785×** | -6.7 | 2e-09 | 28/48 (SW 900, C32, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.745×** | -5.8 | 8e-07 | 29/48 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.774×** | -5.0 | 4e-05 | 29/47 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.776×** | -4.8 | 1e-04 | 31/48 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.820×** | -4.0 | 0.003 | 28/48 (A-427, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.826×** | -3.9 | 0.006 | 24/48 (A-172, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.821×** | -3.8 | 0.006 | 24/47 (MIA PaCa-2, PANC-1, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.837× | -3.6 | 0.015 | 21/49 (A498, A-172, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.839× | -3.6 | 0.015 | 23/47 (hTERT-HPNE, Panc 03.27, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.835× | -3.5 | 0.020 | 23/49 (A-427, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -3.4 | 0.029 | 19/48 (KATO III, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2107. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 320 | 2 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.83× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.474× (z -14.6) |
| [[SW480 (line)]] | alt | 255 | 5 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.51× (z +12.8) | — |
| [[NCI-H1573 (line)]] | alt | 93.6 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.41× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 4.72× (z +9.6) | — |
| [[NCI-H23 (line)]] | alt | 186 | 2 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.52× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.465× (z -11.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 232 | 2 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.79× (z +9.2) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 2.87× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -9.7) |
| [[SNU-1 (line)]] | wt | 302 | 1 | 3 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 3.95× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -12.7) |
| [[BT-474 (line)]] | alt | 198 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -10.3) |
| [[COLO 205 (line)]] | alt | 206 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.72× (z +10.9) | — |
| [[LOX-IMVI (line)]] | wt | 197 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 3.25× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.591× (z -10.1) |
| [[NCI-H2347 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.481× (z -10.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 311 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.70× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -8.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 225 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.12× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 152 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 3.21× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.421× (z -13.4) ⚠ cell-cycle shift, explains ~10% of this change |
| [[A498 (line)]] | wt | 127 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.02× (z +10.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.653× (z -8.6) |
| [[C-33 A (line)]] | alt | 214 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.275× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.604× (z -8.6) |
| [[C32 (line)]] | wt | 120 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.547× (z -9.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[HEC-1-A (line)]] | alt | 198 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.82× (z +11.1) | — |
| [[HepG2_C3A (line)]] | wt | 259 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.375× (z -11.0) ⚠ toxic |
| [[HOP62 (line)]] | alt | 273 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 3.81× (z +10.1) | — |
| [[LoVo (line)]] | wt | 147 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.01× (z +8.7) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.469× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 166 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.24× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.523× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 182 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.7) |
| [[A549 (line)]] | wt | 237 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 213 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.35× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 206 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.383× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 244 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 225 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.402× (z -9.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 171 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.21× (z +8.5) | — |
| [[HT-29 (line)]] | alt | 184 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.01× (z +9.9) | — |
| [[KATO III (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.333× (z -11.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 265 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 4.28× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 195 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.92× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 208 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.595× (z -9.9) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW48 (line)]] | wt | 249 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.554× (z -9.2) |
| [[AN3 CA (line)]] | alt | 165 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 230 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 181 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 144 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 233 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 154 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 238 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 142 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2107), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COG5]] | +0.73 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[EIF4EBP1]] | +0.72 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[SDHB]] | +0.71 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[HSPA5]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ST6GALNAC4]] | +0.67 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.67 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[TMEM182]] | +0.67 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[TMEM41B]] | +0.66 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[MYPOP]] | +0.66 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[GARS1]] | +0.66 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[USPL1]] | +0.65 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[SNRPD2]] | +0.64 | +0.66 / +0.38 | both halves | 6e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIA1]] | -0.65 | -0.74 / -0.44 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.64 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[CFLAR]] | -0.62 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ZNF764]] | -0.62 | -0.63 / -0.50 | both halves | 1e-05 |  |
| [[ARFGAP2]] | -0.60 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.59 | -0.66 / -0.43 | both halves | 3e-05 |  |
| [[ST7L]] | -0.59 | -0.71 / -0.29 | both halves | 2e-04 |  |
| [[ZBED5]] | -0.58 | -0.68 / -0.35 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.58 | -0.66 / -0.33 | both halves | 1e-04 |  |
| [[FAM111A]] | -0.58 | -0.64 / -0.40 | both halves | 5e-05 |  |
| [[PATL2]] | -0.58 | -0.74 / -0.23 | both halves | 5e-04 |  |
| [[BAZ1A]] | -0.58 | -0.64 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C2orf27A]] | B | C2orf27A activity raises CSNK2A1's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.36× lower at baseline in the lines without C2orf27A | 0.039 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.648). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (2.4, -19.8); signed map (-43.8, 7.8). **Vector** length 124, 44.6% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.6 | +5.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +8.2 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.2 | +4.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.9 | +3.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +11.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.5 | +3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +3.3 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.7 | -5.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | -9.7 | -6.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -8.5 | -4.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.3 | -4.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.5 | -3.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.4 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -3.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 2 alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p13 — chr20:472,498-543,835 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Cka1, Cka2 |
| Gene groups (HGNC) | Casein kinase 2 alpha family |
| Reactome | 58 pathways, smallest: Phosphorylation and nuclear translocation of BMAL1 (ARNTL) and CLOCK; WNT mediated activation of DVL; Condensation of Prometaphase Chromosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [P68400](https://www.uniprot.org/uniprotkb/P68400) (Casein kinase II subunit alpha):

> Catalytic subunit of a constitutively active serine/threonine-protein kinase complex that phosphorylates a large number of substrates containing acidic residues C-terminal to the phosphorylated serine or threonine. Regulates numerous cellular processes, such as cell cycle progression, apoptosis and transcription, as well as viral infection. May act as a regulatory node which integrates and coordinates numerous signals leading to an appropriate cellular response. During mitosis, functions as a …

**Summary**, from NCBI Gene [1457](https://www.ncbi.nlm.nih.gov/gene/1457):

> Casein kinase II is a serine/threonine protein kinase that phosphorylates acidic proteins such as casein. It is involved in various cellular processes, including cell cycle control, apoptosis, and circadian rhythm. The kinase exists as a tetramer and is composed of an alpha, an alpha-prime, and two beta subunits. The alpha subunits contain the catalytic activity while the beta subunits undergo autophosphorylation. The protein encoded by this gene represents the alpha subunit. Multiple …

**Accessions** — [HGNC:2457](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2457) · Entrez [1457](https://www.ncbi.nlm.nih.gov/gene/1457) · UniProt [P68400](https://www.uniprot.org/uniprotkb/P68400) · Ensembl [ENSG00000101266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101266)

## Data

Gene col 2107: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2107); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2107, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2107]; `tensor/DDL_lfc|DDL_z.npy` [2107]; `embed/gene_vectors.npy` [2107]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2107 or target_col == 2107). Every well: [[CSNK2A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK2A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
