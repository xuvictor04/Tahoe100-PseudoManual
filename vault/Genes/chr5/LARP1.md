---
symbol: "LARP1"
type: "gene"
col: 7898
ensembl_id: "ENSG00000155506"
name: "La ribonucleoprotein 1, translational regulator"
location: "5q33.2"
module: 18
arm: "+"
pooled_cpm: 196.32
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# LARP1

*La ribonucleoprotein 1, translational regulator* — 5q33.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.88× (z +20.7, q 0e+00, up in 44 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Bortezomib (drug)]] 0.05 µM: 1.44× (z +11.4, q 5e-28, up in 39 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.482× (z -24.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GSR]] (+0.71, fdr 7e-06), [[KPNA3]] (+0.70, fdr 7e-06), [[LARP4]] (+0.69, fdr 7e-06); moves opposite to [[BTG1]] (-0.64, fdr 7e-06), [[GCC2]] (-0.62, fdr 1e-05), [[GTF2B]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FAXC]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7898.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.88×** | +20.7 | 0e+00 | 44/49 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +17.0 | 0e+00 | 39/44 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +15.6 | 0e+00 | 39/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +11.4 | 5e-28 | 39/48 (A-172, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.36×** | +10.2 | 3e-22 | 41/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +9.9 | 3e-21 | 30/48 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +9.1 | 7e-18 | 33/48 (C32, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +8.7 | 2e-16 | 27/45 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.61×** | +8.1 | 3e-14 | 36/49 (SNU-423, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +7.0 | 1e-10 | 26/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.23×** | +6.6 | 2e-09 | 29/48 (NCI-H1792, COLO 205, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +5.8 | 3e-07 | 31/48 (NCI-H460, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +5.5 | 1e-06 | 0/50 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.18× | +5.5 | 2e-06 | 22/48 (NCI-H460, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +5.3 | 4e-06 | 22/48 (H4, NCI-H460, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.33×** | +4.9 | 3e-05 | 26/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.31×** | +4.7 | 8e-05 | 28/48 (NCI-H460, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.31×** | +4.7 | 8e-05 | 24/48 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +4.2 | 7e-04 | 12/48 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +4.1 | 0.001 | 4/48 (CHP-212, RPMI-7951, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.09× | +4.0 | 0.001 | 1/48 (SW 1271) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.13× | +4.0 | 0.002 | 22/48 (COLO 205, HOP62, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.25×** | +3.9 | 0.002 | 18/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7898.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.482×** | -24.0 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.493×** | -23.2 | 0e+00 | 47/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.614×** | -22.6 | 0e+00 | 37/48 (LOX-IMVI, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.609×** | -16.3 | 0e+00 | 41/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -15.0 | 0e+00 | 35/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.695×** | -11.9 | 8e-31 | 35/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.855× | -7.3 | 3e-11 | 21/48 (J82, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.812×** | -6.8 | 6e-10 | 25/48 (SW1417, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.830×** | -5.9 | 3e-07 | 23/48 (PANC-1, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.876× | -4.2 | 0.002 | 17/48 (MIA PaCa-2, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.896× | -3.6 | 0.015 | 12/48 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.896× | -3.6 | 0.015 | 12/48 (RKO, BT-474, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.812×** | -3.6 | 0.016 | 14/49 (A498, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.863× | -3.4 | 0.024 | 15/48 (AN3 CA, LS 180, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.901× | -3.3 | 0.037 | 6/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.937× | -3.0 | 0.084 | 5/48 (A-172, SW480, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7898. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 182 | 7 (5 ⚠) | 4 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.22× (z +13.3) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.80× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.475× (z -12.4) |
| [[HOP62 (line)]] | alt | 140 | 7 (4 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +16.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.20× (z +13.3) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -26.0) |
| [[PANC-1 (line)]] | alt | 275 | 2 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 1.57× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -31.9) |
| [[SW480 (line)]] | alt | 200 | 4 (4 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.78× (z +19.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -26.0) |
| [[HS-578T (line)]] | alt | 157 | 4 (4 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.97× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -19.3) |
| [[LOX-IMVI (line)]] | wt | 205 | 3 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -36.8) |
| [[MIA PaCa-2 (line)]] | alt | 262 | 2 (2 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 1.82× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -23.8) |
| [[HEC-1-A (line)]] | alt | 307 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 1.76× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.57× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.400× (z -18.7) |
| [[J82 (line)]] | alt | 209 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +13.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.391× (z -16.8) |
| [[KATO III (line)]] | alt | 145 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Bortezomib (drug)]] 0.05 µM 1.81× (z +8.8) | [[Panobinostat (drug)]] 5 µM 0.414× (z -13.9) |
| [[LoVo (line)]] | wt | 264 | 1 (1 ⚠) | 6 | [[Niclosamide (olamine) (drug)]] 5 µM 1.73× (z +9.2) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -31.6) |
| [[RKO (line)]] | wt | 233 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +12.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.370× (z -14.9) |
| [[A-172 (line)]] | wt | 208 | 3 (1 ⚠) | 3 | [[Bortezomib (drug)]] 0.05 µM 2.02× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.559× (z -14.4) |
| [[A549 (line)]] | wt | 158 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +16.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.487× (z -11.0) |
| [[AsPC-1 (line)]] | alt | 141 | 1 (1 ⚠) | 5 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.92× (z +8.8) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -20.9) |
| [[C32 (line)]] | wt | 118 | 4 | 2 | [[Ixazomib citrate (drug)]] 5 µM 2.30× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -23.9) |
| [[Hs 766T (line)]] | wt | 180 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +13.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.546× (z -8.9) |
| [[HT-29 (line)]] | alt | 215 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.65× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -19.9) |
| [[LS 180 (line)]] | wt | 191 | 2 (2 ⚠) | 4 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.418× (z -14.0) |
| [[NCI-H1792 (line)]] | alt | 98.6 | 5 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.51× (z +18.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.609× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 205 | 4 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 2.76× (z +8.8) | [[Panobinostat (drug)]] 0.5 µM 0.492× (z -11.7) |
| [[SNU-423 (line)]] | alt | 181 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +14.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.562× (z -8.8) |
| [[SW1417 (line)]] | alt | 266 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.72× (z +12.1) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.436× (z -18.7) |
| [[A498 (line)]] | wt | 184 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.516× (z -11.4) |
| [[H4 (line)]] | wt | 145 | 4 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 2.44× (z +9.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.429× (z -9.0) |
| [[NCI-H1573 (line)]] | alt | 190 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -26.5) |
| [[NCI-H2030 (line)]] | alt | 181 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -16.6) |
| [[NCI-H23 (line)]] | alt | 179 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -19.4) |
| [[SK-MEL-2 (line)]] | alt | 202 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -24.5) |
| [[SW48 (line)]] | wt | 207 | 1 | 4 | [[TAK-901 (drug)]] 0.05 µM 3.01× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.298× (z -14.2) |
| [[A-427 (line)]] | wt | 310 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.443× (z -15.7) |
| [[BT-474 (line)]] | alt | 163 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -17.1) |
| [[C-33 A (line)]] | alt | 263 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.405× (z -14.2) |
| [[COLO 205 (line)]] | alt | 118 | 3 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.07× (z +11.8) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.73× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.512× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 138 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -13.8) |
| [[AN3 CA (line)]] | alt | 306 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -10.6) |
| [[SNU-1 (line)]] | wt | 257 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.367× (z -13.1) |
| [[SW 900 (line)]] | alt | 99.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.25× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.5) |
| [[CFPAC-1 (line)]] | alt | 156 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 195 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.14× (z +10.5) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 163 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 111 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.432× (z -8.9) |
| [[CHP-212 (line)]] | wt | 203 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 216 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 181 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7898), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSR]] | +0.71 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[KPNA3]] | +0.70 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[LARP4]] | +0.69 | +0.59 / +0.71 | both halves | 7e-06 | same gene group; STRING 400 |
| [[NUDT3]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[ABCC4]] | +0.65 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[VWA8]] | +0.63 | +0.64 / +0.60 | both halves | 7e-06 | same gene group |
| [[NAA50]] | +0.62 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[LTBR]] | +0.61 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[TMEM33]] | +0.61 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[NFIC]] | +0.61 | +0.63 / +0.56 | both halves | 1e-05 |  |
| [[DDX54]] | +0.61 | +0.61 / +0.55 | both halves | 1e-05 | same gene group |
| [[CHCHD3]] | +0.60 | +0.55 / +0.65 | both halves | 1e-05 | same gene group |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTG1]] | -0.64 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[GCC2]] | -0.62 | -0.65 / -0.57 | both halves | 1e-05 |  |
| [[GTF2B]] | -0.62 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[NOSIP]] | -0.61 | -0.62 / -0.54 | both halves | 1e-05 |  |
| [[BLZF1]] | -0.60 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CIB1]] | -0.59 | -0.40 / -0.66 | both halves | 5e-05 |  |
| [[DIS3]] | -0.58 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZKSCAN1]] | -0.57 | -0.65 / -0.49 | both halves | 1e-05 |  |
| [[POLD4]] | -0.56 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[H3-3B]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 | STRING 511 |
| [[FAM43A]] | -0.55 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[SHOC2]] | -0.55 | -0.52 / -0.51 | both halves | 1e-05 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAXC]] | B | FAXC activity raises LARP1's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.29× lower at baseline in the lines without FAXC | 0.009 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[FAM43A]] | B | FAM43A activity lowers LARP1's level | lines that do not express FAM43A (14) vs lines expressing it (36) | 1.31× higher at baseline in the lines without FAM43A | 0.031 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NFIA]] | B | NFIA activity strengthens LARP1's drug response | lines that do not express NFIA (11) vs lines expressing it (38) | the lines without NFIA respond 0.94× as strongly (z diff +0.78); strongest at Belinostat 5 µM: 0.78x vs 0.57x (z diff +3.8) | 0.056 | ⚠ within organs, on part of the lines; also absent: CRACD, TSPAN33, PCAT7; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[NUP210]] | B | NUP210 activity raises LARP1's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 1.30× lower at baseline in the lines without NUP210 | 0.079 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A |
| [[HDAC6]] | B | HDAC6 activity raises LARP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IGFBP3]] | B | IGFBP3 activity lowers LARP1's level | lines that do not express IGFBP3 (20) vs lines expressing it (30) | 1.25× higher at baseline in the lines without IGFBP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADRA1B, ADAM12, MAF |
| [[MGST1]] | B | MGST1 activity lowers LARP1's level | lines that do not express MGST1 (12) vs lines expressing it (38) | 1.19× higher at baseline in the lines without MGST1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000283240, STON2, MAPK13 |
| [[CIB1]] | C | CIB1 activity lowers LARP1's level | lines that do not express CIB1 (4) vs lines expressing it (46) | 1.45× higher at baseline in the lines without CIB1 | 0.094 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: SHB, NIBAN2, IER3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-6.8, -34.8); signed map (-10.6, -43.5). **Vector** length 140, 47.7% of its response variance represented; |z| ≥ 3 in 1,524 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.2 | +10.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +8.2 | +15.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +9.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.7 | +11.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.6 | +4.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +9.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.5 | +4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +4.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +5.2 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.2 | -22.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -11.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.1 | -15.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.6 | -2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.4 | -3.4 |
|  | [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | -2.7 | -3.0 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.5 | -1.3 |
|  | [[Vilanterol (drug)]] 5 µM |  | -2.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | La ribonucleoprotein 1, translational regulator |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.2 — chr5:154,682,986-154,817,605 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LARP, KIAA0731, MGC19556, Lar1, Lhp1 |
| Gene groups (HGNC) | La ribonucleoproteins; MicroRNA protein coding host genes |
| Reactome | 5 pathways, smallest: SARS-CoV-2 activates/modulates innate and adaptive immune responses; SARS-CoV-2-host interactions; SARS-CoV-2 Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PKG0](https://www.uniprot.org/uniprotkb/Q6PKG0) (La-related protein 1):

> RNA-binding protein that regulates the translation of specific target mRNA species downstream of the mTORC1 complex, in function of growth signals and nutrient availability. Interacts on the one hand with the 3' poly-A tails that are present in all mRNA molecules, and on the other hand with the 7-methylguanosine cap structure of mRNAs containing a 5' terminal oligopyrimidine (5'TOP) motif, which is present in mRNAs encoding ribosomal proteins and several components of the translation machinery. …

**Summary**, from NCBI Gene [23367](https://www.ncbi.nlm.nih.gov/gene/23367):

> Enables several functions, including RNA binding activity; eukaryotic initiation factor 4E binding activity; and ribosomal small subunit binding activity. Involved in several processes, including TORC1 signaling; cellular response to rapamycin; and post-transcriptional regulation of gene expression. Located in TORC1 complex; cytoplasmic stress granule; and cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29531](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29531) · Entrez [23367](https://www.ncbi.nlm.nih.gov/gene/23367) · UniProt [Q6PKG0](https://www.uniprot.org/uniprotkb/Q6PKG0) · Ensembl [ENSG00000155506](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155506)

## Data

Gene col 7898: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7898); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7898, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7898]; `tensor/DDL_lfc|DDL_z.npy` [7898]; `embed/gene_vectors.npy` [7898]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7898 or target_col == 7898). Every well: [[LARP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LARP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
