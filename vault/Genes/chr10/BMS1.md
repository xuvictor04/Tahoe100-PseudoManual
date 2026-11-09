---
symbol: "BMS1"
type: "gene"
col: 9179
ensembl_id: "ENSG00000165733"
name: "BMS1 ribosome biogenesis factor"
location: "10q11.21"
module: 1
arm: "+"
pooled_cpm: 89.11
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 18
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# BMS1

*BMS1 ribosome biogenesis factor* — 10q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.33× (z +25.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.609× (z -14.9, q 0e+00, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX1]] (+0.80, fdr 7e-06), [[SF3A3]] (+0.79, fdr 7e-06), [[RBM28]] (+0.77, fdr 7e-06); moves opposite to [[HIGD2A]] (-0.63, fdr 1e-05), [[GPBP1L1]] (-0.61, fdr 1e-05), [[PDE6D]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.33×** | +25.3 | 0e+00 | 48/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.71×** | +21.0 | 0e+00 | 48/48 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.02×** | +15.4 | 0e+00 | 47/49 (SW480, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.05×** | +14.6 | 0e+00 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.76×** | +11.9 | 7e-31 | 46/48 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +10.9 | 2e-25 | 44/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.64×** | +10.5 | 1e-23 | 41/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +10.3 | 5e-23 | 43/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.48×** | +8.3 | 5e-15 | 41/48 (SW480, SHP-77, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +7.8 | 2e-13 | 42/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +7.1 | 6e-11 | 36/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +6.8 | 5e-10 | 37/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.35×** | +6.3 | 1e-08 | 31/48 (LoVo, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.33×** | +6.1 | 6e-08 | 34/48 (SW480, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.27×** | +5.1 | 1e-05 | 28/48 (SW480, BT-474, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +5.0 | 2e-05 | 31/48 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +4.7 | 9e-05 | 28/47 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.43×** | +3.9 | 0.002 | 24/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.005 | 23/48 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.008 | 20/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.609×** | -14.9 | 0e+00 | 45/49 (RKO, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.753×** | -5.8 | 2e-06 | 30/48 (H4, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | **0.765×** | -5.7 | 3e-06 | 31/48 (SW48, NCI-H460, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.724×** | -4.9 | 1e-04 | 33/48 (MIA PaCa-2, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.006 | 23/48 (H4, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.826×** | -3.9 | 0.008 | 25/50 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | 0.837× | -3.8 | 0.012 | 19/48 (hTERT-HPNE, SW480, …) | inconsistent across doses | position effect removed |
| [[Rapamycin (drug)]] 5 µM |  | 0.897× | -3.3 | 0.073 | 6/48 (AsPC-1, LoVo, …) | inconsistent across doses | position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | 0.867× | -3.0 | 0.15 | 15/48 (HepG2/C3A, NCI-H1792, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 0.821× | -3.0 | 0.15 | 19/48 (SNU-423, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 97.7 | 9 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 0.05 µM 2.71× (z +12.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -13.8) |
| [[PANC-1 (line)]] | alt | 102 | 9 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +23.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -10.5) |
| [[LoVo (line)]] | wt | 99.6 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +14.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 64.6 | 6 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +17.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -11.3) |
| [[NCI-H460 (line)]] | wt | 93.3 | 7 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +16.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -9.5) |
| [[SW480 (line)]] | alt | 131 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.2) | — |
| [[A-427 (line)]] | wt | 86.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +15.2) | — |
| [[HOP62 (line)]] | alt | 76.8 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +16.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.510× (z -11.7) |
| [[HT-29 (line)]] | alt | 58.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +19.2) | — |
| [[LS 180 (line)]] | wt | 98.4 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.4) | — |
| [[RKO (line)]] | wt | 153 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.25× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -20.3) |
| [[H4 (line)]] | wt | 93.2 | 2 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.22× (z +12.3) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 83.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +18.6) | — |
| [[NCI-H1792 (line)]] | alt | 65.1 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 106 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +14.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.7) |
| [[Panc 03.27 (line)]] | alt | 82.3 | 4 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.10× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.444× (z -12.8) |
| [[SW1417 (line)]] | alt | 75.1 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +14.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.484× (z -11.1) |
| [[A-172 (line)]] | wt | 47.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.64× (z +18.8) | — |
| [[COLO 205 (line)]] | alt | 67.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.1) | — |
| [[Hs 766T (line)]] | wt | 71.5 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 44.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) | — |
| [[SW 900 (line)]] | alt | 101 | 2 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.1) |
| [[A498 (line)]] | wt | 113 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -16.1) |
| [[CFPAC-1 (line)]] | alt | 90.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +18.3) | — |
| [[J82 (line)]] | alt | 93.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +15.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.626× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 100 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 5.70× (z +10.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 76.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +14.9) | — |
| [[SHP-77 (line)]] | alt | 113 | 2 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 99.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +10.4) | — |
| [[SNU-423 (line)]] | alt | 84.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.2) |
| [[A549 (line)]] | wt | 91.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +17.2) | — |
| [[C32 (line)]] | wt | 41.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +10.4) | — |
| [[CHP-212 (line)]] | wt | 101 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0974× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -10.4) |
| [[HepG2_C3A (line)]] | wt | 92.1 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +13.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.406× (z -13.1) |
| [[HS-578T (line)]] | alt | 57.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.3) | — |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.2) |
| [[KATO III (line)]] | alt | 72.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +14.1) | — |
| [[RPMI-7951 (line)]] | alt | 77.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.37× (z +11.9) | — |
| [[SNU-1 (line)]] | wt | 104 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -10.2) |
| [[SW48 (line)]] | wt | 121 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 79.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -10.6) |
| [[BT-474 (line)]] | alt | 71.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +13.0) | — |
| [[HCT15 (line)]] | alt | 151 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.0) | — |
| [[AN3 CA (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 77.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX1]] | +0.80 | +0.77 / +0.80 | both halves | 7e-06 | STRING 476 |
| [[SF3A3]] | +0.79 | +0.81 / +0.78 | both halves | 7e-06 | STRING 407 |
| [[RBM28]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 986 |
| [[AGGF1]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PWP1]] | +0.67 | +0.67 / +0.60 | both halves | 7e-06 | STRING 875 |
| [[CCT2]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[DLAT]] | +0.67 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[MAK16]] | +0.67 | +0.68 / +0.69 | both halves | 7e-06 | STRING 886 |
| [[PRMT5]] | +0.67 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[AGK]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[PES1]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 | pathway: Major pathway of rRNA processing in the nucleolus and cytosol; STRING 947 |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HIGD2A]] | -0.63 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[GPBP1L1]] | -0.61 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[PDE6D]] | -0.60 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[WDR20]] | -0.59 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[GNAS]] | -0.59 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TESK2]] | -0.58 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[CDK19]] | -0.58 | -0.63 / -0.45 | both halves | 3e-05 |  |
| [[NARF]] | -0.57 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[GNRH1]] | -0.57 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[PPM1B]] | -0.57 | -0.63 / -0.43 | both halves | 3e-05 |  |
| [[TPTEP2-CSNK1E]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[PPP2R2D]] | -0.56 | -0.53 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises BMS1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.4, -39.3); signed map (-3.0, -42.0). **Vector** length 110, 35.0% of its response variance represented; |z| ≥ 3 in 1,276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +21.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +7.1 | +10.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +6.3 | +11.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.2 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.3 | +2.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | -0.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +7.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.4 | +10.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.7 | -14.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.8 | +3.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -6.0 | +6.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -3.9 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -5.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.6 | -4.9 |
|  | [[Decitabine (drug)]] 0.05 µM |  | -2.2 | -1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | BMS1 ribosome biogenesis factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.21 — chr10:42,782,795-42,834,937 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0187; previously BMS1L |
| Gene groups (HGNC) | SSU processome |
| Reactome | 5 pathways, smallest: rRNA modification in the nucleus and cytosol; Major pathway of rRNA processing in the nucleolus and cytosol; rRNA processing in the nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14692](https://www.uniprot.org/uniprotkb/Q14692) (Ribosome biogenesis protein BMS1 homolog):

> GTPase required for the synthesis of 40S ribosomal subunits and for processing of pre-ribosomal RNA (pre-rRNA) at sites A0, A1, and A2. Controls access of pre-rRNA intermediates to RCL1 during ribosome biogenesis by binding RCL1 in a GTP-dependent manner, and delivering it to pre-ribosomes. GTP-binding and/or GTP hydrolysis may induce conformational rearrangements within the BMS1-RCL1 complex allowing the interaction of RCL1 with its RNA substrate. Required for RCL1 import into the nucleus.

**Summary**, from NCBI Gene [9790](https://www.ncbi.nlm.nih.gov/gene/9790):

> This gene likely encodes a ribosome assembly protein. A similar protein in yeast functions in 35S-rRNA processing, which includes a series of cleavage steps critical for formation of 40S ribosomes. Related pseudogenes exist on chromosomes 2, 9, 10, 15, 16, and 22.[provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:23505](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23505) · Entrez [9790](https://www.ncbi.nlm.nih.gov/gene/9790) · UniProt [Q14692](https://www.uniprot.org/uniprotkb/Q14692) · Ensembl [ENSG00000165733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165733)

## Data

Gene col 9179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9179); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9179]; `tensor/DDL_lfc|DDL_z.npy` [9179]; `embed/gene_vectors.npy` [9179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9179 or target_col == 9179). Every well: [[BMS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
