---
symbol: "TPD52L1"
type: "gene"
col: 3305
ensembl_id: "ENSG00000111907"
name: "TPD52 like 1"
location: "6q22.31"
module: 190
arm: "+"
pooled_cpm: 30.82
n_lines_expressing: 38
n_dd_up: 21
n_dd_down: 19
n_dd_up_clean: 17
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 9
direction_downstream: 7
tags: ["gene", "module/190"]
generated_by: "tahoemap"
---

# TPD52L1

*TPD52 like 1* — 6q22.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.61× (z +14.3, q 8e-44, up in 28 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.476× (z -15.7, q 0e+00, down in 33 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC18B1]] (+0.67, fdr 7e-06), [[RAVER2]] (+0.67, fdr 7e-06), [[STEAP2]] (+0.64, fdr 7e-06); moves opposite to [[CYTH2]] (-0.61, fdr 1e-05), [[PKNOX1]] (-0.57, fdr 1e-05), [[DDX5]] (-0.54, fdr 3e-05).
> It is in [[Module 190]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ICA1]] → it (grade B ⚠); 7 go from it, the strongest it → [[SLC18B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3305.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **1.61×** | +14.3 | 8e-44 | 28/36 (NCI-H2347, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~24% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.79×** | +12.4 | 1e-32 | 32/36 (SW1417, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.73×** | +11.7 | 2e-29 | 26/34 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.45×** | +11.1 | 2e-26 | 25/36 (NCI-H2347, J82, …) | all doses, stronger at high dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.65×** | +10.7 | 9e-25 | 29/35 (SW1417, LS 180, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +8.8 | 1e-16 | 24/33 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.46×** | +8.0 | 1e-13 | 19/35 (J82, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +7.8 | 5e-13 | 23/36 (BT-474, LS 180, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.27×** | +7.2 | 3e-11 | 19/36 (NCI-H1792, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.37×** | +6.8 | 7e-10 | 11/29 (A498, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.69×** | +5.8 | 3e-07 | 12/36 (NCI-H1792, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.2 | 1e-05 | 16/35 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.53×** | +4.7 | 1e-04 | 6/33 (A498, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.34×** | +4.4 | 4e-04 | 8/35 (HT-29, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.22×** | +4.1 | 0.002 | 10/28 (NCI-H1792, C32, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.002 | 12/34 (HCT15, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.002 | 10/34 (CFPAC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.004 | 9/34 (SW48, SW480, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3305.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.476×** | -15.7 | 0e+00 | 33/35 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.488×** | -15.2 | 0e+00 | 25/34 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.552×** | -12.6 | 3e-34 | 29/34 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.678×** | -11.6 | 4e-29 | 23/36 (LoVo, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.636×** | -9.2 | 3e-18 | 22/35 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.652×** | -9.1 | 1e-17 | 22/34 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.699×** | -7.6 | 2e-12 | 20/34 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.518×** | -7.3 | 2e-11 | 20/36 (LoVo, LS 180, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.721×** | -6.9 | 2e-10 | 20/35 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.837× | -5.3 | 6e-06 | 17/36 (SW1417, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.779×** | -5.3 | 7e-06 | 20/35 (LoVo, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.662×** | -4.6 | 2e-04 | 15/34 (RKO, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.793×** | -4.5 | 2e-04 | 11/33 (HCT15, LoVo, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.819×** | -4.2 | 1e-03 | 15/35 (SW480, LoVo, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **0.714×** | -3.7 | 0.007 | 8/36 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.721×** | -3.6 | 0.010 | 12/33 (A498, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.842× | -3.5 | 0.014 | 6/36 (RKO, AN3 CA, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.849× | -3.5 | 0.016 | 9/36 (A498, HS-578T, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.741×** | -3.3 | 0.023 | 9/35 (LoVo, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3305. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 104 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -43.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -27.8) |
| [[SW480 (line)]] | alt | 62.4 | 0 | 9 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.190× (z -20.5) |
| [[LS 180 (line)]] | wt | 97.7 | 2 | 6 (4 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.12× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -16.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.358× (z -12.2) |
| [[SW48 (line)]] | wt | 104 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -15.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -10.9) |
| [[Hs 766T (line)]] | wt | 68.8 | 1 | 5 (3 ⚠) | [[Selinexor (drug)]] 5 µM 2.42× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.300× (z -13.1) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 32.7 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -24.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -12.1) |
| [[NCI-H1573 (line)]] | alt | 36.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0644× (z -24.9) |
| [[RKO (line)]] | wt | 20.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -10.4) |
| [[A498 (line)]] | wt | 45.2 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -19.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -17.7) |
| [[SW1417 (line)]] | alt | 53.5 | 1 | 3 (1 ⚠) | [[Selinexor (drug)]] 0.05 µM 2.91× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.291× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 39.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -19.5) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.310× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 28.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.2) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -8.8) |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -10.4) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -9.5) |
| [[HCT15 (line)]] | alt | 44.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -10.6) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.236× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 75.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.484× (z -9.2) ⚠ cell-cycle shift, explains ~7% of this change |
| [[HT-29 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -13.7) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 12.8 | 1 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.44× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.274× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 19.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SHP-77 (line)]] | alt | 63.5 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0638× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 22.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -14.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 3.29 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.05 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.79 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.64 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.26 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.30 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3305), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC18B1]] | +0.67 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RAVER2]] | +0.67 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[STEAP2]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[PECR]] | +0.62 | +0.50 / +0.70 | both halves | 1e-05 |  |
| [[PIK3C2B]] | +0.60 | +0.69 / +0.51 | both halves | 1e-05 |  |
| [[STK32A]] | +0.57 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[RASAL1]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FRAS1]] | +0.56 | +0.60 / +0.57 | both halves | 8e-06 |  |
| [[CIBAR1]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[LRRC8D]] | +0.55 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[PIGB]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ZFP64]] | +0.55 | +0.43 / +0.52 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYTH2]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[PKNOX1]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[DDX5]] | -0.54 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[PPP1CA]] | -0.51 | -0.40 / -0.56 | both halves | 4e-05 |  |
| [[CD59]] | -0.50 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[GRK4]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[ZNF324]] | -0.48 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[WFDC10B]] | -0.48 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[KPNA4]] | -0.47 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[LRRC14]] | -0.47 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[RB1]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 | pathway: HALLMARK_MYOGENESIS |
| [[TRPV1]] | -0.46 | -0.47 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ICA1]] | B | ICA1 activity raises TPD52L1's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without ICA1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[STK32A]] | B | STK32A activity raises TPD52L1's level | lines that do not express STK32A (23) vs lines expressing it (27) | 1.65× lower at baseline in the lines without STK32A | 0.030 | ⚠ within organs, on part of the lines; also absent: CHSY3, FRMPD4, SAA1 |
| [[RASAL1]] | B | RASAL1 activity raises TPD52L1's level | lines that do not express RASAL1 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without RASAL1 | 0.036 | ⚠ within organs, on part of the lines; also absent: CSF2RA, SMPDL3B, SKAP1 |
| [[FRAS1]] | B | FRAS1 activity raises TPD52L1's level | lines that do not express FRAS1 (22) vs lines expressing it (28) | 1.55× lower at baseline in the lines without FRAS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ANO9, ELF3, FAAH2 |
| [[ENTREP1]] | B | ENTREP1 activity raises TPD52L1's level | lines that do not express ENTREP1 (18) vs lines expressing it (32) | 1.33× lower at baseline in the lines without ENTREP1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LHX2, OLFM1, COL4A4 |
| [[TTC22]] | B | TTC22 activity raises TPD52L1's level | lines that do not express TTC22 (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without TTC22 | 0.063 | ⚠ within organs, on part of the lines; also absent: COL17A1, TRIM15, SERPINB5 |
| [[CHN2]] | B | CHN2 activity raises TPD52L1's level | lines that do not express CHN2 (20) vs lines expressing it (30) | 1.92× lower at baseline in the lines without CHN2 | 0.067 | ⚠ within organs, on part of the lines; also absent: CPVL, IL20RA, PRR15 |
| [[SLC25A27]] | B | SLC25A27 activity raises TPD52L1's level | lines that do not express SLC25A27 (8) vs lines expressing it (42) | 2.75× lower at baseline in the lines without SLC25A27 | 0.081 | ⚠ within organs, on part of the lines; also absent: PPM1L, CYP39A1, ATP8A1 |
| [[SULT1A1]] | B | SULT1A1 activity raises TPD52L1's level | lines that do not express SULT1A1 (16) vs lines expressing it (34) | 2.35× lower at baseline in the lines without SULT1A1 | 0.095 | ⚠ within organs, on part of the lines; also absent: ARHGEF5, KRT18, MARVELD2 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC18B1]] | B | TPD52L1 activity raises SLC18B1's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 2.45× lower at baseline in the lines without TPD52L1 | 0.001 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[ICA1]] | B | TPD52L1 activity raises ICA1's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 3.32× lower at baseline in the lines without TPD52L1 | 0.004 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[STK32A]] | B | TPD52L1 activity raises STK32A's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 2.36× lower at baseline in the lines without TPD52L1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[LINC00205]] | B | TPD52L1 activity lowers LINC00205's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 1.38× higher at baseline in the lines without TPD52L1 | 0.059 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[PIK3C2B]] | B | TPD52L1 activity raises PIK3C2B's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 1.87× lower at baseline in the lines without TPD52L1 | 0.061 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| cells under [[NVP-BHG712 (drug)]] 5 µM | B | TPD52L1 activity raises the cells' numbers under NVP-BHG712 5 µM (protects the cells) | lines that do not express TPD52L1 (12) vs lines expressing it (36) | the lines without TPD52L1: 0.90× the cells of the other lines | 0.090 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |
| [[SAMD12]] | B | TPD52L1 activity raises SAMD12's level | lines that do not express TPD52L1 (12) vs lines expressing it (38) | 3.15× lower at baseline in the lines without TPD52L1 | 0.091 | ⚠ within organs, on part of the lines; also absent: TNFRSF21, EML5 |

## Where it sits

- **Module**: [[Module 190]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.40; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.0, 13.0); signed map (14.8, -45.4). **Vector** length 96.1, 23.2% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.0 | +14.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.2 | +11.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.9 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +8.8 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +4.7 | +12.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.7 | +7.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.6 | +10.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +7.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +4.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -15.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -5.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.6 | -9.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.5 | -3.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -6.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.4 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -5.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | TPD52 like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q22.31 — chr6:125,119,049-125,264,407 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D53, hD53, TPD53 |
| Hallmark sets | MYOGENESIS, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY, P53_PATHWAY |
| Reactome | 4 pathways, smallest: Golgi Associated Vesicle Biogenesis; trans-Golgi Network Vesicle Budding; Membrane Trafficking |
| Matched by | ensembl_id |

UniProt [Q16890](https://www.uniprot.org/uniprotkb/Q16890) carries no function annotation.

**Summary**, from NCBI Gene [7164](https://www.ncbi.nlm.nih.gov/gene/7164):

> This gene encodes a member of a family of proteins that contain coiled-coil domains and may form hetero- or homomers. The encoded protein is involved in cell proliferation and calcium signaling. It also interacts with the mitogen-activated protein kinase kinase kinase 5 (MAP3K5/ASK1) and positively regulates MAP3K5-induced apoptosis. Multiple alternatively spliced transcript variants have been observed. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:12006](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12006) · Entrez [7164](https://www.ncbi.nlm.nih.gov/gene/7164) · UniProt [Q16890](https://www.uniprot.org/uniprotkb/Q16890) · Ensembl [ENSG00000111907](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111907)

## Data

Gene col 3305: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3305); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3305, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3305]; `tensor/DDL_lfc|DDL_z.npy` [3305]; `embed/gene_vectors.npy` [3305]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3305 or target_col == 3305). Every well: [[TPD52L1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPD52L1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
