---
symbol: "GABPB2"
type: "gene"
col: 6749
ensembl_id: "ENSG00000143458"
name: "GA binding protein transcription factor subunit beta 2"
location: "1q21.3"
module: 88
arm: "+"
pooled_cpm: 25.93
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 27
n_dd_up_clean: 15
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/088"]
generated_by: "tahoemap"
---

# GABPB2

*GA binding protein transcription factor subunit beta 2* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.56× (z +8.7, q 2e-15, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.326× (z -15.4, q 0e+00, down in 44 of 47 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPP3CB-AS1]] (+0.82, fdr 7e-06), [[KRCC1]] (+0.80, fdr 1e-05), [[RAB30-DT]] (+0.76, fdr 1e-05); moves opposite to [[AP1S1]] (-0.76, fdr 3e-05), [[IGSF8]] (-0.71, fdr 2e-05), [[YIF1B]] (-0.70, fdr 3e-04).
> It sits in the **+** arm of [[Module 088]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[IL1RAP]] → it (grade B ⚠); 5 go from it, the strongest it → [[SIRT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6749.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.56×** | +8.7 | 2e-15 | 26/46 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.72×** | +7.2 | 2e-10 | 19/32 (SW1417, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.50×** | +5.6 | 3e-06 | 26/43 (NCI-H2347, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +5.3 | 2e-05 | 25/46 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.45×** | +5.1 | 3e-05 | 27/47 (RKO, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.31×** | +5.1 | 3e-05 | 27/47 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +4.3 | 0.001 | 17/47 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +4.1 | 0.003 | 20/47 (NCI-H1792, PANC-1, …) | two highest doses |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.31×** | +3.8 | 0.011 | 16/47 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.027 | 16/46 (SK-MEL-2, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.027 | 13/46 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.031 | 12/47 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.036 | 16/46 (NCI-H2347, SW48, …) | top dose only |  |
| [[Meloxicam (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.040 | 8/47 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.081 | 9/47 (CFPAC-1, RPMI-7951, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.083 | 5/47 (SK-MEL-2, J82, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.083 | 8/47 (AsPC-1, HEC-1-A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6749.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.326×** | -15.4 | 0e+00 | 44/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.363×** | -14.0 | 8e-42 | 44/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.368×** | -13.8 | 7e-41 | 43/47 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.391×** | -12.9 | 5e-36 | 42/47 (LoVo, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.450×** | -11.0 | 5e-26 | 40/46 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.460×** | -10.7 | 1e-24 | 39/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.468×** | -10.4 | 1e-23 | 38/46 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.536×** | -8.6 | 6e-16 | 34/45 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.537×** | -8.5 | 9e-16 | 38/47 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.541×** | -8.1 | 3e-14 | 28/43 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.629×** | -6.4 | 1e-08 | 27/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.419×** | -6.3 | 2e-08 | 33/45 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -5.6 | 7e-07 | 27/47 (LoVo, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.666×** | -5.6 | 1e-06 | 25/46 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.677×** | -5.3 | 3e-06 | 27/47 (PANC-1, KATO III, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.692×** | -5.0 | 2e-05 | 22/47 (HT-29, KATO III, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.497×** | -5.0 | 2e-05 | 29/47 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.546×** | -4.4 | 4e-04 | 20/45 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6749. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 11 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.153× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.158× (z -17.8) |
| [[SW480 (line)]] | alt | 28.2 | 0 | 11 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -16.9) |
| [[LoVo (line)]] | wt | 49.1 | 0 | 9 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -16.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 49.7 | 0 | 8 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.255× (z -11.7) |
| [[HT-29 (line)]] | alt | 24.8 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -14.2) |
| [[COLO 205 (line)]] | alt | 42.4 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0315× (z -21.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.148× (z -12.1) |
| [[J82 (line)]] | alt | 32.5 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -11.5) |
| [[LS 180 (line)]] | wt | 35.7 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0938× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.219× (z -11.4) |
| [[HEC-1-A (line)]] | alt | 45.4 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.182× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -11.7) |
| [[NCI-H23 (line)]] | alt | 44.0 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +11.0) | [[Belinostat (drug)]] 5 µM 0.219× (z -13.0) |
| [[A-427 (line)]] | wt | 24.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +11.5) | [[AZD2858 (drug)]] 0.5 µM 0.0605× (z -13.8) ⚠ toxic |
| [[KATO III (line)]] | alt | 31.0 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.247× (z -10.6) |
| [[A-172 (line)]] | wt | 33.6 | 2 | 1 | [[Ixazomib citrate (drug)]] 5 µM 4.73× (z +10.8) | [[Panobinostat (drug)]] 0.5 µM 0.286× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 28.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.282× (z -9.0) |
| [[H4 (line)]] | wt | 25.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.162× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 31.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.173× (z -10.5) |
| [[HOP62 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 20.0 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.277× (z -8.6) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 18.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 7.96 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +9.9) | — |
| [[RKO (line)]] | wt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 19.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.93× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.81 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6749), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP3CB-AS1]] | +0.82 | +0.76 / +0.58 | both halves | 7e-06 |  |
| [[KRCC1]] | +0.80 | +0.83 / +0.55 | both halves | 1e-05 |  |
| [[RAB30-DT]] | +0.76 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | +0.76 | +0.74 / +0.56 | both halves | 1e-05 |  |
| [[CLHC1]] | +0.75 | +0.78 / +0.47 | both halves | 2e-05 |  |
| [[ZCWPW1]] | +0.75 | +0.73 / +0.51 | both halves | 1e-05 |  |
| [[ST7L]] | +0.74 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[INO80D]] | +0.73 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | +0.72 | +0.78 / +0.28 | both halves | 3e-04 |  |
| [[LINC00174]] | +0.72 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[NEPRO-AS1]] | +0.72 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[ATE1OSP]] | +0.71 | +0.76 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AP1S1]] | -0.76 | -0.77 / -0.45 | both halves | 3e-05 |  |
| [[IGSF8]] | -0.71 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[YIF1B]] | -0.70 | -0.66 / -0.27 | both halves | 3e-04 |  |
| [[TRAPPC1]] | -0.69 | -0.70 / -0.37 | both halves | 8e-05 |  |
| [[GMCL1]] | -0.69 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[GNA12]] | -0.68 | -0.69 / -0.36 | both halves | 1e-04 |  |
| [[PEDS1]] | -0.67 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[GNB2]] | -0.67 | -0.68 / -0.38 | both halves | 6e-05 |  |
| [[ST6GALNAC4]] | -0.66 | -0.61 / -0.34 | both halves | 1e-04 |  |
| [[BRK1]] | -0.65 | -0.68 / -0.50 | both halves | 1e-05 |  |
| [[ATRN]] | -0.65 | -0.62 / -0.39 | both halves | 5e-05 |  |
| [[LPCAT4]] | -0.64 | -0.67 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL1RAP]] | B | IL1RAP activity raises GABPB2's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without IL1RAP | 0.037 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[CCDC122]] | B | CCDC122 activity raises GABPB2's level | lines that do not express CCDC122 (5) vs lines expressing it (45) | 1.42× lower at baseline in the lines without CCDC122 | 0.060 | ⚠ within organs, on part of the lines; also absent: LACC1, SDC4, IL1RAP; its own permutation p |
| [[SIRT5]] | C | SIRT5's natural level strengthens GABPB2's drug response | SIRT5's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.66; direction not clear | 0.046 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIRT5]] | C | GABPB2's natural level strengthens SIRT5's drug response | GABPB2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.66; direction not clear | 0.047 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | GABPB2's natural level raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | GABPB2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.67 | 0.339 over the table, 0.028 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Fluvoxamine (drug)]] 0.5 µM | C | GABPB2's natural level lowers the cells' numbers under Fluvoxamine 0.5 µM (makes them more sensitive) | GABPB2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64 | 0.400 over the table, 0.052 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Clofarabine (drug)]] 0.5 µM | C | GABPB2's natural level lowers the cells' numbers under Clofarabine 0.5 µM (makes them more sensitive) | GABPB2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.500 over the table, 0.088 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Bendamustine (drug)]] 0.5 µM | C | GABPB2's natural level lowers the cells' numbers under Bendamustine 0.5 µM (makes them more sensitive) | GABPB2's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.58 | 0.507 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 088]]; 51 genes; this gene is in the **+** arm (projection on the module's main direction 0.842). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.46).
- **Nodal map** (x, y) = (4.6, 8.4); signed map (17.2, -24.7). **Vector** length 100, 26.2% of its response variance represented; |z| ≥ 3 in 1,257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +8.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +9.4 | +5.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +8.3 | +2.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.1 | +4.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +5.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +2.6 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.4 | +4.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -7.0 | -15.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -6.3 | -13.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -6.2 | -8.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.9 | -8.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.7 | -12.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.9 | -5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.6 | -3.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | -2.0 | -2.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | GA binding protein transcription factor subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:151,070,578-151,125,542 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC29891 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; GA binding protein transcription factor subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TAK5](https://www.uniprot.org/uniprotkb/Q8TAK5) (GA-binding protein subunit beta-2):

> May function as transcription factor capable of interacting with purine rich repeats (GA repeats).

**Summary**, from NCBI Gene [126626](https://www.ncbi.nlm.nih.gov/gene/126626):

> Enables transcription cis-regulatory region binding activity. Acts upstream of or within positive regulation of transcription by RNA polymerase II. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28441](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28441) · Entrez [126626](https://www.ncbi.nlm.nih.gov/gene/126626) · UniProt [Q8TAK5](https://www.uniprot.org/uniprotkb/Q8TAK5) · Ensembl [ENSG00000143458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143458)

## Data

Gene col 6749: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6749); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6749, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6749]; `tensor/DDL_lfc|DDL_z.npy` [6749]; `embed/gene_vectors.npy` [6749]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6749 or target_col == 6749). Every well: [[GABPB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GABPB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
