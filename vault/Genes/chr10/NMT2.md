---
symbol: "NMT2"
type: "gene"
col: 7633
ensembl_id: "ENSG00000152465"
name: "N-myristoyltransferase 2"
location: "10p13"
module: 24
arm: "+"
pooled_cpm: 56.54
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 4
n_dd_up_clean: 15
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# NMT2

*N-myristoyltransferase 2* — 10p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.77× (z +24.8, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 0.754× (z -6.9, q 4e-09, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HABP4]] (+0.59, fdr 2e-05), [[CDKN2D]] (+0.59, fdr 4e-05), [[RRAS]] (+0.56, fdr 1e-04); moves opposite to [[EMG1]] (-0.57, fdr 2e-05), [[E2F3]] (-0.56, fdr 3e-05), [[KRR1]] (-0.56, fdr 5e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PGM5P2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7633.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.77×** | +24.8 | 0e+00 | 46/47 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +20.9 | 0e+00 | 44/47 (SW1417, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +19.6 | 0e+00 | 44/47 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +18.2 | 0e+00 | 35/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +11.4 | 4e-28 | 34/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +9.1 | 1e-17 | 27/47 (HEC-1-A, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +9.0 | 3e-17 | 34/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +8.7 | 4e-16 | 29/47 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.92×** | +8.3 | 5e-15 | 35/47 (RKO, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.78×** | +7.3 | 1e-11 | 33/47 (CFPAC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +7.3 | 1e-11 | 27/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.33×** | +7.0 | 2e-10 | 27/47 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.8 | 6e-10 | 23/47 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.31×** | +6.6 | 2e-09 | 26/47 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +6.3 | 9e-09 | 19/48 (A-172, SW 900, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +5.4 | 2e-06 | 13/47 (HOP62, RKO, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.21×** | +4.7 | 9e-05 | 19/47 (CFPAC-1, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7633.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.754×** | -6.9 | 4e-09 | 29/47 (J82, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.682×** | -4.9 | 3e-04 | 21/48 (A-172, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.821×** | -4.6 | 8e-04 | 14/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.735×** | -3.9 | 0.013 | 15/46 (SNU-1, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.896× | -3.8 | 0.019 | 11/47 (J82, Hs 766T, …) | top dose only | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.858× | -3.7 | 0.019 | 19/47 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.859× | -3.7 | 0.019 | 18/46 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.871× | -3.3 | 0.055 | 12/47 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.865× | -3.3 | 0.055 | 14/46 (SW480, SW1417, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 0.874× | -3.3 | 0.059 | 8/47 (MIA PaCa-2, CHP-212, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.883× | -3.0 | 0.13 | 15/47 (A-172, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7633. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 57.5 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +21.5) | — |
| [[SW1417 (line)]] | alt | 63.0 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.6) | — |
| [[A-427 (line)]] | wt | 38.9 | 6 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.65× (z +11.8) | — |
| [[J82 (line)]] | alt | 78.4 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.341× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.432× (z -9.6) |
| [[SNU-423 (line)]] | alt | 71.8 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.03× (z +12.4) | — |
| [[A498 (line)]] | wt | 52.2 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +20.8) | — |
| [[A549 (line)]] | wt | 64.7 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +15.6) | — |
| [[CFPAC-1 (line)]] | alt | 65.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 36.6 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.291× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 105 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +25.6) | — |
| [[NCI-H460 (line)]] | wt | 100 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 0.05 µM 2.39× (z +8.7) ⚠ cell-cycle shift, explains ~68% of this change · without an alert: [[Triamcinolone (drug)]] 5 µM 1.84× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 56.2 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.51× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 35.2 | 4 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.75× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.4) | — |
| [[HT-29 (line)]] | alt | 29.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.78× (z +11.0) | [[PH-797804 (drug)]] 5 µM 0.0478× (z -13.1) |
| [[PANC-1 (line)]] | alt | 33.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +12.6) | — |
| [[A-172 (line)]] | wt | 135 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.96× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[AsPC-1 (line)]] | alt | 61.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[HEC-1-A (line)]] | alt | 53.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 83.7 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.314× (z -10.8) ⚠ cell-cycle shift, explains ~79% of this change |
| [[LoVo (line)]] | wt | 30.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.60× (z +12.5) | — |
| [[NCI-H1792 (line)]] | alt | 68.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +12.9) | — |
| [[NCI-H2030 (line)]] | alt | 93.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.46× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 54.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 55.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.58× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 39.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 50.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +9.1) | — |
| [[KATO III (line)]] | alt | 37.1 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.77× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H2347 (line)]] | alt | 43.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.68× (z +10.6) | — |
| [[Panc 03.27 (line)]] | alt | 39.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +11.0) | — |
| [[SNU-1 (line)]] | wt | 47.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +12.8) | — |
| [[C32 (line)]] | wt | 43.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.373× (z -8.5) |
| [[HOP62 (line)]] | alt | 48.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.38× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 40.9 | 0 | 1 | — | [[IQ 1 (drug)]] 5 µM 0.0992× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 45.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.8) | — |
| [[SW48 (line)]] | wt | 44.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +8.9) | — |
| [[AN3 CA (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 71.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.29 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 95.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 51.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 49.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7633), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HABP4]] | +0.59 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CDKN2D]] | +0.59 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[RRAS]] | +0.56 | +0.36 / +0.37 | both halves | 1e-04 |  |
| [[LLGL2]] | +0.55 | +0.43 / +0.32 | both halves | 2e-04 |  |
| [[MEGF9]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[RAP1A]] | +0.55 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[CYTH3]] | +0.54 | +0.32 / +0.58 | both halves | 2e-04 |  |
| [[UGCG]] | +0.54 | +0.48 / +0.41 | both halves | 4e-05 |  |
| [[NKTR]] | +0.54 | +0.47 / +0.41 | both halves | 4e-05 |  |
| [[HDAC5]] | +0.54 | +0.51 / +0.38 | both halves | 6e-05 |  |
| [[GPX4]] | +0.53 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[PPP1R2]] | +0.53 | +0.30 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EMG1]] | -0.57 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[E2F3]] | -0.56 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[KRR1]] | -0.56 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[MCPH1]] | -0.53 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[ZNF195]] | -0.52 | -0.41 / -0.38 | both halves | 7e-05 |  |
| [[YIPF7]] | -0.52 | -0.36 / -0.36 | both halves | 9e-05 |  |
| [[PIGW]] | -0.52 | -0.41 / -0.31 | both halves | 2e-04 |  |
| [[HCG18]] | -0.51 | -0.44 / -0.36 | both halves | 1e-04 |  |
| [[GTF3C4]] | -0.51 | -0.41 / -0.33 | both halves | 1e-04 |  |
| [[RPTOR]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[ANKAR]] | -0.51 | -0.41 / -0.29 | both halves | 2e-04 |  |
| [[GLIPR1-AS1]] | -0.50 | -0.37 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PGM5P2]] | B | PGM5P2 activity raises NMT2's level | lines that do not express PGM5P2 (9) vs lines expressing it (41) | 1.57× lower at baseline in the lines without PGM5P2 | 0.071 | ⚠ within organs, on part of the lines; also absent: PGM5P2-1, PALM2AKAP2, FKBP7; maybe low, not absent |
| [[CLTCL1]] | C | CLTCL1 activity raises NMT2's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 2.36× lower at baseline in the lines without CLTCL1 | 0.038 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.325). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.7, -1.4); signed map (-28.4, 15.7). **Vector** length 109, 28.2% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.5 | +20.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.4 | +19.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +24.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.8 | +6.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.6 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.9 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +9.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.6 | +7.3 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -3.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.5 | -1.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.4 | -3.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -4.8 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.1 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | N-myristoyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p13 — chr10:15,102,584-15,168,693 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | N-myristoyltransferase family |
| Reactome | 13 pathways, smallest: eNOS activation; Membrane binding and targetting of GAG proteins; Synthesis And Processing Of GAG, GAGPOL Polyproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O60551](https://www.uniprot.org/uniprotkb/O60551) (Glycylpeptide N-tetradecanoyltransferase 2):

> Adds a myristoyl group to the N-terminal glycine residue of certain cellular and viral proteins. Also able to mediate N-terminal lysine myristoylation of proteins: catalyzes myristoylation of ARF6 on both 'Gly-2' and 'Lys-3'. Lysine myristoylation is required to maintain ARF6 on membranes during the GTPase cycle.

**Summary**, from NCBI Gene [9397](https://www.ncbi.nlm.nih.gov/gene/9397):

> This gene encodes one of two N-myristoyltransferase proteins. N-terminal myristoylation is a lipid modification that is involved in regulating the function and localization of signaling proteins. The encoded protein catalyzes the addition of a myristoyl group to the N-terminal glycine residue of many signaling proteins, including the human immunodeficiency virus type 1 (HIV-1) proteins, Gag and Nef. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Apr 2015]

**Accessions** — [HGNC:7858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7858) · Entrez [9397](https://www.ncbi.nlm.nih.gov/gene/9397) · UniProt [O60551](https://www.uniprot.org/uniprotkb/O60551) · Ensembl [ENSG00000152465](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152465)

## Data

Gene col 7633: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7633); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7633, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7633]; `tensor/DDL_lfc|DDL_z.npy` [7633]; `embed/gene_vectors.npy` [7633]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7633 or target_col == 7633). Every well: [[NMT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
