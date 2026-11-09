---
symbol: "ABLIM2"
type: "gene"
col: 8829
ensembl_id: "ENSG00000163995"
name: "actin binding LIM protein family member 2"
location: "4p16.1"
module: 97
arm: "+"
pooled_cpm: 19.05
n_lines_expressing: 37
n_dd_up: 41
n_dd_down: 26
n_dd_up_clean: 39
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# ABLIM2

*actin binding LIM protein family member 2* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 8.60× (z +27.9, q 0e+00, up in 31 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.305× (z -15.4, q 0e+00, down in 32 of 34 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ERGIC1]] (+0.64, fdr 3e-05), [[PKP2]] (+0.61, fdr 1e-05), [[TNS4]] (+0.60, fdr 1e-05); moves opposite to [[TTC6]] (-0.52, fdr 8e-05), [[FOXA1]] (-0.51, fdr 3e-05), [[SPAG16]] (-0.51, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[KRT6A]] → it (grade B ⚠); 6 go from it, the strongest it → [[CLYBL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 2 with an alert ⚠; shown: the 15 strongest. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **8.60×** | +27.9 | 0e+00 | 31/34 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.43×** | +24.1 | 0e+00 | 29/33 (PANC-1, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.33×** | +19.0 | 0e+00 | 29/34 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.54×** | +17.1 | 0e+00 | 27/34 (J82, HT-29, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.21×** | +15.0 | 0e+00 | 27/34 (J82, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **2.29×** | +10.7 | 1e-24 | 23/33 (AsPC-1, A549, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +9.0 | 2e-17 | 17/33 (HT-29, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.97×** | +8.8 | 9e-17 | 16/33 (AsPC-1, A549, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **3.43×** | +8.3 | 4e-15 | 21/35 (PANC-1, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.84×** | +7.9 | 2e-13 | 13/34 (AsPC-1, A549, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.77×** | +7.4 | 9e-12 | 13/33 (AsPC-1, A549, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **1.70×** | +6.9 | 3e-10 | 12/34 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.42×** | +6.5 | 4e-09 | 11/34 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.62×** | +6.2 | 2e-08 | 13/33 (AsPC-1, A549, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **1.51×** | +5.3 | 4e-06 | 10/34 (AsPC-1, A549, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.305×** | -15.4 | 0e+00 | 32/34 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.429×** | -11.0 | 2e-25 | 28/34 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -10.0 | 5e-21 | 26/32 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.470×** | -9.4 | 7e-19 | 26/33 (LoVo, LS 180, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.603×** | -9.3 | 2e-18 | 29/33 (LoVo, KATO III, …) | rises with dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.645×** | -8.0 | 8e-14 | 26/34 (SW480, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -8.0 | 1e-13 | 21/33 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.382×** | -6.5 | 5e-09 | 21/34 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.617×** | -6.3 | 2e-08 | 21/31 (LoVo, SW1417, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -6.1 | 5e-08 | 18/30 (LS 180, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.636×** | -5.9 | 2e-07 | 19/34 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.650×** | -5.6 | 1e-06 | 17/33 (PANC-1, LoVo, …) | two highest doses |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.470×** | -5.1 | 1e-05 | 14/31 (LS 180, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.679×** | -5.0 | 2e-05 | 23/34 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.677×** | -4.8 | 7e-05 | 13/32 (LoVo, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.678×** | -3.6 | 0.010 | 9/35 (SW480, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.040 | 12/33 (Hs 766T, KATO III, …) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.786×** | -3.1 | 0.048 | 6/34 (SW480, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.788×** | -3.1 | 0.050 | 9/33 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.783×** | -3.1 | 0.055 | 6/34 (A498, PANC-1, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 20.6 | 21 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 22.4× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -13.5) ⚠ cell-cycle shift, explains ~57% of this change |
| [[Hs 766T (line)]] | wt | 91.4 | 11 | 11 (9 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 4.11× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.114× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.282× (z -13.1) |
| [[LoVo (line)]] | wt | 92.6 | 2 | 18 (9 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.04× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -30.0) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0662× (z -25.2) |
| [[A549 (line)]] | wt | 7.60 | 16 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 25.8× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 10.9 | 5 | 11 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 8.49× (z +15.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.116× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 5.40 | 12 | 0 | [[Clobetasol propionate (drug)]] 5 µM 10.2× (z +9.7) | — |
| [[KATO III (line)]] | alt | 77.0 | 2 | 9 (6 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -23.5) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.208× (z -12.6) |
| [[LS 180 (line)]] | wt | 77.4 | 1 | 9 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.22× (z +10.1) | [[Digitoxin (drug)]] 5 µM 0.0570× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.135× (z -18.0) |
| [[SW480 (line)]] | alt | 27.0 | 2 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.58× (z +10.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -15.3) |
| [[SHP-77 (line)]] | alt | 54.5 | 0 | 7 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -14.6) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.129× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 10.1 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 14.9× (z +9.9) | — |
| [[A-427 (line)]] | wt | 23.4 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.36× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.171× (z -12.4) |
| [[J82 (line)]] | alt | 9.07 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 18.4× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 15.1 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.67× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.0665× (z -14.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.186× (z -9.2) |
| [[SW1417 (line)]] | alt | 29.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -14.2) ⚠ cell-cycle shift, explains ~57% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.211× (z -10.4) |
| [[SW48 (line)]] | wt | 38.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0739× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.137× (z -10.5) |
| [[HT-29 (line)]] | alt | 9.39 | 3 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.69× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -8.6) ⚠ cell-cycle shift, explains ~57% of this change |
| [[A498 (line)]] | wt | 5.21 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.5× (z +12.1) | — |
| [[A-172 (line)]] | wt | 11.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.5× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 7.10 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.8× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 9.63 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.80× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 5.36 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.17 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.72 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.81 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 9.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERGIC1]] | +0.64 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[PKP2]] | +0.61 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TNS4]] | +0.60 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[C16orf74]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 | same gene group |
| [[PHACTR3]] | +0.58 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[GPR153]] | +0.57 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[TMCO6]] | +0.56 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[VSIR]] | +0.55 | +0.42 / +0.43 | both halves | 4e-05 |  |
| [[FKBP1B]] | +0.55 | +0.41 / +0.48 | both halves | 4e-05 |  |
| [[CORO2A]] | +0.55 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[AKAP13]] | +0.54 | +0.40 / +0.46 | both halves | 5e-05 | same gene group |
| [[PTK2B]] | +0.54 | +0.53 / +0.47 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TTC6]] | -0.52 | -0.37 / -0.42 | both halves | 8e-05 |  |
| [[FOXA1]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[SPAG16]] | -0.51 | -0.36 / -0.44 | both halves | 1e-04 | same gene group |
| [[ZNF827]] | -0.50 | -0.29 / -0.38 | both halves | 2e-04 |  |
| [[TSTD3]] | -0.48 | -0.21 / -0.40 | both halves | 6e-04 |  |
| [[LINC02542]] | -0.48 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[TENT5A]] | -0.48 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[MFF-DT]] | -0.47 | -0.24 / -0.30 | both halves | 5e-04 |  |
| [[ZBED5-AS1]] | -0.47 | -0.24 / -0.32 | both halves | 4e-04 |  |
| [[TLR1]] | -0.47 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[SOCS2-AS1]] | -0.47 | -0.31 / -0.39 | both halves | 2e-04 |  |
| [[HOXA10]] | -0.46 | -0.38 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KRT6A]] | B | KRT6A activity raises ABLIM2's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 3.37× lower at baseline in the lines without KRT6A | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588 |
| [[PHACTR3]] | B | PHACTR3 activity raises ABLIM2's level | lines that do not express PHACTR3 (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without PHACTR3 | 0.045 | ⚠ within organs, on part of the lines; also absent: CDH3, PADI2, PDE9A; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity raises ABLIM2's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 6.4% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[HES2]] | B | HES2 activity raises ABLIM2's level | lines that do not express HES2 (20) vs lines expressing it (30) | 2.22× lower at baseline in the lines without HES2 | 0.088 | ⚠ within organs, on part of the lines; also absent: FBXO2, PADI2, YBX2 |
| [[TLR1]] | B | TLR1 activity lowers ABLIM2's level | lines that do not express TLR1 (15) vs lines expressing it (35) | 2.41× higher at baseline in the lines without TLR1 | 0.098 | ⚠ within organs, on part of the lines; also absent: TLR6, ENSG00000289526, TMEM158 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CLYBL]] | B | ABLIM2 activity raises CLYBL's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without ABLIM2 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[GIPC1]] | B | ABLIM2 activity raises GIPC1's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 1.71× lower at baseline in the lines without ABLIM2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[CHKA]] | B | ABLIM2 activity raises CHKA's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 1.68× lower at baseline in the lines without ABLIM2 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[RAP1GAP2]] | B | ABLIM2 activity raises RAP1GAP2's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 2.09× lower at baseline in the lines without ABLIM2 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[ARRDC1]] | B | ABLIM2 activity raises ARRDC1's level | lines that do not express ABLIM2 (13) vs lines expressing it (37) | 1.80× lower at baseline in the lines without ABLIM2 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent |
| [[ITPK1]] | B | ABLIM2 activity weakens ITPK1's drug response | lines that do not express ABLIM2 (11) vs lines expressing it (34) | the lines without ABLIM2 respond 1.24× as strongly (z diff -0.36); strongest at Panobinostat 5 µM: 1.84x vs 1.11x (z diff -3.4) | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CAMSAP3, SLC9A2, MNX1; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (11.0, 49.6); signed map (10.4, 34.7). **Vector** length 103, 26.4% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +17.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | +27.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +24.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.9 | +19.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.7 | +9.0 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.3 | +8.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.2 | +7.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +3.2 | +5.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.2 | +10.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -6.4 | -8.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -4.5 | -9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -2.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.7 | -3.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | actin binding LIM protein family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:7,965,310-8,158,832 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1808 |
| Gene groups (HGNC) | LIM domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: DCC mediated attractive signaling; Netrin-1 signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6H8Q1](https://www.uniprot.org/uniprotkb/Q6H8Q1) (Actin-binding LIM protein 2):

> May act as scaffold protein. May stimulate ABRA activity and ABRA-dependent SRF transcriptional activity.

**Summary**, from NCBI Gene [84448](https://www.ncbi.nlm.nih.gov/gene/84448):

> Predicted to enable actin filament binding activity. Predicted to be involved in lamellipodium assembly. Predicted to act upstream of or within positive regulation of transcription by RNA polymerase II. Located in actin cytoskeleton. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19195](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19195) · Entrez [84448](https://www.ncbi.nlm.nih.gov/gene/84448) · UniProt [Q6H8Q1](https://www.uniprot.org/uniprotkb/Q6H8Q1) · Ensembl [ENSG00000163995](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163995)

## Data

Gene col 8829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8829); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8829]; `tensor/DDL_lfc|DDL_z.npy` [8829]; `embed/gene_vectors.npy` [8829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8829 or target_col == 8829). Every well: [[ABLIM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ABLIM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
