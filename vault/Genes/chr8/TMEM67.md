---
symbol: "TMEM67"
type: "gene"
col: 9042
ensembl_id: "ENSG00000164953"
name: "transmembrane protein 67"
location: "8q22.1"
module: 205
arm: "+"
pooled_cpm: 41.48
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 22
n_dd_up_clean: 8
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/205"]
generated_by: "tahoemap"
---

# TMEM67

*transmembrane protein 67* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.97× (z +10.2, q 9e-22, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.524× (z -9.7, q 1e-19, down in 35 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFHC1]] (+0.69, fdr 7e-06), [[CCDC157]] (+0.69, fdr 7e-06), [[SLC25A14]] (+0.66, fdr 1e-05); moves opposite to [[CDV3]] (-0.55, fdr 1e-05), [[ZNF800]] (-0.50, fdr 3e-05), [[GCNT4]] (-0.48, fdr 1e-04).
> It is in [[Module 205]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[DYNC2H1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +10.2 | 9e-22 | 40/46 (LoVo, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +9.1 | 2e-17 | 36/46 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.69×** | +7.9 | 6e-13 | 32/46 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +5.4 | 8e-06 | 22/46 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +5.2 | 3e-05 | 23/47 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +5.0 | 5e-05 | 27/46 (RKO, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 1e-04 | 24/46 (NCI-H2347, C-33 A, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.2 | 0.002 | 22/46 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.026 | 21/46 (RKO, NCI-H2030, …) | top dose only | composition shift |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.26×** | +3.5 | 0.029 | 12/46 (NCI-H2030, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.60×** | +3.4 | 0.037 | 19/46 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.524×** | -9.7 | 1e-19 | 35/46 (SW480, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -7.2 | 2e-10 | 31/45 (HCT15, RKO, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.727×** | -6.8 | 2e-09 | 33/46 (NCI-H1573, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -6.5 | 1e-08 | 29/44 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.677×** | -5.9 | 4e-07 | 33/46 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.677×** | -5.9 | 4e-07 | 26/44 (HS-578T, CHP-212, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.675×** | -5.7 | 1e-06 | 27/46 (C32, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.688×** | -5.4 | 5e-06 | 21/36 (C-33 A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.699×** | -5.2 | 1e-05 | 26/45 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.710×** | -5.1 | 1e-05 | 26/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.788×** | -5.1 | 2e-05 | 24/46 (RPMI-7951, HS-578T, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.718×** | -4.7 | 1e-04 | 25/45 (NCI-H460, HT-29, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.733×** | -4.7 | 1e-04 | 23/46 (HS-578T, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.762×** | -4.1 | 0.002 | 23/46 (CFPAC-1, NCI-H460, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -4.0 | 0.002 | 20/45 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[vincristine (drug)]] 0.5 µM |  | **0.606×** | -4.0 | 0.003 | 20/46 (HS-578T, Hs 766T, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.05 µM |  | **0.764×** | -3.8 | 0.004 | 24/46 (MIA PaCa-2, HS-578T, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.858× | -3.2 | 0.032 | 17/46 (A498, HS-578T, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.655×** | -3.0 | 0.061 | 18/44 (NCI-H1792, SNU-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.805×** | -3.0 | 0.063 | 16/46 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.814×** | -3.0 | 0.070 | 13/46 (Hs 766T, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 48.8 | 4 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +15.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.74× (z +9.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -11.7) ⚠ toxic |
| [[C32 (line)]] | wt | 90.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.8) |
| [[CFPAC-1 (line)]] | alt | 44.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -13.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 14.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.65× (z +10.1) | — |
| [[HS-578T (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 50.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.3) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 63.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.444× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.337× (z -8.8) |
| [[SW480 (line)]] | alt | 43.6 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.249× (z -15.0) |
| [[A-172 (line)]] | wt | 28.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.250× (z -11.2) |
| [[A-427 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.193× (z -11.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[A498 (line)]] | wt | 61.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 16.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change |
| [[C-33 A (line)]] | alt | 70.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.5) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 31.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.199× (z -9.0) ⚠ toxic |
| [[H4 (line)]] | wt | 45.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.158× (z -11.7) |
| [[HCT15 (line)]] | alt | 68.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0474× (z -21.2) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 35.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.340× (z -8.7) |
| [[LS 180 (line)]] | wt | 10.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.70× (z +8.9) | — |
| [[NCI-H2030 (line)]] | alt | 66.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H2347 (line)]] | alt | 26.7 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 38.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.438× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -8.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -9.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 52.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.15 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 54.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 61.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.80 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 47.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 39.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFHC1]] | +0.69 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[CCDC157]] | +0.69 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[SLC25A14]] | +0.66 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[TTC26]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[NPHP1]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 | pathway: Anchoring of the basal body to the plasma membrane; STRING 994 |
| [[CFAP210]] | +0.64 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[FAM174A]] | +0.64 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CFAP69]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DNAL1]] | +0.63 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[IFT172]] | +0.60 | +0.57 / +0.54 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 594 |
| [[SPATA6]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MOK]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDV3]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ZNF800]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[GCNT4]] | -0.48 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SPON1-AS1]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[NACC2]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[RAPH1]] | -0.46 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[MICALL1]] | -0.46 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[LINC00393]] | -0.46 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[JADE3]] | -0.46 | -0.42 / -0.39 | both halves | 5e-05 |  |
| [[TLNRD1]] | -0.46 | -0.40 / -0.43 | both halves | 4e-05 |  |
| [[DUSP5-DT]] | -0.45 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[REEP3]] | -0.45 | -0.36 / -0.50 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2H1]] | B | DYNC2H1 activity raises TMEM67's level | lines that do not express DYNC2H1 (8) vs lines expressing it (42) | 3.47× lower at baseline in the lines without DYNC2H1 | 0.013 | ⚠ within organs, on part of the lines; also absent: FJX1, GIHCG, LINC02798 |
| [[HDAC6]] | B | HDAC6 activity lowers TMEM67's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 205]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-42.4, 21.3); signed map (-19.7, 4.9). **Vector** length 112, 30.0% of its response variance represented; |z| ≥ 3 in 1,179 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +5.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.3 | +5.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +3.3 | +5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | -0.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +2.4 |
|  | [[Arbutin (drug)]] 5 µM |  | +2.6 | +0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.5 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.1 | +0.7 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.9 | +0.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.1 | -9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -5.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.2 | -7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.9 | -6.8 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.4 | -5.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.2 | -5.9 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 67 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.1 — chr8:93,754,844-93,819,234 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC26979, JBTS6, NPHP11; previously MKS3 |
| Gene groups (HGNC) | MKS complex |
| Reactome | 4 pathways, smallest: Anchoring of the basal body to the plasma membrane; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5HYA8](https://www.uniprot.org/uniprotkb/Q5HYA8) (Meckelin):

> Required for ciliary structure and function. Part of the tectonic-like complex which is required for tissue-specific ciliogenesis and may regulate ciliary membrane composition (By similarity). Involved in centrosome migration to the apical cell surface during early ciliogenesis. Involved in the regulation of cilia length and appropriate number through the control of centrosome duplication. Is a key regulator of stereociliary bundle orientation (By similarity). Required for epithelial cell …

**Summary**, from NCBI Gene [91147](https://www.ncbi.nlm.nih.gov/gene/91147):

> The protein encoded by this gene localizes to the primary cilium and to the plasma membrane. The gene functions in centriole migration to the apical membrane and formation of the primary cilium. Multiple transcript variants encoding different isoforms have been found for this gene. Defects in this gene are a cause of Meckel syndrome type 3 (MKS3) and Joubert syndrome type 6 (JBTS6). [provided by RefSeq, Nov 2008]

**Accessions** — [HGNC:28396](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28396) · Entrez [91147](https://www.ncbi.nlm.nih.gov/gene/91147) · UniProt [Q5HYA8](https://www.uniprot.org/uniprotkb/Q5HYA8) · Ensembl [ENSG00000164953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164953)

## Data

Gene col 9042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9042); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9042]; `tensor/DDL_lfc|DDL_z.npy` [9042]; `embed/gene_vectors.npy` [9042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9042 or target_col == 9042). Every well: [[TMEM67 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM67.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
