---
symbol: "FNDC3B"
type: "gene"
col: 1120
ensembl_id: "ENSG00000075420"
name: "fibronectin type III domain containing 3B"
location: "3q26.31"
module: 139
arm: "+"
pooled_cpm: 1252.54
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# FNDC3B

*fibronectin type III domain containing 3B* — 3q26.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.57× (z +4.4, q 0.007, up in 34 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (MIA PaCa-2 2.56×, A-172 2.14×, A-427 2.17×, A498 1.96×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 2.65×, MIA PaCa-2 2.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.11×, MIA PaCa-2 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.75×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 5.73×); [[PH-797804 (drug)]] 5 µM in 1 line (A-172 2.84×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.396× (z -24.1, q 0e+00, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHR]] (+0.56, fdr 3e-05), [[CYP1B1]] (+0.55, fdr 1e-04), [[NAMPT]] (+0.53, fdr 1e-05); moves opposite to [[SIMC1]] (-0.50, fdr 1e-05), [[TRMT2B]] (-0.46, fdr 1e-04), [[EPHX4]] (-0.45, fdr 4e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PLD1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1120.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 9 lines (MIA PaCa-2 2.56×, A-172 2.14×, A-427 2.17×, A498 1.96×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (A-427 2.65×, MIA PaCa-2 2.13×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (A-172 2.11×, MIA PaCa-2 2.05×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (MIA PaCa-2 1.75×); [[TAK-901 (drug)]] 5 µM in 1 line (BT-474 5.73×); [[PH-797804 (drug)]] 5 µM in 1 line (A-172 2.84×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.57×** | +4.4 | 0.007 | 34/49 (BT-474, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.48×** | +3.8 | 0.044 | 32/48 (A-172, HS-578T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 5 µM |  | 1.38× | +3.1 | 0.34 | 27/49 (HT-29, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 16 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1120.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.396×** | -24.1 | 0e+00 | 42/49 (A549, A498, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.269×** | -23.3 | 0e+00 | 46/47 (HepG2/C3A, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.288×** | -22.9 | 0e+00 | 48/48 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.314×** | -21.3 | 0e+00 | 48/48 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.329×** | -19.7 | 0e+00 | 42/44 (CFPAC-1, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.335×** | -19.3 | 0e+00 | 44/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.375×** | -18.1 | 0e+00 | 48/48 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.409×** | -15.2 | 0e+00 | 44/45 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.498×** | -12.3 | 9e-33 | 46/48 (HepG2/C3A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -7.9 | 2e-13 | 41/48 (SK-MEL-2, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.669×** | -7.4 | 7e-12 | 41/48 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.670×** | -7.4 | 8e-12 | 39/48 (SK-MEL-2, SW 900, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.674×** | -7.0 | 1e-10 | 35/48 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.690×** | -6.8 | 3e-10 | 42/48 (SW1417, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.708×** | -6.1 | 4e-08 | 34/50 (SNU-423, hTERT-HPNE, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.716×** | -5.8 | 2e-07 | 34/48 (NCI-H1573, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.802×** | -5.7 | 3e-07 | 31/48 (HOP62, A-172, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.736×** | -5.6 | 5e-07 | 37/48 (H4, SNU-423, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.754×** | -5.2 | 6e-06 | 32/48 (SK-MEL-2, NCI-H2347, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.584×** | -5.2 | 6e-06 | 40/49 (SK-MEL-2, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.602×** | -4.9 | 3e-05 | 35/47 (SW 900, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.765×** | -4.6 | 1e-04 | 40/47 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Amsacrine (drug)]] 5 µM |  | 0.846× | -4.4 | 3e-04 | 23/48 (A549, NCI-H2030, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.003 | 25/49 (LOX-IMVI, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1120. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 2,056 | 0 | 19 (11 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.159× (z -25.5) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.279× (z -25.0) |
| [[SW 900 (line)]] | alt | 1,553 | 0 | 18 (10 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -25.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -23.4) |
| [[HOP62 (line)]] | alt | 2,149 | 0 | 17 (9 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -26.3) |
| [[A549 (line)]] | wt | 1,839 | 0 | 16 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -35.1) |
| [[HepG2_C3A (line)]] | wt | 2,341 | 0 | 15 (11 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -26.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.135× (z -26.4) |
| [[NCI-H2347 (line)]] | alt | 2,015 | 0 | 14 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -26.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 1,293 | 0 | 14 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.265× (z -23.1) |
| [[A-172 (line)]] | wt | 1,176 | 3 (2 ⚠) | 10 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +17.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 2.84× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -23.0) |
| [[HS-578T (line)]] | alt | 2,131 | 1 (1 ⚠) | 12 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.243× (z -29.7) |
| [[hTERT-HPNE (line)]] | wt | 1,514 | 1 (1 ⚠) | 12 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -19.4) |
| [[LOX-IMVI (line)]] | wt | 1,127 | 0 | 13 (9 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -21.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.217× (z -19.7) |
| [[RPMI-7951 (line)]] | alt | 1,774 | 0 | 13 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -22.2) |
| [[H4 (line)]] | wt | 1,790 | 0 | 12 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.200× (z -19.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.205× (z -19.6) |
| [[KATO III (line)]] | alt | 1,085 | 0 | 12 (9 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.255× (z -19.3) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.283× (z -18.5) |
| [[MIA PaCa-2 (line)]] | alt | 511 | 6 (5 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +20.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.75× (z +12.2) | [[Panobinostat (drug)]] 5 µM 0.370× (z -15.2) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.380× (z -14.8) |
| [[NCI-H2030 (line)]] | alt | 1,289 | 0 | 12 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -24.0) |
| [[A498 (line)]] | wt | 1,563 | 1 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +15.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -31.5) |
| [[C32 (line)]] | wt | 1,072 | 1 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -19.6) |
| [[HT-29 (line)]] | alt | 1,165 | 0 | 11 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.222× (z -18.8) |
| [[J82 (line)]] | alt | 1,582 | 1 (1 ⚠) | 10 (7 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -21.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -21.1) |
| [[NCI-H1573 (line)]] | alt | 1,102 | 0 | 11 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.201× (z -21.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.273× (z -18.1) |
| [[NCI-H1792 (line)]] | alt | 2,243 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -28.3) |
| [[SNU-423 (line)]] | alt | 1,990 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -29.1) |
| [[CFPAC-1 (line)]] | alt | 2,612 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.143× (z -25.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.209× (z -21.6) |
| [[HEC-1-A (line)]] | alt | 1,171 | 1 (1 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +11.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.298× (z -17.2) |
| [[LoVo (line)]] | wt | 643 | 2 (2 ⚠) | 8 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.378× (z -14.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.450× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 1,347 | 1 (1 ⚠) | 9 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.275× (z -19.5) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.321× (z -17.8) |
| [[PANC-1 (line)]] | alt | 1,425 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -25.8) |
| [[SW1417 (line)]] | alt | 935 | 0 | 10 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -18.6) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.314× (z -17.7) |
| [[CHP-212 (line)]] | wt | 1,236 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -19.2) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.296× (z -18.0) |
| [[Hs 766T (line)]] | wt | 854 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -19.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.365× (z -14.1) |
| [[A-427 (line)]] | wt | 508 | 6 (6 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[BT-474 (line)]] | alt | 596 | 2 (1 ⚠) | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 5.73× (z +12.2) | [[Dinaciclib (drug)]] 5 µM 0.387× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.529× (z -8.5) |
| [[COLO 205 (line)]] | alt | 1,260 | 0 | 8 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.232× (z -16.9) |
| [[AN3 CA (line)]] | alt | 985 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -15.3) |
| [[AsPC-1 (line)]] | alt | 1,012 | 0 | 7 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.208× (z -22.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.212× (z -21.7) |
| [[SNU-1 (line)]] | wt | 620 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.52× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.260× (z -17.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.502× (z -9.3) |
| [[SW 1271 (line)]] | alt | 2,152 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -18.1) |
| [[RKO (line)]] | wt | 604 | 2 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.394× (z -13.3) |
| [[HCT15 (line)]] | alt | 563 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.374× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.437× (z -11.2) |
| [[LS 180 (line)]] | wt | 686 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -13.1) |
| [[NCI-H661 (line)]] | alt | 1,334 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -13.7) |
| [[SW 1088 (line)]] | alt | 1,278 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -10.8) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -10.8) |
| [[SW480 (line)]] | alt | 352 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.405× (z -12.9) |
| [[NCI-H23 (line)]] | alt | 459 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.325× (z -14.9) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.376× (z -13.0) |
| [[SW48 (line)]] | wt | 490 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.371× (z -12.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.487× (z -9.1) |
| [[C-33 A (line)]] | alt | 333 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.61× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 376 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -10.9) ⚠ toxic |
| [[NCI-H2122 (line)]] | alt | 1,208 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1120), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHR]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[CYP1B1]] | +0.55 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[NAMPT]] | +0.53 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TSPAN31]] | +0.53 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[NFKBIZ]] | +0.52 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[ATP2B1]] | +0.51 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[HIF1A]] | +0.51 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SOD2]] | +0.49 | +0.36 / +0.50 | both halves | 1e-04 |  |
| [[RHOV]] | +0.49 | +0.43 / +0.33 | both halves | 1e-04 |  |
| [[LUM]] | +0.49 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[KYNU]] | +0.49 | +0.37 / +0.50 | both halves | 8e-05 |  |
| [[CEACAM22P-1]] | +0.48 | +0.31 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SIMC1]] | -0.50 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TRMT2B]] | -0.46 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[EPHX4]] | -0.45 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[ANKS6]] | -0.45 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[C19orf12]] | -0.45 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[SMAGP]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[LSM11]] | -0.44 | -0.20 / -0.43 | both halves | 7e-04 |  |
| [[ZNF749]] | -0.44 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[SMG5]] | -0.43 | -0.30 / -0.34 | both halves | 2e-04 |  |
| [[VKORC1L1]] | -0.43 | -0.31 / -0.42 | both halves | 2e-04 |  |
| [[HERC2P2]] | -0.42 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[CRACD]] | -0.42 | -0.35 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLD1]] | B | PLD1 activity raises FNDC3B's level | lines that do not express PLD1 (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without PLD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: DUSP1, ATP1B1, DUSP10; maybe low, not absent |
| [[CFH]] | B | CFH activity raises FNDC3B's level | lines that do not express CFH (28) vs lines expressing it (22) | 1.71× lower at baseline in the lines without CFH | 0.027 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[TOP2A]] | B | TOP2A activity raises FNDC3B's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KYNU]] | B | KYNU activity raises FNDC3B's level | lines that do not express KYNU (29) vs lines expressing it (21) | 1.79× lower at baseline in the lines without KYNU | 0.051 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725 |
| [[NFATC2]] | B | NFATC2 activity raises FNDC3B's level | lines that do not express NFATC2 (11) vs lines expressing it (39) | 1.68× lower at baseline in the lines without NFATC2 | 0.058 | ⚠ within organs, on part of the lines; also absent: CACNG2; maybe low, not absent |
| [[IL6]] | B | IL6 activity raises FNDC3B's level | lines that do not express IL6 (32) vs lines expressing it (18) | 1.88× lower at baseline in the lines without IL6 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2 |
| [[BICC1]] | B | BICC1 activity raises FNDC3B's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 1.72× lower at baseline in the lines without BICC1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[MYOF]] | B | MYOF activity raises FNDC3B's level | lines that do not express MYOF (6) vs lines expressing it (44) | 1.69× lower at baseline in the lines without MYOF | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000286511, ACCS, CAV2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.440). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.8, 22.5); signed map (48.8, 24.2). **Vector** length 103, 44.6% of its response variance represented; |z| ≥ 3 in 1,991 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.5 | +1.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.9 | +1.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +7.4 | -19.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +6.9 | -15.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.6 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | -2.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +0.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +1.0 |
|  | [[Thymol (drug)]] 5 µM |  | +2.2 | -1.0 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -8.1 | -12.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -6.9 | -6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -6.7 | -23.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.5 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.9 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.9 | -5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -2.8 | -0.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | fibronectin type III domain containing 3B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q26.31 — chr3:172,039,578-172,401,669 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAD104, DKFZp762K137, FLJ23399, PRO4979, YVTM2421 |
| Gene groups (HGNC) | Fibronectin type III domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53EP0](https://www.uniprot.org/uniprotkb/Q53EP0) (Fibronectin type III domain-containing protein 3B):

> May be a positive regulator of adipogenesis.

**Summary**, from NCBI Gene [64778](https://www.ncbi.nlm.nih.gov/gene/64778):

> Enables RNA binding activity. Predicted to act upstream of or within several processes, including negative regulation of osteoblast differentiation; substrate adhesion-dependent cell spreading; and type II pneumocyte differentiation. Predicted to be located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24670](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24670) · Entrez [64778](https://www.ncbi.nlm.nih.gov/gene/64778) · UniProt [Q53EP0](https://www.uniprot.org/uniprotkb/Q53EP0) · Ensembl [ENSG00000075420](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000075420)

## Data

Gene col 1120: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1120); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1120, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1120]; `tensor/DDL_lfc|DDL_z.npy` [1120]; `embed/gene_vectors.npy` [1120]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1120 or target_col == 1120). Every well: [[FNDC3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FNDC3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
