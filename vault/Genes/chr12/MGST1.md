---
symbol: "MGST1"
type: "gene"
col: 172
ensembl_id: "ENSG00000008394"
name: "microsomal glutathione S-transferase 1"
location: "12p12.3"
module: 34
arm: "+"
pooled_cpm: 113.29
n_lines_expressing: 38
n_dd_up: 33
n_dd_down: 8
n_dd_up_clean: 24
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 12
direction_downstream: 12
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# MGST1

*microsomal glutathione S-transferase 1* — 12p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.00× (z +14.9, q 0e+00, up in 36 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.95× (z +9.1, q 2e-17, up in 25 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -14.2, q 3e-43, down in 25 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKR1C1]] (+0.66, fdr 7e-06), [[LARP4]] (+0.64, fdr 8e-06), [[ABCC2]] (+0.62, fdr 1e-05); moves opposite to [[RAC2]] (-0.65, fdr 1e-05), [[ARID3B]] (-0.61, fdr 3e-05), [[MTMR14]] (-0.61, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); 12 go from it, the strongest it → [[AKR1C3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 10 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 172.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.00×** | +14.9 | 0e+00 | 36/37 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.74×** | +13.2 | 4e-37 | 30/32 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +10.5 | 2e-23 | 28/33 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.95×** | +9.1 | 2e-17 | 25/36 (LS 180, COLO 205, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +8.1 | 5e-14 | 26/36 (COLO 205, HepG2/C3A, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +7.0 | 3e-10 | 24/36 (HepG2/C3A, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.72×** | +6.9 | 4e-10 | 25/36 (HT-29, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +6.8 | 1e-09 | 23/35 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.48×** | +5.3 | 6e-06 | 23/36 (COLO 205, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +5.2 | 1e-05 | 24/35 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +5.2 | 1e-05 | 19/36 (NCI-H2347, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +4.5 | 3e-04 | 20/28 (HEC-1-A, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 4e-04 | 22/36 (COLO 205, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **1.78×** | +4.1 | 0.002 | 22/35 (SW 900, A549, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.33×** | +3.9 | 0.004 | 20/36 (HT-29, COLO 205, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.006 | 19/36 (HOP62, NCI-H1573, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.006 | 18/36 (NCI-H1792, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.012 | 22/35 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.016 | 14/36 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.016 | 15/37 (NCI-H460, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.017 | 16/36 (J82, NCI-H2347, …) | top dose only |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.60×** | +3.3 | 0.021 | 18/36 (SW 900, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.025 | 18/36 (NCI-H1792, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 172.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -14.2 | 3e-43 | 25/36 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.368×** | -13.6 | 2e-39 | 35/36 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.419×** | -11.8 | 6e-30 | 36/36 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.460×** | -10.5 | 8e-24 | 35/36 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.706×** | -4.7 | 3e-04 | 22/36 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.724×** | -4.4 | 0.001 | 19/36 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.553×** | -4.2 | 0.002 | 26/37 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.637×** | -3.2 | 0.099 | 13/36 (Panc 03.27, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 172. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 276 | 5 (1 ⚠) | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.07× (z +12.8) | [[Panobinostat (drug)]] 5 µM 0.167× (z -20.3) |
| [[NCI-H460 (line)]] | wt | 302 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -32.7) |
| [[COLO 205 (line)]] | alt | 73.0 | 7 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 7.13× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.7) |
| [[NCI-H1573 (line)]] | alt | 327 | 1 | 7 (2 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.57× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.0761× (z -30.3) |
| [[HS-578T (line)]] | alt | 109 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +11.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.79× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.197× (z -12.2) |
| [[HT-29 (line)]] | alt | 64.8 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.83× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 4.79× (z +11.8) | — |
| [[hTERT-HPNE (line)]] | wt | 177 | 3 | 4 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.52× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.144× (z -15.6) |
| [[LoVo (line)]] | wt | 96.7 | 5 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.51× (z +10.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.26× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 77.2 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.98× (z +10.6) | — |
| [[NCI-H1792 (line)]] | alt | 141 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.69× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.88× (z +13.0) | — |
| [[NCI-H2347 (line)]] | alt | 304 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +21.5) | — |
| [[SW48 (line)]] | wt | 99.9 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -13.9) |
| [[A549 (line)]] | wt | 119 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 6.33× (z +14.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -9.0) |
| [[J82 (line)]] | alt | 88.5 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 3.57× (z +10.1) | [[Panobinostat (drug)]] 0.5 µM 0.358× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 184 | 3 (1 ⚠) | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.51× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.513× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.465× (z -8.5) |
| [[RKO (line)]] | wt | 98.7 | 1 (1 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0912× (z -23.4) |
| [[SNU-423 (line)]] | alt | 71.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -10.4) |
| [[SW 900 (line)]] | alt | 240 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 2.51× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.382× (z -9.7) |
| [[A498 (line)]] | wt | 393 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 43.9 | 3 | 1 | [[Ixazomib citrate (drug)]] 5 µM 8.72× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -9.5) |
| [[HOP62 (line)]] | alt | 53.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.65× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 3.90× (z +8.5) | — |
| [[NCI-H2030 (line)]] | alt | 141 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -17.9) |
| [[KATO III (line)]] | alt | 78.7 | 2 | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.02× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.294× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +10.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -13.3) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 58.6 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.170× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 67.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 137 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.3) |
| [[RPMI-7951 (line)]] | alt | 73.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 103 | 1 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.84× (z +10.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -10.5) |
| [[SNU-1 (line)]] | wt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.36× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 29.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.80× (z +10.1) | — |
| [[A-172 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 9.56 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.33 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.6 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 73.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.9 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 11.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 91.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.4 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 172), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*42 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKR1C1]] | +0.66 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[LARP4]] | +0.64 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[ABCC2]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[NMRAL2P-1]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[STXBP5]] | +0.59 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[LARP1]] | +0.58 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ME1]] | +0.58 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[HECW2]] | +0.57 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[NMRAL2P]] | +0.56 | +0.62 / +0.52 | both halves | 1e-05 |  |
| [[C1RL]] | +0.56 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[GSR]] | +0.56 | +0.47 / +0.66 | both halves | 2e-05 | pathway: HALLMARK_REACTIVE_OXYGEN_SPECIES_PATHWAY; STRING 936 |
| [[NSMAF]] | +0.55 | +0.50 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*58 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAC2]] | -0.65 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.61 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[MTMR14]] | -0.61 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[TRPT1]] | -0.61 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[FAM89B]] | -0.60 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[TMEM158]] | -0.60 | -0.48 / -0.65 | both halves | 2e-05 |  |
| [[TBC1D10A]] | -0.60 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ADAM8]] | -0.59 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[CIB1]] | -0.59 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PLAUR]] | -0.58 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[STC1]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[PPARA]] | -0.57 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises MGST1's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 2.71× lower at baseline in the lines without NMRAL2P-1 | 0.021 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[MAP2K1]] | B | MAP2K1 activity lowers MGST1's level | compounds that target MAP2K1: 4 of 4 raise it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 7.0% of all compounds | 0.030 | ⚠ off-target possible; 4 compounds |
| [[HIPK2]] | B | HIPK2 activity raises MGST1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 3.66× lower at baseline in the lines without HIPK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[PLAUR]] | B | PLAUR activity raises MGST1's level | lines that do not express PLAUR (10) vs lines expressing it (40) | 2.92× lower at baseline in the lines without PLAUR | 0.042 | ⚠ within organs, on part of the lines; also absent: HRH1, CAV2, MGLL; maybe low, not absent |
| [[SLC39A8]] | B | SLC39A8 activity raises MGST1's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 2.28× lower at baseline in the lines without SLC39A8 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[CREG2]] | B | CREG2 activity raises MGST1's level | lines that do not express CREG2 (19) vs lines expressing it (31) | 2.14× lower at baseline in the lines without CREG2 | 0.053 | ⚠ within organs, on part of the lines; also absent: ADGRF4, IGSF9, IL1A |
| [[LINC02057]] | B | LINC02057 activity raises MGST1's level | lines that do not express LINC02057 (25) vs lines expressing it (25) | 2.14× lower at baseline in the lines without LINC02057 | 0.053 | ⚠ within organs, on part of the lines; also absent: CSF3, PTHLH, IL6 |
| [[IL1R1]] | B | IL1R1 activity raises MGST1's level | lines that do not express IL1R1 (17) vs lines expressing it (33) | 1.93× lower at baseline in the lines without IL1R1 | 0.058 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, CXCL8, NR3C1 |
| [[ROS1]] | B | ROS1 activity raises MGST1's level | lines that do not express ROS1 (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without ROS1 | 0.064 | ⚠ within organs, on part of the lines; also absent: COL1A1, APCDD1L, GYPC; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises MGST1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TMEM158]] | B | TMEM158 activity raises MGST1's level | lines that do not express TMEM158 (19) vs lines expressing it (31) | 1.63× lower at baseline in the lines without TMEM158 | 0.087 | ⚠ within organs, on part of the lines; also absent: ENSG00000289526, NALCN, CLEC2B |
| [[ABCC2]] | B | ABCC2 activity raises MGST1's level | lines that do not express ABCC2 (22) vs lines expressing it (28) | 2.04× lower at baseline in the lines without ABCC2 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000230647, NR0B1, DNAJC12; maybe low, not absent |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1C3]] | B | MGST1 activity raises AKR1C3's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 3.19× lower at baseline in the lines without MGST1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[AKR1C1]] | B | MGST1 activity raises AKR1C1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 3.39× lower at baseline in the lines without MGST1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[IL1R1]] | B | MGST1 activity raises IL1R1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without MGST1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[NMRAL2P]] | B | MGST1 activity raises NMRAL2P's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.57× lower at baseline in the lines without MGST1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[PLAUR]] | B | MGST1 activity raises PLAUR's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without MGST1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[GPN3]] | B | MGST1 activity lowers GPN3's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.31× higher at baseline in the lines without MGST1 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[TBC1D10A]] | B | MGST1 activity raises TBC1D10A's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without MGST1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[TRIM16L]] | B | MGST1 activity raises TRIM16L's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.56× lower at baseline in the lines without MGST1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[NMRAL2P-1]] | B | MGST1 activity raises NMRAL2P-1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.68× lower at baseline in the lines without MGST1 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[AKR1C2]] | B | MGST1 activity raises AKR1C2's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 2.67× lower at baseline in the lines without MGST1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[HECW1]] | B | MGST1 activity raises HECW1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without MGST1 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[LARP1]] | B | MGST1 activity lowers LARP1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.19× higher at baseline in the lines without MGST1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction -0.401). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.8, 46.6); signed map (51.5, -9.2). **Vector** length 120, 35.0% of its response variance represented; |z| ≥ 3 in 1,271 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +6.8 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +7.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +8.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.9 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.4 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.4 | +3.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -13.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -10.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.2 | -11.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -4.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -2.4 | -4.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | microsomal glutathione S-transferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.3 — chr12:16,347,142-16,609,259 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGST-I, PMAN; previously GST12 |
| Gene groups (HGNC) | Microsomal glutathione S-transferases; MAPEG superfamily |
| Hallmark sets | REACTIVE_OXYGEN_SPECIES_PATHWAY |
| Reactome | 6 pathways, smallest: Aflatoxin activation and detoxification; Glutathione conjugation; Phase II - Conjugation of compounds |
| Matched by | ensembl_id |

**Function**, from UniProt [P10620](https://www.uniprot.org/uniprotkb/P10620) (Microsomal glutathione S-transferase 1):

> Conjugation of reduced glutathione to a wide number of exogenous and endogenous hydrophobic electrophiles.

**Summary**, from NCBI Gene [4257](https://www.ncbi.nlm.nih.gov/gene/4257):

> The MAPEG (Membrane Associated Proteins in Eicosanoid and Glutathione metabolism) family consists of six human proteins, two of which are involved in the production of leukotrienes and prostaglandin E, important mediators of inflammation. Other family members, demonstrating glutathione S-transferase and peroxidase activities, are involved in cellular defense against toxic, carcinogenic, and pharmacologically active electrophilic compounds. This gene encodes a protein that catalyzes the …

**Accessions** — [HGNC:7061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7061) · Entrez [4257](https://www.ncbi.nlm.nih.gov/gene/4257) · UniProt [P10620](https://www.uniprot.org/uniprotkb/P10620) · Ensembl [ENSG00000008394](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000008394)

## Data

Gene col 172: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 172); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 172, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 172]; `tensor/DDL_lfc|DDL_z.npy` [172]; `embed/gene_vectors.npy` [172]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 172 or target_col == 172). Every well: [[MGST1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MGST1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
