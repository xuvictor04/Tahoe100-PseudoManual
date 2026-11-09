---
symbol: "OXR1"
type: "gene"
col: 9013
ensembl_id: "ENSG00000164830"
name: "oxidation resistance 1"
location: "8q23.1"
module: 79
arm: "+"
pooled_cpm: 236.87
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 23
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 26
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# OXR1

*oxidation resistance 1* — 8q23.1

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 4 lines (KATO III 2.28×, SK-MEL-2 1.76×, SHP-77 1.99×, NCI-H460 1.73×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 2.45×); [[Trametinib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.15×).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.518× (z -29.9, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPC2]] (+0.59, fdr 3e-05), [[VKORC1]] (+0.56, fdr 1e-05), [[GPR155]] (+0.56, fdr 1e-05); moves opposite to [[NRAS]] (-0.55, fdr 6e-05), [[ZSCAN29]] (-0.55, fdr 8e-05), [[BNIP2]] (-0.53, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LOX]] → it (grade B ⚠); 26 go from it, the strongest it → cells under [[Homoharringtonine (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9013.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Tucidinostat (drug)]] 5 µM in 4 lines (KATO III 2.28×, SK-MEL-2 1.76×, SHP-77 1.99×, NCI-H460 1.73×); [[Homoharringtonine (drug)]] 5 µM in 1 line (AsPC-1 2.45×); [[Trametinib (drug)]] 0.5 µM in 1 line (HEC-1-A 2.15×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 1.20× | +8.4 | 4e-14 | 19/44 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +5.7 | 4e-06 | 15/44 (LOX-IMVI, CFPAC-1, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.18× | +5.3 | 2e-05 | 17/45 (A-172, HS-578T, …) | rises with dose |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +4.2 | 0.004 | 7/44 (NCI-H1573, HEC-1-A, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.12× | +3.6 | 0.030 | 13/45 (SK-MEL-2, KATO III, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.5 µM |  | 1.11× | +3.5 | 0.042 | 7/44 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.047 | 15/44 (LS 180, RKO, …) | top dose only |  |
| [[Citalopram (hydrobromide) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.11 | 0/44 | rises with dose |  |
| [[Levobupivacaine (hydrochloride) (drug)]] 0.5 µM |  | 1.10× | +3.1 | 0.14 | 3/44 (SW 1088, LoVo, …) | all doses, stronger at high dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 23 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9013.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.518×** | -29.9 | 0e+00 | 40/44 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.537×** | -20.0 | 0e+00 | 38/44 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.545×** | -18.8 | 0e+00 | 36/44 (HOP62, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -16.2 | 0e+00 | 34/45 (NCI-H2347, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.629×** | -14.9 | 0e+00 | 38/44 (SW48, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.672×** | -12.8 | 2e-35 | 28/45 (C32, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -12.5 | 5e-34 | 31/40 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.679×** | -12.4 | 1e-33 | 28/44 (HOP62, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.481×** | -12.3 | 5e-33 | 37/44 (HOP62, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -10.4 | 1e-23 | 33/44 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -9.0 | 7e-18 | 27/44 (SW48, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.739×** | -8.7 | 1e-16 | 26/41 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | **0.785×** | -7.8 | 4e-13 | 26/44 (HOP62, COLO 205, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.790×** | -7.5 | 2e-12 | 26/44 (SW48, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.800×** | -7.2 | 3e-11 | 23/44 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.806×** | -6.9 | 2e-10 | 27/44 (Panc 03.27, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.808×** | -6.4 | 3e-09 | 21/43 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.764×** | -4.5 | 1e-04 | 17/44 (HT-29, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.883× | -4.0 | 0.001 | 11/44 (SW480, HEC-1-A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.886× | -3.7 | 0.004 | 12/44 (C32, NCI-H1792, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9013. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 814 | 0 | 20 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -22.3) |
| [[HOP62 (line)]] | alt | 209 | 0 | 18 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -29.1) |
| [[HEC-1-A (line)]] | alt | 355 | 12 (1 ⚠) | 5 (1 ⚠) | [[Trametinib (drug)]] 0.5 µM 2.15× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -18.0) |
| [[hTERT-HPNE (line)]] | wt | 922 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 429 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -21.6) |
| [[SW48 (line)]] | wt | 926 | 0 | 12 (9 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.212× (z -17.5) |
| [[LOX-IMVI (line)]] | wt | 230 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -24.5) |
| [[SW480 (line)]] | alt | 505 | 0 | 11 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -19.6) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -13.8) |
| [[NCI-H2347 (line)]] | alt | 306 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -26.0) |
| [[A-172 (line)]] | wt | 147 | 1 (1 ⚠) | 8 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.66× (z +9.9) ⚠ cell-cycle shift, explains ~14% of this change | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -13.7) |
| [[KATO III (line)]] | alt | 233 | 2 (1 ⚠) | 6 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.28× (z +15.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -12.5) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.8) |
| [[LS 180 (line)]] | wt | 190 | 2 (2 ⚠) | 6 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Harringtonine (drug)]] 5 µM 0.479× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 265 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.608× (z -11.5) |
| [[RPMI-7951 (line)]] | alt | 271 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -19.3) |
| [[J82 (line)]] | alt | 234 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -24.1) |
| [[NCI-H460 (line)]] | wt | 88.8 | 2 (1 ⚠) | 5 | [[Tucidinostat (drug)]] 5 µM 1.73× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -13.3) |
| [[HS-578T (line)]] | alt | 426 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -22.2) |
| [[AsPC-1 (line)]] | alt | 344 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +23.4) | [[Lonafarnib (drug)]] 5 µM 0.388× (z -9.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 144 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.2) |
| [[RKO (line)]] | wt | 284 | 1 (1 ⚠) | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.406× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.623× (z -10.8) |
| [[SW 900 (line)]] | alt | 359 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -16.5) |
| [[A-427 (line)]] | wt | 273 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -15.5) |
| [[CFPAC-1 (line)]] | alt | 147 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -17.8) |
| [[H4 (line)]] | wt | 258 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -29.1) |
| [[SNU-423 (line)]] | alt | 144 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -19.1) |
| [[A549 (line)]] | wt | 91.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -13.5) |
| [[Hs 766T (line)]] | wt | 325 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -18.8) |
| [[HT-29 (line)]] | alt | 159 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.495× (z -11.2) |
| [[SW1417 (line)]] | alt | 387 | 1 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 1.74× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~20% of this change | [[Auranofin (drug)]] 5 µM 0.579× (z -10.3) |
| [[A498 (line)]] | wt | 184 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +8.9) ⚠ cell-cycle shift, explains ~14% of this change | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 93.0 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.70× (z +10.1) | — |
| [[PANC-1 (line)]] | alt | 96.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.492× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 171 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 1.76× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -17.1) |
| [[HepG2_C3A (line)]] | wt | 127 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.328× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 60.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.90× (z +9.3) | — |
| [[SHP-77 (line)]] | alt | 137 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 1.99× (z +11.7) | — |
| [[AN3 CA (line)]] | alt | 54.8 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 77.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 37.8 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 91.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 229 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 90.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9013), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPC2]] | +0.59 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[VKORC1]] | +0.56 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[GPR155]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[TSHZ3]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[FYN]] | +0.53 | +0.37 / +0.54 | both halves | 7e-05 |  |
| [[IGFBP2]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[RNF24]] | +0.53 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[DDT]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[CHCHD10]] | +0.52 | +0.40 / +0.49 | both halves | 4e-05 |  |
| [[OST4]] | +0.52 | +0.47 / +0.46 | both halves | 2e-05 |  |
| [[PPP1R2]] | +0.52 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[NDUFA2]] | +0.52 | +0.39 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRAS]] | -0.55 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[ZSCAN29]] | -0.55 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[BNIP2]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[PIGO]] | -0.53 | -0.52 / -0.49 | both halves | 1e-05 |  |
| [[DPP8]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZFP41]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[ZXDB]] | -0.51 | -0.41 / -0.47 | both halves | 4e-05 |  |
| [[ZC3H4]] | -0.50 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[ZNF839]] | -0.50 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[PRELID3B]] | -0.49 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[FAM83H]] | -0.49 | -0.57 / -0.30 | both halves | 2e-04 |  |
| [[MDM4]] | -0.49 | -0.41 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOX]] | B | LOX activity strengthens OXR1's drug response | lines that do not express LOX (27) vs lines expressing it (18) | the lines without LOX respond 0.67× as strongly (z diff +2.65); strongest at Ouabain (Octahydrate) 5 µM: 0.79x vs 0.56x (z diff +3.8) | 0.033 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; target measured in part of the lines; the reference differs; artifact flags |
| [[ZNF521]] | B | ZNF521 activity raises OXR1's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 2.20× lower at baseline in the lines without ZNF521 | 0.036 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |
| [[LOX]] | B | LOX activity raises OXR1's level | lines that do not express LOX (31) vs lines expressing it (19) | 1.66× lower at baseline in the lines without LOX | 0.040 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411 |
| [[ADAMTS14]] | B | ADAMTS14 activity raises OXR1's level | lines that do not express ADAMTS14 (31) vs lines expressing it (19) | 1.87× lower at baseline in the lines without ADAMTS14 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000287335, CARD11, LINC01411 |
| [[PLAG1]] | B | PLAG1 activity raises OXR1's level | lines that do not express PLAG1 (9) vs lines expressing it (41) | 1.76× lower at baseline in the lines without PLAG1 | 0.079 | ⚠ within organs, on part of the lines; also absent: FCGRT; maybe low, not absent |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.55× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.74× the cells of the other lines | 0.008 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Homoharringtonine (drug)]] 0.5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Homoharringtonine 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.22× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.76× the cells of the other lines | 0.021 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Sulfatinib (drug)]] 5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.72× the cells of the other lines | 0.025 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Harringtonine (drug)]] 0.5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Harringtonine 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.38× the cells of the other lines | 0.032 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| [[KIAA1958]] | C | OXR1 activity lowers KIAA1958's level | lines that do not express OXR1 (4) vs lines expressing it (46) | 2.34× higher at baseline in the lines without OXR1 | 0.036 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent |
| cells under [[Entrectinib (drug)]] 5 µM | C | [[LRRCC1]], OXR1 activity lowers the cells' numbers under Entrectinib 5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.28× the cells of the other lines | 0.038 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Rimonabant (drug)]] 5 µM | C | [[LRRCC1]], OXR1 activity lowers the cells' numbers under Rimonabant 5 µM (makes them more sensitive) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 1.20× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.72× the cells of the other lines | 0.039 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.79× the cells of the other lines | 0.042 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | [[LRRCC1]], OXR1 activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express LRRCC1, OXR1 (4) vs lines expressing them (44) | the lines without LRRCC1, OXR1: 0.71× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; also absent: SFXN3, GCA, CDKN1A; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.6, -15.8); signed map (-35.3, 21.0). **Vector** length 102, 26.8% of its response variance represented; |z| ≥ 3 in 1,472 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +5.9 | -2.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | +5.1 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.5 | +1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +2.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Saquinavir (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -16.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.4 | -12.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -20.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.0 | -5.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -4.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.7 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.5 | -14.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -6.9 |

## What is on record

|  |  |
|---|---|
| Name | oxidation resistance 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.1 — chr8:106,270,144-106,752,694 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TLDC3 |
| Gene groups (HGNC) | TLDc domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N573](https://www.uniprot.org/uniprotkb/Q8N573) (Oxidation resistance protein 1):

> Inhibits the activity of the vacuolar-type ATPase (V-ATPase) by inducing disassembly of the V-ATPase complex. Protects the Golgi apparatus lumen from excess acidification by inhibiting V-ATPase ATP hydrolytic activity through interaction with V-ATPase catalytic subunit ATP6V1A, maintaining optimal conditions for glycosylation enzymes (By similarity). Involved in protection from oxidative damage. Protects neuronal cells from oxidative stress (By similarity).

**Summary**, from NCBI Gene [55074](https://www.ncbi.nlm.nih.gov/gene/55074):

> Predicted to enable oxidoreductase activity. Predicted to be involved in response to oxidative stress. Predicted to act upstream of or within several processes, including adult walking behavior; negative regulation of cellular response to oxidative stress; and negative regulation of peptidyl-cysteine S-nitrosylation. Located in mitochondrion. Implicated in cerebellar hyplasia/atrophy, epilepsy, and global developmental delay. [provided by Alliance of Genome Resources, Apr 2025]

**Accessions** — [HGNC:15822](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15822) · Entrez [55074](https://www.ncbi.nlm.nih.gov/gene/55074) · UniProt [Q8N573](https://www.uniprot.org/uniprotkb/Q8N573) · Ensembl [ENSG00000164830](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164830)

## Data

Gene col 9013: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9013); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9013, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9013]; `tensor/DDL_lfc|DDL_z.npy` [9013]; `embed/gene_vectors.npy` [9013]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9013 or target_col == 9013). Every well: [[OXR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OXR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
