---
symbol: "RECQL"
type: "gene"
col: 50
ensembl_id: "ENSG00000004700"
name: "RecQ like helicase"
location: "12p12.1"
module: 42
arm: "+"
pooled_cpm: 88.75
n_lines_expressing: 49
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# RECQL

*RecQ like helicase* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +17.6, q 0e+00, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.476× (z -24.1, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARPC2]] (+0.67, fdr 7e-06), [[P3H1]] (+0.65, fdr 7e-06), [[ERI1]] (+0.65, fdr 1e-05); moves opposite to [[REPIN1]] (-0.71, fdr 7e-06), [[DHFR2]] (-0.61, fdr 7e-06), [[COIL]] (-0.61, fdr 1e-05).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 50.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +17.6 | 0e+00 | 45/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.98×** | +16.3 | 0e+00 | 45/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.93×** | +15.7 | 0e+00 | 42/47 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.89×** | +15.2 | 0e+00 | 42/47 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.82×** | +13.7 | 1e-40 | 36/42 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.67×** | +12.2 | 2e-32 | 40/48 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.58×** | +10.6 | 4e-24 | 42/49 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.57×** | +10.4 | 2e-23 | 36/47 (HS-578T, MIA PaCa-2, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.44×** | +8.0 | 7e-14 | 29/44 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.35×** | +7.2 | 5e-11 | 29/47 (C32, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +6.7 | 1e-09 | 26/47 (SW1417, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +6.1 | 5e-08 | 27/47 (C32, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.29×** | +6.1 | 5e-08 | 22/47 (KATO III, A498, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.24×** | +4.9 | 4e-05 | 23/47 (MIA PaCa-2, AsPC-1, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.17× | +3.8 | 0.006 | 13/46 (MIA PaCa-2, AsPC-1, …) | two highest doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.013 | 9/47 (A-427, A549, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.37×** | +3.3 | 0.034 | 9/47 (SW480, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.10× | +3.1 | 0.048 | 5/48 (HS-578T, MIA PaCa-2, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 50.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.476×** | -24.1 | 0e+00 | 45/47 (AsPC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.663×** | -9.4 | 1e-18 | 36/47 (A-172, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.739×** | -7.2 | 9e-11 | 29/47 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.763×** | -6.5 | 1e-08 | 30/47 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.764×** | -6.4 | 1e-08 | 24/47 (HOP62, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.702×** | -6.0 | 1e-07 | 24/47 (A498, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.793×** | -5.6 | 2e-06 | 24/47 (RKO, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.799×** | -5.4 | 6e-06 | 19/47 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.820×** | -4.7 | 1e-04 | 22/47 (NCI-H1792, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.828×** | -4.3 | 8e-04 | 20/47 (SK-MEL-2, RKO, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.828×** | -4.3 | 0.001 | 21/47 (A-427, AsPC-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.838× | -4.2 | 0.001 | 21/47 (A-172, A498, …) | all doses, stronger at high dose | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.834× | -4.1 | 0.002 | 18/46 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.683×** | -4.0 | 0.002 | 19/48 (AsPC-1, SNU-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.848× | -3.9 | 0.003 | 18/47 (NCI-H1792, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.844× | -3.9 | 0.004 | 18/46 (RKO, SW480, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.004 | 12/47 (RKO, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.859× | -3.6 | 0.009 | 12/47 (A549, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.898× | -3.6 | 0.010 | 11/47 (NCI-H23, RKO, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 50. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 82.6 | 8 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +14.1) | — |
| [[HT-29 (line)]] | alt | 36.9 | 6 (5 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 3.73× (z +11.3) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 53.4 | 6 (5 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.66× (z +12.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -11.1) |
| [[SW480 (line)]] | alt | 134 | 6 (5 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.603× (z -9.0) |
| [[A-427 (line)]] | wt | 128 | 4 (4 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 2.25× (z +9.8) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -18.2) |
| [[A498 (line)]] | wt | 131 | 2 (2 ⚠) | 4 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.97× (z +10.0) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -22.5) |
| [[SW1417 (line)]] | alt | 58.7 | 6 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.63× (z +10.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +10.1) | — |
| [[A-172 (line)]] | wt | 104 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -19.2) |
| [[KATO III (line)]] | alt | 62.7 | 4 (4 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.81× (z +10.9) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -11.3) |
| [[NCI-H1573 (line)]] | alt | 42.2 | 4 (4 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -9.5) |
| [[A549 (line)]] | wt | 100 | 3 (3 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.35× (z +10.4) ⚠ cell-cycle shift, explains ~38% of this change | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -12.0) |
| [[HS-578T (line)]] | alt | 127 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +13.7) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -16.2) |
| [[J82 (line)]] | alt | 167 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -16.1) |
| [[LoVo (line)]] | wt | 45.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +10.6) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 93.5 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.387× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.404× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 79.0 | 2 (1 ⚠) | 2 | [[Panobinostat (drug)]] 0.5 µM 1.95× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.62× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -16.9) |
| [[PANC-1 (line)]] | alt | 69.2 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.60× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.532× (z -12.2) |
| [[HOP62 (line)]] | alt | 156 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 127 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +15.5) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -18.2) |
| [[NCI-H23 (line)]] | alt | 224 | 2 (2 ⚠) | 1 | [[Belinostat (drug)]] 5 µM 2.29× (z +10.1) ⚠ cell-cycle shift, explains ~41% of this change | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 89.6 | 2 (1 ⚠) | 1 | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +9.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.33× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.7) |
| [[SW 1088 (line)]] | alt | 105 | 0 | 3 (1 ⚠) | — | [[Omeprazole (drug)]] 0.5 µM 0.0579× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 95.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -27.5) |
| [[C32 (line)]] | wt | 61.8 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.12× (z +9.5) | — |
| [[Panc 03.27 (line)]] | alt | 102 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.15× (z +9.0) ⚠ cell-cycle shift, explains ~46% of this change | — |
| [[SHP-77 (line)]] | alt | 42.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.92× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-423 (line)]] | alt | 60.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -9.6) |
| [[SW 900 (line)]] | alt | 114 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -10.2) |
| [[AN3 CA (line)]] | alt | 59.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.126× (z -10.2) |
| [[C-33 A (line)]] | alt | 56.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[H4 (line)]] | wt | 114 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -14.6) |
| [[HCT15 (line)]] | alt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 50.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -10.9) |
| [[Hs 766T (line)]] | wt | 93.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 116 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 133 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -18.8) |
| [[NCI-H596 (line)]] | alt | 67.8 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.418× (z -8.9) |
| [[RKO (line)]] | wt | 130 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.77× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 117 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -12.9) |
| [[SNU-1 (line)]] | wt | 63.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -18.5) |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 34.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 36.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 50), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARPC2]] | +0.67 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[P3H1]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ERI1]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TPP2]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.64 | +0.69 / +0.63 | both halves | 7e-06 | STRING 441; ⚠ same locus (0.1 kb: neighbours can correlate without regulation) |
| [[SENP5]] | +0.64 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[ODF2]] | +0.64 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[TPM3]] | +0.63 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[GDI2]] | +0.63 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[CALU]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZCCHC17]] | +0.62 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[CENPJ]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[C11orf24]] | +0.61 | +0.64 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[REPIN1]] | -0.71 | -0.67 / -0.69 | both halves | 7e-06 |  |
| [[DHFR2]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[COIL]] | -0.61 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[THUMPD2]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[PLD6]] | -0.60 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[SETD2]] | -0.60 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[LIPT1]] | -0.60 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[CHIC1]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF480]] | -0.59 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ZNF317]] | -0.59 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[NFYC]] | -0.59 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[RAB9A]] | -0.57 | -0.54 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RECQL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FOXA1]] | B | FOXA1 activity lowers RECQL's level | lines that do not express FOXA1 (22) vs lines expressing it (28) | 1.63× higher at baseline in the lines without FOXA1 | 0.036 | ⚠ within organs, on part of the lines; also absent: MYO5C, SPINT1, COBL |
| [[PWWP2B]] | C | PWWP2B activity strengthens RECQL's drug response | lines that do not express PWWP2B (3) vs lines expressing it (46) | the lines without PWWP2B respond 0.70× as strongly (z diff +1.73); strongest at Panobinostat 5 µM: 0.90x vs 2.00x (z diff +5.9) | 0.081 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[P3H1]] | C | P3H1 activity raises RECQL's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without P3H1 | 0.082 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.9, -27.9); signed map (-53.1, 4.4). **Vector** length 140, 46.0% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +6.6 | +10.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +6.1 | +10.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.0 | +15.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +17.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.2 | +16.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | +7.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.3 | +4.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +3.3 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +2.6 | +3.6 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.5 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -11.8 | -24.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -9.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.1 | -6.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.9 | -5.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -5.2 | -3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.8 | -3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.6 | -4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -1.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RecQ like helicase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p12.1 — chr12:21,468,910-21,501,669 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RecQ1, RecQL1 |
| Gene groups (HGNC) | RecQ like helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [P46063](https://www.uniprot.org/uniprotkb/P46063) (ATP-dependent DNA helicase Q1):

> DNA helicase that plays a role in DNA damage repair and genome stability. Exhibits a Mg(2+)- and ATP-dependent DNA-helicase activity that unwinds single- and double-stranded DNA in a 3'-5' direction. Full-length protein unwinds forked DNA substrates, resolves Holliday junctions, and has DNA strand annealing activity. Plays a role in restoring regressed replication forks. Required to restart stalled replication forks induced by abortive topoisomerase 1 and 2 lesions. Does not unwind G-quadruplex …

**Summary**, from NCBI Gene [5965](https://www.ncbi.nlm.nih.gov/gene/5965):

> The protein encoded by this gene is a member of the RecQ DNA helicase family. DNA helicases are enzymes involved in various types of DNA repair, including mismatch repair, nucleotide excision repair and direct repair. The encoded protein is involved in the processing of Holliday junctions, the suppression of sister chromatid exchanges, telomere maintenance, and is required for genotoxic stress resistance. Defects in this gene have been associated with several types of cancer. [provided by …

**Accessions** — [HGNC:9948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9948) · Entrez [5965](https://www.ncbi.nlm.nih.gov/gene/5965) · UniProt [P46063](https://www.uniprot.org/uniprotkb/P46063) · Ensembl [ENSG00000004700](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000004700)

## Data

Gene col 50: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 50); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 50, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 50]; `tensor/DDL_lfc|DDL_z.npy` [50]; `embed/gene_vectors.npy` [50]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 50 or target_col == 50). Every well: [[RECQL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RECQL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
