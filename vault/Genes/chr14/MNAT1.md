---
symbol: "MNAT1"
type: "gene"
col: 321
ensembl_id: "ENSG00000020426"
name: "MNAT1 component of CDK activating kinase"
location: "14q23.1"
module: 17
arm: "+"
pooled_cpm: 212.37
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# MNAT1

*MNAT1 component of CDK activating kinase* — 14q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.74× (z +14.5, q 4e-45, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.443× (z -20.5, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.646× (z -16.2, q 0e+00, down in 47 of 49 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NDUFA12]] (+0.72, fdr 8e-06), [[VTA1]] (+0.68, fdr 1e-05), [[HDAC8]] (+0.66, fdr 7e-06); moves opposite to [[CSRNP2]] (-0.63, fdr 1e-05), [[TRIM39]] (-0.57, fdr 2e-04), [[TSTD2]] (-0.57, fdr 2e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +14.5 | 4e-45 | 46/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.62×** | +12.6 | 4e-34 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +9.6 | 2e-19 | 42/48 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.29×** | +9.4 | 8e-19 | 35/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.91×** | +8.0 | 8e-14 | 40/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +8.0 | 8e-14 | 37/48 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +7.4 | 1e-11 | 41/48 (KATO III, SW480, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.61×** | +5.9 | 3e-07 | 33/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.27×** | +5.8 | 4e-07 | 31/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.23×** | +5.5 | 3e-06 | 26/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +5.1 | 2e-05 | 25/48 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.0 | 3e-05 | 23/48 (BT-474, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +4.8 | 8e-05 | 17/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.46×** | +4.7 | 1e-04 | 37/49 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 1.19× | +4.5 | 2e-04 | 22/48 (RPMI-7951, HOP62, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.18× | +4.0 | 0.002 | 23/47 (SW48, LOX-IMVI, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +3.2 | 0.038 | 5/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.059 | 5/48 (SNU-423, HT-29, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.443×** | -20.5 | 0e+00 | 43/44 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.538×** | -16.2 | 0e+00 | 46/49 (NCI-H23, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -16.2 | 0e+00 | 47/49 (KATO III, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.582×** | -13.1 | 4e-37 | 42/45 (SW48, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.669×** | -10.5 | 9e-24 | 38/48 (HS-578T, CFPAC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.718×** | -8.3 | 7e-15 | 34/47 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -7.2 | 5e-11 | 37/50 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.794×** | -5.8 | 5e-07 | 26/48 (HOP62, SW48, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.903× | -3.8 | 0.010 | 14/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.963× | -3.3 | 0.048 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.887× | -3.1 | 0.081 | 13/48 (J82, BT-474, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 0.919× | -3.1 | 0.081 | 0/48 | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.890× | -3.0 | 0.10 | 12/48 (SNU-423, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 247 | 9 (4 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +15.7) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -13.0) |
| [[SW480 (line)]] | alt | 259 | 5 (1 ⚠) | 6 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.414× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -16.1) |
| [[MIA PaCa-2 (line)]] | alt | 301 | 4 (1 ⚠) | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.24× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.480× (z -12.3) |
| [[PANC-1 (line)]] | alt | 158 | 6 (2 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.540× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 339 | 5 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.56× (z +10.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.79× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.437× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.597× (z -12.5) |
| [[SW48 (line)]] | wt | 324 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.77× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -20.9) |
| [[C32 (line)]] | wt | 202 | 1 | 6 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 3.96× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.369× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.609× (z -9.8) |
| [[HOP62 (line)]] | alt | 181 | 2 | 5 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +14.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.500× (z -11.5) |
| [[J82 (line)]] | alt | 182 | 2 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 1.86× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.463× (z -18.3) |
| [[LOX-IMVI (line)]] | wt | 225 | 3 | 4 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.34× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.503× (z -15.2) |
| [[NCI-H2347 (line)]] | alt | 253 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.68× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -21.3) |
| [[LoVo (line)]] | wt | 186 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.23× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.408× (z -15.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 185 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -17.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 338 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.416× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 266 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.82× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.450× (z -17.6) |
| [[NCI-H2030 (line)]] | alt | 347 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.68× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.438× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 349 | 2 (1 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 1.91× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.88× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -25.1) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.528× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 314 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.99× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -20.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.602× (z -12.5) |
| [[SW1417 (line)]] | alt | 245 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.409× (z -13.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 194 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 1.78× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -21.4) |
| [[AsPC-1 (line)]] | alt | 150 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -10.4) |
| [[H4 (line)]] | wt | 210 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.36× (z +11.0) | [[Dinaciclib (drug)]] 0.05 µM 0.403× (z -10.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 228 | 1 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.75× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.615× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 206 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.199× (z -19.3) ⚠ toxic |
| [[HT-29 (line)]] | alt | 107 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.33× (z +11.4) | — |
| [[KATO III (line)]] | alt | 165 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +14.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 196 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.327× (z -21.3) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 187 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.429× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.630× (z -9.2) |
| [[SW 900 (line)]] | alt | 296 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.83× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -12.0) |
| [[AN3 CA (line)]] | alt | 374 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -10.8) |
| [[Hs 766T (line)]] | wt | 184 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.388× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.646× (z -8.9) |
| [[HS-578T (line)]] | alt | 127 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +10.1) | [[Docetaxel (drug)]] 0.05 µM 0.380× (z -12.7) ⚠ transcription drop |
| [[SHP-77 (line)]] | alt | 230 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.75× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -15.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 200 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.04× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.550× (z -11.8) |
| [[C-33 A (line)]] | alt | 198 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -11.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 259 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.248× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -9.3) |
| [[HCT15 (line)]] | alt | 284 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.401× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -9.1) |
| [[hTERT-HPNE (line)]] | wt | 121 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.98× (z +10.9) | — |
| [[NCI-H1573 (line)]] | alt | 211 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -18.2) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 255 | 0 | 2 (1 ⚠) | — | [[Hydroxyurea (drug)]] 0.05 µM 0.122× (z -14.6) |
| [[SNU-423 (line)]] | alt | 156 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.504× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 133 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -17.2) |
| [[LS 180 (line)]] | wt | 121 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -9.8) |
| [[SNU-1 (line)]] | wt | 281 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.561× (z -11.0) |
| [[SW 1088 (line)]] | alt | 164 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 195 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 241 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA12]] | +0.72 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[VTA1]] | +0.68 | +0.49 / +0.71 | both halves | 1e-05 | pathway: HIV Infection |
| [[HDAC8]] | +0.66 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[NDUFC2]] | +0.66 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[NDUFS4]] | +0.66 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[CSTPP1]] | +0.65 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[STX8]] | +0.65 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[IRAK1BP1]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[DPY30]] | +0.64 | +0.57 / +0.46 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression |
| [[METTL5]] | +0.63 | +0.37 / +0.61 | both halves | 8e-05 |  |
| [[DNAJC19]] | +0.63 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[IMMP1L]] | +0.62 | +0.68 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSRNP2]] | -0.63 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[TRIM39]] | -0.57 | -0.31 / -0.59 | both halves | 2e-04 | same gene group |
| [[TSTD2]] | -0.57 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[AOC2]] | -0.54 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | -0.53 | -0.46 / -0.28 | both halves | 3e-04 |  |
| [[ATXN1L]] | -0.53 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[ADCY10P1]] | -0.52 | -0.50 / -0.35 | both halves | 1e-04 |  |
| [[HIVEP1]] | -0.52 | -0.38 / -0.48 | both halves | 7e-05 |  |
| [[ZBTB21]] | -0.51 | -0.33 / -0.34 | both halves | 1e-04 |  |
| [[MAEA]] | -0.51 | -0.24 / -0.47 | both halves | 4e-04 |  |
| [[SECISBP2]] | -0.51 | -0.47 / -0.28 | both halves | 3e-04 |  |
| [[TRPV1]] | -0.51 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises MNAT1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.624). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-26.7, -5.2); signed map (-21.9, -12.3). **Vector** length 109, 37.4% of its response variance represented; |z| ≥ 3 in 1,288 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | +11.6 | +9.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +7.5 | +7.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +14.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +9.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.0 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +0.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +4.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -12.7 | -16.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -5.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -7.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.1 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.6 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.5 | -2.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | -1.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | MNAT1 component of CDK activating kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q23.1 — chr14:60,734,742-60,969,965 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAT1, RNF66 |
| Gene groups (HGNC) | Ring finger proteins; Nucleotide excision repair; CDK activating kinase complex; RING finger E3 ubiquitin protein ligases |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 55 pathways, smallest: RNA Pol II CTD phosphorylation and interaction with CE during HIV infection; RNA Pol II CTD phosphorylation and interaction with CE; mRNA Capping |
| Matched by | ensembl_id |

**Function**, from UniProt [P51948](https://www.uniprot.org/uniprotkb/P51948) (CDK-activating kinase assembly factor MAT1):

> Component of the CDK-activating kinase (CAK) complex, a master regulator of CDK activity by catalyzing the activating threonine phosphorylation of CDKs. Binds and activates CDK7, the catalytic subunit of CAK. CAK activates major mediators of cell cycle control, including CDK1, CDK2, CDK4 and CDK6, and plays a key role in regulating cell cycle progression. CAK complexed to the core-TFIIH basal transcription factor activates RNA polymerase II by serine phosphorylation of the repetitive C-terminal …

**Summary**, from NCBI Gene [4331](https://www.ncbi.nlm.nih.gov/gene/4331):

> The protein encoded by this gene, along with cyclin H and CDK7, forms the CDK-activating kinase (CAK) enzymatic complex. This complex activates several cyclin-associated kinases and can also associate with TFIIH to activate transcription by RNA polymerase II. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:7181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7181) · Entrez [4331](https://www.ncbi.nlm.nih.gov/gene/4331) · UniProt [P51948](https://www.uniprot.org/uniprotkb/P51948) · Ensembl [ENSG00000020426](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000020426)

## Data

Gene col 321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 321); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 321]; `tensor/DDL_lfc|DDL_z.npy` [321]; `embed/gene_vectors.npy` [321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 321 or target_col == 321). Every well: [[MNAT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MNAT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
