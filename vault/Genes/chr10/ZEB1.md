---
symbol: "ZEB1"
type: "gene"
col: 7294
ensembl_id: "ENSG00000148516"
name: "zinc finger E-box binding homeobox 1"
location: "10p11.22"
module: 110
arm: "+"
pooled_cpm: 294.25
n_lines_expressing: 41
n_dd_up: 12
n_dd_down: 31
n_dd_up_clean: 10
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/110"]
generated_by: "tahoemap"
---

# ZEB1

*zinc finger E-box binding homeobox 1* — 10p11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.50× (z +8.8, q 1e-15, up in 31 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.425× (z -17.8, q 0e+00, down in 31 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.542× (z -13.3, q 8e-38, down in 30 of 39 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CORO2B]] (+0.66, fdr 7e-06), [[KIAA1549L]] (+0.62, fdr 1e-05), [[LRRC8C]] (+0.61, fdr 1e-05); moves opposite to [[MBNL2]] (-0.50, fdr 3e-05), [[PEX13]] (-0.49, fdr 5e-05), [[ZBTB5]] (-0.49, fdr 5e-05).
> It is in [[Module 110]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LINC02509]] → it (grade B ⚠); 8 go from it, the strongest it → [[RASA3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7294.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +8.8 | 1e-15 | 31/39 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.40×** | +7.3 | 9e-11 | 28/39 (SW480, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.35×** | +6.4 | 2e-08 | 25/39 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.4 | 3e-08 | 22/39 (A498, COLO 205, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.0 | 2e-07 | 23/39 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.34×** | +5.9 | 4e-07 | 27/39 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.8 | 6e-07 | 24/39 (HS-578T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.3 | 9e-06 | 21/38 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.26×** | +5.0 | 3e-05 | 21/39 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.16× | +4.7 | 1e-04 | 17/39 (CFPAC-1, A498, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.23×** | +4.5 | 4e-04 | 20/39 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.18× | +3.6 | 0.015 | 15/39 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.025 | 18/39 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 1.17× | +3.4 | 0.030 | 17/39 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.3 | 0.039 | 13/39 (SW480, SW 900, …) | all doses, stronger at high dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.049 | 17/39 (HEC-1-A, H4, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7294.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.425×** | -17.8 | 0e+00 | 31/35 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.521×** | -14.1 | 1e-42 | 31/40 (SNU-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.542×** | -13.3 | 8e-38 | 30/39 (SNU-1, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.545×** | -13.1 | 4e-37 | 32/39 (COLO 205, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.663×** | -8.9 | 8e-17 | 25/39 (COLO 205, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.644×** | -8.8 | 1e-16 | 25/36 (LOX-IMVI, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.757×** | -8.5 | 2e-15 | 30/39 (RKO, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.689×** | -7.7 | 8e-13 | 31/38 (SNU-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.714×** | -7.3 | 3e-11 | 30/39 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.724×** | -7.0 | 2e-10 | 26/39 (RKO, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.768×** | -6.1 | 6e-08 | 24/41 (C32, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.762×** | -5.6 | 8e-07 | 25/39 (HOP62, C32, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.825×** | -5.6 | 1e-06 | 21/40 (MIA PaCa-2, HOP62, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.773×** | -5.6 | 1e-06 | 24/40 (C32, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.771×** | -5.4 | 3e-06 | 25/39 (HOP62, C32, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.586×** | -5.1 | 1e-05 | 27/38 (H4, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.786×** | -5.0 | 2e-05 | 25/39 (C32, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.792×** | -5.0 | 2e-05 | 20/39 (RKO, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.800×** | -5.0 | 2e-05 | 22/40 (RKO, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.780×** | -4.9 | 2e-05 | 23/39 (RKO, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7294. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 190 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -13.0) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.372× (z -11.9) |
| [[HOP62 (line)]] | alt | 359 | 0 | 13 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.399× (z -10.7) |
| [[SNU-1 (line)]] | wt | 1,101 | 0 | 12 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0715× (z -33.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.327× (z -14.8) |
| [[SW480 (line)]] | alt | 280 | 9 (3 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.72× (z +14.4) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -12.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 718 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.370× (z -14.3) |
| [[RKO (line)]] | wt | 1,185 | 0 | 10 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.281× (z -20.6) |
| [[A549 (line)]] | wt | 330 | 4 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +16.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.29× (z +13.6) | [[Dinaciclib (drug)]] 0.5 µM 0.341× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.545× (z -10.3) |
| [[HS-578T (line)]] | alt | 437 | 3 (1 ⚠) | 6 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.66× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -11.7) |
| [[A498 (line)]] | wt | 239 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +18.6) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.11× (z +15.8) | [[Dinaciclib (drug)]] 0.5 µM 0.352× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.495× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 752 | 2 (1 ⚠) | 6 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +11.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -19.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.433× (z -11.6) |
| [[CFPAC-1 (line)]] | alt | 252 | 5 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.80× (z +22.6) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.55× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 105 | 3 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +16.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.86× (z +13.6) | [[Belinostat (drug)]] 5 µM 0.122× (z -18.7) |
| [[PANC-1 (line)]] | alt | 405 | 1 | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.386× (z -14.6) |
| [[AN3 CA (line)]] | alt | 1,130 | 0 | 7 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -17.9) ⚠ cell-cycle shift, explains ~6% of this change |
| [[MIA PaCa-2 (line)]] | alt | 462 | 0 | 7 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.590× (z -20.8) ⚠ position not correctable · without an alert: [[Panobinostat (drug)]] 5 µM 0.455× (z -9.2) |
| [[SW 900 (line)]] | alt | 276 | 6 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.1) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.38× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.420× (z -11.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 526 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.264× (z -14.5) |
| [[NCI-H1573 (line)]] | alt | 107 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.44× (z +12.0) | [[Belinostat (drug)]] 0.5 µM 0.346× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 448 | 4 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.25× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 367 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -14.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 373 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -27.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.420× (z -12.1) |
| [[HepG2_C3A (line)]] | wt | 457 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +9.7) ⚠ cell-cycle shift, explains ~6% of this change | [[Dinaciclib (drug)]] 5 µM 0.194× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.375× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 188 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.94× (z +10.1) | [[Dinaciclib (drug)]] 0.05 µM 0.470× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 476 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.356× (z -9.7) |
| [[SW48 (line)]] | wt | 99.1 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.216× (z -9.9) |
| [[HEC-1-A (line)]] | alt | 77.7 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 1.95× (z +9.4) | — |
| [[NCI-H23 (line)]] | alt | 259 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.394× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.535× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 648 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.411× (z -8.9) |
| [[SNU-423 (line)]] | alt | 273 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +14.9) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 1.98× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 314 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.410× (z -9.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 484 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.298× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 184 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.7) ⚠ cell-cycle shift, explains ~6% of this change | — |
| [[SHP-77 (line)]] | alt | 299 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.339× (z -13.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 36.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 264 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.7 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 39.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 40.3 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 26.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 240 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 295 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 98.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 60.9 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 352 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 64.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7294), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CORO2B]] | +0.66 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[KIAA1549L]] | +0.62 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[LRRC8C]] | +0.61 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[SLC4A7]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SH2B3]] | +0.61 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_COMPLEMENT |
| [[SPRY4]] | +0.61 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[B4GALT6]] | +0.59 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.58 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[MYO10]] | +0.58 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[ARHGAP31]] | +0.57 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[SPRY4-AS1]] | +0.57 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[KBTBD8]] | +0.57 | +0.37 / +0.58 | both halves | 8e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBNL2]] | -0.50 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[PEX13]] | -0.49 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[ZBTB5]] | -0.49 | -0.44 / -0.40 | both halves | 5e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02509]] | B | LINC02509 activity raises ZEB1's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 2.37× lower at baseline in the lines without LINC02509 | 0.020 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2 |
| [[NEK10]] | B | NEK10 activity raises ZEB1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 2.66× lower at baseline in the lines without NEK10 | 0.057 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |
| [[RASSF8]] | B | RASSF8 activity raises ZEB1's level | lines that do not express RASSF8 (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without RASSF8 | 0.061 | ⚠ within organs, on part of the lines; also absent: RASSF8-AS1, KCNG1, B4GALNT1 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RASA3]] | B | ZEB1 activity raises RASA3's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 2.25× lower at baseline in the lines without ZEB1 | 0.011 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[NBPF20]] | B | ZEB1 activity raises NBPF20's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 2.02× lower at baseline in the lines without ZEB1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[NEK10]] | B | ZEB1 activity raises NEK10's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 2.75× lower at baseline in the lines without ZEB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[NBPF9]] | B | ZEB1 activity raises NBPF9's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 1.98× lower at baseline in the lines without ZEB1 | 0.035 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[PARVB]] | B | ZEB1 activity raises PARVB's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 3.21× lower at baseline in the lines without ZEB1 | 0.058 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[NBPF15]] | B | ZEB1 activity raises NBPF15's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 1.95× lower at baseline in the lines without ZEB1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |
| [[NBPF8]] | B | ZEB1 activity strengthens NBPF8's drug response | lines that do not express ZEB1 (9) vs lines expressing it (37) | the lines without ZEB1 respond 0.20× as strongly (z diff +2.14); rises at some drug-doses, falls at others (27% from rises): Panobinostat 5 µM: 0.99x vs 0.52x (z diff +4.1); Panobinostat 0.5 µM: 0.94x vs 0.54x (z diff +3.7); Daptomycin 5 µM: 1.11x vs 1.43x (z diff +1.8) | 0.060 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1; target measured in part of the lines; rises at some drug-doses, falls at others; artifact flags |
| [[IQCJ-SCHIP1]] | B | ZEB1 activity raises IQCJ-SCHIP1's level | lines that do not express ZEB1 (9) vs lines expressing it (41) | 3.04× lower at baseline in the lines without ZEB1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ITGA10, LIX1L, BRSK1 |

## Where it sits

- **Module**: [[Module 110]]; 43 genes; every member is in the + arm (projection on the module's main direction 0.747). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.9, 6.6); signed map (11.3, 48.0). **Vector** length 117, 37.3% of its response variance represented; |z| ≥ 3 in 1,540 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.9 | +5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.5 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +5.3 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | -2.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.4 | +2.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | -1.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.0 | -6.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.1 | -5.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.7 | -5.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.5 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.5 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.3 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger E-box binding homeobox 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p11.22 — chr10:31,318,495-31,529,814 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BZP, ZEB, AREB6, NIL-2-A, Zfhep, Zfhx1a, FECD6; previously TCF8, PPCD3 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; ZF class homeoboxes and pseudogenes |
| Hallmark sets | COMPLEMENT |
| Reactome | 15 pathways, smallest: Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition; Negative Regulation of CDH1 Gene Transcription; Regulation of CDH1 Gene Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [P37275](https://www.uniprot.org/uniprotkb/P37275) (Zinc finger E-box-binding homeobox 1):

> Acts as a transcriptional repressor. Inhibits interleukin-2 (IL-2) gene expression. Enhances or represses the promoter activity of the ATP1A1 gene depending on the quantity of cDNA and on the cell type. Represses E-cadherin promoter and induces an epithelial-mesenchymal transition (EMT) by recruiting SMARCA4/BRG1. Represses BCL6 transcription in the presence of the corepressor CTBP1. Positively regulates neuronal differentiation. Represses RCOR1 transcription activation during neurogenesis. …

**Summary**, from NCBI Gene [6935](https://www.ncbi.nlm.nih.gov/gene/6935):

> This gene encodes a zinc finger transcription factor. The encoded protein likely plays a role in transcriptional repression of interleukin 2. Mutations in this gene have been associated with posterior polymorphous corneal dystrophy-3 and late-onset Fuchs endothelial corneal dystrophy. Alternatively spliced transcript variants encoding different isoforms have been described.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:11642](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11642) · Entrez [6935](https://www.ncbi.nlm.nih.gov/gene/6935) · UniProt [P37275](https://www.uniprot.org/uniprotkb/P37275) · Ensembl [ENSG00000148516](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148516)

## Data

Gene col 7294: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7294); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7294, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7294]; `tensor/DDL_lfc|DDL_z.npy` [7294]; `embed/gene_vectors.npy` [7294]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7294 or target_col == 7294). Every well: [[ZEB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZEB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
