---
symbol: "AAGAB"
type: "gene"
col: 2385
ensembl_id: "ENSG00000103591"
name: "alpha and gamma adaptin binding protein"
location: "15q23"
module: 36
arm: "+"
pooled_cpm: 63.03
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 2
n_dd_up_clean: 19
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# AAGAB

*alpha and gamma adaptin binding protein* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (17 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.67× (z +16.3, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.823× (z -5.6, q 9e-06, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.129×, SK-MEL-2 0.167×, Panc 03.27 0.294×, C32 0.374×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0559×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 1271 0.108×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (H4 0.152×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTOR]] (+0.61, fdr 1e-05), [[KPNA1]] (+0.59, fdr 9e-06), [[NDUFS6]] (+0.59, fdr 1e-05); moves opposite to [[CDKL2]] (-0.57, fdr 1e-05), [[FAM53C]] (-0.55, fdr 1e-05), [[TENT5C]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 46 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.67×** | +16.3 | 0e+00 | 47/49 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.96×** | +13.6 | 2e-39 | 45/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.80×** | +11.8 | 7e-30 | 42/48 (HEC-1-A, HOP62, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +11.8 | 7e-30 | 44/48 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.51×** | +11.7 | 3e-29 | 37/48 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.78×** | +11.6 | 6e-29 | 40/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **1.74×** | +11.1 | 8e-27 | 41/47 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.71×** | +10.7 | 5e-25 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.68×** | +10.4 | 9e-24 | 41/48 (HEC-1-A, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.67×** | +10.4 | 2e-23 | 42/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.67×** | +10.3 | 5e-23 | 41/48 (PANC-1, HEC-1-A, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.61×** | +9.6 | 4e-20 | 42/48 (HOP62, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +9.5 | 8e-20 | 40/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.53×** | +8.5 | 8e-16 | 36/48 (HEC-1-A, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.51×** | +8.0 | 5e-14 | 33/48 (SW480, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.45×** | +7.5 | 3e-12 | 33/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.47×** | +7.3 | 7e-12 | 37/48 (KATO III, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.43×** | +7.1 | 3e-11 | 33/48 (NCI-H1792, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.41×** | +7.0 | 1e-10 | 32/48 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2385.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (A-427 0.129×, SK-MEL-2 0.167×, Panc 03.27 0.294×, C32 0.374×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (C-33 A 0.0559×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Docetaxel (drug)]] 0.05 µM in 1 line (SW 1271 0.108×; ⚠ transcription drop; cell-cycle shift, explains ~0% of this change); [[Thymol (drug)]] 0.5 µM in 1 line (H4 0.152×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -5.6 | 9e-06 | 25/48 (SNU-1, NCI-H661, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.793×** | -4.7 | 6e-04 | 22/48 (KATO III, A498, …) | all doses, stronger at high dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.841× | -3.4 | 0.12 | 12/49 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.807× | -3.1 | 0.25 | 15/48 (HCT15, NCI-H2030, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | 0.863× | -3.0 | 0.26 | 9/48 (C32, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 97.3 | 10 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.21× (z +19.2) | — |
| [[NCI-H1573 (line)]] | alt | 79.7 | 9 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.07× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +16.1) | — |
| [[SW480 (line)]] | alt | 77.3 | 8 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.78× (z +15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 28.5 | 6 (5 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.37× (z +9.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.25× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 25.9 | 5 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +12.0) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.58× (z +9.6) | — |
| [[HEC-1-A (line)]] | alt | 48.7 | 4 (3 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.93× (z +11.1) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.84× (z +10.4) | — |
| [[NCI-H23 (line)]] | alt | 101 | 4 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.83× (z +10.5) | — |
| [[Panc 03.27 (line)]] | alt | 49.4 | 3 (2 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.60× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.14× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 55.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +8.9) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[KATO III (line)]] | alt | 69.1 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 10.0× (z +12.5) | — |
| [[LS 180 (line)]] | wt | 60.1 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 8.88× (z +11.2) | — |
| [[NCI-H1792 (line)]] | alt | 55.1 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.7) ⚠ cell-cycle shift, explains ~67% of this change | — |
| [[A-172 (line)]] | wt | 41.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 39.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.7) ⚠ cell-cycle shift, explains ~67% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.86× (z +11.5) | — |
| [[H4 (line)]] | wt | 37.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +8.6) | [[Thymol (drug)]] 0.5 µM 0.152× (z -10.9) |
| [[LoVo (line)]] | wt | 69.7 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.07× (z +11.7) | — |
| [[NCI-H2347 (line)]] | alt | 30.7 | 2 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.75× (z +9.2) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H460 (line)]] | wt | 49.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.0) | — |
| [[SW1417 (line)]] | alt | 78.5 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.21× (z +9.6) | — |
| [[A-427 (line)]] | wt | 70.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -21.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 65.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.26× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 61.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -8.5) ⚠ cell-cycle shift, explains ~67% of this change |
| [[C-33 A (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0559× (z -25.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 61.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Hs 766T (line)]] | wt | 37.3 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.18× (z +8.8) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[HS-578T (line)]] | alt | 40.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.84× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 87.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.74× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 125 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +9.5) | — |
| [[RKO (line)]] | wt | 88.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.63× (z +8.8) | — |
| [[SK-MEL-2 (line)]] | alt | 60.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 33.2 | 1 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 3.08× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[SW 1271 (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 71.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.258× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[A549 (line)]] | wt | 99.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 72.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 66.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 56.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 60.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 42.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTOR]] | +0.61 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[KPNA1]] | +0.59 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[NDUFS6]] | +0.59 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[DIS3L2]] | +0.59 | +0.57 / +0.58 | both halves | 8e-06 |  |
| [[PARN]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[ATAD1]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[GTF2F2]] | +0.57 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PEX26]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[NUDT5]] | +0.57 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[EXT2]] | +0.57 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.56 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[GFM1]] | +0.56 | +0.53 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL2]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[FAM53C]] | -0.55 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TENT5C]] | -0.55 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[FAM117A]] | -0.55 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[FAM222A]] | -0.54 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[MYLIP]] | -0.53 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[NBPF19]] | -0.53 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[NBPF10]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[STK17B]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[RSRP1]] | -0.52 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[VASN]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[MEX3B]] | -0.52 | -0.48 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AAGAB's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-8.8, -29.5); signed map (-20.4, -53.7). **Vector** length 88.4, 25.0% of its response variance represented; |z| ≥ 3 in 1,415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +16.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.1 | +3.1 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.9 | +9.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.2 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +11.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.1 | +10.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.5 | +4.1 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.7 | -5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | +11.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.6 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | +0.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.4 | -1.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.8 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | alpha and gamma adaptin binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:67,200,667-67,255,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11506, p34 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PD74](https://www.uniprot.org/uniprotkb/Q6PD74) (Alpha- and gamma-adaptin-binding protein p34):

> May be involved in endocytic recycling of growth factor receptors such as EGFR.

**Summary**, from NCBI Gene [79719](https://www.ncbi.nlm.nih.gov/gene/79719):

> The protein encoded by this gene interacts with the gamma-adaptin and alpha-adaptin subunits of complexes involved in clathrin-coated vesicle trafficking. Mutations in this gene are associated with type I punctate palmoplantar keratoderma. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:25662](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25662) · Entrez [79719](https://www.ncbi.nlm.nih.gov/gene/79719) · UniProt [Q6PD74](https://www.uniprot.org/uniprotkb/Q6PD74) · Ensembl [ENSG00000103591](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103591)

## Data

Gene col 2385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2385); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2385]; `tensor/DDL_lfc|DDL_z.npy` [2385]; `embed/gene_vectors.npy` [2385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2385 or target_col == 2385). Every well: [[AAGAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AAGAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
