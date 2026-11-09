---
symbol: "FGD4"
type: "gene"
col: 6262
ensembl_id: "ENSG00000139132"
name: "FYVE, RhoGEF and PH domain containing 4"
location: "12p11.21"
module: 98
arm: "+"
pooled_cpm: 157.38
n_lines_expressing: 40
n_dd_up: 26
n_dd_down: 17
n_dd_up_clean: 24
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 21
direction_downstream: 15
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# FGD4

*FYVE, RhoGEF and PH domain containing 4* — 12p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 1.77× (z +11.8, q 1e-29, up in 24 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.504× (z -13.8, q 1e-40, down in 27 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.623× (z -9.9, q 7e-21, down in 34 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EPS8]] (+0.67, fdr 7e-06), [[FKBP5]] (+0.65, fdr 7e-06), [[MAOA]] (+0.65, fdr 7e-06); moves opposite to [[KCNMA1]] (-0.59, fdr 1e-05), [[VEGFC]] (-0.55, fdr 1e-05), [[GJA1]] (-0.55, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[SCNN1A]] → it (grade B ⚠); 15 go from it, the strongest it → [[BMPER]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.77×** | +11.8 | 1e-29 | 24/38 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.69×** | +10.9 | 2e-25 | 20/38 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.68×** | +10.8 | 5e-25 | 38/39 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.38×** | +9.6 | 2e-19 | 25/38 (PANC-1, MIA PaCa-2, …) | all doses, flat | low cells (technical?) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.58×** | +9.5 | 3e-19 | 20/38 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.57×** | +9.4 | 7e-19 | 21/38 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **1.54×** | +9.0 | 2e-17 | 22/38 (A498, Hs 766T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.51×** | +8.5 | 1e-15 | 20/38 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.49×** | +8.4 | 4e-15 | 28/38 (PANC-1, LS 180, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +8.3 | 8e-15 | 20/39 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.47×** | +8.1 | 3e-14 | 21/38 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.47×** | +8.0 | 5e-14 | 19/38 (A498, NCI-H1573, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.46×** | +7.9 | 1e-13 | 21/40 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.44×** | +7.3 | 8e-12 | 20/39 (NCI-H1573, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.28×** | +7.3 | 8e-12 | 19/38 (Hs 766T, A498, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.41×** | +7.2 | 2e-11 | 18/38 (A498, Hs 766T, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.41×** | +7.2 | 3e-11 | 19/38 (NCI-H1573, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6262.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.504×** | -13.8 | 1e-40 | 27/36 (KATO III, LS 180, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.514×** | -12.9 | 2e-35 | 26/36 (SW1417, LoVo, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -9.9 | 7e-21 | 34/38 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.627×** | -9.8 | 2e-20 | 24/39 (LoVo, AsPC-1, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -8.3 | 1e-14 | 26/38 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **0.700×** | -7.5 | 6e-12 | 28/38 (KATO III, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.704×** | -7.4 | 1e-11 | 29/38 (CFPAC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.711×** | -7.2 | 6e-11 | 25/38 (COLO 205, A549, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.765×** | -5.6 | 1e-06 | 22/38 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **0.629×** | -5.1 | 2e-05 | 22/38 (SW480, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 0.847× | -5.0 | 4e-05 | 19/39 (NCI-H2347, BT-474, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.812×** | -4.4 | 5e-04 | 16/38 (HepG2/C3A, CFPAC-1, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 0.875× | -4.0 | 0.003 | 7/38 (CFPAC-1, NCI-H23, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | 0.836× | -3.8 | 0.007 | 17/38 (PANC-1, SNU-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.711×** | -3.7 | 0.007 | 18/38 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.714×** | -3.7 | 0.008 | 14/38 (Panc 03.27, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.025 | 14/37 (NCI-H23, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.740×** | -3.3 | 0.027 | 17/38 (Panc 03.27, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.904× | -3.0 | 0.065 | 1/39 (SNU-1) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.867× | -3.0 | 0.065 | 12/39 (BT-474, CFPAC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 62.1 | 24 (6 ⚠) | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.5 µM 3.54× (z +14.0) | [[Digitoxin (drug)]] 0.5 µM 0.444× (z -9.1) ⚠ cell-cycle shift, explains ~67% of this change |
| [[A498 (line)]] | wt | 107 | 19 | 3 (2 ⚠) | [[Budesonide (drug)]] 0.05 µM 4.05× (z +17.8) | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.518× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 164 | 19 | 3 (3 ⚠) | [[Budesonide (drug)]] 0.05 µM 4.86× (z +18.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.301× (z -13.5) ⚠ toxic |
| [[A549 (line)]] | wt | 61.3 | 19 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 6.38× (z +15.6) | — |
| [[Hs 766T (line)]] | wt | 45.5 | 19 | 0 | [[Budesonide (drug)]] 5 µM 12.8× (z +17.5) | — |
| [[HOP62 (line)]] | alt | 56.5 | 18 (1 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 5.69× (z +15.4) | — |
| [[HS-578T (line)]] | alt | 42.3 | 17 | 0 | [[Clobetasol propionate (drug)]] 5 µM 6.93× (z +13.5) | — |
| [[AsPC-1 (line)]] | alt | 484 | 8 | 6 (5 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.19× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 449 | 3 | 8 (8 ⚠) | [[Budesonide (drug)]] 0.05 µM 2.12× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[CFPAC-1 (line)]] | alt | 208 | 1 | 9 (9 ⚠) | [[Budesonide (drug)]] 5 µM 2.02× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HEC-1-A (line)]] | alt | 350 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -9.9) |
| [[HT-29 (line)]] | alt | 326 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.458× (z -9.4) |
| [[KATO III (line)]] | alt | 369 | 0 | 9 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.148× (z -24.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 289 | 0 | 8 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -17.8) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SW1417 (line)]] | alt | 340 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SW480 (line)]] | alt | 213 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.301× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -10.1) |
| [[LoVo (line)]] | wt | 500 | 0 | 7 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1792 (line)]] | alt | 51.0 | 6 | 0 | [[Budesonide (drug)]] 0.05 µM 3.22× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 165 | 3 | 2 (2 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.61× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -13.7) ⚠ cell-cycle shift, explains ~18% of this change |
| [[A-427 (line)]] | wt | 231 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.61× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[HepG2_C3A (line)]] | wt | 200 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -15.2) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.357× (z -10.1) |
| [[LS 180 (line)]] | wt | 244 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[BT-474 (line)]] | alt | 208 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -16.0) ⚠ cell-cycle shift, explains ~18% of this change |
| [[MIA PaCa-2 (line)]] | alt | 42.6 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 0.05 µM 3.59× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 43.7 | 3 | 0 | [[Budesonide (drug)]] 5 µM 3.56× (z +9.2) | — |
| [[COLO 205 (line)]] | alt | 204 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[J82 (line)]] | alt | 69.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.86× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 80.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -13.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 112 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.258× (z -8.9) |
| [[HCT15 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[SW 1271 (line)]] | alt | 97.5 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0692× (z -10.5) |
| [[SW 900 (line)]] | alt | 97.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.16× (z +8.8) | — |
| [[A-172 (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 27.1 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 38.4 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 47.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.6 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.8 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.8 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 73.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 112 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.2 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 116 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPS8]] | +0.67 | +0.61 / +0.69 | both halves | 7e-06 |  |
| [[FKBP5]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[MAOA]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[GAREM1]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 | **novel candidate** |
| [[ADGRG2]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[KRT7]] | +0.60 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[MT1M]] | +0.59 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SGPP2]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[SCNN1A]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[SH3TC1]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[CCND3]] | +0.58 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[TLE1]] | +0.57 | +0.47 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KCNMA1]] | -0.59 | -0.62 / -0.57 | both halves | 1e-05 |  |
| [[VEGFC]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[GJA1]] | -0.55 | -0.62 / -0.43 | both halves | 3e-05 |  |
| [[CRLF2]] | -0.51 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[SIRLNT]] | -0.49 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[IGFBP3]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[BMPER]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[PTGS2]] | -0.47 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[FBXL13]] | -0.46 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[SLC6A6]] | -0.46 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[LIF]] | -0.45 | -0.43 / -0.46 | both halves | 4e-05 |  |
| [[LINC01411]] | -0.45 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 21, C 0. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCNN1A]] | B | SCNN1A activity raises FGD4's level | lines that do not express SCNN1A (27) vs lines expressing it (23) | 4.08× lower at baseline in the lines without SCNN1A | 1e-04 | ⚠ within organs, on part of the lines; also absent: KDF1, PLEKHG6, CDH1 |
| [[CNKSR1]] | B | CNKSR1 activity raises FGD4's level | lines that do not express CNKSR1 (24) vs lines expressing it (26) | 3.96× lower at baseline in the lines without CNKSR1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SPINT1, SLC52A3, ESRP2 |
| [[SGPP2]] | B | SGPP2 activity raises FGD4's level | lines that do not express SGPP2 (32) vs lines expressing it (18) | 3.90× lower at baseline in the lines without SGPP2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ST14, CATSPERB, TMPRSS4 |
| [[SHROOM3]] | B | SHROOM3 activity raises FGD4's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 2.95× lower at baseline in the lines without SHROOM3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[ARHGEF34P]] | B | ARHGEF34P activity raises FGD4's level | lines that do not express ARHGEF34P (19) vs lines expressing it (31) | 3.07× lower at baseline in the lines without ARHGEF34P | 0.003 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[KCNMA1]] | B | KCNMA1 activity lowers FGD4's level | lines that do not express KCNMA1 (26) vs lines expressing it (24) | 2.82× higher at baseline in the lines without KCNMA1 | 0.007 | ⚠ within organs, on part of the lines; also absent: F2RL2, SIRLNT, SRGN |
| [[AFF3]] | B | AFF3 activity lowers FGD4's level | lines that do not express AFF3 (22) vs lines expressing it (28) | 3.27× higher at baseline in the lines without AFF3 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTX3, DCLK2, SRPX |
| [[ITGA10]] | B | ITGA10 activity lowers FGD4's level | lines that do not express ITGA10 (9) vs lines expressing it (41) | 3.59× higher at baseline in the lines without ITGA10 | 0.015 | ⚠ within organs, on part of the lines; also absent: SLC17A7, ZEB1, BOLA3-DT; maybe low, not absent |
| [[GRAMD2B]] | B | GRAMD2B activity raises FGD4's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 2.65× lower at baseline in the lines without GRAMD2B | 0.020 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[GAREM1]] | B | GAREM1 activity raises FGD4's level | lines that do not express GAREM1 (10) vs lines expressing it (40) | 2.53× lower at baseline in the lines without GAREM1 | 0.025 | ⚠ within organs, on part of the lines; also absent: TESMIN, GRTP1; maybe low, not absent |
| [[MT1F]] | B | MT1F activity raises FGD4's level | lines that do not express MT1F (17) vs lines expressing it (33) | 2.61× lower at baseline in the lines without MT1F | 0.026 | ⚠ within organs, on part of the lines; also absent: CDC42BPG, RASAL1, ENSG00000289862 |
| [[TFCP2L1]] | B | TFCP2L1 activity raises FGD4's level | lines that do not express TFCP2L1 (22) vs lines expressing it (28) | 3.14× lower at baseline in the lines without TFCP2L1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, OCLN, SPINT2 |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BMPER]] | B | FGD4 activity lowers BMPER's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.25× higher at baseline in the lines without FGD4 | 0.010 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[PLEKHA7]] | B | FGD4 activity raises PLEKHA7's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 3.08× lower at baseline in the lines without FGD4 | 0.012 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SIRLNT]] | B | FGD4 activity lowers SIRLNT's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 1.88× higher at baseline in the lines without FGD4 | 0.015 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| cells under [[Omeprazole (drug)]] 0.05 µM | B | FGD4 activity lowers the cells' numbers under Omeprazole 0.05 µM (makes them more sensitive) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 1.25× the cells of the other lines | 0.027 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SHROOM3]] | B | FGD4 activity raises SHROOM3's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.30× lower at baseline in the lines without FGD4 | 0.048 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[CNKSR1]] | B | FGD4 activity raises CNKSR1's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 3.34× lower at baseline in the lines without FGD4 | 0.050 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | B | FGD4 activity raises the cells' numbers under Vinblastine (sulfate) 0.05 µM (protects the cells) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 0.82× the cells of the other lines | 0.058 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[REPS2]] | B | FGD4 activity raises REPS2's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.36× lower at baseline in the lines without FGD4 | 0.060 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[VSIR]] | B | FGD4 activity raises VSIR's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without FGD4 | 0.070 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| [[SCNN1A]] | B | FGD4 activity raises SCNN1A's level | lines that do not express FGD4 (10) vs lines expressing it (40) | 4.30× lower at baseline in the lines without FGD4 | 0.074 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| cells under [[vincristine (drug)]] 5 µM | B | FGD4 activity raises the cells' numbers under vincristine 5 µM (protects the cells) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 0.63× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |
| cells under [[Lactate (calcium) (drug)]] 0.05 µM | B | FGD4 activity lowers the cells' numbers under Lactate (calcium) 0.05 µM (makes them more sensitive) | lines that do not express FGD4 (10) vs lines expressing it (38) | the lines without FGD4: 1.16× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: PARD6B, CARD10, VAMP8; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.5, 15.7); signed map (17.3, 30.4). **Vector** length 137, 45.2% of its response variance represented; |z| ≥ 3 in 1,435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +8.0 | +9.6 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +7.0 | +8.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +6.8 | +11.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.8 | +9.4 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +6.8 | +9.5 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +6.6 | +7.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -1.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.6 | -7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.4 | -9.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.9 | -8.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.4 | -3.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | FYVE, RhoGEF and PH domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.21 — chr12:32,399,558-32,646,050 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FRABP, frabin, ZFYVE6, CMT4H |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 11 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96M96](https://www.uniprot.org/uniprotkb/Q96M96) (FYVE, RhoGEF and PH domain-containing protein 4):

> Activates CDC42, a member of the Ras-like family of Rho- and Rac proteins, by exchanging bound GDP for free GTP. Plays a role in regulating the actin cytoskeleton and cell shape. Activates MAPK8 (By similarity).

**Summary**, from NCBI Gene [121512](https://www.ncbi.nlm.nih.gov/gene/121512):

> This gene encodes a protein that is involved in the regulation of the actin cytoskeleton and cell shape. This protein contains an actin filament-binding domain, which together with its Dbl homology domain and one of its pleckstrin homology domains, can form microspikes. This protein can activate MAPK8 independently of the actin filament-binding domain, and it is also involved in the activation of CDC42 via the exchange of bound GDP for free GTP. The activation of CDC42 also enables this protein …

**Accessions** — [HGNC:19125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19125) · Entrez [121512](https://www.ncbi.nlm.nih.gov/gene/121512) · UniProt [Q96M96](https://www.uniprot.org/uniprotkb/Q96M96) · Ensembl [ENSG00000139132](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139132)

## Data

Gene col 6262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6262); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6262]; `tensor/DDL_lfc|DDL_z.npy` [6262]; `embed/gene_vectors.npy` [6262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6262 or target_col == 6262). Every well: [[FGD4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGD4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
