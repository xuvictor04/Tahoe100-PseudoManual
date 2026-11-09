---
symbol: "ANKRD26"
type: "gene"
col: 2895
ensembl_id: "ENSG00000107890"
name: "ankyrin repeat domain 26"
location: "10p12.1"
module: 28
arm: "+"
pooled_cpm: 95.95
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# ANKRD26

*ankyrin repeat domain 26* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.59× (z +11.9, q 9e-30, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.474× (z -13.4, q 6e-38, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZC3H6]] (+0.77, fdr 7e-06), [[ZNF638]] (+0.70, fdr 7e-06), [[TRMT1L]] (+0.70, fdr 7e-06); moves opposite to [[TPST2]] (-0.67, fdr 2e-05), [[FBXW2]] (-0.67, fdr 1e-05), [[ABHD17A]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2895.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.59×** | +11.9 | 9e-30 | 42/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.6 | 9e-12 | 32/49 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.1 | 2e-10 | 36/48 (A498, HS-578T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.46×** | +6.6 | 7e-09 | 33/48 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +5.5 | 5e-06 | 36/50 (RKO, LS 180, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.29×** | +4.7 | 3e-04 | 25/48 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.20× | +4.6 | 3e-04 | 21/48 (SW1417, RKO, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.27×** | +4.3 | 0.001 | 30/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.003 | 26/48 (KATO III, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.012 | 14/49 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.014 | 24/49 (RPMI-7951, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.016 | 23/48 (KATO III, LS 180, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.18× | +3.3 | 0.044 | 17/49 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.044 | 23/48 (C-33 A, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 1.19× | +3.2 | 0.044 | 20/48 (A-172, KATO III, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.044 | 21/48 (A549, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2895.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.474×** | -13.4 | 6e-38 | 46/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.498×** | -12.5 | 4e-33 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.523×** | -11.6 | 9e-29 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.554×** | -10.5 | 7e-24 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.423×** | -8.0 | 1e-13 | 40/48 (MIA PaCa-2, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -7.2 | 7e-11 | 40/48 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.661×** | -7.1 | 1e-10 | 34/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -6.9 | 3e-10 | 37/49 (A-427, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.698×** | -6.0 | 1e-07 | 31/48 (C-33 A, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.800×** | -5.6 | 1e-06 | 28/49 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.776×** | -4.5 | 4e-04 | 26/48 (SW480, KATO III, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.635×** | -4.2 | 0.001 | 20/38 (hTERT-HPNE, A549, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.764×** | -4.2 | 0.001 | 25/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.795×** | -4.1 | 0.002 | 32/48 (MIA PaCa-2, AN3 CA, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.930× | -4.0 | 0.003 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.786×** | -3.8 | 0.006 | 24/47 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[NVP-BHG712 (drug)]] 0.05 µM |  | **0.830×** | -3.1 | 0.053 | 12/48 (NCI-H2030, SHP-77, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.843× | -3.0 | 0.068 | 17/48 (NCI-H2030, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2895. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 150 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.417× (z -12.5) |
| [[SW480 (line)]] | alt | 118 | 2 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +13.9) | [[Digitoxin (drug)]] 0.5 µM 0.255× (z -18.4) |
| [[PANC-1 (line)]] | alt | 78.5 | 1 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.2) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.286× (z -15.3) |
| [[J82 (line)]] | alt | 110 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.314× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 108 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +15.2) | [[Digitoxin (drug)]] 0.5 µM 0.347× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 157 | 0 | 5 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.366× (z -11.9) |
| [[NCI-H23 (line)]] | alt | 125 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +11.5) | [[Digitoxin (drug)]] 0.5 µM 0.336× (z -14.4) |
| [[HOP62 (line)]] | alt | 108 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.382× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.445× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 102 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +10.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.496× (z -9.1) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.528× (z -8.7) |
| [[SNU-423 (line)]] | alt | 110 | 2 | 2 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.8) | [[Digitoxin (drug)]] 5 µM 0.471× (z -9.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 138 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.364× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 91.1 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +15.1) | [[Digitoxin (drug)]] 0.5 µM 0.357× (z -8.7) |
| [[HS-578T (line)]] | alt | 58.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +13.3) | — |
| [[HT-29 (line)]] | alt | 67.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.317× (z -11.4) |
| [[LoVo (line)]] | wt | 86.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +19.4) | — |
| [[RKO (line)]] | wt | 113 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -8.7) ⚠ toxic |
| [[AsPC-1 (line)]] | alt | 35.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +23.2) | — |
| [[BT-474 (line)]] | alt | 74.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +12.1) | — |
| [[hTERT-HPNE (line)]] | wt | 84.7 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.356× (z -9.3) |
| [[KATO III (line)]] | alt | 72.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.425× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 119 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +16.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.415× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 119 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +9.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.387× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 33.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +12.9) | — |
| [[SHP-77 (line)]] | alt | 91.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 94.3 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +10.7) | — |
| [[CFPAC-1 (line)]] | alt | 73.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.83× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 58.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.230× (z -12.2) |
| [[LS 180 (line)]] | wt | 69.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 60.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 135 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 83.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.1) | — |
| [[SW 1271 (line)]] | alt | 140 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.207× (z -8.6) |
| [[SW 900 (line)]] | alt | 80.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.6) | — |
| [[A-172 (line)]] | wt | 145 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 129 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 156 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 48.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 69.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 168 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 69.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 87.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 77.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2895), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H6]] | +0.77 | +0.80 / +0.68 | both halves | 7e-06 |  |
| [[ZNF638]] | +0.70 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TRMT1L]] | +0.70 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.69 | +0.77 / +0.52 | both halves | 1e-05 |  |
| [[LRRC37A2]] | +0.69 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[DZIP3]] | +0.68 | +0.82 / +0.50 | both halves | 1e-05 |  |
| [[C1orf131]] | +0.68 | +0.77 / +0.56 | both halves | 1e-05 |  |
| [[ZNF518A]] | +0.68 | +0.73 / +0.48 | both halves | 2e-05 |  |
| [[ZNF429]] | +0.68 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[BPTF]] | +0.67 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[RSF1]] | +0.67 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[TCEAL4]] | +0.67 | +0.76 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST2]] | -0.67 | -0.73 / -0.48 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.67 | -0.71 / -0.51 | both halves | 1e-05 |  |
| [[ABHD17A]] | -0.66 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[TBC1D24]] | -0.65 | -0.66 / -0.36 | both halves | 9e-05 |  |
| [[USB1]] | -0.65 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[CPSF4]] | -0.64 | -0.70 / -0.40 | both halves | 5e-05 |  |
| [[ST6GALNAC4]] | -0.64 | -0.70 / -0.38 | both halves | 6e-05 |  |
| [[PACC1]] | -0.64 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[ST6GALNAC6]] | -0.63 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[INTS11]] | -0.63 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[TRABD]] | -0.63 | -0.71 / -0.36 | both halves | 1e-04 |  |
| [[SDHAP4]] | -0.62 | -0.70 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANKRD26's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.669). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-25.3, 7.5); signed map (6.0, -16.3). **Vector** length 106, 34.9% of its response variance represented; |z| ≥ 3 in 1,202 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.7 | +11.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.4 | +6.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.3 | +4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +3.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.2 | +4.3 |
|  | [[Glycyrrhizic acid (drug)]] 5 µM |  | +1.8 | +1.5 |
|  | [[γ-Oryzanol (drug)]] 0.05 µM |  | +1.7 | +1.9 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +1.7 | +3.7 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -5.9 | +3.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | +1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | -5.3 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.9 | -3.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.6 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat domain 26 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:26,973,793-27,100,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1074; previously THC2 |
| Gene groups (HGNC) | N-Ank proteins |
| Reactome | 6 pathways, smallest: RND1 GTPase cycle; RND2 GTPase cycle; RND3 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPS8](https://www.uniprot.org/uniprotkb/Q9UPS8) (Ankyrin repeat domain-containing protein 26):

> Acts as a regulator of adipogenesis. Involved in the regulation of the feeding behavior.

**Summary**, from NCBI Gene [22852](https://www.ncbi.nlm.nih.gov/gene/22852):

> This gene encodes a protein containing N-terminal ankyrin repeats which function in protein-protein interactions. Mutations in this gene are associated with autosomal dominant thrombocytopenia-2. Pseudogenes of this gene are found on chromosome 7, 10, 13 and 16. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:29186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29186) · Entrez [22852](https://www.ncbi.nlm.nih.gov/gene/22852) · UniProt [Q9UPS8](https://www.uniprot.org/uniprotkb/Q9UPS8) · Ensembl [ENSG00000107890](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107890)

## Data

Gene col 2895: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2895); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2895, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2895]; `tensor/DDL_lfc|DDL_z.npy` [2895]; `embed/gene_vectors.npy` [2895]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2895 or target_col == 2895). Every well: [[ANKRD26 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANKRD26.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
