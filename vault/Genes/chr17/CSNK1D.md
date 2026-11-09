---
symbol: "CSNK1D"
type: "gene"
col: 6542
ensembl_id: "ENSG00000141551"
name: "casein kinase 1 delta"
location: "17q25.3"
module: 219
arm: "+"
pooled_cpm: 114.12
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/219"]
generated_by: "tahoemap"
---

# CSNK1D

*casein kinase 1 delta* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.57× (z +10.5, q 7e-23, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.600× (z -11.9, q 1e-29, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAFB]] (+0.62, fdr 1e-05), [[ZCCHC3]] (+0.61, fdr 4e-05), [[RPAP1]] (+0.60, fdr 2e-05); moves opposite to [[SCAI]] (-0.58, fdr 4e-05), [[USP3]] (-0.55, fdr 4e-05), [[STAM]] (-0.54, fdr 3e-05).
> It is in [[Module 219]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6542.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +10.5 | 7e-23 | 41/48 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +9.2 | 8e-18 | 29/48 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +7.0 | 6e-10 | 30/48 (MIA PaCa-2, COLO 205, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.75×** | +6.8 | 2e-09 | 36/49 (COLO 205, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.7 | 3e-09 | 30/48 (SNU-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.32×** | +6.5 | 9e-09 | 30/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.4 | 2e-08 | 32/48 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.28×** | +5.8 | 6e-07 | 31/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.29×** | +5.7 | 8e-07 | 29/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +5.1 | 2e-05 | 0/50 | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.22×** | +4.4 | 5e-04 | 24/48 (NCI-H23, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.1 | 0.002 | 20/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.8 | 0.005 | 19/48 (NCI-H1792, hTERT-HPNE, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.8 | 0.005 | 16/48 (Panc 03.27, SW1417, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.8 | 0.006 | 21/48 (Hs 766T, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.007 | 21/47 (RKO, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | 1.12× | +3.7 | 0.007 | 14/48 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Posaconazole (drug)]] 5 µM |  | 1.18× | +3.7 | 0.007 | 15/48 (MIA PaCa-2, NCI-H2347, …) | top dose only | plate-row cell shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.007 | 22/48 (A498, NCI-H1792, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6542.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.600×** | -11.9 | 1e-29 | 44/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -11.5 | 3e-28 | 43/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.630×** | -10.7 | 1e-24 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.667×** | -8.7 | 6e-16 | 33/45 (A549, SW48, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.666×** | -8.4 | 6e-15 | 39/49 (A549, COLO 205, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.698×** | -8.0 | 9e-14 | 29/44 (HCT15, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.743×** | -6.9 | 4e-10 | 35/48 (SK-MEL-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -4.8 | 9e-05 | 18/48 (C32, SW1417, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.865× | -4.8 | 1e-04 | 15/48 (A549, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.811×** | -4.7 | 2e-04 | 25/47 (SK-MEL-2, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.694×** | -4.4 | 5e-04 | 26/49 (PANC-1, SK-MEL-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.831×** | -4.3 | 8e-04 | 24/48 (C32, NCI-H23, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.834× | -4.2 | 0.001 | 20/48 (NCI-H23, NCI-H2030, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~46% of this change | 0.867× | -3.2 | 0.056 | 21/47 (RKO, HepG2/C3A, …) | top dose only |  |
| [[Radotinib (drug)]] 0.5 µM |  | 0.876× | -3.1 | 0.080 | 11/48 (Hs 766T, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6542. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 157 | 3 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.57× (z +11.2) | [[Panobinostat (drug)]] 5 µM 0.380× (z -17.1) |
| [[SK-MEL-2 (line)]] | alt | 153 | 1 | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.402× (z -11.8) |
| [[A498 (line)]] | wt | 108 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +21.6) | [[Panobinostat (drug)]] 5 µM 0.411× (z -13.7) |
| [[NCI-H23 (line)]] | alt | 163 | 0 | 5 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.454× (z -12.0) |
| [[A549 (line)]] | wt | 150 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.8) | [[Dinaciclib (drug)]] 0.05 µM 0.295× (z -15.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 96.5 | 2 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.98× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -12.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 188 | 2 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 2.10× (z +9.4) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.96× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.508× (z -8.7) |
| [[COLO 205 (line)]] | alt | 123 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 120 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.457× (z -10.9) |
| [[SNU-423 (line)]] | alt | 157 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.462× (z -9.3) |
| [[SW 900 (line)]] | alt | 112 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +9.0) | [[Belinostat (drug)]] 5 µM 0.450× (z -8.9) |
| [[SW480 (line)]] | alt | 128 | 2 | 1 | [[Digitoxin (drug)]] 0.5 µM 1.68× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.584× (z -9.0) |
| [[A-172 (line)]] | wt | 96.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.523× (z -9.1) |
| [[A-427 (line)]] | wt | 93.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.493× (z -9.2) |
| [[H4 (line)]] | wt | 117 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.271× (z -11.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 111 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.53× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.487× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HT-29 (line)]] | alt | 104 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.487× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 113 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.35× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 99.2 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 2.21× (z +8.7) | — |
| [[SNU-1 (line)]] | wt | 87.4 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.58× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 84.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -8.6) |
| [[C-33 A (line)]] | alt | 91.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -11.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 98.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 108 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.364× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 83.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.8) | — |
| [[J82 (line)]] | alt | 94.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 130 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.474× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 117 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.18× (z +8.5) | — |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.482× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 104 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.429× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 88.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +8.7) | — |
| [[SHP-77 (line)]] | alt | 119 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW 1088 (line)]] | alt | 94.5 | 0 | 1 | — | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM 0.0600× (z -10.0) |
| [[AN3 CA (line)]] | alt | 89.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 194 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 74.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 122 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 91.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 99.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 105 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6542), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAFB]] | +0.62 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ZCCHC3]] | +0.61 | +0.59 / +0.41 | both halves | 4e-05 |  |
| [[RPAP1]] | +0.60 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[REXO1]] | +0.60 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[MEPCE]] | +0.59 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[FEM1A]] | +0.59 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[EIF2B5]] | +0.58 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[KMT2B]] | +0.57 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[KDM6B]] | +0.57 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[ZC3H12A]] | +0.57 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[BCL9L]] | +0.57 | +0.46 / +0.57 | both halves | 2e-05 |  |
| [[WDR13]] | +0.56 | +0.50 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SCAI]] | -0.58 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[USP3]] | -0.55 | -0.55 / -0.42 | both halves | 4e-05 |  |
| [[STAM]] | -0.54 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[IER3IP1]] | -0.52 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[PRRC1]] | -0.51 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[COG5]] | -0.51 | -0.41 / -0.42 | both halves | 4e-05 | pathway: Asparagine N-linked glycosylation |
| [[CBX1]] | -0.50 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[USP48]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[SLC35A3]] | -0.50 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PPP1R2]] | -0.50 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[RAB18]] | -0.50 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[SERAC1]] | -0.50 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CSNK1D's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 219]]; 11 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.44; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.2, 7.3); signed map (4.9, -17.5). **Vector** length 120, 36.2% of its response variance represented; |z| ≥ 3 in 1,304 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Budesonide (drug)]] 0.5 µM |  | +5.4 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +5.3 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | +1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +1.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +4.5 | +0.8 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.7 | -11.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -3.3 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | -3.1 | -4.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.9 | -11.9 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.9 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.9 | -4.8 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -2.8 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | casein kinase 1 delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,239,023-82,273,700 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HCKID, CKID, CKIdelta |
| Gene groups (HGNC) | Casein kinase 1 family |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 32 pathways, smallest: Phosphorylation and nuclear translocation of the CRY:PER:kinase complex; The CRY:PER:kinase complex represses transactivation by the BMAL:CLOCK (ARNTL:CLOCK) complex; NAD+ and Sirtuins regulate the circadian clock |
| Matched by | ensembl_id |

**Function**, from UniProt [P48730](https://www.uniprot.org/uniprotkb/P48730) (Casein kinase I isoform delta):

> Essential serine/threonine-protein kinase that regulates diverse cellular growth and survival processes including Wnt signaling, DNA repair and circadian rhythms. It can phosphorylate a large number of proteins. Casein kinases are operationally defined by their preferential utilization of acidic proteins such as caseins as substrates. Phosphorylates connexin-43/GJA1, MAP1A, SNAPIN, MAPT/TAU, TOP2A, DCK, HIF1A, EIF6, p53/TP53, DVL2, DVL3, DNMT1, PKD2, RIPK3, YAP1, PER1 and PER2. Central …

**Summary**, from NCBI Gene [1453](https://www.ncbi.nlm.nih.gov/gene/1453):

> This gene is a member of the casein kinase I (CKI) gene family whose members have been implicated in the control of cytoplasmic and nuclear processes, including DNA replication and repair. The encoded protein may also be involved in the regulation of apoptosis, circadian rhythm, microtubule dynamics, chromosome segregation, and p53-mediated effects on growth. The encoded protein is highly similar to the mouse and rat CK1 delta homologs. Three transcript variants encoding different isoforms have …

**Accessions** — [HGNC:2452](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2452) · Entrez [1453](https://www.ncbi.nlm.nih.gov/gene/1453) · UniProt [P48730](https://www.uniprot.org/uniprotkb/P48730) · Ensembl [ENSG00000141551](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141551)

## Data

Gene col 6542: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6542); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6542, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6542]; `tensor/DDL_lfc|DDL_z.npy` [6542]; `embed/gene_vectors.npy` [6542]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6542 or target_col == 6542). Every well: [[CSNK1D — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CSNK1D.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
