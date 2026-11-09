---
symbol: "OSBPL1A"
type: "gene"
col: 6521
ensembl_id: "ENSG00000141447"
name: "oxysterol binding protein like 1A"
location: "18q11.2"
module: 57
arm: "+"
pooled_cpm: 80.56
n_lines_expressing: 48
n_dd_up: 25
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# OSBPL1A

*oxysterol binding protein like 1A* — 18q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (6 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 1.99× (z +17.4, q 0e+00, up in 37 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.651× (z -11.5, q 6e-28, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAVER2]] (+0.66, fdr 7e-06), [[CASP6]] (+0.65, fdr 7e-06), [[EPDR1]] (+0.64, fdr 9e-06); moves opposite to [[SLC30A7]] (-0.55, fdr 2e-05), [[BCL2L12]] (-0.52, fdr 2e-05), [[LRWD1]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6521.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **1.99×** | +17.4 | 0e+00 | 37/46 (A498, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.78×** | +15.5 | 0e+00 | 36/46 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.75×** | +15.0 | 0e+00 | 34/46 (A498, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.98×** | +13.1 | 8e-37 | 34/47 (A498, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.21×** | +10.8 | 3e-25 | 32/43 (A-427, A498, …) | all doses, flat | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +10.7 | 1e-24 | 32/47 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.25×** | +8.4 | 2e-15 | 28/46 (AsPC-1, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.37×** | +8.4 | 4e-15 | 32/46 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.21×** | +7.2 | 5e-11 | 20/46 (A-172, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +6.8 | 6e-10 | 24/42 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.27×** | +6.4 | 7e-09 | 23/46 (A-172, C32, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +6.4 | 7e-09 | 26/46 (A-172, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +6.0 | 8e-08 | 22/46 (A-427, C32, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.54×** | +5.9 | 2e-07 | 26/45 (KATO III, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +5.8 | 3e-07 | 23/47 (SW480, BT-474, …) | two highest doses |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.23×** | +5.6 | 7e-07 | 22/46 (HS-578T, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.46×** | +5.2 | 7e-06 | 24/46 (KATO III, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.20× | +4.6 | 1e-04 | 19/46 (RKO, SK-MEL-2, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.18× | +4.5 | 2e-04 | 14/46 (A-172, NCI-H1792, …) | top dose only |  |
| [[Afatinib (drug)]] 5 µM |  | 1.19× | +4.5 | 2e-04 | 16/47 (J82, C32, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.12× | +4.2 | 7e-04 | 16/46 (CFPAC-1, NCI-H1573, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6521.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.651×** | -11.5 | 6e-28 | 32/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.686×** | -10.1 | 1e-21 | 31/46 (AsPC-1, C-33 A, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.691×** | -9.9 | 5e-21 | 29/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.691×** | -9.9 | 5e-21 | 30/46 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -9.9 | 6e-21 | 30/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -9.7 | 5e-20 | 28/46 (PANC-1, A498, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.747×** | -7.8 | 4e-13 | 26/46 (AsPC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.769×** | -7.0 | 1e-10 | 25/46 (SNU-1, AsPC-1, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.844× | -6.4 | 9e-09 | 23/46 (HEC-1-A, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.636×** | -6.2 | 4e-08 | 22/47 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.850× | -6.2 | 4e-08 | 22/47 (MIA PaCa-2, CHP-212, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | 0.863× | -5.6 | 1e-06 | 22/46 (PANC-1, A549, …) | two highest doses | composition shift |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.832×** | -4.9 | 4e-05 | 22/46 (C-33 A, AsPC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.838× | -4.7 | 9e-05 | 17/45 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.839× | -4.7 | 1e-04 | 19/46 (CHP-212, HEC-1-A, …) | two highest doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.805×** | -3.0 | 0.087 | 9/46 (SHP-77, SW480, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.890× | -2.9 | 0.087 | 12/45 (SW480, A-172, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.859× | -2.9 | 0.096 | 6/46 (A498, J82, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6521. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 125 | 1 (1 ⚠) | 8 (4 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.71× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -22.9) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -19.6) |
| [[A498 (line)]] | wt | 56.1 | 5 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.58× (z +23.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.393× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 175 | 2 | 5 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.87× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.277× (z -16.9) |
| [[KATO III (line)]] | alt | 50.9 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 5.77× (z +17.2) | [[Panobinostat (drug)]] 5 µM 0.345× (z -10.4) ⚠ cell-cycle shift, explains ~24% of this change |
| [[SW480 (line)]] | alt | 81.0 | 0 | 7 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -19.0) |
| [[HEC-1-A (line)]] | alt | 97.4 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.48× (z +17.0) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.608× (z -9.6) |
| [[RKO (line)]] | wt | 105 | 3 | 3 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.402× (z -9.9) |
| [[A-427 (line)]] | wt | 172 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.49× (z +19.7) | [[Dinaciclib (drug)]] 0.05 µM 0.508× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 52.6 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.18× (z +12.0) | — |
| [[C32 (line)]] | wt | 99.8 | 5 | 0 | [[Auranofin (drug)]] 5 µM 3.16× (z +11.9) | — |
| [[HS-578T (line)]] | alt | 70.5 | 2 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.46× (z +12.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.292× (z -12.1) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 1 | 4 (3 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.80× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -14.1) ⚠ cell-cycle shift, explains ~7% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.209× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 61.2 | 3 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.12× (z +14.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.474× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 63.2 | 0 | 5 (3 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.360× (z -13.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.503× (z -8.9) |
| [[SNU-1 (line)]] | wt | 159 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.379× (z -10.9) |
| [[C-33 A (line)]] | alt | 150 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -13.0) |
| [[LoVo (line)]] | wt | 79.9 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.34× (z +11.5) | — |
| [[SW1417 (line)]] | alt | 107 | 3 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.52× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -10.0) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A549 (line)]] | wt | 55.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -13.8) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.386× (z -10.3) |
| [[AN3 CA (line)]] | alt | 153 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -12.3) ⚠ cell-cycle shift, explains ~87% of this change |
| [[CFPAC-1 (line)]] | alt | 42.3 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[HOP62 (line)]] | alt | 35.7 | 3 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.54× (z +12.8) | — |
| [[HT-29 (line)]] | alt | 55.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.1) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.47× (z +10.2) | — |
| [[A-172 (line)]] | wt | 72.4 | 2 (1 ⚠) | 0 | [[Ponatinib (drug)]] 5 µM 2.42× (z +9.5) | — |
| [[J82 (line)]] | alt | 51.7 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.39× (z +12.4) | — |
| [[LOX-IMVI (line)]] | wt | 58.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -12.3) ⚠ cell-cycle shift, explains ~87% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.440× (z -8.7) |
| [[NCI-H1573 (line)]] | alt | 42.4 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.00× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 3.02× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 185 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.4) ⚠ cell-cycle shift, explains ~7% of this change |
| [[COLO 205 (line)]] | alt | 42.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 88.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.343× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 45.2 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.436× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 71.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -9.3) ⚠ cell-cycle shift, explains ~87% of this change |
| [[Panc 03.27 (line)]] | alt | 46.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +9.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 83.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -9.3) |
| [[SHP-77 (line)]] | alt | 92.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -10.8) ⚠ cell-cycle shift, explains ~87% of this change |
| [[SK-MEL-2 (line)]] | alt | 92.1 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.59× (z +9.0) | — |
| [[SW 900 (line)]] | alt | 42.8 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 3.23× (z +9.3) | — |
| [[SW48 (line)]] | wt | 123 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.402× (z -9.1) |
| [[H4 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 80.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 68.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 66.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 86.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6521), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAVER2]] | +0.66 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[CASP6]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EPDR1]] | +0.64 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[GNPDA2]] | +0.62 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[CAP2]] | +0.60 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[SMO]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CUL5]] | +0.59 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[HSPB1]] | +0.58 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[NUDT9]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.57 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[TYW3]] | +0.57 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[EFCAB7]] | +0.57 | +0.57 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC30A7]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[BCL2L12]] | -0.52 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[LRWD1]] | -0.52 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[MYL12A]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TRIOBP]] | -0.51 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[SLC25A44]] | -0.50 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[PPP1CA]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[AHRR]] | -0.49 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[TXNDC17]] | -0.49 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ATG7]] | -0.48 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TIMP1]] | -0.48 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[CFL1]] | -0.48 | -0.39 / -0.52 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises OSBPL1A's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without ANK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises OSBPL1A's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.397). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-19.3, -7.8); signed map (-26.7, -22.2). **Vector** length 130, 37.7% of its response variance represented; |z| ≥ 3 in 1,481 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.2 | +15.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +10.9 | +17.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.8 | +15.0 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.2 | +10.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.6 | +8.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +7.6 | +8.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +7.0 | +13.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.5 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.3 | -11.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.0 | -9.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | -3.9 | -9.9 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.8 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -6.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -1.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q11.2 — chr18:24,162,045-24,397,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORP-1, ORP1; previously OSBPL1B |
| Gene groups (HGNC) | Ankyrin repeat domain containing; Oxysterol binding proteins |
| Reactome | 9 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Processing of antigen in germinal center B cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BXW6](https://www.uniprot.org/uniprotkb/Q9BXW6) (Oxysterol-binding protein-related protein 1):

> Binds phospholipids; exhibits strong binding to phosphatidic acid and weak binding to phosphatidylinositol 3-phosphate (By similarity). Stabilizes GTP-bound RAB7A on late endosomes/lysosomes and alters functional properties of late endocytic compartments via its interaction with RAB7A. Binds 25-hydroxycholesterol and cholesterol.

**Summary**, from NCBI Gene [114876](https://www.ncbi.nlm.nih.gov/gene/114876):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain, although some members contain only the sterol-binding domain. Transcript variants derived from alternative promoter usage and/or alternative splicing exist; they encode different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16398](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16398) · Entrez [114876](https://www.ncbi.nlm.nih.gov/gene/114876) · UniProt [Q9BXW6](https://www.uniprot.org/uniprotkb/Q9BXW6) · Ensembl [ENSG00000141447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141447)

## Data

Gene col 6521: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6521); `tables/drug_effects.parquet` (77 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6521, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6521]; `tensor/DDL_lfc|DDL_z.npy` [6521]; `embed/gene_vectors.npy` [6521]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6521 or target_col == 6521). Every well: [[OSBPL1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
