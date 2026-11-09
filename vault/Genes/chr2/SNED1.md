---
symbol: "SNED1"
type: "gene"
col: 8581
ensembl_id: "ENSG00000162804"
name: "sushi, nidogen and EGF like domains 1"
location: "2q37.3"
module: 97
arm: "+"
pooled_cpm: 25.16
n_lines_expressing: 42
n_dd_up: 32
n_dd_down: 33
n_dd_up_clean: 28
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/097"]
generated_by: "tahoemap"
---

# SNED1

*sushi, nidogen and EGF like domains 1* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.98× (z +9.2, q 2e-17, up in 29 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.463× (z -10.3, q 6e-22, down in 25 of 40 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPGR]] (+0.59, fdr 1e-05), [[ATP1A1]] (+0.58, fdr 1e-05), [[ADGRG2]] (+0.57, fdr 1e-05); moves opposite to [[HNF1B]] (-0.46, fdr 5e-05), [[TLR1]] (-0.45, fdr 6e-05), [[ZNF624]] (-0.44, fdr 1e-04).
> It is in [[Module 097]], a single-armed module (estrogen response early).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDKN2B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8581.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.98×** | +9.2 | 2e-17 | 29/40 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.61×** | +6.4 | 4e-08 | 23/39 (HS-578T, NCI-H460, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.56×** | +6.0 | 4e-07 | 27/40 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.37×** | +5.9 | 4e-07 | 21/40 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.51×** | +5.6 | 3e-06 | 20/40 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.52×** | +5.4 | 5e-06 | 12/26 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.4 | 6e-06 | 14/34 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.46×** | +5.1 | 3e-05 | 15/39 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.5 | 3e-04 | 19/40 (SHP-77, NCI-H2347, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.39×** | +4.4 | 6e-04 | 15/40 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.24×** | +4.2 | 0.002 | 17/38 (A549, AsPC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 16/40 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.38×** | +4.0 | 0.003 | 14/39 (Panc 03.27, SW1417, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.33×** | +3.9 | 0.004 | 15/39 (NCI-H1573, NCI-H460, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +3.8 | 0.006 | 16/40 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.007 | 18/40 (RPMI-7951, H4, …) | inconsistent across doses | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.007 | 15/38 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.30×** | +3.6 | 0.011 | 10/40 (C32, A-172, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8581.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.463×** | -10.3 | 6e-22 | 25/40 (SW480, A-172, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.505×** | -9.1 | 3e-17 | 27/40 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.495×** | -9.0 | 3e-17 | 23/40 (SW480, LoVo, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.516×** | -8.8 | 2e-16 | 27/39 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.643×** | -8.3 | 1e-14 | 29/40 (A-172, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.543×** | -8.1 | 4e-14 | 23/39 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.588×** | -7.1 | 1e-10 | 29/40 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -6.6 | 3e-09 | 19/40 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -5.5 | 3e-06 | 23/40 (SW 1271, C32, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.669×** | -5.4 | 5e-06 | 20/40 (PANC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.464×** | -5.3 | 5e-06 | 19/39 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.487×** | -5.0 | 2e-05 | 19/40 (LS 180, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.688×** | -5.0 | 3e-05 | 18/40 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.794×** | -4.3 | 6e-04 | 19/40 (NCI-H1573, RPMI-7951, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.727×** | -4.2 | 9e-04 | 17/40 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.800×** | -4.2 | 0.001 | 14/40 (SW480, NCI-H460, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.645×** | -4.2 | 0.001 | 14/40 (MIA PaCa-2, NCI-H1792, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.554×** | -4.1 | 0.001 | 15/38 (SK-MEL-2, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.003 | 13/40 (NCI-H1792, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.743×** | -3.7 | 0.005 | 16/39 (C32, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8581. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 45.0 | 18 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.60× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Triamcinolone (drug)]] 5 µM 3.21× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 40.6 | 2 (2 ⚠) | 3 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.4) ⚠ cell-cycle shift, explains ~15% of this change | [[Harringtonine (drug)]] 5 µM 0.274× (z -9.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 24.3 | 3 (1 ⚠) | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.22× (z +12.9) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.32× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -8.5) |
| [[PANC-1 (line)]] | alt | 29.7 | 1 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.82× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -11.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.339× (z -9.3) |
| [[SW480 (line)]] | alt | 26.4 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.256× (z -11.6) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.417× (z -10.9) |
| [[A-172 (line)]] | wt | 45.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -14.8) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.272× (z -10.4) |
| [[LoVo (line)]] | wt | 23.6 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.80× (z +9.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.233× (z -11.1) |
| [[H4 (line)]] | wt | 87.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0112× (z -18.7) |
| [[A-427 (line)]] | wt | 26.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.289× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 6.80 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 17.4× (z +15.0) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[C32 (line)]] | wt | 60.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -12.7) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.181× (z -8.9) |
| [[COLO 205 (line)]] | alt | 10.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 35.7× (z +18.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[HS-578T (line)]] | alt | 36.1 | 1 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 4.42× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.4) ⚠ cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 39.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.01× (z +17.5) ⚠ cell-cycle shift, explains ~50% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -8.7) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 63.1 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.02× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -9.3) ⚠ cell-cycle shift, explains ~12% of this change |
| [[A549 (line)]] | wt | 11.4 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.26× (z +12.5) ⚠ cell-cycle shift, explains ~12% of this change | — |
| [[AN3 CA (line)]] | alt | 71.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -8.6) |
| [[HT-29 (line)]] | alt | 6.42 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.28× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -9.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[RPMI-7951 (line)]] | alt | 136 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.0) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -9.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW 1271 (line)]] | alt | 70.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0499× (z -9.2) |
| [[SW1417 (line)]] | alt | 46.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -12.9) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW48 (line)]] | wt | 95.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -9.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.94 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.84 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 57.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.80 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.19 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 34.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8581), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPGR]] | +0.59 | +0.54 / +0.51 | both halves | 1e-05 | **novel candidate** |
| [[ATP1A1]] | +0.58 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[ADGRG2]] | +0.57 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[DIP2C]] | +0.57 | +0.44 / +0.60 | both halves | 3e-05 | **novel candidate** |
| [[PTPN12]] | +0.57 | +0.40 / +0.47 | both halves | 5e-05 |  |
| [[SH3RF3]] | +0.56 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[EVA1C]] | +0.54 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[PYGB]] | +0.53 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ABLIM2]] | +0.53 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[LDLRAD3]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[RHOBTB2]] | +0.52 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[SLC20A1]] | +0.52 | +0.39 / +0.52 | both halves | 6e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1B]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TLR1]] | -0.45 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[ZNF624]] | -0.44 | -0.32 / -0.53 | both halves | 1e-04 |  |
| [[B4GALT4]] | -0.42 | -0.39 / -0.34 | both halves | 1e-04 |  |
| [[SLAMF7]] | -0.40 | -0.25 / -0.43 | both halves | 4e-04 |  |
| [[FOXA1]] | -0.40 | -0.33 / -0.41 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDKN2B]] | B | CDKN2B activity weakens SNED1's drug response | recorded loss-of-function mutation of CDKN2B in 11 lines vs 29 not recorded | the CDKN2B-altered lines respond 1.73× as strongly (z diff -1.73); strongest at Digitoxin 5 µM: 0.41x vs 0.71x (z diff -2.8) | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; CDKN2B not expressed in 12 of the 13 altered lines; target measured in part of the lines; artifact flags |
| [[TRNP1]] | B | TRNP1 activity lowers SNED1's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 1.72× higher at baseline in the lines without TRNP1 | 0.058 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[RPS6KA2]] | B | RPS6KA2 activity raises SNED1's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 2.27× lower at baseline in the lines without RPS6KA2 | 0.079 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[TRIB2]] | B | TRIB2 activity raises SNED1's level | lines that do not express TRIB2 (10) vs lines expressing it (40) | 2.33× lower at baseline in the lines without TRIB2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SDC3]] | C | SDC3 activity strengthens SNED1's drug response | lines that do not express SDC3 (4) vs lines expressing it (36) | the lines without SDC3 respond 0.08× as strongly (z diff +2.75); strongest at Ouabain (Octahydrate) 5 µM: 1.54x vs 0.52x (z diff +5.6) | 0.081 | ⚠ few lines (4 vs 46); across organs; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 097]] — estrogen response early; 48 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.7, 13.1); signed map (15.2, 33.7). **Vector** length 89.8, 20.1% of its response variance represented; |z| ≥ 3 in 1,231 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.7 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.4 | +5.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.4 | +6.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +3.8 | +5.6 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +3.4 | +5.1 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -10.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -4.1 | -9.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -5.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.9 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | sushi, nidogen and EGF like domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,998,618-241,095,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ00133, SST3, Snep |
| Gene groups (HGNC) | Fibronectin type III domain containing; Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TER0](https://www.uniprot.org/uniprotkb/Q8TER0) (Sushi, nidogen and EGF-like domain-containing protein 1):

> Mediates cell adhesion via integrins ITGA5:ITGB1 and ITGAV:ITGB3 which bind to the R-G-D cell attachment site in SNED1. Cell adhesion is also likely to occur through additional integrin and/or non-integrin receptors at the cell surface. Plays a role in craniofacial morphogenesis (By similarity).

**Summary**, from NCBI Gene [25992](https://www.ncbi.nlm.nih.gov/gene/25992):

> Predicted to enable Notch binding activity. Predicted to be involved in cell-matrix adhesion. Located in extracellular matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24696](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24696) · Entrez [25992](https://www.ncbi.nlm.nih.gov/gene/25992) · UniProt [Q8TER0](https://www.uniprot.org/uniprotkb/Q8TER0) · Ensembl [ENSG00000162804](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162804)

## Data

Gene col 8581: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8581); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8581, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8581]; `tensor/DDL_lfc|DDL_z.npy` [8581]; `embed/gene_vectors.npy` [8581]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8581 or target_col == 8581). Every well: [[SNED1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNED1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
