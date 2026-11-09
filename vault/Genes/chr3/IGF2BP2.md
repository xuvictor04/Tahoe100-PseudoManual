---
symbol: "IGF2BP2"
type: "gene"
col: 1061
ensembl_id: "ENSG00000073792"
name: "insulin like growth factor 2 mRNA binding protein 2"
location: "3q27.2"
module: 120
arm: "+"
pooled_cpm: 486.47
n_lines_expressing: 47
n_dd_up: 22
n_dd_down: 28
n_dd_up_clean: 16
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 8
tags: ["gene", "module/120"]
generated_by: "tahoemap"
---

# IGF2BP2

*insulin like growth factor 2 mRNA binding protein 2* — 3q27.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.94× (z +28.1, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.291× (z -36.9, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRNP1]] (+0.65, fdr 7e-06), [[SVIL]] (+0.63, fdr 1e-05), [[SRGAP1]] (+0.59, fdr 2e-05); moves opposite to [[DERL1]] (-0.55, fdr 5e-05), [[ATPAF1]] (-0.52, fdr 5e-05), [[ANAPC10]] (-0.50, fdr 4e-05).
> It is in [[Module 120]], a single-armed module (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[AKAP12]] → it (grade B ⚠); 8 go from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.94×** | +28.1 | 0e+00 | 38/45 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.15×** | +22.9 | 0e+00 | 43/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +17.1 | 0e+00 | 42/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.77×** | +16.4 | 0e+00 | 42/45 (MIA PaCa-2, A549, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.67×** | +15.3 | 0e+00 | 41/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.62×** | +14.5 | 1e-45 | 42/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.51×** | +12.3 | 1e-32 | 30/45 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +11.0 | 2e-26 | 31/44 (COLO 205, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.40×** | +10.1 | 2e-22 | 31/45 (NCI-H1573, C32, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **2.03×** | +9.6 | 5e-20 | 35/46 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.93×** | +8.9 | 4e-17 | 40/45 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.35×** | +8.7 | 2e-16 | 31/44 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +8.3 | 3e-15 | 29/45 (MIA PaCa-2, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.21×** | +8.2 | 8e-15 | 24/46 (NCI-H1573, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.28×** | +7.3 | 1e-11 | 27/44 (NCI-H1573, C32, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +5.8 | 2e-07 | 25/45 (NCI-H1573, C32, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +5.7 | 4e-07 | 23/44 (C32, NCI-H1573, …) | rises with dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.41×** | +4.7 | 1e-04 | 26/45 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.001 | 7/45 (HEC-1-A, SW 900, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.14× | +3.7 | 0.006 | 13/46 (A498, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 22 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.291×** | -36.9 | 0e+00 | 45/45 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.322×** | -33.9 | 0e+00 | 44/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.480×** | -22.0 | 0e+00 | 41/45 (HepG2/C3A, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.625×** | -19.9 | 0e+00 | 35/46 (LOX-IMVI, SNU-423, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.548×** | -17.3 | 0e+00 | 42/44 (HepG2/C3A, SW1417, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.566×** | -17.0 | 0e+00 | 38/46 (CHP-212, RKO, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.564×** | -16.5 | 0e+00 | 36/41 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.620×** | -13.2 | 6e-38 | 34/42 (HOP62, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.710×** | -9.8 | 5e-21 | 35/45 (LOX-IMVI, SNU-423, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.716×** | -9.6 | 4e-20 | 38/47 (SNU-423, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.739×** | -9.0 | 1e-17 | 32/45 (RKO, LoVo, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.808×** | -9.0 | 1e-17 | 26/45 (J82, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **0.760×** | -8.2 | 1e-14 | 30/45 (PANC-1, HS-578T, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.770×** | -7.8 | 2e-13 | 34/45 (SW1417, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.805×** | -6.5 | 3e-09 | 24/45 (HepG2/C3A, CHP-212, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.678×** | -5.3 | 4e-06 | 35/45 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.839× | -5.2 | 5e-06 | 20/44 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.868× | -5.0 | 2e-05 | 13/45 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.850× | -4.9 | 3e-05 | 20/45 (KATO III, J82, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.880× | -4.8 | 5e-05 | 17/45 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | 0.846× | -4.6 | 9e-05 | 17/44 (NCI-H460, C32, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.714×** | -4.6 | 1e-04 | 23/44 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.893× | -4.5 | 2e-04 | 10/46 (PANC-1, NCI-H460, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.862× | -4.2 | 5e-04 | 14/44 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.737×** | -4.1 | 8e-04 | 25/45 (HOP62, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 0.882× | -4.1 | 9e-04 | 14/46 (NCI-H460, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.745×** | -4.0 | 0.001 | 24/45 (LoVo, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 451 | 14 (6 ⚠) | 10 (8 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.38× (z +19.7) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.95× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.295× (z -19.6) |
| [[PANC-1 (line)]] | alt | 692 | 10 (4 ⚠) | 12 (10 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.76× (z +26.0) | [[Panobinostat (drug)]] 5 µM 0.234× (z -28.5) |
| [[LOX-IMVI (line)]] | wt | 895 | 8 (1 ⚠) | 13 (11 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +17.8) | [[Panobinostat (drug)]] 5 µM 0.175× (z -29.8) |
| [[NCI-H1573 (line)]] | alt | 255 | 12 (4 ⚠) | 9 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +29.3) | [[Panobinostat (drug)]] 5 µM 0.342× (z -15.5) |
| [[SW480 (line)]] | alt | 618 | 10 (3 ⚠) | 11 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.07× (z +22.5) | [[Panobinostat (drug)]] 5 µM 0.184× (z -34.1) |
| [[RKO (line)]] | wt | 843 | 8 (3 ⚠) | 11 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +30.2) | [[Panobinostat (drug)]] 5 µM 0.275× (z -19.1) |
| [[HepG2_C3A (line)]] | wt | 895 | 6 (2 ⚠) | 12 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.34× (z +15.3) | [[Panobinostat (drug)]] 5 µM 0.142× (z -35.1) |
| [[HEC-1-A (line)]] | alt | 919 | 5 (2 ⚠) | 10 (8 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.94× (z +11.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.51× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.291× (z -22.4) |
| [[HOP62 (line)]] | alt | 691 | 3 | 12 (10 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +21.1) | [[Panobinostat (drug)]] 5 µM 0.248× (z -22.1) |
| [[SW1417 (line)]] | alt | 648 | 6 (1 ⚠) | 9 (7 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.266× (z -25.6) |
| [[A549 (line)]] | wt | 213 | 10 (3 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +27.2) | [[Panobinostat (drug)]] 5 µM 0.244× (z -21.4) |
| [[RPMI-7951 (line)]] | alt | 451 | 6 (2 ⚠) | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.363× (z -17.0) |
| [[AsPC-1 (line)]] | alt | 528 | 7 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +20.5) | [[Panobinostat (drug)]] 5 µM 0.186× (z -29.3) |
| [[SNU-423 (line)]] | alt | 606 | 3 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.169× (z -32.3) |
| [[HT-29 (line)]] | alt | 703 | 2 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +16.3) | [[Panobinostat (drug)]] 5 µM 0.154× (z -24.8) |
| [[KATO III (line)]] | alt | 499 | 6 (2 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.271× (z -22.3) |
| [[NCI-H23 (line)]] | alt | 229 | 8 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +37.8) | [[Panobinostat (drug)]] 5 µM 0.242× (z -22.0) |
| [[SW 900 (line)]] | alt | 285 | 9 (4 ⚠) | 3 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.342× (z -16.2) |
| [[LoVo (line)]] | wt | 593 | 2 (1 ⚠) | 9 (7 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.73× (z +11.2) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 2.79× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.132× (z -43.4) |
| [[NCI-H460 (line)]] | wt | 190 | 6 (2 ⚠) | 5 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.338× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 1,105 | 0 | 11 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.217× (z -26.3) |
| [[A-427 (line)]] | wt | 446 | 7 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.05× (z +31.9) | [[Panobinostat (drug)]] 5 µM 0.255× (z -21.9) |
| [[C-33 A (line)]] | alt | 378 | 6 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.20× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.398× (z -13.9) |
| [[CFPAC-1 (line)]] | alt | 785 | 2 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +18.8) | [[Panobinostat (drug)]] 5 µM 0.248× (z -23.8) |
| [[HS-578T (line)]] | alt | 396 | 6 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +19.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.522× (z -14.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.578× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 390 | 2 (1 ⚠) | 8 (6 ⚠) | [[Harringtonine (drug)]] 5 µM 2.04× (z +11.5) | [[Panobinostat (drug)]] 5 µM 0.256× (z -23.0) |
| [[COLO 205 (line)]] | alt | 403 | 6 (2 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +22.0) | [[Panobinostat (drug)]] 5 µM 0.327× (z -17.8) |
| [[hTERT-HPNE (line)]] | wt | 532 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.228× (z -18.1) |
| [[J82 (line)]] | alt | 418 | 5 (2 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +28.7) | [[Selinexor (drug)]] 5 µM 0.458× (z -20.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.505× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 468 | 7 (2 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 13.1× (z +47.3) | [[Panobinostat (drug)]] 5 µM 0.351× (z -13.6) |
| [[Panc 03.27 (line)]] | alt | 1,056 | 0 | 9 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -28.0) |
| [[CHP-212 (line)]] | wt | 571 | 1 | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.3) | [[Panobinostat (drug)]] 5 µM 0.163× (z -25.6) |
| [[H4 (line)]] | wt | 256 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.45× (z +13.5) | — |
| [[LS 180 (line)]] | wt | 280 | 4 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.345× (z -16.8) |
| [[Hs 766T (line)]] | wt | 256 | 3 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.1) | [[Panobinostat (drug)]] 5 µM 0.257× (z -17.9) |
| [[NCI-H2030 (line)]] | alt | 268 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +15.2) | [[Panobinostat (drug)]] 5 µM 0.535× (z -9.0) |
| [[A498 (line)]] | wt | 180 | 4 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +28.0) | [[Panobinostat (drug)]] 5 µM 0.545× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 458 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -12.4) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.378× (z -12.2) |
| [[SW48 (line)]] | wt | 400 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +9.5) | [[Panobinostat (drug)]] 0.5 µM 0.340× (z -12.0) |
| [[A-172 (line)]] | wt | 325 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +18.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -11.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW 1271 (line)]] | alt | 679 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -12.8) ⚠ toxic; cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 304 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 351 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.89× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.497× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[BT-474 (line)]] | alt | 56.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 397 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 501 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 438 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 44.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 248 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRNP1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SVIL]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 | same gene group |
| [[SRGAP1]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[MAFF]] | +0.58 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[FJX1]] | +0.57 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ANKRD1]] | +0.57 | +0.39 / +0.58 | both halves | 6e-05 |  |
| [[TEAD1]] | +0.57 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[IGF2BP2-AS1]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ERBIN]] | +0.54 | +0.34 / +0.63 | both halves | 1e-04 |  |
| [[VGLL3]] | +0.54 | +0.46 / +0.50 | both halves | 2e-05 |  |
| [[MYL12A]] | +0.54 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[RASAL2]] | +0.53 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[PTPRN2]] | +0.53 | +0.46 / +0.50 | both halves | 2e-05 | same gene group |

## Genes that move opposite

*32 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DERL1]] | -0.55 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[ATPAF1]] | -0.52 | -0.40 / -0.49 | both halves | 5e-05 |  |
| [[ANAPC10]] | -0.50 | -0.46 / -0.40 | both halves | 4e-05 |  |
| [[ALG9]] | -0.49 | -0.30 / -0.49 | both halves | 2e-04 |  |
| [[VDAC3]] | -0.48 | -0.33 / -0.50 | both halves | 1e-04 |  |
| [[EOLA1]] | -0.48 | -0.38 / -0.44 | both halves | 6e-05 |  |
| [[IFI27L1]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[STAG3L4]] ⚠ | -0.48 | -0.31 / -0.51 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM9]] | -0.47 | -0.43 / -0.39 | both halves | 6e-05 |  |
| [[UBAC1]] | -0.47 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[EEF1AKMT2]] | -0.47 | -0.24 / -0.54 | both halves | 4e-04 |  |
| [[PMS2P3-1]] | -0.47 | -0.22 / -0.51 | both halves | 6e-04 |  |
| [[PRDX3]] | -0.47 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKAP12]] | B | AKAP12 activity raises IGF2BP2's level | lines that do not express AKAP12 (18) vs lines expressing it (32) | 1.80× lower at baseline in the lines without AKAP12 | 0.026 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: ADAMTS18, IGF2BP1, CLEC2B |
| [[TRNP1]] | B | TRNP1 activity raises IGF2BP2's level | lines that do not express TRNP1 (10) vs lines expressing it (40) | 2.45× lower at baseline in the lines without TRNP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: USP43, STEAP2 |
| [[HMGA2]] | B | HMGA2 activity raises IGF2BP2's level | lines that do not express HMGA2 (9) vs lines expressing it (41) | 2.53× lower at baseline in the lines without HMGA2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SEMA4G, LINC02454 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | IGF2BP2 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.66× the cells of the other lines | 0.004 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| [[HMGA2]] | C | IGF2BP2 activity raises HMGA2's level | lines that do not express IGF2BP2 (3) vs lines expressing it (47) | 9.96× lower at baseline in the lines without IGF2BP2 | 0.019 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| [[ELK3]] | C | IGF2BP2 activity raises ELK3's level | lines that do not express IGF2BP2 (3) vs lines expressing it (47) | 3.98× lower at baseline in the lines without IGF2BP2 | 0.029 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| cells under [[Tucatinib (drug)]] 5 µM | C | IGF2BP2 activity raises the cells' numbers under Tucatinib 5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.67× the cells of the other lines | 0.040 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| [[SMURF2]] | C | IGF2BP2 activity raises SMURF2's level | lines that do not express IGF2BP2 (3) vs lines expressing it (47) | 2.32× lower at baseline in the lines without IGF2BP2 | 0.056 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| cells under [[Tranilast (drug)]] 0.5 µM | C | IGF2BP2 activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.77× the cells of the other lines | 0.077 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | IGF2BP2 activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.75× the cells of the other lines | 0.082 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |
| cells under [[Radotinib (drug)]] 5 µM | C | IGF2BP2 activity raises the cells' numbers under Radotinib 5 µM (protects the cells) | lines that do not express IGF2BP2 (3) vs lines expressing it (45) | the lines without IGF2BP2: 0.84× the cells of the other lines | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: PLS3, SLC25A43, SGK2 |

## Where it sits

- **Module**: [[Module 120]] — RHOA GTPase cycle; 41 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (40.7, 12.0); signed map (16.0, 40.3). **Vector** length 113, 42.4% of its response variance represented; |z| ≥ 3 in 2,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +10.8 | +8.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +28.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.4 | +11.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.1 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.2 | -2.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.0 | +8.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | +4.7 | +3.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.9 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -0.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -5.2 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.2 | -9.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | -5.1 | -17.3 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.9 | -4.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.8 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.5 | -3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | insulin like growth factor 2 mRNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q27.2 — chr3:185,643,130-185,825,042 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IMP-2, p62, P62 |
| Gene groups (HGNC) | RNA binding motif containing; MicroRNA protein coding host genes |
| Reactome | 2 pathways, smallest: Insulin-like Growth Factor-2 mRNA Binding Proteins (IGF2BPs/IMPs/VICKZs) bind RNA; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6M1](https://www.uniprot.org/uniprotkb/Q9Y6M1) (Insulin-like growth factor 2 mRNA-binding protein 2):

> RNA-binding factor that recruits target transcripts to cytoplasmic protein-RNA complexes (mRNPs). This transcript 'caging' into mRNPs allows mRNA transport and transient storage. It also modulates the rate and location at which target transcripts encounter the translational apparatus and shields them from endonuclease attacks or microRNA-mediated degradation (By similarity). Preferentially binds to N6-methyladenosine (m6A)-containing mRNAs and increases their stability. Binds to the 5'-UTR of …

**Summary**, from NCBI Gene [10644](https://www.ncbi.nlm.nih.gov/gene/10644):

> This gene encodes a protein that binds the 5' UTR of insulin-like growth factor 2 (IGF2) mRNA and regulates its translation. It plays an important role in metabolism and variation in this gene is associated with susceptibility to diabetes. Alternative splicing and promoter usage results in multiple transcript variants. Related pseudogenes are found on several chromosomes. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:28867](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28867) · Entrez [10644](https://www.ncbi.nlm.nih.gov/gene/10644) · UniProt [Q9Y6M1](https://www.uniprot.org/uniprotkb/Q9Y6M1) · Ensembl [ENSG00000073792](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000073792)

## Data

Gene col 1061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1061); `tables/drug_effects.parquet` (90 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1061]; `tensor/DDL_lfc|DDL_z.npy` [1061]; `embed/gene_vectors.npy` [1061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1061 or target_col == 1061). Every well: [[IGF2BP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IGF2BP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
