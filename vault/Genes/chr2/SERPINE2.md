---
symbol: "SERPINE2"
type: "gene"
col: 5778
ensembl_id: "ENSG00000135919"
name: "serpin family E member 2"
location: "2q36.1"
module: 81
arm: "+"
pooled_cpm: 228.95
n_lines_expressing: 29
n_dd_up: 21
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 11
direction_downstream: 24
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# SERPINE2

*serpin family E member 2* — 2q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +14.3, q 1e-43, up in 25 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +8.6, q 8e-16, up in 19 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.603× (z -7.4, q 8e-11, down in 15 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPHA4]] (+0.63, fdr 1e-05), [[TFPI2]] (+0.63, fdr 7e-06), [[PTGS2]] (+0.62, fdr 7e-06); moves opposite to [[CDC23]] (-0.49, fdr 4e-05), [[PCYT1A]] (-0.48, fdr 3e-05), [[RUFY2]] (-0.47, fdr 9e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 24 go from it, the strongest it → [[AHR]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5778.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +14.3 | 1e-43 | 25/28 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +10.5 | 3e-23 | 23/25 (AsPC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.80×** | +9.0 | 5e-17 | 19/27 (HS-578T, hTERT-HPNE, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +8.7 | 3e-16 | 21/25 (SW1417, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +8.6 | 8e-16 | 19/27 (hTERT-HPNE, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.75×** | +8.6 | 8e-16 | 21/27 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +6.9 | 3e-10 | 14/27 (A549, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.36×** | +6.7 | 1e-09 | 13/27 (hTERT-HPNE, SNU-423, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +6.7 | 1e-09 | 9/28 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.54×** | +6.6 | 3e-09 | 20/27 (hTERT-HPNE, SNU-423, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.23×** | +6.4 | 8e-09 | 18/28 (AsPC-1, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.3 | 2e-08 | 22/28 (hTERT-HPNE, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +6.2 | 2e-08 | 18/26 (SNU-423, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.47×** | +5.9 | 1e-07 | 18/27 (hTERT-HPNE, C32, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.45×** | +5.7 | 4e-07 | 13/27 (HT-29, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 15/27 (SNU-423, LoVo, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.003 | 9/29 (H4, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.022 | 10/27 (NCI-H2030, HS-578T, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.022 | 7/27 (A549, A498, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.023 | 11/27 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5778.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.603×** | -7.4 | 8e-11 | 15/26 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.611×** | -7.0 | 7e-10 | 14/29 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.618×** | -6.8 | 2e-09 | 14/27 (LoVo, LS 180, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.779×** | -5.3 | 2e-05 | 13/27 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.718×** | -5.0 | 5e-05 | 12/26 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.718×** | -5.0 | 5e-05 | 17/27 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.722×** | -4.7 | 2e-04 | 22/27 (C32, NCI-H460, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.761×** | -4.1 | 0.002 | 16/27 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | **0.599×** | -4.1 | 0.003 | 11/27 (NCI-H460, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.007 | 18/27 (HS-578T, NCI-H1573, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.814×** | -3.8 | 0.007 | 13/27 (LoVo, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.780×** | -3.8 | 0.008 | 17/27 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.794×** | -3.5 | 0.020 | 12/27 (NCI-H1573, HS-578T, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.650×** | -3.4 | 0.025 | 12/27 (NCI-H460, A498, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.656×** | -3.4 | 0.030 | 16/25 (C32, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **0.665×** | -3.2 | 0.040 | 8/29 (NCI-H460, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.802×** | -3.2 | 0.041 | 11/28 (LoVo, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5778. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 616 | 0 | 18 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -16.0) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.271× (z -14.2) |
| [[LoVo (line)]] | wt | 377 | 0 | 15 (4 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.294× (z -16.1) |
| [[LS 180 (line)]] | wt | 240 | 0 | 12 (5 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.321× (z -12.1) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.359× (z -10.5) |
| [[hTERT-HPNE (line)]] | wt | 249 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +23.3) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.26× (z +9.9) | — |
| [[AsPC-1 (line)]] | alt | 325 | 6 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.48× (z +12.1) | [[Daptomycin (drug)]] 5 µM 0.443× (z -8.8) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 101 | 6 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.46× (z +17.6) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[C32 (line)]] | wt | 2,848 | 1 (1 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.19× (z +9.8) ⚠ toxic; transcription drop | [[Bortezomib (drug)]] 0.05 µM 0.248× (z -16.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.378× (z -12.2) |
| [[HS-578T (line)]] | alt | 439 | 4 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.61× (z +11.9) ⚠ cell-cycle shift, explains ~69% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.68× (z +8.8) | [[Budesonide (drug)]] 5 µM 0.381× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 156 | 0 | 5 (1 ⚠) | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.388× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 1,283 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -16.2) ⚠ cell-cycle shift, explains ~83% of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.355× (z -9.5) |
| [[A549 (line)]] | wt | 118 | 4 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 3.25× (z +9.6) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H2030 (line)]] | alt | 356 | 1 | 2 (2 ⚠) | [[Pentamidine (isethionate) (drug)]] 5 µM 2.05× (z +10.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.349× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 258 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.1) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[HepG2_C3A (line)]] | wt | 85.6 | 0 | 2 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM 0.223× (z -8.8) |
| [[Hs 766T (line)]] | wt | 242 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -16.3) ⚠ cell-cycle shift, explains ~83% of this change |
| [[J82 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.00× (z +15.1) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[NCI-H1792 (line)]] | alt | 434 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.236× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.2) |
| [[SW1417 (line)]] | alt | 306 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.50× (z +10.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 408 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +8.9) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[CFPAC-1 (line)]] | alt | 92.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +15.8) ⚠ cell-cycle shift, explains ~83% of this change | — |
| [[H4 (line)]] | wt | 152 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 60.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.02× (z +10.2) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 314 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.65× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 157 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.91× (z +12.3) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[A-427 (line)]] | wt | 16.5 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 49.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 39.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 36.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 50.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 19.8 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 56.5 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 17.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 29.5 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.3 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.3 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 28.8 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 21.3 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 872 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 323 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 46.9 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 53.3 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5778), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPHA4]] | +0.63 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[TFPI2]] | +0.63 | +0.59 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[PTGS2]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ATP2B1]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[CEMIP]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[IER3]] | +0.58 | +0.49 / +0.67 | both halves | 1e-05 |  |
| [[AHR]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SMOC1]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PMEPA1]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[IL6]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FST]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[GNG11]] | +0.55 | +0.53 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC23]] | -0.49 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[PCYT1A]] | -0.48 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[RUFY2]] | -0.47 | -0.48 / -0.36 | both halves | 9e-05 |  |
| [[LRRC47]] | -0.46 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[SLC30A6]] | -0.44 | -0.37 / -0.40 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises SERPINE2's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 3.9% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPIND1]] | B | SERPIND1 activity raises SERPINE2's level | lines that do not express SERPIND1 (16) vs lines expressing it (34) | 3.75× lower at baseline in the lines without SERPIND1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000254303, ENSG00000287390, LANCL3; maybe low, not absent |
| [[DUSP4]] | B | DUSP4 activity raises SERPINE2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.53× lower at baseline in the lines without DUSP4 | 0.067 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[SEMA3A]] | B | SEMA3A activity raises SERPINE2's level | lines that do not express SEMA3A (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without SEMA3A | 0.097 | ⚠ within organs, on part of the lines; also absent: PRRX2, SEMA3D, CD5L |
| [[CEMIP]] | C | CEMIP activity raises SERPINE2's level | lines that do not express CEMIP (19) vs lines expressing it (31) | 3.57× lower at baseline in the lines without CEMIP | 0.022 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, DUSP4, SHC4; co-absent with the target |
| [[LINC01583]] | C | LINC01583 activity raises SERPINE2's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 3.99× lower at baseline in the lines without LINC01583 | 0.027 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2; co-absent with the target |
| [[RSPO3]] | C | RSPO3 activity raises SERPINE2's level | lines that do not express RSPO3 (39) vs lines expressing it (11) | 2.74× lower at baseline in the lines without RSPO3 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, TBXT, GSG1L2; co-absent with the target |
| [[AADAC]] | C | AADAC activity raises SERPINE2's level | lines that do not express AADAC (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without AADAC | 0.067 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |
| [[ITIH5]] | C | ITIH5 activity raises SERPINE2's level | lines that do not express ITIH5 (37) vs lines expressing it (13) | 3.67× lower at baseline in the lines without ITIH5 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GDNF, TDRD9, ENSG00000234426; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises SERPINE2's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.95× lower at baseline in the lines without IGFBP7 | 0.079 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[CSF2]] | C | CSF2 activity raises SERPINE2's level | lines that do not express CSF2 (26) vs lines expressing it (24) | 3.32× lower at baseline in the lines without CSF2 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: IL6, CCBE1, G0S2; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 18, C 6. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AHR]] | B | SERPINE2 activity raises AHR's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.74× lower at baseline in the lines without SERPINE2 | 0.001 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[ATP2B1]] | B | SERPINE2 activity raises ATP2B1's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without SERPINE2 | 0.002 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[FAM107B]] | B | SERPINE2 activity raises FAM107B's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 3.25× lower at baseline in the lines without SERPINE2 | 0.003 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[PLA2G4A]] | B | SERPINE2 activity raises PLA2G4A's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without SERPINE2 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[CD55]] | B | SERPINE2 activity raises CD55's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.36× lower at baseline in the lines without SERPINE2 | 0.008 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[IER3]] | B | SERPINE2 activity raises IER3's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.10× lower at baseline in the lines without SERPINE2 | 0.009 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[ITPRID2]] | B | SERPINE2 activity raises ITPRID2's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.59× lower at baseline in the lines without SERPINE2 | 0.017 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[PPP3CA]] | B | SERPINE2 activity raises PPP3CA's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.62× lower at baseline in the lines without SERPINE2 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[DOCK4]] | B | SERPINE2 activity raises DOCK4's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.29× lower at baseline in the lines without SERPINE2 | 0.040 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[ADGRL4]] | B | SERPINE2 activity raises ADGRL4's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 2.03× lower at baseline in the lines without SERPINE2 | 0.048 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[TNFAIP8]] | B | SERPINE2 activity raises TNFAIP8's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without SERPINE2 | 0.050 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |
| [[MAP3K5]] | B | SERPINE2 activity raises MAP3K5's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 1.52× lower at baseline in the lines without SERPINE2 | 0.067 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12 |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.462). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.4, 14.2); signed map (17.5, 52.2). **Vector** length 102, 26.1% of its response variance represented; |z| ≥ 3 in 1,121 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.4 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.6 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +8.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.3 | +6.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +6.9 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | +1.8 | +1.9 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.6 | +1.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.8 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~43% of this change | -4.2 | -4.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.3 | -6.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.0 | -3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | serpin family E member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q36.1 — chr2:223,975,045-224,039,318 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PN1, GDN, PNI, nexin; previously PI7 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 6 pathways, smallest: Amplification and propagation of coagulation cascade; Fibrin formation; Dissolution of Fibrin Clot |
| Matched by | ensembl_id |

**Function**, from UniProt [P07093](https://www.uniprot.org/uniprotkb/P07093) (Glia-derived nexin):

> Serine protease inhibitor with activity toward thrombin, trypsin, and urokinase. Promotes neurite extension by inhibiting thrombin. Binds heparin.

**Summary**, from NCBI Gene [5270](https://www.ncbi.nlm.nih.gov/gene/5270):

> This gene encodes a member of the serpin family of proteins, a group of proteins that inhibit serine proteases. Thrombin, urokinase, plasmin and trypsin are among the proteases that this family member can inhibit. This gene is a susceptibility gene for chronic obstructive pulmonary disease and for emphysema. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Aug 2012]

**Accessions** — [HGNC:8951](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8951) · Entrez [5270](https://www.ncbi.nlm.nih.gov/gene/5270) · UniProt [P07093](https://www.uniprot.org/uniprotkb/P07093) · Ensembl [ENSG00000135919](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135919)

## Data

Gene col 5778: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5778); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5778, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5778]; `tensor/DDL_lfc|DDL_z.npy` [5778]; `embed/gene_vectors.npy` [5778]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5778 or target_col == 5778). Every well: [[SERPINE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
