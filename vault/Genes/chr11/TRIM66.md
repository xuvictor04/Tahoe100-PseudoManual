---
symbol: "TRIM66"
type: "gene"
col: 9304
ensembl_id: "ENSG00000166436"
name: "tripartite motif containing 66"
location: "11p15.4"
module: 124
arm: "+"
pooled_cpm: 45.15
n_lines_expressing: 48
n_dd_up: 23
n_dd_down: 20
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# TRIM66

*tripartite motif containing 66* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +5.9, q 2e-06, up in 29 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.302× (z -14.5, q 8e-45, down in 45 of 46 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.333× (z -13.3, q 5e-38, down in 43 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GABPB1-AS1]] (+0.66, fdr 1e-05), [[LINC01376]] (+0.64, fdr 1e-05), [[TMEM9B-AS1]] (+0.59, fdr 3e-05); moves opposite to [[TPST1]] (-0.51, fdr 7e-04), [[ABAT]] (-0.48, fdr 3e-04), [[MSRB1]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TMEM9B-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.9 | 2e-06 | 29/46 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.39×** | +5.7 | 3e-06 | 27/46 (AsPC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.7 | 3e-06 | 33/46 (HS-578T, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.48×** | +4.8 | 2e-04 | 29/46 (KATO III, LS 180, …) | rises with dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +4.5 | 9e-04 | 24/46 (A-172, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.3 | 0.002 | 27/46 (A498, HT-29, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.014 | 21/46 (HS-578T, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.018 | 22/46 (SW480, HCT15, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.40×** | +3.5 | 0.024 | 20/46 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.024 | 20/46 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.23×** | +3.5 | 0.025 | 23/46 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.3 | 0.044 | 18/46 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.3 | 0.047 | 19/46 (A498, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.30×** | +3.2 | 0.054 | 20/46 (A549, LOX-IMVI, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.054 | 17/46 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.057 | 19/46 (LoVo, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.057 | 16/46 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.302×** | -14.5 | 8e-45 | 45/46 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.303×** | -13.9 | 3e-41 | 42/46 (PANC-1, NCI-H460, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.333×** | -13.3 | 5e-38 | 43/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.334×** | -13.3 | 5e-38 | 42/45 (RKO, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.388×** | -11.4 | 3e-28 | 42/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.529×** | -10.9 | 1e-25 | 39/46 (A549, PANC-1, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.417×** | -10.2 | 3e-22 | 40/45 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.446×** | -9.7 | 1e-20 | 39/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.252×** | -8.3 | 9e-15 | 42/46 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.267×** | -7.9 | 1e-13 | 35/46 (LOX-IMVI, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.571×** | -6.8 | 7e-10 | 34/46 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.589×** | -6.2 | 2e-08 | 27/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.591×** | -6.0 | 1e-07 | 34/46 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.657×** | -5.1 | 2e-05 | 30/46 (SW480, NCI-H460, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.431×** | -5.0 | 2e-05 | 30/41 (HepG2/C3A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.484×** | -4.3 | 5e-04 | 29/46 (SNU-1, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.751×** | -3.4 | 0.022 | 20/46 (SW1417, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.692×** | -3.2 | 0.048 | 18/46 (PANC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.69 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 88.4 | 0 | 14 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.133× (z -20.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.151× (z -18.8) |
| [[PANC-1 (line)]] | alt | 182 | 0 | 13 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.122× (z -22.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.185× (z -18.2) |
| [[LoVo (line)]] | wt | 48.5 | 0 | 8 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.170× (z -17.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.296× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 30.7 | 0 | 8 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -16.1) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.227× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 55.6 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.137× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.258× (z -11.4) |
| [[A-427 (line)]] | wt | 63.1 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.258× (z -11.6) |
| [[C-33 A (line)]] | alt | 54.6 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0956× (z -16.0) |
| [[HOP62 (line)]] | alt | 39.1 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.140× (z -13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 51.7 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0994× (z -15.7) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.220× (z -10.7) |
| [[H4 (line)]] | wt | 32.8 | 0 | 5 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0610× (z -14.2) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HCT15 (line)]] | alt | 73.1 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.201× (z -11.5) |
| [[J82 (line)]] | alt | 30.2 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.246× (z -9.9) |
| [[A549 (line)]] | wt | 38.0 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -18.0) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SK-MEL-2 (line)]] | alt | 41.1 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~82% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.276× (z -8.6) |
| [[SNU-423 (line)]] | alt | 29.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.215× (z -9.7) |
| [[BT-474 (line)]] | alt | 27.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.136× (z -12.1) |
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.260× (z -9.8) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 39.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -13.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.286× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 26.0 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0492× (z -10.2) |
| [[LS 180 (line)]] | wt | 30.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -10.1) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0675× (z -9.2) |
| [[SW1417 (line)]] | alt | 48.1 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -10.4) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.333× (z -8.8) |
| [[C32 (line)]] | wt | 41.2 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.250× (z -8.8) ⚠ cell-cycle shift, explains ~51% of this change |
| [[COLO 205 (line)]] | alt | 37.1 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -10.8) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 44.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -9.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.245× (z -8.8) |
| [[KATO III (line)]] | alt | 31.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.139× (z -11.4) ⚠ cell-cycle shift, explains ~34% of this change |
| [[Panc 03.27 (line)]] | alt | 25.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 33.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0297× (z -23.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[RPMI-7951 (line)]] | alt | 32.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -9.1) ⚠ cell-cycle shift, explains ~78% of this change |
| [[SHP-77 (line)]] | alt | 24.7 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.231× (z -8.9) |
| [[SNU-1 (line)]] | wt | 29.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -15.0) ⚠ cell-cycle shift, explains ~78% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0848× (z -12.0) |
| [[SW48 (line)]] | wt | 58.3 | 0 | 2 | — | [[Ixazomib citrate (drug)]] 5 µM 0.116× (z -12.1) |
| [[A498 (line)]] | wt | 31.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.54× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +10.6) | — |
| [[HS-578T (line)]] | alt | 32.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-172 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.93 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GABPB1-AS1]] | +0.66 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[LINC01376]] | +0.64 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[TMEM9B-AS1]] | +0.59 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[ERMARD]] | +0.59 | +0.64 / +0.41 | both halves | 4e-05 |  |
| [[CBR4]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.56 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[ADCK1]] | +0.56 | +0.59 / +0.44 | both halves | 3e-05 |  |
| [[SIRT5]] | +0.56 | +0.60 / +0.36 | both halves | 9e-05 |  |
| [[TMCC1-DT]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[POLR1HASP]] | +0.55 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[SPOPL-DT]] | +0.54 | +0.54 / +0.43 | both halves | 3e-05 |  |
| [[SLC12A2-DT]] | +0.54 | +0.63 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPST1]] | -0.51 | -0.54 / -0.21 | both halves | 7e-04 |  |
| [[ABAT]] | -0.48 | -0.28 / -0.29 | both halves | 3e-04 |  |
| [[MSRB1]] | -0.48 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[NCMAP]] | -0.47 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[PPARA]] | -0.45 | -0.44 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM9B-AS1]] | B | TMEM9B-AS1 activity raises TRIM66's level | lines that do not express TMEM9B-AS1 (5) vs lines expressing it (45) | 2.18× lower at baseline in the lines without TMEM9B-AS1 | 0.076 | ⚠ within organs, on part of the lines; also absent: TSEN2, SCML2, CAP2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (0.7, 20.4); signed map (30.6, -11.1). **Vector** length 71.7, 18.5% of its response variance represented; |z| ≥ 3 in 1,291 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.6 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.6 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +2.8 | +3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.1 | -0.1 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.7 | -0.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | -2.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.9 | -10.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.9 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -3.5 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.0 | -3.2 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.8 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | tripartite motif containing 66 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:8,612,037-8,682,694 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0298, TIF1D; previously C11orf29 |
| Gene groups (HGNC) | Tripartite motif family; PHD finger proteins; Bromodomain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [O15016](https://www.uniprot.org/uniprotkb/O15016) (Tripartite motif-containing protein 66):

> May function as transcription repressor; The repressive effects are mediated, at least in part, by recruitment of deacetylase activity. May play a role as negative regulator of postmeiotic genes acting through CBX3 complex formation and centromere association (By similarity).

**Summary**, from NCBI Gene [9866](https://www.ncbi.nlm.nih.gov/gene/9866):

> Predicted to enable chromatin binding activity; identical protein binding activity; and zinc ion binding activity. Predicted to act upstream of or within negative regulation of DNA-templated transcription. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29005) · Entrez [9866](https://www.ncbi.nlm.nih.gov/gene/9866) · UniProt [O15016](https://www.uniprot.org/uniprotkb/O15016) · Ensembl [ENSG00000166436](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166436)

## Data

Gene col 9304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9304); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9304]; `tensor/DDL_lfc|DDL_z.npy` [9304]; `embed/gene_vectors.npy` [9304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9304 or target_col == 9304). Every well: [[TRIM66 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIM66.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
