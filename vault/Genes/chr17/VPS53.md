---
symbol: "VPS53"
type: "gene"
col: 6496
ensembl_id: "ENSG00000141252"
name: "VPS53 subunit of GARP complex"
location: "17p13.3"
module: 52
arm: "+"
pooled_cpm: 159.91
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# VPS53

*VPS53 subunit of GARP complex* — 17p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.43× (z +23.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.665× (z -10.2, q 1e-21, down in 32 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 0.5 µM: 0.688× (z -9.7, q 1e-19, down in 43 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SENP5]] (+0.75, fdr 7e-06), [[MROH1]] (+0.70, fdr 7e-06), [[VTI1A]] (+0.69, fdr 7e-06); moves opposite to [[ZSCAN12]] (-0.60, fdr 1e-05), [[SUGT1P3]] (-0.59, fdr 1e-05), [[PNRC2]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6496.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.43×** | +23.0 | 0e+00 | 48/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.17×** | +20.2 | 0e+00 | 48/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.08×** | +19.0 | 0e+00 | 48/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.82×** | +15.6 | 0e+00 | 46/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.87×** | +14.2 | 9e-44 | 47/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +13.9 | 4e-42 | 38/49 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +13.6 | 3e-40 | 45/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.54×** | +11.2 | 4e-27 | 41/48 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.47×** | +10.0 | 1e-21 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.05×** | +8.7 | 2e-16 | 40/49 (HEC-1-A, SHP-77, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +8.4 | 2e-15 | 37/48 (HOP62, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +7.8 | 2e-13 | 35/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +7.6 | 1e-12 | 26/48 (HOP62, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.48×** | +7.2 | 2e-11 | 39/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.31×** | +7.0 | 1e-10 | 29/48 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +6.8 | 5e-10 | 30/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6496.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -10.2 | 1e-21 | 32/44 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.688×** | -9.7 | 1e-19 | 43/49 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.707×** | -9.0 | 6e-17 | 37/49 (RKO, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.797×** | -8.3 | 1e-14 | 32/48 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.740×** | -7.2 | 6e-11 | 35/45 (A-427, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.811×** | -5.2 | 2e-05 | 26/48 (AsPC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.868× | -5.2 | 2e-05 | 18/48 (J82, C32, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.828×** | -4.9 | 8e-05 | 24/48 (A498, HS-578T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | 0.841× | -4.5 | 5e-04 | 23/48 (PANC-1, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.785×** | -4.5 | 5e-04 | 23/47 (SW48, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.847× | -4.3 | 9e-04 | 18/48 (NCI-H460, AsPC-1, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | 0.853× | -4.1 | 0.002 | 17/48 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.857× | -3.7 | 0.010 | 18/47 (A549, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.820×** | -3.7 | 0.010 | 19/48 (A-427, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.871× | -3.6 | 0.014 | 10/47 (SW1417, A498, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.828×** | -3.5 | 0.018 | 21/48 (SW 1271, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Flutamide (drug)]] 5 µM |  | 0.888× | -3.1 | 0.062 | 4/48 (BT-474, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6496. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 224 | 10 (2 ⚠) | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +20.0) | [[Dinaciclib (drug)]] 5 µM 0.522× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.612× (z -8.8) |
| [[NCI-H460 (line)]] | wt | 171 | 12 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +17.1) | — |
| [[HOP62 (line)]] | alt | 106 | 11 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.34× (z +20.0) | — |
| [[C32 (line)]] | wt | 164 | 3 (1 ⚠) | 6 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.06× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -14.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 211 | 7 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.78× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.418× (z -12.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 156 | 7 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.47× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.440× (z -12.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 173 | 8 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.75× (z +15.8) | — |
| [[A-172 (line)]] | wt | 183 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.45× (z +13.3) | — |
| [[LS 180 (line)]] | wt | 184 | 6 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 82.0 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +14.4) | — |
| [[PANC-1 (line)]] | alt | 113 | 7 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.96× (z +17.7) | — |
| [[A-427 (line)]] | wt | 80.8 | 4 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.86× (z +13.7) | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -13.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 169 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 116 | 6 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.56× (z +11.6) | — |
| [[J82 (line)]] | alt | 292 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.418× (z -13.4) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 133 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 95.9 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.48× (z +12.2) | — |
| [[RKO (line)]] | wt | 214 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.15× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -28.3) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 124 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 2.78× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 81.0 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 173 | 1 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +9.4) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 200 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.69× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.542× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 304 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -14.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 178 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +13.7) | [[Harringtonine (drug)]] 0.5 µM 0.517× (z -8.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[LOX-IMVI (line)]] | wt | 103 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.27× (z +15.5) | — |
| [[NCI-H2347 (line)]] | alt | 74.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +11.9) | — |
| [[SW48 (line)]] | wt | 143 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.25× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 120 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.61× (z +12.6) | — |
| [[C-33 A (line)]] | alt | 128 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.40× (z +13.9) | — |
| [[LoVo (line)]] | wt | 175 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.456× (z -12.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 97.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 155 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.96× (z +11.9) | [[Dinaciclib (drug)]] 0.05 µM 0.326× (z -11.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 255 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.13× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.514× (z -9.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 209 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.443× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 195 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 2.61× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 128 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.27× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 148 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.00× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.498× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 152 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.44× (z +9.3) | — |
| [[KATO III (line)]] | alt | 178 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.06× (z +9.1) | — |
| [[RPMI-7951 (line)]] | alt | 150 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.09× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 113 | 1 | 1 (1 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 1.57× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.622× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 132 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 173 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 186 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6496), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SENP5]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[MROH1]] | +0.70 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[VTI1A]] | +0.69 | +0.59 / +0.68 | both halves | 7e-06 | pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 764 |
| [[DRD4]] | +0.68 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[XPNPEP3]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ZCCHC17]] | +0.66 | +0.57 / +0.69 | both halves | 8e-06 |  |
| [[GAK]] | +0.66 | +0.57 / +0.67 | both halves | 9e-06 |  |
| [[GDAP2]] | +0.65 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[CTDP1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[HIRA]] | +0.64 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[DPP9]] | +0.64 | +0.50 / +0.71 | both halves | 1e-05 |  |
| [[DHDDS]] | +0.64 | +0.61 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSCAN12]] | -0.60 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[SUGT1P3]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[PNRC2]] | -0.57 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[ISOC1]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[CLK4]] | -0.57 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[CX3CL1]] | -0.57 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[VEZF1]] | -0.57 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[TBL1XR1]] | -0.57 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[POGZ]] | -0.56 | -0.40 / -0.62 | both halves | 4e-05 |  |
| [[ZNF608]] | -0.56 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[BMI1]] | -0.56 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[BCL3]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers VPS53's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-14.1, -2.8); signed map (-46.7, 2.9). **Vector** length 122, 44.1% of its response variance represented; |z| ≥ 3 in 1,526 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.8 | +13.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +8.2 | +14.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.7 | +15.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.2 | +11.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +5.3 | +8.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | +7.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.2 | +7.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.5 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -12.6 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -11.9 | -8.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -10.1 | -9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.0 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | -8.2 | -4.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -4.3 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | VPS53 subunit of GARP complex |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.3 — chr17:508,503-721,717 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10979, HCCS1 |
| Gene groups (HGNC) | Endosome-associated recycling protein (EARP) complex; Golgi associated retrograde protein (GARP) complex |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VIR6](https://www.uniprot.org/uniprotkb/Q5VIR6) (Vacuolar protein sorting-associated protein 53 homolog):

> Acts as a component of the GARP complex that is involved in retrograde transport from early and late endosomes to the trans-Golgi network (TGN). The GARP complex is required for the maintenance of the cycling of mannose 6-phosphate receptors between the TGN and endosomes, this cycling is necessary for proper lysosomal sorting of acid hydrolases such as CTSD. Acts as a component of the EARP complex that is involved in endocytic recycling. The EARP complex associates with Rab4-positive endosomes …

**Summary**, from NCBI Gene [55275](https://www.ncbi.nlm.nih.gov/gene/55275):

> Involved in endocytic recycling and retrograde transport, endosome to Golgi. Acts upstream of or within lysosomal transport. Located in several cellular components, including Golgi apparatus; perinuclear region of cytoplasm; and recycling endosome. Part of EARP complex and GARP complex. Implicated in pontocerebellar hypoplasia type 2E. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25608](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25608) · Entrez [55275](https://www.ncbi.nlm.nih.gov/gene/55275) · UniProt [Q5VIR6](https://www.uniprot.org/uniprotkb/Q5VIR6) · Ensembl [ENSG00000141252](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141252)

## Data

Gene col 6496: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6496); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6496, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6496]; `tensor/DDL_lfc|DDL_z.npy` [6496]; `embed/gene_vectors.npy` [6496]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6496 or target_col == 6496). Every well: [[VPS53 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS53.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
