---
symbol: "LRRC28"
type: "gene"
col: 9720
ensembl_id: "ENSG00000168904"
name: "leucine rich repeat containing 28"
location: "15q26.3"
module: 80
arm: "+"
pooled_cpm: 31.5
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 32
n_dd_up_clean: 11
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# LRRC28

*leucine rich repeat containing 28* — 15q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.24× (z +12.6, q 2e-33, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (15 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.425× (z -13.3, q 7e-38, down in 45 of 48 measured lines) ⚠ cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.473× (z -11.6, q 4e-29, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (40 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 60 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COPG2]] (+0.57, fdr 4e-04), [[RNF41]] (+0.57, fdr 2e-04), [[LHPP]] (+0.56, fdr 1e-04); moves opposite to [[ZNF101]] (-0.56, fdr 9e-04, ⚠ not reproduced), [[ARRDC3-AS1]] (-0.54, fdr 0.003, ⚠ not reproduced), [[MMADHC-DT]] (-0.53, fdr 0.004, ⚠ one half only (not replicated)), [[ZNF563]] (-0.52, fdr 7e-04), [[ALOXE3]] (-0.51, fdr 3e-04), [[ESR2]] (-0.50, fdr 6e-04).
> It is in [[Module 080]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9720.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.24×** | +12.6 | 2e-33 | 42/48 (NCI-H2347, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.98×** | +10.7 | 4e-24 | 42/48 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +8.1 | 8e-14 | 36/48 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.2 | 7e-08 | 29/48 (NCI-H2347, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.06×** | +5.9 | 4e-07 | 32/48 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.7 | 9e-07 | 25/48 (HEC-1-A, HOP62, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.35×** | +4.7 | 3e-04 | 25/48 (HT-29, A498, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 0.001 | 22/48 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.7 | 0.012 | 20/48 (NCI-H2347, KATO III, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.028 | 17/48 (RKO, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.086 | 8/48 (SW480, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.094 | 15/48 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.099 | 13/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.11 | 15/47 (NCI-H23, A498, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.425×** | -13.3 | 7e-38 | 45/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.451×** | -12.4 | 6e-33 | 44/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.443×** | -12.2 | 5e-32 | 42/48 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.473×** | -11.6 | 4e-29 | 37/48 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.589×** | -8.3 | 2e-14 | 39/48 (C-33 A, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.616×** | -7.6 | 4e-12 | 37/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.621×** | -7.4 | 8e-12 | 32/47 (A-427, A549, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.631×** | -7.2 | 5e-11 | 30/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.421×** | -7.0 | 1e-10 | 34/48 (SW48, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.428×** | -6.9 | 2e-10 | 38/48 (SW 900, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.674×** | -6.1 | 4e-08 | 30/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.667×** | -6.1 | 6e-08 | 30/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.701×** | -5.6 | 1e-06 | 27/48 (A549, NCI-H460, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.735×** | -4.8 | 6e-05 | 26/48 (SW480, PANC-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.758×** | -4.2 | 0.001 | 21/47 (CFPAC-1, H4, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.781×** | -3.7 | 0.006 | 22/48 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.847× | -3.7 | 0.007 | 18/48 (C32, NCI-H1792, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.811×** | -3.3 | 0.028 | 12/47 (H4, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.682×** | -3.1 | 0.041 | 10/48 (SK-MEL-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.805×** | -2.9 | 0.071 | 17/48 (HT-29, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.833×** | -2.8 | 0.083 | 7/48 (AN3 CA, NCI-H460, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.776×** | -2.8 | 0.086 | 9/48 (MIA PaCa-2, RKO, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 47.8 | 0 | 9 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.284× (z -11.0) |
| [[A549 (line)]] | wt | 46.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -16.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.204× (z -13.1) |
| [[PANC-1 (line)]] | alt | 61.0 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.293× (z -13.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.366× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 72.4 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -14.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 23.1 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.254× (z -11.8) |
| [[SW480 (line)]] | alt | 35.6 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.186× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.406× (z -9.1) |
| [[A-427 (line)]] | wt | 44.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.114× (z -19.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 37.3 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 51.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -14.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 27.5 | 0 | 3 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~81% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.199× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -15.8) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.271× (z -10.1) |
| [[A498 (line)]] | wt | 17.6 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 3.28× (z +9.3) | [[Harringtonine (drug)]] 0.5 µM 0.294× (z -9.5) |
| [[C-33 A (line)]] | alt | 78.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.361× (z -8.6) |
| [[C32 (line)]] | wt | 36.2 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +28.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Hs 766T (line)]] | wt | 31.1 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.276× (z -9.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 25.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 48.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.187× (z -16.3) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 13.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.23× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 28.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.53× (z +12.4) ⚠ cell-cycle shift, would explain all of this change | [[Docetaxel (drug)]] 0.05 µM 0.112× (z -12.7) ⚠ transcription drop; cell-cycle shift, explains ~81% of this change |
| [[SW 900 (line)]] | alt | 23.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0357× (z -11.2) |
| [[SW1417 (line)]] | alt | 25.7 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 18.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.227× (z -9.6) ⚠ cell-cycle shift, explains ~32% of this change |
| [[AsPC-1 (line)]] | alt | 10.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.55× (z +9.5) | — |
| [[HCT15 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.155× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 20.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.88× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.110× (z -10.4) |
| [[HOP62 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.286× (z -8.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 30.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -9.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 36.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 19.9× (z +32.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.179× (z -9.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9720), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPG2]] | +0.57 | +0.26 / +0.57 | both halves | 4e-04 |  |
| [[RNF41]] | +0.57 | +0.30 / +0.52 | both halves | 2e-04 |  |
| [[LHPP]] | +0.56 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[RALGPS1]] | +0.54 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[TTLL1]] | +0.54 | +0.35 / +0.54 | both halves | 1e-04 |  |
| [[CEP131]] | +0.52 | +0.14 / +0.42 | ⚠ not reproduced | 0.002 |  |
| [[FAM20B]] | +0.52 | +0.23 / +0.45 | both halves | 5e-04 |  |
| [[SPATA6]] | +0.51 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[ATG5]] | +0.50 | +0.24 / +0.49 | both halves | 4e-04 |  |
| [[DAG1]] | +0.50 | +0.30 / +0.42 | both halves | 2e-04 |  |
| [[SERAC1]] | +0.49 | +0.19 / +0.50 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ARMC2]] | +0.49 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[SPIDR]] | +0.49 | +0.35 / +0.35 | both halves | 1e-04 |  |
| [[MGAT4A]] | +0.49 | +0.36 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 49 of them with an alert (⚠; 49 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF101]] | -0.56 | -0.18 / -0.41 | ⚠ not reproduced | 9e-04 |  |
| [[ARRDC3-AS1]] | -0.54 | -0.08 / -0.42 | ⚠ not reproduced | 0.003 |  |
| [[MMADHC-DT]] | -0.53 | -0.08 / -0.53 | ⚠ one half (not replicated) | 0.004 |  |
| [[ZNF563]] | -0.52 | -0.20 / -0.25 | both halves | 7e-04 |  |
| [[ALOXE3]] | -0.51 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[RRP8]] | -0.51 | -0.18 / -0.24 | ⚠ not reproduced | 0.001 |  |
| [[SDSL]] | -0.51 | -0.14 / -0.44 | ⚠ not reproduced | 0.002 |  |
| [[NNT-AS1]] | -0.51 | -0.18 / -0.45 | ⚠ not reproduced | 9e-04 |  |
| [[ESR2]] | -0.50 | -0.22 / -0.27 | both halves | 6e-04 |  |
| [[COL27A1]] | -0.50 | -0.27 / -0.45 | both halves | 3e-04 |  |
| [[ZNF441]] | -0.49 | -0.15 / -0.41 | ⚠ not reproduced | 0.001 |  |
| [[ZNF341-AS1]] | -0.49 | -0.24 / -0.28 | both halves | 4e-04 |  |
| [[ZNF234]] | -0.47 | -0.27 / -0.25 | both halves | 4e-04 |  |
| [[LGALS8]] | -0.47 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[TLCD3A]] | -0.46 | -0.23 / -0.31 | both halves | 5e-04 |  |
| [[TBX3]] | -0.45 | -0.31 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction -0.500). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.0, 4.8); signed map (-42.7, -23.0). **Vector** length 61.3, 11.9% of its response variance represented; |z| ≥ 3 in 1,241 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +2.2 | +10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.0 | +12.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.9 | +8.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +1.8 | +4.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.0 | +0.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +0.9 | +1.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -11.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -8.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -1.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.0 | -2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.9 | -2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing 28 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.3 — chr15:99,251,362-99,390,729 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC24976, FLJ34269, FLJ45242 |
| Matched by | ensembl_id |

UniProt [Q86X40](https://www.uniprot.org/uniprotkb/Q86X40) carries no function annotation.

**Summary**, from NCBI Gene [123355](https://www.ncbi.nlm.nih.gov/gene/123355):

> Predicted to be involved in intracellular signal transduction. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28355) · Entrez [123355](https://www.ncbi.nlm.nih.gov/gene/123355) · UniProt [Q86X40](https://www.uniprot.org/uniprotkb/Q86X40) · Ensembl [ENSG00000168904](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168904)

## Data

Gene col 9720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9720); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9720, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9720]; `tensor/DDL_lfc|DDL_z.npy` [9720]; `embed/gene_vectors.npy` [9720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9720 or target_col == 9720). Every well: [[LRRC28 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRRC28.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
