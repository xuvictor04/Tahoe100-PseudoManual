---
symbol: "SRRT"
type: "gene"
col: 1482
ensembl_id: "ENSG00000087087"
name: "serrate, RNA effector molecule"
location: "7q22.1"
module: 157
arm: "+"
pooled_cpm: 55.46
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/157"]
generated_by: "tahoemap"
---

# SRRT

*serrate, RNA effector molecule* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.07× (z +28.5, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Carbidopa (monohydrate) (drug)]] 0.05 µM: 0.778× (z -4.5, q 0.003, down in 29 of 49 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Artesunate (drug)]] 0.5 µM: 0.804× (z -3.9, q 0.023, down in 22 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.0822×); [[MK-3903 (drug)]] 0.05 µM in 1 line (SW 1271 0.0514×); [[Dexamethasone (drug)]] 5 µM in 1 line (SW 1088 0.0896×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNRNPD]] (+0.64, fdr 7e-06), [[SNRNP70]] (+0.63, fdr 1e-05), [[AKT2]] (+0.60, fdr 1e-05); moves opposite to [[DHX32]] (-0.57, fdr 1e-05), [[MPLKIP]] (-0.55, fdr 2e-04), [[MTM1]] (-0.53, fdr 1e-05).
> It is in [[Module 157]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 21 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1482.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.07×** | +28.5 | 0e+00 | 48/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **5.75×** | +16.4 | 0e+00 | 48/49 (PANC-1, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +14.8 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **2.21×** | +14.2 | 2e-43 | 47/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.01×** | +11.5 | 1e-28 | 41/45 (PANC-1, SW480, …) | all doses, flat | composition shift; position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **3.29×** | +11.2 | 6e-27 | 43/48 (C32, SW48, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.83×** | +10.8 | 3e-25 | 36/48 (PANC-1, NCI-H460, …) | all doses, flat | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.84×** | +10.5 | 7e-24 | 42/48 (NCI-H460, PANC-1, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.69×** | +9.4 | 5e-19 | 44/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **1.70×** | +9.1 | 4e-18 | 32/43 (NCI-H460, NCI-H1573, …) | all doses, flat | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.63×** | +8.7 | 2e-16 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.58×** | +8.1 | 2e-14 | 32/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **1.57×** | +7.8 | 4e-13 | 36/47 (LoVo, PANC-1, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.53×** | +7.6 | 1e-12 | 34/48 (RKO, SW480, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +7.4 | 4e-12 | 34/48 (NCI-H2347, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.5 | 1e-06 | 28/48 (NCI-H460, A-172, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.4 | 2e-06 | 30/48 (PANC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +3.9 | 0.002 | 23/47 (SW48, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.015 | 17/48 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.015 | 9/48 (Hs 766T, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +3.3 | 0.016 | 11/49 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.20× | +3.2 | 0.023 | 11/48 (SNU-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.034 | 17/48 (PANC-1, SW480, …) | rises with dose |  |
| [[8-Hydroxyquinoline (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.053 | 11/48 (HT-29, PANC-1, …) | inconsistent across doses |  |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.18× | +2.8 | 0.087 | 13/48 (HCT15, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1482.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM in 1 line (CHP-212 0.0822×); [[MK-3903 (drug)]] 0.05 µM in 1 line (SW 1271 0.0514×); [[Dexamethasone (drug)]] 5 µM in 1 line (SW 1088 0.0896×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.778×** | -4.5 | 0.003 | 29/49 (CFPAC-1, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.804×** | -3.9 | 0.023 | 22/48 (HEC-1-A, HT-29, …) | rises with dose | position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.814×** | -3.7 | 0.037 | 21/48 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | 0.869× | -3.6 | 0.048 | 15/48 (SNU-1, A-427, …) | rises with dose | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | 0.842× | -3.1 | 0.20 | 12/48 (A-427, KATO III, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 5 µM | ⚠ unreliable plate only | 0.844× | -3.1 | 0.20 | 11/48 (AsPC-1, J82, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1482. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 40.6 | 14 (11 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +24.7) | — |
| [[PANC-1 (line)]] | alt | 45.6 | 12 (9 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.94× (z +20.6) | — |
| [[SW480 (line)]] | alt | 67.7 | 10 (7 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.53× (z +15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.25× (z +14.0) | — |
| [[SW48 (line)]] | wt | 84.3 | 7 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.6) | — |
| [[LoVo (line)]] | wt | 53.7 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +20.3) | — |
| [[NCI-H1573 (line)]] | alt | 37.6 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +18.1) | — |
| [[RKO (line)]] | wt | 72.3 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +16.9) | — |
| [[KATO III (line)]] | alt | 51.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 48.3 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +15.9) | — |
| [[LS 180 (line)]] | wt | 45.1 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.56× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 9.09× (z +10.1) | — |
| [[A-172 (line)]] | wt | 49.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +17.7) | — |
| [[A549 (line)]] | wt | 36.5 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +18.6) | — |
| [[C32 (line)]] | wt | 77.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.70× (z +20.9) | — |
| [[HEC-1-A (line)]] | alt | 50.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.00× (z +16.3) | — |
| [[J82 (line)]] | alt | 54.0 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +20.7) | — |
| [[SNU-1 (line)]] | wt | 67.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 51.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 39.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +16.8) | — |
| [[SW1417 (line)]] | alt | 60.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +13.6) | — |
| [[AsPC-1 (line)]] | alt | 47.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.2) | — |
| [[HOP62 (line)]] | alt | 42.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.95× (z +14.4) | — |
| [[Hs 766T (line)]] | wt | 42.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +13.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 62.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.0) | — |
| [[NCI-H2347 (line)]] | alt | 63.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +12.5) | — |
| [[Panc 03.27 (line)]] | alt | 42.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +13.3) | — |
| [[SHP-77 (line)]] | alt | 44.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +10.3) | — |
| [[SW 900 (line)]] | alt | 69.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +14.3) | — |
| [[A-427 (line)]] | wt | 59.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.41× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A498 (line)]] | wt | 95.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 53.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +11.8) | — |
| [[CHP-212 (line)]] | wt | 54.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0822× (z -11.3) |
| [[COLO 205 (line)]] | alt | 39.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +9.8) | — |
| [[H4 (line)]] | wt | 63.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.25× (z +16.4) | — |
| [[HepG2_C3A (line)]] | wt | 29.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.7) | — |
| [[HS-578T (line)]] | alt | 55.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 42.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +10.4) | — |
| [[NCI-H1792 (line)]] | alt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +15.2) | — |
| [[RPMI-7951 (line)]] | alt | 65.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +16.2) | — |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +15.2) | — |
| [[SW 1088 (line)]] | alt | 79.6 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.0896× (z -8.5) |
| [[SW 1271 (line)]] | alt | 47.8 | 0 | 1 | — | [[MK-3903 (drug)]] 0.05 µM 0.0514× (z -8.9) |
| [[AN3 CA (line)]] | alt | 102 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 77.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 95.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 70.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 68.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 79.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1482), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNRNPD]] | +0.64 | +0.66 / +0.58 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[SNRNP70]] | +0.63 | +0.77 / +0.57 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 627 |
| [[AKT2]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SCRIB]] | +0.59 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ARF3]] | +0.58 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[HNRNPM]] | +0.57 | +0.54 / +0.58 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 855 |
| [[TUBGCP6]] | +0.57 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[SF1]] | +0.56 | +0.47 / +0.59 | both halves | 2e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 927 |
| [[PRPF31]] | +0.56 | +0.49 / +0.53 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[SRSF1]] | +0.56 | +0.47 / +0.60 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions; STRING 634 |
| [[RMRP]] | +0.55 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[U2AF2]] | +0.55 | +0.56 / +0.61 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 758 |

## Genes that move opposite

*20 of its nearest partners move opposite, 4 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DHX32]] | -0.57 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[MPLKIP]] | -0.55 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[MTM1]] | -0.53 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[ADGRL3-AS1]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[RPL15]] | -0.49 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[RNF181]] | -0.49 | -0.24 / -0.56 | both halves | 5e-04 |  |
| [[GAN]] | -0.49 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[MID2]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[ATP6V1F]] | -0.48 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[NDUFA6]] | -0.46 | -0.24 / -0.54 | both halves | 5e-04 |  |
| [[KATNBL1]] | -0.46 | -0.41 / -0.49 | both halves | 4e-05 |  |
| [[EIF1B]] | -0.46 | -0.35 / -0.54 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 157]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.514). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-32.6, -5.7); signed map (-15.2, -26.8). **Vector** length 89.5, 25.9% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.7 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | +6.5 | +9.1 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.0 | +7.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +5.9 | +10.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.0 | +16.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.0 | +11.2 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +2.6 | +0.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.9 |
|  | [[Arbutin (drug)]] 0.5 µM |  | +2.4 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | +2.4 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -1.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.7 | -1.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -0.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -0.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.3 | -3.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.9 | +3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -1.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | serrate, RNA effector molecule |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,875,103-100,888,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Asr2, serrate, ARS2 |
| Reactome | 11 pathways, smallest: Nuclear RNA decay; RNA polymerase II transcribes snRNA genes; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXP5](https://www.uniprot.org/uniprotkb/Q9BXP5) (Serrate RNA effector molecule homolog):

> Acts as a mediator between the cap-binding complex (CBC) and the primary microRNAs (miRNAs) processing machinery during cell proliferation. Contributes to the stability and delivery of capped primary miRNA transcripts to the primary miRNA processing complex containing DGCR8 and DROSHA, thereby playing a role in RNA-mediated gene silencing (RNAi) by miRNAs. Binds capped RNAs (m7GpppG-capped RNA); however interaction is probably mediated via its interaction with NCBP1/CBP80 component of the CBC …

**Summary**, from NCBI Gene [51593](https://www.ncbi.nlm.nih.gov/gene/51593):

> Enables mRNA cap binding complex binding activity and protein-macromolecule adaptor activity. Involved in primary miRNA processing. Located in nucleoplasm. Part of ribonucleoprotein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24101) · Entrez [51593](https://www.ncbi.nlm.nih.gov/gene/51593) · UniProt [Q9BXP5](https://www.uniprot.org/uniprotkb/Q9BXP5) · Ensembl [ENSG00000087087](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000087087)

## Data

Gene col 1482: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1482); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1482, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1482]; `tensor/DDL_lfc|DDL_z.npy` [1482]; `embed/gene_vectors.npy` [1482]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1482 or target_col == 1482). Every well: [[SRRT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRRT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
