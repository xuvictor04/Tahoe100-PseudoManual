---
symbol: "ADD3"
type: "gene"
col: 7308
ensembl_id: "ENSG00000148700"
name: "adducin 3"
location: "10q25.1-q25.2"
module: 5
arm: "-"
pooled_cpm: 142.96
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 36
n_dd_up_clean: 13
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 5
direction_downstream: 27
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# ADD3

*adducin 3* — 10q25.1-q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +8.5, q 9e-15, up in 31 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.483× (z -21.6, q 0e+00, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GGH]] (+0.62, fdr 1e-05), [[SLC44A1]] (+0.62, fdr 1e-05), [[CLSTN1]] (+0.61, fdr 1e-05); moves opposite to [[PUS1]] (-0.61, fdr 1e-05), [[SMIM12]] (-0.60, fdr 1e-05), [[TRIM65]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PAPSS2]] → it (grade B ⚠); 27 go from it, the strongest it → [[MAGI3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7308.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +8.5 | 9e-15 | 31/43 (J82, SNU-423, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +6.1 | 3e-07 | 27/43 (J82, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +6.0 | 3e-07 | 29/42 (AsPC-1, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +5.2 | 3e-05 | 22/44 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.9 | 1e-04 | 23/43 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.27×** | +4.8 | 2e-04 | 23/43 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 2e-04 | 25/43 (AsPC-1, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib (drug)]] 5 µM |  | **1.52×** | +4.6 | 3e-04 | 22/43 (SNU-423, A498, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +4.5 | 5e-04 | 22/42 (C32, AsPC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +4.5 | 5e-04 | 19/40 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +4.3 | 9e-04 | 27/44 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.001 | 24/42 (RPMI-7951, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +4.2 | 0.001 | 20/44 (C32, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.18× | +4.1 | 0.001 | 18/43 (C32, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.21×** | +4.0 | 0.002 | 19/43 (PANC-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.20×** | +3.9 | 0.004 | 19/44 (C32, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.7 | 0.008 | 15/43 (NCI-H1573, AN3 CA, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7308.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.483×** | -21.6 | 0e+00 | 37/43 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.386×** | -20.0 | 0e+00 | 41/43 (NCI-H1792, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.464×** | -16.1 | 0e+00 | 41/43 (SW480, HT-29, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.488×** | -14.5 | 1e-45 | 37/43 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.543×** | -12.5 | 6e-34 | 41/43 (SW1417, HT-29, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.568×** | -11.9 | 1e-30 | 37/43 (Hs 766T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.574×** | -11.7 | 1e-29 | 36/43 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.601×** | -10.7 | 7e-25 | 37/43 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.611×** | -10.4 | 2e-23 | 38/43 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.613×** | -10.3 | 4e-23 | 38/43 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.729×** | -9.4 | 2e-19 | 34/44 (HT-29, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.644×** | -9.2 | 1e-18 | 31/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -8.4 | 1e-15 | 33/44 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.683×** | -7.7 | 5e-13 | 29/42 (NCI-H1792, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.501×** | -7.6 | 1e-12 | 35/43 (NCI-H1792, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.700×** | -7.5 | 2e-12 | 33/43 (HT-29, SW 900, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.515×** | -7.3 | 1e-11 | 33/43 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.530×** | -7.0 | 9e-11 | 33/43 (NCI-H1792, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7308. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 149 | 0 | 18 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -25.3) |
| [[NCI-H1792 (line)]] | alt | 575 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -24.9) |
| [[SW480 (line)]] | alt | 174 | 0 | 12 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.362× (z -18.0) |
| [[LoVo (line)]] | wt | 222 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.254× (z -19.2) |
| [[SW 900 (line)]] | alt | 255 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 213 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.189× (z -18.9) |
| [[LS 180 (line)]] | wt | 408 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 116 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.89× (z +11.8) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.300× (z -13.4) |
| [[PANC-1 (line)]] | alt | 100 | 1 (1 ⚠) | 8 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.08× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.514× (z -13.9) |
| [[A549 (line)]] | wt | 102 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.233× (z -15.2) |
| [[COLO 205 (line)]] | alt | 308 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.165× (z -19.9) |
| [[Hs 766T (line)]] | wt | 114 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -23.7) |
| [[HT-29 (line)]] | alt | 300 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -19.1) |
| [[KATO III (line)]] | alt | 328 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -23.7) |
| [[SNU-423 (line)]] | alt | 158 | 1 | 7 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.63× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.269× (z -17.6) |
| [[H4 (line)]] | wt | 129 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -14.2) |
| [[HOP62 (line)]] | alt | 84.2 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.334× (z -13.1) |
| [[Panc 03.27 (line)]] | alt | 105 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -14.6) |
| [[A-427 (line)]] | wt | 90.8 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -18.8) |
| [[HCT15 (line)]] | alt | 244 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.461× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 71.6 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -12.3) |
| [[A-172 (line)]] | wt | 115 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 1.79× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -16.3) |
| [[HEC-1-A (line)]] | alt | 126 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +10.5) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.533× (z -10.1) |
| [[hTERT-HPNE (line)]] | wt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.394× (z -10.2) |
| [[SK-MEL-2 (line)]] | alt | 96.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.286× (z -12.7) |
| [[HS-578T (line)]] | alt | 154 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.368× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 164 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -17.9) |
| [[LOX-IMVI (line)]] | wt | 56.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.207× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 60.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 75.5 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -13.7) |
| [[SW 1088 (line)]] | alt | 94.9 | 0 | 2 | — | [[Verapamil (drug)]] 5 µM 0.0698× (z -9.4) |
| [[SW1417 (line)]] | alt | 196 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.396× (z -14.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.515× (z -10.4) |
| [[A498 (line)]] | wt | 113 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.461× (z -9.4) |
| [[J82 (line)]] | alt | 69.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.75× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 97.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.2 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 105 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 69.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 87.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 171 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 19.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 187 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.0 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.9 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7308), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GGH]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[SLC44A1]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[CLSTN1]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CAT]] | +0.61 | +0.48 / +0.63 | both halves | 2e-05 |  |
| [[ITM2B]] | +0.60 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[MPC2]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[TMEM59]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[MDH1]] | +0.56 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[MAPRE2]] | +0.56 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PSIP1]] | +0.56 | +0.39 / +0.57 | both halves | 6e-05 | STRING 600 |
| [[DPY19L1]] | +0.55 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[PCYOX1]] | +0.54 | +0.50 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUS1]] | -0.61 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[SMIM12]] | -0.60 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TRIM65]] | -0.60 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[NIFK]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[USP36]] | -0.58 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ZNF696]] | -0.57 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[FBXO10]] | -0.57 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[PARVB]] | -0.57 | -0.50 / -0.61 | both halves | 1e-05 |  |
| [[DHX34]] | -0.57 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[DDX51]] | -0.56 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[MECR]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[NOP16]] | -0.55 | -0.49 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAPSS2]] | B | PAPSS2 activity raises ADD3's level | lines that do not express PAPSS2 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without PAPSS2 | 0.032 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, A4GALT, NT5E |
| [[LINC00511]] | B | LINC00511 activity raises ADD3's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without LINC00511 | 0.048 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[MAP2K1]] | B | MAP2K1 activity lowers ADD3's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds |
| [[PBX1]] | B | PBX1 activity raises ADD3's level | lines that do not express PBX1 (20) vs lines expressing it (30) | 1.87× lower at baseline in the lines without PBX1 | 0.066 | ⚠ within organs, on part of the lines; also absent: LIPG, ENSG00000287003, GALNT9 |
| [[ADD3-AS1]] | C | ADD3-AS1 activity raises ADD3's level | lines that do not express ADD3-AS1 (9) vs lines expressing it (41) | 4.13× lower at baseline in the lines without ADD3-AS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: ADD3, ARHGAP23, ENSG00000286830; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 26, C 1. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAGI3]] | B | ADD3 activity raises MAGI3's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.63× lower at baseline in the lines without ADD3 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[ACTR3B]] | B | ADD3 activity strengthens ACTR3B's drug response | lines that do not express ADD3 (5) vs lines expressing it (43) | the lines without ADD3 respond 0.79× as strongly (z diff +0.94); strongest at Panobinostat 0.5 µM: 1.22x vs 2.26x (z diff +3.1) | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3; target measured in part of the lines; artifact flags |
| [[ALDH9A1]] | B | ADD3 activity lowers ALDH9A1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.53× higher at baseline in the lines without ADD3 | 0.014 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[NIP7]] | B | ADD3 activity lowers NIP7's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.59× higher at baseline in the lines without ADD3 | 0.025 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[CMTM3]] | B | ADD3 activity lowers CMTM3's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.45× higher at baseline in the lines without ADD3 | 0.032 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[MAPRE2]] | B | ADD3 activity raises MAPRE2's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 2.44× lower at baseline in the lines without ADD3 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[NIFK]] | B | ADD3 activity strengthens NIFK's drug response | lines that do not express ADD3 (5) vs lines expressing it (43) | the lines without ADD3 respond 0.66× as strongly (z diff +1.75); strongest at Homoharringtonine 5 µM: 0.96x vs 1.97x (z diff +5.9) | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3; target measured in part of the lines; artifact flags |
| [[LINC00511]] | B | ADD3 activity raises LINC00511's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 4.79× lower at baseline in the lines without ADD3 | 0.039 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[NOP16]] | B | ADD3 activity lowers NOP16's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.49× higher at baseline in the lines without ADD3 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[PPP3CA]] | B | ADD3 activity raises PPP3CA's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.92× lower at baseline in the lines without ADD3 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[AFG3L1P]] | B | ADD3 activity lowers AFG3L1P's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.45× higher at baseline in the lines without ADD3 | 0.048 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |
| [[DPY19L1]] | B | ADD3 activity raises DPY19L1's level | lines that do not express ADD3 (5) vs lines expressing it (45) | 1.82× lower at baseline in the lines without ADD3 | 0.054 | ⚠ within organs, on part of the lines; also absent: LINC02842, ADD3-AS1, WWC3 |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.571). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (12.6, 6.0); signed map (-4.7, 19.2). **Vector** length 107, 34.0% of its response variance represented; |z| ≥ 3 in 1,709 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[NG25 (drug)]] 5 µM |  | +6.7 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +8.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.1 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.1 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.8 | +4.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +6.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.5 | +4.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.6 | -12.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.0 | -16.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.9 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.1 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -20.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.6 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -5.6 | -6.8 |
|  | [[EX229 (drug)]] 5 µM |  | -5.3 | -7.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.3 | -9.2 |

## What is on record

|  |  |
|---|---|
| Name | adducin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1-q25.2 — chr10:109,996,368-110,135,565 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ADDL |
| Gene groups (HGNC) | Adducin family |
| Hallmark sets | UV_RESPONSE_DN, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Miscellaneous transport and binding events; RHOF GTPase cycle; RHOD GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UEY8](https://www.uniprot.org/uniprotkb/Q9UEY8) (Gamma-adducin):

> Membrane-cytoskeleton-associated protein that promotes the assembly of the spectrin-actin network. Plays a role in actin filament capping. Binds to calmodulin (Probable). Involved in myogenic reactivity of the renal afferent arteriole (Af-art), renal interlobular arteries and middle cerebral artery (MCA) to increased perfusion pressure. Involved in regulation of potassium channels in the vascular smooth muscle cells (VSMCs) of the Af-art and MCA ex vivo. Involved in regulation of glomerular …

**Summary**, from NCBI Gene [120](https://www.ncbi.nlm.nih.gov/gene/120):

> Adducins are heteromeric proteins composed of different subunits referred to as adducin alpha, beta and gamma. The three subunits are encoded by distinct genes and belong to a family of membrane skeletal proteins involved in the assembly of spectrin-actin network in erythrocytes and at sites of cell-cell contact in epithelial tissues. While adducins alpha and gamma are ubiquitously expressed, the expression of adducin beta is restricted to brain and hematopoietic tissues. Adducin, originally …

**Accessions** — [HGNC:245](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:245) · Entrez [120](https://www.ncbi.nlm.nih.gov/gene/120) · UniProt [Q9UEY8](https://www.uniprot.org/uniprotkb/Q9UEY8) · Ensembl [ENSG00000148700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148700)

## Data

Gene col 7308: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7308); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7308, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7308]; `tensor/DDL_lfc|DDL_z.npy` [7308]; `embed/gene_vectors.npy` [7308]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7308 or target_col == 7308). Every well: [[ADD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ADD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
