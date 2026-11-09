---
symbol: "BRWD1"
type: "gene"
col: 11712
ensembl_id: "ENSG00000185658"
name: "bromodomain and WD repeat domain containing 1"
location: "21q22.2"
module: 74
arm: "+"
pooled_cpm: 299.12
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# BRWD1

*bromodomain and WD repeat domain containing 1* — 21q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +11.6, q 2e-28, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.461× (z -21.5, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.827× (z -7.7, q 8e-13, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZMYM2]] (+0.66, fdr 7e-06), [[FBXL20]] (+0.64, fdr 7e-06), [[FOXN3]] (+0.60, fdr 1e-05); moves opposite to [[GPR156]] (-0.51, fdr 2e-05), [[INO80C]] (-0.50, fdr 8e-05), [[CDC42EP2]] (-0.50, fdr 4e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11712.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +11.6 | 2e-28 | 43/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +7.5 | 1e-11 | 35/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.28×** | +7.1 | 2e-10 | 33/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +5.5 | 6e-06 | 26/48 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.45×** | +5.4 | 8e-06 | 33/48 (SW480, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.18× | +4.8 | 1e-04 | 14/48 (NCI-H460, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +4.1 | 0.003 | 14/48 (LOX-IMVI, A498, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.15× | +4.0 | 0.004 | 12/47 (SNU-1, A-172, …) | top dose only |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.29×** | +3.7 | 0.013 | 27/48 (MIA PaCa-2, A549, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.4 | 0.034 | 14/47 (COLO 205, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.3 | 0.059 | 12/47 (SW480, H4, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.2 | 0.072 | 13/48 (H4, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 22 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11712.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.461×** | -21.5 | 0e+00 | 44/44 (AN3 CA, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.490×** | -20.6 | 0e+00 | 47/49 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -20.2 | 0e+00 | 45/45 (NCI-H2347, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.650×** | -12.4 | 2e-33 | 42/48 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.642×** | -12.3 | 1e-32 | 46/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.759×** | -11.2 | 2e-27 | 33/49 (NCI-H2030, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.695×** | -10.5 | 8e-24 | 40/48 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.827×** | -7.7 | 8e-13 | 27/48 (RKO, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.768×** | -7.6 | 2e-12 | 32/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.607×** | -7.2 | 3e-11 | 41/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.781×** | -7.1 | 6e-11 | 31/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | **0.811×** | -6.0 | 8e-08 | 29/48 (COLO 205, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.863× | -6.0 | 9e-08 | 24/48 (A-172, hTERT-HPNE, …) | rises with dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.823×** | -5.4 | 3e-06 | 26/50 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.703×** | -5.1 | 1e-05 | 30/47 (SW 900, SW48, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.890× | -4.7 | 8e-05 | 10/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -4.6 | 2e-04 | 14/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.734×** | -4.5 | 2e-04 | 28/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.735×** | -4.4 | 3e-04 | 32/48 (SW480, SW48, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.002 | 24/48 (SW480, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.918× | -3.5 | 0.011 | 0/48 | rises with dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.896× | -3.2 | 0.033 | 5/48 (SW 1088, AN3 CA, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.804×** | -3.2 | 0.033 | 19/48 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.05 µM |  | 0.893× | -3.0 | 0.049 | 10/48 (SW 1271, NCI-H1792, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.903× | -2.9 | 0.060 | 5/49 (NCI-H2347, NCI-H1573, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.855× | -2.9 | 0.061 | 13/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.855× | -2.9 | 0.061 | 11/48 (NCI-H23, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11712. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 341 | 0 | 13 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -17.3) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.627× (z -8.5) |
| [[A-172 (line)]] | wt | 322 | 0 | 11 (10 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.604× (z -13.1) |
| [[MIA PaCa-2 (line)]] | alt | 549 | 0 | 11 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -23.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 308 | 5 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +22.7) | [[Dinaciclib (drug)]] 0.5 µM 0.529× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H1573 (line)]] | alt | 551 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.327× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.05 µM 0.595× (z -8.7) |
| [[PANC-1 (line)]] | alt | 241 | 4 (1 ⚠) | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +15.4) | [[Dinaciclib (drug)]] 0.05 µM 0.473× (z -14.3) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 324 | 3 | 5 (5 ⚠) | [[TAK-901 (drug)]] 0.05 µM 1.93× (z +10.2) | [[Panobinostat (drug)]] 0.5 µM 0.489× (z -11.7) ⚠ cell-cycle shift, explains ~37% of this change |
| [[NCI-H23 (line)]] | alt | 328 | 2 | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.73× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.445× (z -14.5) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 211 | 0 | 7 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.498× (z -16.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[A-427 (line)]] | wt | 311 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.67× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.470× (z -13.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 401 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -22.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[COLO 205 (line)]] | alt | 275 | 5 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +14.8) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.58× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.434× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[H4 (line)]] | wt | 261 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.71× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 263 | 2 (1 ⚠) | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.391× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.542× (z -8.6) |
| [[NCI-H1792 (line)]] | alt | 303 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.389× (z -16.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 344 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -17.8) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 231 | 0 | 6 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -13.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HOP62 (line)]] | alt | 285 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.02× (z +10.6) | [[Dinaciclib (drug)]] 0.05 µM 0.422× (z -12.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 425 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.305× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H2347 (line)]] | alt | 286 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -19.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 282 | 2 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -22.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 337 | 1 | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.65× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.376× (z -15.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 375 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 219 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +11.7) ⚠ cell-cycle shift, explains ~4% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.10× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.534× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 247 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -15.1) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 401 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.463× (z -13.9) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 246 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -17.3) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HT-29 (line)]] | alt | 203 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -13.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 220 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -18.0) ⚠ cell-cycle shift, explains ~4% of this change |
| [[J82 (line)]] | alt | 253 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.300× (z -18.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 309 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.648× (z -12.2) ⚠ cell-cycle shift, explains ~4% of this change |
| [[NCI-H460 (line)]] | wt | 237 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 351 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.323× (z -16.8) ⚠ toxic · without an alert: [[Selinexor (drug)]] 5 µM 0.615× (z -10.6) |
| [[A498 (line)]] | wt | 249 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CHP-212 (line)]] | wt | 381 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 382 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -20.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 324 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.69× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.405× (z -14.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 274 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -17.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 263 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.483× (z -10.7) ⚠ cell-cycle shift, explains ~52% of this change |
| [[AN3 CA (line)]] | alt | 328 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0861× (z -25.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 206 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.435× (z -11.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 239 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 456 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[NCI-H661 (line)]] | alt | 344 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 232 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.526× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[KATO III (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 348 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 326 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11712), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM2]] | +0.66 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[FOXN3]] | +0.60 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[PHIP]] | +0.60 | +0.49 / +0.63 | both halves | 1e-05 | same gene group |
| [[TNRC6B]] | +0.59 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[KLHL24]] | +0.59 | +0.42 / +0.62 | both halves | 4e-05 |  |
| [[BRD3]] | +0.58 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[JMY]] | +0.58 | +0.35 / +0.68 | both halves | 1e-04 |  |
| [[MAP2K5]] | +0.58 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[FCHO2]] | +0.57 | +0.71 / +0.50 | both halves | 1e-05 |  |
| [[ZNRF2P1]] | +0.56 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[TUT4]] | +0.56 | +0.66 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPR156]] | -0.51 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[INO80C]] | -0.50 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[CDC42EP2]] | -0.50 | -0.47 / -0.41 | both halves | 4e-05 |  |
| [[NRAS]] | -0.48 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[MTRF1L]] | -0.48 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[RP2]] | -0.47 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ZKSCAN2]] | -0.46 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[PANX1]] | -0.46 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[UBXN11]] | -0.46 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[AP1B1]] | -0.45 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[NOP14-AS1]] | -0.45 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[BCAN-AS2]] | -0.45 | -0.46 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.434). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.7, -41.9); signed map (-16.4, 12.7). **Vector** length 104, 37.4% of its response variance represented; |z| ≥ 3 in 1,403 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.9 | +0.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.1 | +7.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.7 | +11.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +2.6 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | -0.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | -0.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.0 | +2.7 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.2 | -0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.2 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -4.8 | -3.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.7 | -7.7 |
|  | [[EX229 (drug)]] 5 µM |  | -4.4 | -4.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.3 | -1.2 |
|  | [[Belzutifan (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.1 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | bromodomain and WD repeat domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.2 — chr21:39,184,176-39,321,559 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11315, N143, DCAF19; previously C21orf107, WDR9 |
| Gene groups (HGNC) | Bromodomain and WD repeat domain containing |
| Reactome | 5 pathways, smallest: Interleukin-7 signaling; Chromatin modifying enzymes; Chromatin organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NSI6](https://www.uniprot.org/uniprotkb/Q9NSI6) (Bromodomain and WD repeat-containing protein 1):

> May be a transcriptional activator. May be involved in chromatin remodeling (By similarity). Required for regulation of cell morphology and cytoskeletal organization.

**Summary**, from NCBI Gene [54014](https://www.ncbi.nlm.nih.gov/gene/54014):

> This gene encodes a member of the WD repeat protein family. WD repeats are minimally conserved regions of approximately 40 amino acids typically bracketed by gly-his and trp-asp (GH-WD) residues which may facilitate formation of heterotrimeric or multiprotein complexes. Members of this family are involved in a variety of cellular processes including cell cycle progression, signal transduction, apoptosis, and gene regulation. This protein contains 2 bromodomains and multiple WD repeats. This …

**Accessions** — [HGNC:12760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12760) · Entrez [54014](https://www.ncbi.nlm.nih.gov/gene/54014) · UniProt [Q9NSI6](https://www.uniprot.org/uniprotkb/Q9NSI6) · Ensembl [ENSG00000185658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185658)

## Data

Gene col 11712: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11712); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11712, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11712]; `tensor/DDL_lfc|DDL_z.npy` [11712]; `embed/gene_vectors.npy` [11712]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11712 or target_col == 11712). Every well: [[BRWD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BRWD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
