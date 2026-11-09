---
symbol: "AKAP10"
type: "gene"
col: 2975
ensembl_id: "ENSG00000108599"
name: "A-kinase anchoring protein 10"
location: "17p11.2"
module: 144
arm: "+"
pooled_cpm: 151.2
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 21
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# AKAP10

*A-kinase anchoring protein 10* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.56× (z +10.3, q 6e-22, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.259× (z -29.8, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.495× (z -16.1, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC1]] (+0.65, fdr 7e-06), [[RBPJ]] (+0.65, fdr 7e-06), [[PEX3]] (+0.63, fdr 7e-06); moves opposite to [[GATAD2A]] (-0.57, fdr 1e-05), [[LRP8]] (-0.55, fdr 1e-05), [[RNF32-AS1]] (-0.53, fdr 1e-05).
> It is in [[Module 144]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2975.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.56×** | +10.3 | 6e-22 | 38/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.16×** | +9.2 | 7e-18 | 42/48 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.92×** | +7.8 | 1e-12 | 41/49 (SW480, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.33×** | +6.6 | 6e-09 | 32/48 (PANC-1, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.23×** | +4.8 | 2e-04 | 27/48 (KATO III, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +4.5 | 6e-04 | 26/49 (A-427, A498, …) | top dose only |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.22×** | +4.4 | 1e-03 | 24/49 (A-427, NCI-H23, …) | top dose only | plate-row cell shift |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | 1.10× | +3.1 | 0.15 | 1/48 (AN3 CA) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2975.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.259×** | -29.8 | 0e+00 | 44/44 (A549, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.279×** | -29.3 | 0e+00 | 49/49 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.353×** | -22.1 | 0e+00 | 45/45 (A549, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.495×** | -16.1 | 0e+00 | 48/48 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -13.1 | 7e-37 | 47/48 (NCI-H2030, KATO III, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.602×** | -11.6 | 3e-29 | 46/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -11.2 | 2e-27 | 34/49 (LOX-IMVI, A549, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -9.7 | 2e-20 | 44/48 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.665×** | -9.4 | 5e-19 | 41/48 (NCI-H2030, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.680×** | -8.5 | 1e-15 | 29/47 (C32, C-33 A, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -6.9 | 3e-10 | 32/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.749×** | -6.4 | 8e-09 | 31/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.774×** | -5.9 | 2e-07 | 34/48 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.799×** | -5.2 | 1e-05 | 29/48 (SW 1088, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.654×** | -5.1 | 1e-05 | 39/48 (NCI-H1792, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.801×** | -4.9 | 3e-05 | 27/48 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.692×** | -4.4 | 3e-04 | 24/49 (LOX-IMVI, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.726×** | -3.8 | 0.004 | 24/48 (NCI-H1792, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.742×** | -3.6 | 0.010 | 23/48 (SNU-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.899× | -3.5 | 0.016 | 14/48 (HOP62, A-172, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.017 | 17/48 (NCI-H1573, SHP-77, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.755×** | -3.4 | 0.019 | 24/48 (Panc 03.27, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.769×** | -3.2 | 0.038 | 15/48 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.875× | -3.1 | 0.046 | 13/48 (C32, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2975. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 177 | 4 (3 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +14.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.97× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.239× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.355× (z -15.2) |
| [[NCI-H1573 (line)]] | alt | 163 | 3 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.252× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.379× (z -11.5) |
| [[KATO III (line)]] | alt | 157 | 3 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +16.3) | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -24.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.441× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 186 | 2 (1 ⚠) | 7 (5 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.76× (z +8.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.76× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.252× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.465× (z -11.8) |
| [[PANC-1 (line)]] | alt | 123 | 2 (1 ⚠) | 7 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +15.5) | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.499× (z -10.5) |
| [[SW480 (line)]] | alt | 147 | 3 | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.81× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.489× (z -12.7) |
| [[HEC-1-A (line)]] | alt | 150 | 3 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.24× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -26.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.540× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 169 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.00× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.248× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.456× (z -17.0) |
| [[NCI-H23 (line)]] | alt | 199 | 2 (1 ⚠) | 6 (4 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -12.4) |
| [[A549 (line)]] | wt | 229 | 1 (1 ⚠) | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.4) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 5 µM 0.0452× (z -39.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -15.9) |
| [[NCI-H1792 (line)]] | alt | 89.4 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.405× (z -10.7) |
| [[AsPC-1 (line)]] | alt | 111 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.188× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.398× (z -11.5) |
| [[C32 (line)]] | wt | 181 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.451× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 113 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.371× (z -13.1) |
| [[HOP62 (line)]] | alt | 223 | 1 | 5 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.145× (z -22.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.453× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 115 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.417× (z -12.2) |
| [[A-172 (line)]] | wt | 202 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.258× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -12.6) |
| [[A-427 (line)]] | wt | 132 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +13.8) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 5 µM 0.0618× (z -37.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.542× (z -8.5) |
| [[HS-578T (line)]] | alt | 122 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -12.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 138 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.176× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.459× (z -11.4) |
| [[NCI-H2347 (line)]] | alt | 80.2 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.353× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.511× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 317 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -25.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.497× (z -9.7) |
| [[HCT15 (line)]] | alt | 207 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.428× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 112 | 0 | 4 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0647× (z -14.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 247 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -25.1) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 119 | 2 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.07× (z +13.3) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -17.0) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 146 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.458× (z -9.0) |
| [[SNU-423 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -18.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 211 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.166× (z -22.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.492× (z -9.0) |
| [[SW1417 (line)]] | alt | 77.1 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.464× (z -10.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.482× (z -9.6) |
| [[A498 (line)]] | wt | 133 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -19.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 98.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.44× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.420× (z -8.8) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 218 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -22.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 178 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -8.6) |
| [[H4 (line)]] | wt | 177 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -12.8) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 83.8 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -15.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 120 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -20.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 98.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -19.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 267 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0866× (z -29.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 118 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 171 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -14.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -11.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 125 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.296× (z -13.2) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 145 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0634× (z -11.9) ⚠ transcription drop |
| [[SW 1271 (line)]] | alt | 306 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.207× (z -15.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 70.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 160 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 160 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2975), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC1]] | +0.65 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[RBPJ]] | +0.65 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[PEX3]] | +0.63 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[MED6]] | +0.62 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[WSB1]] | +0.61 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[OGA]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[HMGCL]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[TRIM7-AS2]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[FNTB]] | +0.60 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[SLC35E3]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[SPATA7]] | +0.59 | +0.75 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATAD2A]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[LRP8]] | -0.55 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.53 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[TTL]] | -0.52 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[GFOD1]] | -0.51 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[KPNA4]] | -0.51 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[DIAPH1]] | -0.51 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[DBN1]] | -0.50 | -0.49 / -0.44 | both halves | 3e-05 |  |
| [[C3orf52]] | -0.50 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[NOLC1]] | -0.49 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.696). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.8, -21.1); signed map (-31.5, 24.5). **Vector** length 117, 41.8% of its response variance represented; |z| ≥ 3 in 1,245 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +0.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | -0.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -0.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.9 | -0.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | +4.2 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.0 | -0.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | -3.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.7 | -1.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.5 | -9.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.7 | -8.5 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.9 | -3.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | A-kinase anchoring protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:19,904,302-19,978,343 (-) |
| Ensembl biotype | protein_coding |
| Also known as | D-AKAP2, PRKA10, MGC9414 |
| Gene groups (HGNC) | A-kinase anchoring proteins |
| Hallmark sets | COMPLEMENT |
| Reactome | 2 pathways, smallest: Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43572](https://www.uniprot.org/uniprotkb/O43572) (A-kinase anchor protein 10, mitochondrial):

> Differentially targeted protein that binds to type I and II regulatory subunits of protein kinase A and anchors them to the mitochondria or the plasma membrane. Although the physiological relevance between PKA and AKAPS with mitochondria is not fully understood, one idea is that BAD, a pro-apoptotic member, is phosphorylated and inactivated by mitochondria-anchored PKA. It cannot be excluded too that it may facilitate PKA as well as G protein signal transduction, by acting as an adapter for …

**Summary**, from NCBI Gene [11216](https://www.ncbi.nlm.nih.gov/gene/11216):

> This gene encodes a member of the A-kinase anchor protein family. A-kinase anchor proteins bind to the regulatory subunits of protein kinase A (PKA) and confine the holoenzyme to discrete locations within the cell. The encoded protein is localized to mitochondria and interacts with both the type I and type II regulatory subunits of PKA. Polymorphisms in this gene may be associated with increased risk of arrhythmias and sudden cardiac death. [provided by RefSeq, May 2012]

**Accessions** — [HGNC:368](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:368) · Entrez [11216](https://www.ncbi.nlm.nih.gov/gene/11216) · UniProt [O43572](https://www.uniprot.org/uniprotkb/O43572) · Ensembl [ENSG00000108599](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108599)

## Data

Gene col 2975: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2975); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2975, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2975]; `tensor/DDL_lfc|DDL_z.npy` [2975]; `embed/gene_vectors.npy` [2975]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2975 or target_col == 2975). Every well: [[AKAP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AKAP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
