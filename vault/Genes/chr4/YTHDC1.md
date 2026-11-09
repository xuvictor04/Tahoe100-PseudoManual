---
symbol: "YTHDC1"
type: "gene"
col: 1387
ensembl_id: "ENSG00000083896"
name: "YTH N6-methyladenosine RNA binding protein C1"
location: "4q13.2"
module: 69
arm: "+"
pooled_cpm: 210.55
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# YTHDC1

*YTH N6-methyladenosine RNA binding protein C1* — 4q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.86× (z +27.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.589× (z -9.5, q 2e-18, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.637× (z -4.4, q 0.002, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARID4B]] (+0.71, fdr 7e-06), [[SLU7]] (+0.70, fdr 7e-06), [[CIR1]] (+0.70, fdr 7e-06); moves opposite to [[EFTUD2]] (-0.63, fdr 1e-05), [[NUP188]] (-0.62, fdr 1e-05), [[TOMM40]] (-0.59, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MPZL3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ENY2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1387.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +27.7 | 0e+00 | 48/48 (NCI-H23, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.84×** | +19.5 | 0e+00 | 48/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +16.4 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.39×** | +16.2 | 0e+00 | 47/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.96×** | +12.5 | 6e-34 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.92×** | +12.2 | 2e-32 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.15×** | +11.2 | 4e-27 | 46/49 (NCI-H23, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.83×** | +10.8 | 2e-25 | 42/48 (COLO 205, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.36×** | +8.4 | 4e-15 | 45/48 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +6.1 | 5e-08 | 35/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.8 | 4e-07 | 29/48 (BT-474, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.31×** | +5.1 | 2e-05 | 28/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +5.0 | 2e-05 | 28/48 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.29×** | +4.7 | 1e-04 | 29/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 9e-04 | 23/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +4.2 | 0.001 | 14/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 25/48 (KATO III, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.20×** | +3.5 | 0.015 | 24/48 (KATO III, A498, …) | rises with dose |  |
| [[Sodium Salicylate (drug)]] 5 µM |  | 1.12× | +3.0 | 0.068 | 0/49 | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1387.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -9.5 | 2e-18 | 35/44 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.700×** | -6.6 | 1e-08 | 44/48 (NCI-H2347, SW1417, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.684×** | -6.5 | 2e-08 | 39/49 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.637×** | -4.4 | 0.002 | 37/48 (NCI-H2347, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -3.7 | 0.024 | 29/48 (COLO 205, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.828×** | -3.5 | 0.046 | 23/48 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.710×** | -3.3 | 0.073 | 26/48 (SK-MEL-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.840× | -3.2 | 0.093 | 18/49 (SNU-423, NCI-H2030, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.843× | -3.0 | 0.15 | 19/48 (NCI-H2347, RKO, …) | top dose only |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.850× | -3.0 | 0.15 | 18/49 (NCI-H2030, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1387. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 144 | 14 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.16× (z +25.7) | — |
| [[SW480 (line)]] | alt | 198 | 12 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +23.0) | — |
| [[LoVo (line)]] | wt | 186 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.36× (z +27.7) | — |
| [[NCI-H1573 (line)]] | alt | 335 | 10 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +26.5) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -19.1) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 211 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +21.4) | — |
| [[NCI-H2347 (line)]] | alt | 377 | 5 (1 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -16.8) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 251 | 9 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.382× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 229 | 8 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.490× (z -8.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 171 | 7 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +27.7) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 243 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +28.2) | — |
| [[NCI-H23 (line)]] | alt | 169 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +28.4) | — |
| [[PANC-1 (line)]] | alt | 153 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +25.2) | — |
| [[A-427 (line)]] | wt | 201 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +12.0) | — |
| [[AsPC-1 (line)]] | alt | 277 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.34× (z +20.6) | — |
| [[COLO 205 (line)]] | alt | 230 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +25.4) | — |
| [[HepG2_C3A (line)]] | wt | 271 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.91× (z +18.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.317× (z -13.0) ⚠ toxic; cell-cycle shift, explains ~88% of this change |
| [[KATO III (line)]] | alt | 188 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.57× (z +25.6) | — |
| [[LS 180 (line)]] | wt | 238 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.58× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 241 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +19.5) | — |
| [[SW 900 (line)]] | alt | 250 | 6 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 205 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -12.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 200 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +17.9) | — |
| [[HS-578T (line)]] | alt | 129 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +23.1) | — |
| [[SW1417 (line)]] | alt | 185 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +18.4) | — |
| [[CFPAC-1 (line)]] | alt | 360 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.359× (z -11.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 210 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.08× (z +19.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 158 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +19.7) | — |
| [[Panc 03.27 (line)]] | alt | 242 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +19.5) | [[Dinaciclib (drug)]] 5 µM 0.411× (z -11.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 204 | 5 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.33× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 194 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +23.6) | — |
| [[SW48 (line)]] | wt | 249 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +15.8) | — |
| [[HCT15 (line)]] | alt | 279 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +12.6) | — |
| [[Hs 766T (line)]] | wt | 166 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 217 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.342× (z -10.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 231 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +15.5) | — |
| [[A-172 (line)]] | wt | 94.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +16.5) | — |
| [[A498 (line)]] | wt | 182 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +24.6) | — |
| [[C32 (line)]] | wt | 169 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +17.2) | — |
| [[J82 (line)]] | alt | 150 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 244 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 197 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 223 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +21.2) | — |
| [[SNU-423 (line)]] | alt | 221 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 210 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 291 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 291 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 187 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1387), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | +0.71 | +0.74 / +0.67 | both halves | 7e-06 |  |
| [[SLU7]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[CIR1]] | +0.70 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TERF2IP]] | +0.70 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[SYF2]] | +0.69 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[GCC2]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CHD2]] | +0.68 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[RSF1]] | +0.67 | +0.65 / +0.58 | both halves | 8e-06 |  |
| [[RSRC2]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 | STRING 608 |
| [[PNISR]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[SRSF11]] ⚠ | +0.66 | +0.71 / +0.57 | both halves | 1e-05 | STRING 566; ⚠ in the vector space only through flagged drug-doses |
| [[RB1CC1]] | +0.64 | +0.56 / +0.69 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFTUD2]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[NUP188]] | -0.62 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[TOMM40]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[DPM2]] | -0.59 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TEX2]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[PHB1]] | -0.59 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[CS]] | -0.58 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PRKDC]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[SIGMAR1]] | -0.58 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[PSME3]] | -0.57 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[EIF2S1]] | -0.57 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[BLTP2]] | -0.57 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity raises YTHDC1's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.28× lower at baseline in the lines without MPZL3 | 0.006 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ENY2]] | C | YTHDC1's natural level weakens ENY2's drug response | YTHDC1's natural level across 50 lines (lineage-adjusted; a glimpse) | r -0.69, reverse +0.21; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-2.2, -45.4); signed map (-8.9, 6.2). **Vector** length 104, 42.0% of its response variance represented; |z| ≥ 3 in 1,222 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.6 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +0.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.1 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.1 | +0.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.9 | -6.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.7 | -3.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.1 | -4.4 |
|  | [[EX229 (drug)]] 5 µM |  | -5.6 | -3.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.3 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | YTH N6-methyladenosine RNA binding protein C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.2 — chr4:68,310,387-68,350,090 (-) |
| Ensembl biotype | protein_coding |
| Also known as | YT521, KIAA1966, YT521-B |
| Gene groups (HGNC) | YTH domain containing N6-methyladenosine readers |
| Hallmark sets | UV_RESPONSE_DN, G2M_CHECKPOINT |
| Reactome | 2 pathways, smallest: Nuclear RNA decay; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96MU7](https://www.uniprot.org/uniprotkb/Q96MU7) (YTH domain-containing protein 1):

> Regulator of alternative splicing that specifically recognizes and binds N6-methyladenosine (m6A)-containing RNAs. M6A is a modification present at internal sites of mRNAs and some non-coding RNAs and plays a role in the efficiency of mRNA splicing, processing and stability. Acts as a key regulator of exon-inclusion or exon-skipping during alternative splicing via interaction with mRNA splicing factors SRSF3 and SRSF10. Specifically binds m6A-containing mRNAs and promotes recruitment of SRSF3 …

**Summary**, from NCBI Gene [91746](https://www.ncbi.nlm.nih.gov/gene/91746):

> Enables N6-methyladenosine-containing RNA reader activity and RNA binding activity. Involved in gene expression and regulation of gene expression. Located in nuclear speck. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30626](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30626) · Entrez [91746](https://www.ncbi.nlm.nih.gov/gene/91746) · UniProt [Q96MU7](https://www.uniprot.org/uniprotkb/Q96MU7) · Ensembl [ENSG00000083896](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000083896)

## Data

Gene col 1387: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1387); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1387, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1387]; `tensor/DDL_lfc|DDL_z.npy` [1387]; `embed/gene_vectors.npy` [1387]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1387 or target_col == 1387). Every well: [[YTHDC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/YTHDC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
