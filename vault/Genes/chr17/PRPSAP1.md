---
symbol: "PRPSAP1"
type: "gene"
col: 8437
ensembl_id: "ENSG00000161542"
name: "phosphoribosyl pyrophosphate synthetase associated protein 1"
location: "17q25.1"
module: 38
arm: "+"
pooled_cpm: 42.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PRPSAP1

*phosphoribosyl pyrophosphate synthetase associated protein 1* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.33× (z +42.8, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.666× (z -9.9, q 3e-20, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[QRICH2]] (+0.67, fdr 7e-06, ⚠ same locus), [[TRPV1]] (+0.65, fdr 1e-05), [[SHPK]] (+0.60, fdr 3e-05), [[ING2-DT]] (+0.60, fdr 2e-05); moves opposite to [[ARAF]] (-0.53, fdr 1e-04), [[N6AMT1]] (-0.52, fdr 5e-04), [[MRPL42]] (-0.51, fdr 2e-04).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.33×** | +42.8 | 0e+00 | 47/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +13.7 | 3e-40 | 40/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +9.0 | 5e-17 | 30/49 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +6.9 | 7e-10 | 25/48 (MIA PaCa-2, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +6.6 | 4e-09 | 21/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +4.9 | 1e-04 | 13/48 (KATO III, SW480, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.6 | 4e-04 | 18/48 (NCI-H1792, CFPAC-1, …) | top dose only | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.18× | +4.1 | 0.003 | 14/48 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.077 | 6/48 (Hs 766T, A549, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.14× | +3.2 | 0.077 | 10/48 (LS 180, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 1.13× | +3.2 | 0.077 | 13/48 (PANC-1, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.666×** | -9.9 | 3e-20 | 29/48 (AN3 CA, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.691×** | -9.3 | 3e-18 | 32/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.740×** | -7.6 | 6e-12 | 25/48 (NCI-H460, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.592×** | -6.9 | 6e-10 | 26/48 (LOX-IMVI, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -6.6 | 6e-09 | 23/47 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.787×** | -6.0 | 1e-07 | 23/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.790×** | -5.9 | 2e-07 | 23/48 (J82, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.804×** | -5.5 | 3e-06 | 24/48 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.878× | -4.6 | 2e-04 | 17/48 (NCI-H2347, SNU-1, …) | rises with dose | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.715×** | -4.4 | 6e-04 | 11/34 (A-172, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.888× | -4.2 | 0.001 | 15/48 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **0.726×** | -4.2 | 0.001 | 14/47 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.849× | -4.1 | 0.002 | 15/48 (RPMI-7951, NCI-H2347, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.737×** | -4.0 | 0.002 | 20/49 (LOX-IMVI, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.856× | -3.9 | 0.003 | 8/48 (RKO, A-172, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | 0.857× | -3.9 | 0.004 | 19/48 (SHP-77, LOX-IMVI, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 0.864× | -3.4 | 0.020 | 11/47 (A-172, LOX-IMVI, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.884× | -3.0 | 0.075 | 6/49 (NCI-H661, LoVo, …) | top dose only | plate-row cell shift |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | 0.889× | -3.0 | 0.075 | 7/48 (SW 1271, SW 900, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 34.5 | 3 (1 ⚠) | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.28× (z +26.8) | [[Digitoxin (drug)]] 5 µM 0.313× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.419× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 68.8 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.410× (z -8.9) |
| [[SW480 (line)]] | alt | 34.7 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.19× (z +25.5) | [[Dinaciclib (drug)]] 0.05 µM 0.385× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 68.6 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 70.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +14.4) | [[Digitoxin (drug)]] 5 µM 0.417× (z -8.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.2 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +23.3) | [[Dinaciclib (drug)]] 5 µM 0.351× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.399× (z -8.8) |
| [[C-33 A (line)]] | alt | 39.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.267× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 17.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +19.2) | — |
| [[HCT15 (line)]] | alt | 39.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +10.5) | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 50.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.364× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 80.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +15.7) | — |
| [[Hs 766T (line)]] | wt | 33.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +16.1) | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.121× (z -8.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 28.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +16.6) | — |
| [[NCI-H1573 (line)]] | alt | 26.2 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.12× (z +16.1) | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 40.7 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +17.7) | — |
| [[NCI-H23 (line)]] | alt | 43.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.14× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 39.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.03× (z +21.2) | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 39.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +23.4) | — |
| [[RKO (line)]] | wt | 72.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 48.8 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.52× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 48.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 64.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +13.3) | — |
| [[SW48 (line)]] | wt | 34.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +13.7) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.240× (z -9.6) |
| [[A-172 (line)]] | wt | 63.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +14.6) | — |
| [[A-427 (line)]] | wt | 58.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 37.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.18× (z +20.4) | — |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.168× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 11.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.07× (z +15.2) | — |
| [[BT-474 (line)]] | alt | 20.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +11.1) | — |
| [[C32 (line)]] | wt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +15.5) | — |
| [[CHP-212 (line)]] | wt | 38.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.92× (z +10.8) | — |
| [[COLO 205 (line)]] | alt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.75× (z +14.4) | — |
| [[H4 (line)]] | wt | 62.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +8.9) | — |
| [[HS-578T (line)]] | alt | 55.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +10.9) | — |
| [[HT-29 (line)]] | alt | 27.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.93× (z +16.9) | — |
| [[hTERT-HPNE (line)]] | wt | 105 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[J82 (line)]] | alt | 42.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +11.3) | — |
| [[KATO III (line)]] | alt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.6) | — |
| [[LoVo (line)]] | wt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.03× (z +23.1) | — |
| [[NCI-H2030 (line)]] | alt | 33.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +12.4) | — |
| [[NCI-H2347 (line)]] | alt | 28.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.66× (z +18.2) | — |
| [[SW 900 (line)]] | alt | 21.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +12.1) | — |
| [[SW1417 (line)]] | alt | 28.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.99× (z +16.2) | — |
| [[NCI-H2122 (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[QRICH2]] | +0.67 | +0.62 / +0.69 | both halves | 7e-06 | ⚠ same locus (1.2 kb, same strand: neighbours can correlate without regulation) |
| [[TRPV1]] | +0.65 | +0.49 / +0.73 | both halves | 1e-05 |  |
| [[SHPK]] | +0.60 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[ING2-DT]] | +0.60 | +0.46 / +0.63 | both halves | 2e-05 |  |
| [[C9orf24]] | +0.57 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[L3MBTL2-AS1]] | +0.57 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[C2orf92]] | +0.56 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RABGEF1]] | +0.55 | +0.29 / +0.65 | both halves | 2e-04 |  |
| [[GPR161]] | +0.53 | +0.36 / +0.54 | both halves | 9e-05 |  |
| [[SPSB1]] | +0.53 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[GATD1-DT]] | +0.52 | +0.32 / +0.61 | both halves | 2e-04 |  |
| [[LINC02798]] | +0.51 | +0.51 / +0.45 | both halves | 3e-05 |  |
| [[SFXN5]] | +0.51 | +0.52 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARAF]] | -0.53 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[N6AMT1]] | -0.52 | -0.23 / -0.58 | both halves | 5e-04 |  |
| [[MRPL42]] | -0.51 | -0.31 / -0.56 | both halves | 2e-04 |  |
| [[PEX2]] | -0.50 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[INTS7]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[MRPS31P4]] | -0.49 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[C5orf63]] | -0.48 | -0.29 / -0.47 | both halves | 2e-04 |  |
| [[DTWD2]] | -0.48 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[VPS72]] | -0.48 | -0.22 / -0.57 | both halves | 6e-04 |  |
| [[COG2]] | -0.47 | -0.20 / -0.55 | ⚠ one half (not replicated) | 8e-04 |  |
| [[RBM18]] | -0.46 | -0.16 / -0.58 | ⚠ one half (not replicated) | 0.001 |  |
| [[PIGO]] | -0.46 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[PTAR1]] | -0.45 | -0.28 / -0.52 | both halves | 3e-04 |  |
| [[ABLIM1]] | -0.44 | -0.30 / -0.47 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PRPSAP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 1.4% of all compounds | 0.004 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[C5orf63]] | B | C5orf63 activity lowers PRPSAP1's level | lines that do not express C5orf63 (11) vs lines expressing it (39) | 1.57× higher at baseline in the lines without C5orf63 | 0.018 | ⚠ within organs, on part of the lines; also absent: TSPAN15, TNFRSF10A, ABCC3 |
| [[CCDC120]] | B | CCDC120 activity lowers PRPSAP1's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 1.50× higher at baseline in the lines without CCDC120 | 0.046 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[WNT5B]] | B | WNT5B activity raises PRPSAP1's level | lines that do not express WNT5B (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without WNT5B | 0.051 | ⚠ within organs, on part of the lines; also absent: DPY19L2, TRIML2, VASH1 |
| [[TOP2B]] | B | TOP2B activity lowers PRPSAP1's level | compounds that target TOP2B: 2 of 2 raise it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ABLIM1]] | B | ABLIM1 activity lowers PRPSAP1's level | lines that do not express ABLIM1 (14) vs lines expressing it (36) | 1.28× higher at baseline in the lines without ABLIM1 | 0.086 | ⚠ within organs, on part of the lines; also absent: EVPL, NUP62CL, CCDC68 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.485). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.5, -15.6); signed map (14.4, 2.8). **Vector** length 101, 23.0% of its response variance represented; |z| ≥ 3 in 1,015 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.4 | +42.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +13.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +9.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.3 | +6.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.3 | +2.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.1 | +3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.9 | +6.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.5 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.4 | +1.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -4.1 | -4.1 |
|  | [[NG25 (drug)]] 5 µM |  | -3.6 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -4.6 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -5.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -2.5 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.4 | -2.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.4 | -1.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | phosphoribosyl pyrophosphate synthetase associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:76,309,478-76,384,521 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PAP39 |
| Gene groups (HGNC) | Phosphoribosyl pyrophosphate synthetase associated protein family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14558](https://www.uniprot.org/uniprotkb/Q14558) (Phosphoribosyl pyrophosphate synthase-associated protein 1):

> Seems to play a negative regulatory role in 5-phosphoribose 1-diphosphate synthesis.

**Summary**, from NCBI Gene [5635](https://www.ncbi.nlm.nih.gov/gene/5635):

> Enables identical protein binding activity. Predicted to be involved in 5-phosphoribose 1-diphosphate biosynthetic process and purine nucleotide biosynthetic process. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:9466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9466) · Entrez [5635](https://www.ncbi.nlm.nih.gov/gene/5635) · UniProt [Q14558](https://www.uniprot.org/uniprotkb/Q14558) · Ensembl [ENSG00000161542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161542)

## Data

Gene col 8437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8437); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8437]; `tensor/DDL_lfc|DDL_z.npy` [8437]; `embed/gene_vectors.npy` [8437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8437 or target_col == 8437). Every well: [[PRPSAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PRPSAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
