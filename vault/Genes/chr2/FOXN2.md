---
symbol: "FOXN2"
type: "gene"
col: 10007
ensembl_id: "ENSG00000170802"
name: "forkhead box N2"
location: "2p16.3"
module: 98
arm: "+"
pooled_cpm: 92.94
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 6
n_dd_up_clean: 13
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# FOXN2

*forkhead box N2* — 2p16.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.99× (z +18.5, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.427× (z -18.0, q 0e+00, down in 41 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.743× (z -6.5, q 1e-08, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PANX1]] (+0.62, fdr 7e-06), [[B3GNT5]] (+0.59, fdr 7e-06), [[GJB2]] (+0.56, fdr 1e-05); moves opposite to [[HDAC6]] (-0.51, fdr 3e-05), [[SEPTIN2]] (-0.44, fdr 1e-04), [[TCTN2]] (-0.44, fdr 8e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LAMA3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.99×** | +18.5 | 0e+00 | 48/49 (A-427, SW480, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.75×** | +17.5 | 0e+00 | 37/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.96×** | +14.8 | 0e+00 | 41/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.74×** | +11.8 | 6e-30 | 39/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +11.8 | 6e-30 | 40/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +11.0 | 3e-26 | 37/48 (RKO, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.55×** | +9.6 | 4e-20 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.50×** | +9.0 | 2e-17 | 31/48 (SNU-1, RKO, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +8.7 | 2e-16 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +6.9 | 4e-10 | 31/47 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +6.6 | 2e-09 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +6.4 | 5e-09 | 24/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.31×** | +6.0 | 1e-07 | 27/48 (HT-29, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.9 | 3e-05 | 25/48 (HT-29, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.20×** | +4.0 | 0.002 | 19/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.005 | 21/48 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.12× | +3.6 | 0.010 | 12/49 (MIA PaCa-2, SNU-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.032 | 16/48 (BT-474, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.065 | 17/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10007.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.427×** | -18.0 | 0e+00 | 41/44 (NCI-H2347, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.549×** | -13.2 | 2e-37 | 42/49 (A-427, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.743×** | -6.5 | 1e-08 | 31/48 (AsPC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.792×** | -5.1 | 4e-05 | 25/48 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.807×** | -4.7 | 3e-04 | 25/47 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.814×** | -4.4 | 0.001 | 18/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.843× | -3.8 | 0.014 | 17/49 (HOP62, BT-474, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.886× | -3.6 | 0.019 | 12/49 (HEC-1-A, MIA PaCa-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 67.8 | 6 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +25.0) | [[Dinaciclib (drug)]] 5 µM 0.312× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 116 | 6 | 1 (1 ⚠) | [[Budesonide (drug)]] 5 µM 2.80× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.390× (z -8.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 144 | 3 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.79× (z +12.9) | [[Adagrasib (drug)]] 0.05 µM 0.596× (z -17.0) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 76.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.34× (z +20.0) | — |
| [[PANC-1 (line)]] | alt | 75.2 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +12.9) | — |
| [[AsPC-1 (line)]] | alt | 258 | 2 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.93× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.02× (z +9.8) | [[Panobinostat (drug)]] 5 µM 0.289× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 89.5 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.208× (z -19.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 176 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +11.5) | [[Selinexor (drug)]] 5 µM 0.537× (z -11.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 131 | 5 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.51× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.108× (z -19.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 93.8 | 5 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.66× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.522× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 138 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 13.0× (z +18.7) | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -15.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 52.4 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 70.5 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.97× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -20.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 68.2 | 3 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.63× (z +24.5) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 81.8 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.56× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.404× (z -11.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 87.2 | 2 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.1× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.320× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.409× (z -9.4) |
| [[H4 (line)]] | wt | 61.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 107 | 2 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 10.5× (z +11.3) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 135 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 3.95× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.396× (z -11.3) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 66.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +11.7) | [[Docetaxel (drug)]] 0.05 µM 0.298× (z -11.0) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 90.0 | 3 | 0 | [[PH-797804 (drug)]] 5 µM 7.12× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 117 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +20.8) | — |
| [[SK-MEL-2 (line)]] | alt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +17.6) | — |
| [[SW1417 (line)]] | alt | 138 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.99× (z +11.6) | [[Dinaciclib (drug)]] 5 µM 0.435× (z -11.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 61.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.340× (z -11.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 98.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 34.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +12.1) | — |
| [[KATO III (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.297× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.421× (z -9.1) |
| [[LS 180 (line)]] | wt | 88.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -14.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 75.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.81× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.366× (z -9.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 83.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +17.4) | — |
| [[SHP-77 (line)]] | alt | 69.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.1) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 62.4 | 0 | 2 | — | [[Cinacalcet (drug)]] 0.05 µM 0.0800× (z -9.2) |
| [[SW 900 (line)]] | alt | 65.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -11.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -13.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 81.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +15.1) | — |
| [[J82 (line)]] | alt | 53.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +15.8) | — |
| [[LoVo (line)]] | wt | 108 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.5) |
| [[NCI-H1573 (line)]] | alt | 65.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.359× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.158× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 37.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 68.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 110 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PANX1]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[B3GNT5]] | +0.59 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GJB2]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[MAFB]] | +0.54 | +0.39 / +0.53 | both halves | 5e-05 |  |
| [[GJB3]] | +0.53 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FOXQ1]] | +0.52 | +0.46 / +0.45 | both halves | 3e-05 | same gene group |
| [[BLOC1S4]] | +0.52 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[SLC22A3]] | +0.52 | +0.38 / +0.51 | both halves | 7e-05 |  |
| [[ZFP36L2]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[SGMS2]] | +0.51 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[MT1M]] | +0.50 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[ADO]] | +0.50 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HDAC6]] | -0.51 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SEPTIN2]] | -0.44 | -0.32 / -0.41 | both halves | 1e-04 |  |
| [[TCTN2]] | -0.44 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[EEF1AKMT2]] | -0.44 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[RANBP10]] | -0.43 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[PFDN5]] | -0.42 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[GPR107]] | -0.42 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[COPG1]] | -0.42 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[OS9]] | -0.42 | -0.31 / -0.41 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMA3]] | B | LAMA3 activity weakens FOXN2's drug response | lines that do not express LAMA3 (22) vs lines expressing it (27) | the lines without LAMA3 respond 1.27× as strongly (z diff -1.56); strongest at Homoharringtonine 5 µM: 2.33x vs 1.33x (z diff -4.2) | 0.049 | ⚠ within organs, on part of the lines; also absent: P2RY2, ELF3, MYO5B; target measured in part of the lines; artifact flags |
| [[SLC22A3]] | B | SLC22A3 activity weakens FOXN2's drug response | lines that do not express SLC22A3 (30) vs lines expressing it (19) | the lines without SLC22A3 respond 1.33× as strongly (z diff -1.67); strongest at Homoharringtonine 0.5 µM: 2.42x vs 1.36x (z diff -4.5) | 0.069 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA; target measured in part of the lines; artifact flags |
| [[CEACAM1]] | B | CEACAM1 activity weakens FOXN2's drug response | lines that do not express CEACAM1 (27) vs lines expressing it (22) | the lines without CEACAM1 respond 1.33× as strongly (z diff -1.37); strongest at Homoharringtonine 5 µM: 2.08x vs 1.35x (z diff -4.3) | 0.073 | ⚠ within organs, on part of the lines; also absent: TOX3, FOXQ1, TRIM29; target measured in part of the lines; artifact flags |
| [[FSTL3]] | B | FSTL3 activity raises FOXN2's level | lines that do not express FSTL3 (7) vs lines expressing it (43) | 1.25× lower at baseline in the lines without FSTL3 | 0.088 | ⚠ within organs, on part of the lines; also absent: PDLIM2, TAGLN2, CCND1 |
| [[FOXQ1]] | B | FOXQ1 activity weakens FOXN2's drug response | lines that do not express FOXQ1 (30) vs lines expressing it (19) | the lines without FOXQ1 respond 1.39× as strongly (z diff -1.71); strongest at Homoharringtonine 0.5 µM: 2.36x vs 1.42x (z diff -4.4) | 0.091 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TTC22, COL17A1; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.581). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.3, 39.5); signed map (16.4, 33.1). **Vector** length 110, 33.0% of its response variance represented; |z| ≥ 3 in 1,436 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.5 | +2.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +18.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.0 | +9.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.9 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | +1.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.7 | +1.4 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.3 | +11.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.3 | -6.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.4 | -0.0 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.3 | -0.2 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -2.1 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box N2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.3 — chr2:48,314,637-48,379,295 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HTLF |
| Gene groups (HGNC) | Forkhead boxes |
| Matched by | ensembl_id |

**Function**, from UniProt [P32314](https://www.uniprot.org/uniprotkb/P32314) (Forkhead box protein N2):

> Binds to the purine-rich region in HTLV-I LTR.

**Summary**, from NCBI Gene [3344](https://www.ncbi.nlm.nih.gov/gene/3344):

> This gene encodes a forkhead domain binding protein and may function in the transcriptional regulation of the human T-cell leukemia virus long terminal repeat. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:5281](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5281) · Entrez [3344](https://www.ncbi.nlm.nih.gov/gene/3344) · UniProt [P32314](https://www.uniprot.org/uniprotkb/P32314) · Ensembl [ENSG00000170802](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170802)

## Data

Gene col 10007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10007); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10007]; `tensor/DDL_lfc|DDL_z.npy` [10007]; `embed/gene_vectors.npy` [10007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10007 or target_col == 10007). Every well: [[FOXN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
