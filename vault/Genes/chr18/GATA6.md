---
symbol: "GATA6"
type: "gene"
col: 6522
ensembl_id: "ENSG00000141448"
name: "GATA binding protein 6"
location: "18q11.2"
module: 14
arm: "+"
pooled_cpm: 33.18
n_lines_expressing: 32
n_dd_up: 18
n_dd_down: 16
n_dd_up_clean: 16
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 17
direction_downstream: 31
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# GATA6

*GATA binding protein 6* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.70× (z +26.2, q 0e+00, up in 27 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.474× (z -10.2, q 2e-21, down in 21 of 26 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.635× (z -6.4, q 4e-08, down in 23 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMAD7]] (+0.67, fdr 7e-06), [[MARCKS]] (+0.66, fdr 7e-06), [[SOX9]] (+0.65, fdr 7e-06); moves opposite to [[BCAP31]] (-0.59, fdr 1e-05), [[ZNF731P]] (-0.57, fdr 2e-05), [[FBXW2]] (-0.54, fdr 2e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[BMP2]] → it (grade B ⚠); 31 go from it, the strongest it → [[THOC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6522.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.70×** | +26.2 | 0e+00 | 27/30 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **7.58×** | +15.0 | 0e+00 | 29/30 (LoVo, HS-578T, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **2.83×** | +14.1 | 4e-43 | 26/30 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.34×** | +12.0 | 3e-31 | 24/30 (A498, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **4.11×** | +10.4 | 2e-23 | 24/29 (BT-474, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +6.3 | 2e-08 | 11/30 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.48×** | +5.5 | 3e-06 | 21/30 (KATO III, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.45×** | +5.2 | 1e-05 | 12/29 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.42×** | +5.0 | 4e-05 | 19/30 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.002 | 9/30 (SW480, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.005 | 10/30 (AsPC-1, HCT15, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.005 | 8/30 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.005 | 6/29 (BT-474, A-172, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.009 | 15/29 (KATO III, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~15% here) |
| [[Retinoic acid (drug)]] 5 µM |  | 1.19× | +3.4 | 0.023 | 7/30 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.023 | 5/29 (LoVo, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6522.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -10.2 | 2e-21 | 21/26 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.635×** | -6.4 | 4e-08 | 23/30 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.692×** | -5.2 | 4e-05 | 12/29 (H4, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.728×** | -4.5 | 9e-04 | 16/30 (HS-578T, NCI-H1792, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.718×** | -4.3 | 0.001 | 18/27 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Triamcinolone (drug)]] 5 µM |  | **0.805×** | -4.3 | 0.001 | 14/30 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.742×** | -4.2 | 0.002 | 13/30 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.748×** | -4.1 | 0.003 | 17/30 (AsPC-1, NCI-H1792, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.749×** | -4.1 | 0.003 | 22/28 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.767×** | -3.8 | 0.010 | 15/30 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.771×** | -3.7 | 0.012 | 9/30 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.774×** | -3.6 | 0.014 | 12/29 (NCI-H1792, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.781×** | -3.5 | 0.020 | 10/30 (NCI-H1792, HS-578T, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.793×** | -3.3 | 0.040 | 13/30 (A549, NCI-H1792, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.076 | 13/30 (NCI-H2347, NCI-H1792, …) | rises with dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.741×** | -3.0 | 0.085 | 15/29 (KATO III, COLO 205, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6522. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 41.5 | 3 | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.8) | [[Dinaciclib (drug)]] 5 µM 0.0642× (z -22.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.272× (z -10.9) |
| [[HS-578T (line)]] | alt | 75.7 | 3 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +15.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -14.0) |
| [[LS 180 (line)]] | wt | 119 | 2 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 7.00× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.164× (z -16.9) |
| [[Hs 766T (line)]] | wt | 180 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.0454× (z -20.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.202× (z -11.1) |
| [[HT-29 (line)]] | alt | 69.2 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 6.81× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.0592× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.304× (z -10.8) |
| [[KATO III (line)]] | alt | 131 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.158× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.225× (z -16.3) |
| [[NCI-H1792 (line)]] | alt | 139 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.95× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.286× (z -10.0) |
| [[LoVo (line)]] | wt | 69.8 | 2 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 21.0× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.0486× (z -27.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.389× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 55.1 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.01× (z +19.7) | [[Dinaciclib (drug)]] 5 µM 0.0377× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.274× (z -8.7) |
| [[SNU-423 (line)]] | alt | 31.2 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.375× (z -9.0) |
| [[A-172 (line)]] | wt | 13.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.15× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 25.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.54× (z +14.1) | — |
| [[CFPAC-1 (line)]] | alt | 37.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 62.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +14.9) | — |
| [[SNU-1 (line)]] | wt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0539× (z -21.0) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 15.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 66.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0742× (z -14.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 15.6 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +10.5) | [[Harringtonine (drug)]] 0.05 µM 0.0675× (z -8.9) |
| [[NCI-H1573 (line)]] | alt | 8.50 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.91× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 22.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -9.9) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 9.51 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.52× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 27.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +10.4) | — |
| [[H4 (line)]] | wt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.98× (z +11.3) | — |
| [[HOP62 (line)]] | alt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.05× (z +12.6) | — |
| [[J82 (line)]] | alt | 13.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.67× (z +16.2) | — |
| [[LOX-IMVI (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 31.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +9.8) | — |
| [[A-427 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.89 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.10 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.00 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.65 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 8.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.11 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6522), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMAD7]] | +0.67 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[MARCKS]] | +0.66 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[SOX9]] | +0.65 | +0.59 / +0.66 | both halves | 7e-06 | STRING 591 |
| [[RRAD]] | +0.63 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[LITAF]] | +0.62 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[LGALS3]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[REL]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[KLF4]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 | pathway: Transcriptional regulation of pluripotent stem cells; STRING 635 |
| [[RIPK2]] | +0.61 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[EFNA1]] | +0.61 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[TNFAIP2]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[ATP1B1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAP31]] | -0.59 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[ZNF731P]] | -0.57 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[TPD52L2]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[FUBP3]] | -0.52 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[NTAQ1]] | -0.51 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[THOC5]] | -0.51 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[STK25]] | -0.51 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[HARS1]] | -0.50 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[HSF1]] | -0.49 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[CAP1]] | -0.49 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[CERS5]] | -0.49 | -0.51 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 14, C 3. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMP2]] | B | BMP2 activity raises GATA6's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.43× lower at baseline in the lines without BMP2 | 0.004 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[SOX9]] | B | SOX9 activity raises GATA6's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.95× lower at baseline in the lines without SOX9 | 0.011 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[RRAD]] | B | RRAD activity raises GATA6's level | lines that do not express RRAD (31) vs lines expressing it (19) | 1.93× lower at baseline in the lines without RRAD | 0.020 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA |
| [[CXCL3]] | B | CXCL3 activity raises GATA6's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 2.54× lower at baseline in the lines without CXCL3 | 0.027 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[ETS2]] | B | ETS2 activity raises GATA6's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.76× lower at baseline in the lines without ETS2 | 0.028 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[UGT1A8]] | B | UGT1A8 activity raises GATA6's level | lines that do not express UGT1A8 (33) vs lines expressing it (17) | 3.21× lower at baseline in the lines without UGT1A8 | 0.039 | ⚠ within organs, on part of the lines; co-absent genes; also absent: UGT1A1, UGT1A6, LINC01559 |
| [[ARHGAP42]] | B | ARHGAP42 activity raises GATA6's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 3.18× lower at baseline in the lines without ARHGAP42 | 0.039 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises GATA6's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 2.50× lower at baseline in the lines without NEDD9 | 0.044 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[SERTAD4]] | B | SERTAD4 activity raises GATA6's level | lines that do not express SERTAD4 (14) vs lines expressing it (36) | 1.59× lower at baseline in the lines without SERTAD4 | 0.045 | ⚠ within organs, on part of the lines; also absent: SH3GL3, RNF165, BOC |
| [[FBXO32]] | B | FBXO32 activity raises GATA6's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 2.46× lower at baseline in the lines without FBXO32 | 0.055 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[GBP2]] | B | GBP2 activity raises GATA6's level | lines that do not express GBP2 (13) vs lines expressing it (37) | 2.28× lower at baseline in the lines without GBP2 | 0.062 | ⚠ within organs, on part of the lines; also absent: GBP1, ITGA3, SH3TC1 |
| [[LGALS3]] | B | LGALS3 activity raises GATA6's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 2.49× lower at baseline in the lines without LGALS3 | 0.063 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 30, C 1. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[THOC5]] | B | GATA6 activity lowers THOC5's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.55× higher at baseline in the lines without GATA6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[IKBKE]] | B | GATA6 activity raises IKBKE's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without GATA6 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[BCL3]] | B | GATA6 activity raises BCL3's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without GATA6 | 0.003 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[HARS1]] | B | GATA6 activity lowers HARS1's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.33× higher at baseline in the lines without GATA6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[ATP1B1]] | B | GATA6 activity raises ATP1B1's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.58× lower at baseline in the lines without GATA6 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[GBP2]] | B | GATA6 activity raises GBP2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 3.01× lower at baseline in the lines without GATA6 | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[PER2]] | B | GATA6 activity raises PER2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.57× lower at baseline in the lines without GATA6 | 0.010 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[BCL7C]] | B | GATA6 activity lowers BCL7C's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.38× higher at baseline in the lines without GATA6 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[MAP3K8]] | B | GATA6 activity raises MAP3K8's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without GATA6 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[NFATC2]] | B | GATA6 activity raises NFATC2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.41× lower at baseline in the lines without GATA6 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[SOX9]] | B | GATA6 activity raises SOX9's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.22× lower at baseline in the lines without GATA6 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |
| [[ETS2]] | B | GATA6 activity raises ETS2's level | lines that do not express GATA6 (18) vs lines expressing it (32) | 2.26× lower at baseline in the lines without GATA6 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000264825, CDA, SPTLC3 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.7, 2.3); signed map (45.2, 11.5). **Vector** length 101, 29.6% of its response variance represented; |z| ≥ 3 in 823 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +26.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.0 | +12.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.9 | +15.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +14.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +10.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +2.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.3 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.9 | -10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.7 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.6 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -3.5 | -4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.5 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.3 | -2.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.9 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | GATA binding protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:22,169,589-22,202,528 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | GATA zinc finger domain containing |
| Reactome | 8 pathways, smallest: POU5F1 (OCT4), SOX2, NANOG repress genes related to differentiation; Formation of definitive endoderm; Surfactant metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92908](https://www.uniprot.org/uniprotkb/Q92908) (Transcription factor GATA-6):

> Transcriptional activator. Regulates SEMA3C and PLXNA2. Involved in gene regulation specifically in the gastric epithelium. May regulate genes that protect epithelial cells from bacterial infection. Involved in bone morphogenetic protein (BMP)-mediated cardiac-specific gene expression (By similarity). Binds to BMP response element (BMPRE) DNA sequences within cardiac activating regions (By similarity). In human skin, controls several physiological processes contributing to homeostasis of the …

**Summary**, from NCBI Gene [2627](https://www.ncbi.nlm.nih.gov/gene/2627):

> This gene is a member of a small family of zinc finger transcription factors that play an important role in the regulation of cellular differentiation and organogenesis during vertebrate development. This gene is expressed during early embryogenesis and localizes to endo- and mesodermally derived cells during later embryogenesis and thereby plays an important role in gut, lung, and heart development. Mutations in this gene are associated with several congenital defects. [provided by RefSeq, Mar …

**Accessions** — [HGNC:4174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4174) · Entrez [2627](https://www.ncbi.nlm.nih.gov/gene/2627) · UniProt [Q92908](https://www.uniprot.org/uniprotkb/Q92908) · Ensembl [ENSG00000141448](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141448)

## Data

Gene col 6522: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6522); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6522, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6522]; `tensor/DDL_lfc|DDL_z.npy` [6522]; `embed/gene_vectors.npy` [6522]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6522 or target_col == 6522). Every well: [[GATA6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GATA6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
