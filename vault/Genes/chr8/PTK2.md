---
symbol: "PTK2"
type: "gene"
col: 9802
ensembl_id: "ENSG00000169398"
name: "protein tyrosine kinase 2"
location: "8q24.3"
module: 41
arm: "-"
pooled_cpm: 716.51
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# PTK2

*protein tyrosine kinase 2* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.51× (z +9.4, q 5e-18, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.359× (z -22.6, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.594× (z -16.9, q 0e+00, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPK2]] (+0.65, fdr 3e-05), [[EXT2]] (+0.63, fdr 1e-05), [[XPR1]] (+0.58, fdr 8e-05); moves opposite to [[GOSR1]] (-0.60, fdr 1e-05), [[UFL1]] (-0.58, fdr 2e-05), [[LYSMD3]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9802.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +9.4 | 5e-18 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.15×** | +9.2 | 2e-17 | 43/49 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +8.2 | 5e-14 | 36/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.40×** | +7.6 | 3e-12 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +7.2 | 6e-11 | 43/48 (SW480, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +6.3 | 2e-08 | 35/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.28×** | +5.7 | 1e-06 | 35/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.25×** | +4.8 | 1e-04 | 33/48 (SW480, HT-29, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.22×** | +4.6 | 2e-04 | 30/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +4.1 | 0.002 | 24/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.19× | +4.0 | 0.003 | 23/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.0 | 0.003 | 32/45 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.0 | 0.003 | 22/47 (NCI-H460, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.15× | +3.0 | 0.099 | 19/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9802.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -22.6 | 0e+00 | 44/44 (A-427, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.389×** | -21.6 | 0e+00 | 49/49 (C32, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.594×** | -16.9 | 0e+00 | 38/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.600×** | -16.5 | 0e+00 | 45/49 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.502×** | -15.2 | 0e+00 | 47/47 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.544×** | -13.9 | 4e-42 | 45/48 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.543×** | -12.9 | 2e-36 | 39/45 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.571×** | -12.8 | 8e-36 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.679×** | -8.9 | 5e-17 | 38/48 (C32, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.687×** | -8.6 | 4e-16 | 38/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **0.739×** | -6.9 | 2e-10 | 40/48 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.764×** | -6.2 | 3e-08 | 36/48 (C32, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.797×** | -5.0 | 2e-05 | 29/50 (LOX-IMVI, C32, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.824×** | -4.3 | 8e-04 | 25/48 (C32, SK-MEL-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.830×** | -4.3 | 8e-04 | 22/48 (LoVo, SW 900, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9802. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 1,206 | 1 | 17 (11 ⚠) | [[TAK-901 (drug)]] 5 µM 3.82× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -44.2) |
| [[NCI-H460 (line)]] | wt | 519 | 10 (4 ⚠) | 8 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.59× (z +18.0) | [[Dinaciclib (drug)]] 0.5 µM 0.366× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.585× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 1,200 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.222× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -19.2) |
| [[A549 (line)]] | wt | 774 | 4 (1 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -30.0) |
| [[LOX-IMVI (line)]] | wt | 1,171 | 1 | 11 (6 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.94× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -23.2) |
| [[SK-MEL-2 (line)]] | alt | 642 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -27.1) |
| [[SW 900 (line)]] | alt | 889 | 0 | 12 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.477× (z -17.1) |
| [[HS-578T (line)]] | alt | 1,109 | 2 | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.71× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -23.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -20.4) |
| [[J82 (line)]] | alt | 929 | 0 | 11 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -22.5) |
| [[KATO III (line)]] | alt | 457 | 3 (1 ⚠) | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 2.73× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.446× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.515× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 760 | 0 | 11 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.274× (z -19.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.349× (z -16.3) |
| [[NCI-H1573 (line)]] | alt | 605 | 1 (1 ⚠) | 10 (6 ⚠) | [[Lonafarnib (drug)]] 5 µM 2.73× (z +9.4) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -30.5) |
| [[A-172 (line)]] | wt | 466 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -21.7) |
| [[BT-474 (line)]] | alt | 821 | 5 (1 ⚠) | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.32× (z +13.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 668 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.330× (z -20.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.502× (z -18.3) |
| [[Hs 766T (line)]] | wt | 825 | 3 (2 ⚠) | 7 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.18× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.469× (z -11.6) |
| [[LoVo (line)]] | wt | 494 | 3 (1 ⚠) | 7 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.11× (z +13.8) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.59× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -20.0) |
| [[NCI-H23 (line)]] | alt | 765 | 1 | 9 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.73× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.447× (z -13.5) |
| [[PANC-1 (line)]] | alt | 828 | 2 | 8 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.99× (z +11.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -22.2) |
| [[SNU-423 (line)]] | alt | 521 | 2 (1 ⚠) | 8 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.538× (z -14.3) |
| [[HOP62 (line)]] | alt | 956 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -18.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -16.1) |
| [[SW480 (line)]] | alt | 381 | 5 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.49× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.529× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.621× (z -10.3) |
| [[HepG2_C3A (line)]] | wt | 519 | 1 | 7 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.29× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.467× (z -11.3) |
| [[HT-29 (line)]] | alt | 1,234 | 3 (1 ⚠) | 5 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.00× (z +10.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 1.90× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.543× (z -9.7) |
| [[LS 180 (line)]] | wt | 442 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 2.53× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -16.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.568× (z -14.7) |
| [[Panc 03.27 (line)]] | alt | 758 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.278× (z -23.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -12.5) |
| [[RKO (line)]] | wt | 1,256 | 2 | 6 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -20.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.571× (z -13.1) |
| [[A498 (line)]] | wt | 691 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.556× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 573 | 3 (1 ⚠) | 4 (2 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.11× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -19.5) |
| [[NCI-H2030 (line)]] | alt | 828 | 1 | 6 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 1.94× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.616× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 709 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.462× (z -17.0) |
| [[SW1417 (line)]] | alt | 719 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.332× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.511× (z -12.0) |
| [[hTERT-HPNE (line)]] | wt | 568 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -24.6) |
| [[SW48 (line)]] | wt | 428 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.49× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.361× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.533× (z -12.4) |
| [[A-427 (line)]] | wt | 406 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.249× (z -25.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.594× (z -10.0) |
| [[C-33 A (line)]] | alt | 619 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.578× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 425 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -17.1) |
| [[SHP-77 (line)]] | alt | 552 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.424× (z -14.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 828 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.403× (z -12.4) |
| [[COLO 205 (line)]] | alt | 527 | 2 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 1.92× (z +9.4) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.17× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.522× (z -13.9) |
| [[HCT15 (line)]] | alt | 616 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.411× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.594× (z -11.2) |
| [[SNU-1 (line)]] | wt | 555 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.23× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -14.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 592 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.509× (z -11.5) |
| [[NCI-H661 (line)]] | alt | 558 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.488× (z -9.1) |
| [[AN3 CA (line)]] | alt | 575 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.440× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.4) |
| [[CHP-212 (line)]] | wt | 598 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -14.5) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 675 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 738 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 528 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 505 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9802), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | +0.65 | +0.79 / +0.44 | both halves | 3e-05 |  |
| [[EXT2]] | +0.63 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[XPR1]] | +0.58 | +0.70 / +0.37 | both halves | 8e-05 |  |
| [[COP1]] | +0.58 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[ABCC1]] | +0.58 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[HACD3]] | +0.57 | +0.65 / +0.42 | both halves | 4e-05 |  |
| [[SPATA5]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[LMTK2]] | +0.55 | +0.68 / +0.31 | both halves | 2e-04 | same gene group |
| [[RANBP17]] | +0.54 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[NAXE]] | +0.54 | +0.56 / +0.25 | both halves | 4e-04 |  |
| [[RAP1GDS1]] | +0.53 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[PRIM2]] | +0.53 | +0.63 / +0.33 | both halves | 1e-04 | same gene group |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GOSR1]] | -0.60 | -0.68 / -0.49 | both halves | 1e-05 |  |
| [[UFL1]] | -0.58 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[LYSMD3]] | -0.58 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[PAN2]] | -0.57 | -0.72 / -0.34 | both halves | 1e-04 |  |
| [[MYNN]] | -0.57 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[ZNF550]] | -0.57 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[ZNF773]] | -0.56 | -0.75 / -0.48 | both halves | 2e-05 |  |
| [[SEPSECS]] | -0.56 | -0.71 / -0.45 | both halves | 3e-05 |  |
| [[PPIL4]] | -0.55 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[SEC23B]] | -0.55 | -0.56 / -0.40 | both halves | 4e-05 |  |
| [[CYP20A1]] | -0.52 | -0.72 / -0.39 | both halves | 6e-05 |  |
| [[GORAB]] | -0.52 | -0.67 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers PTK2's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **-** arm (projection on the module's main direction -0.560). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-23.2, -27.8); signed map (-20.4, -48.3). **Vector** length 99.3, 45.2% of its response variance represented; |z| ≥ 3 in 1,586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.8 | +5.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +4.7 | +4.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +3.8 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | -1.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.7 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | -2.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -9.6 | -16.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -5.1 | -4.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -4.3 | -15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -3.5 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -3.3 | -0.4 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.5 | +0.2 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | -2.4 | -0.9 |
|  | [[Posaconazole (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Tirabrutinib (drug)]] 5 µM |  | -2.0 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:140,657,900-141,002,216 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FAK, FADK, FAK1, PPP1R71 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; FERM domain containing; PTK2 family tyrosine kinases; MicroRNA protein coding host genes |
| Hallmark sets | ANGIOGENESIS, APOPTOSIS, APICAL_JUNCTION |
| Reactome | 48 pathways, smallest: Signal regulatory protein family interactions; DCC mediated attractive signaling; GRB2:SOS provides linkage to MAPK signaling for Integrins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q05397](https://www.uniprot.org/uniprotkb/Q05397) (Focal adhesion kinase 1):

> Non-receptor protein-tyrosine kinase that plays an essential role in regulating cell migration, adhesion, spreading, reorganization of the actin cytoskeleton, formation and disassembly of focal adhesions and cell protrusions, cell cycle progression, cell proliferation and apoptosis. Required for early embryonic development and placenta development. Required for embryonic angiogenesis, normal cardiomyocyte migration and proliferation, and normal heart development. Regulates axon growth and …

**Summary**, from NCBI Gene [5747](https://www.ncbi.nlm.nih.gov/gene/5747):

> This gene encodes a cytoplasmic protein tyrosine kinase which is found concentrated in the focal adhesions that form between cells growing in the presence of extracellular matrix constituents. The encoded protein is a member of the FAK subfamily of protein tyrosine kinases but lacks significant sequence similarity to kinases from other subfamilies. Activation of this gene may be an important early step in cell growth and intracellular signal transduction pathways triggered in response to …

**Accessions** — [HGNC:9611](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9611) · Entrez [5747](https://www.ncbi.nlm.nih.gov/gene/5747) · UniProt [Q05397](https://www.uniprot.org/uniprotkb/Q05397) · Ensembl [ENSG00000169398](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169398)

## Data

Gene col 9802: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9802); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9802, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9802]; `tensor/DDL_lfc|DDL_z.npy` [9802]; `embed/gene_vectors.npy` [9802]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9802 or target_col == 9802). Every well: [[PTK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
