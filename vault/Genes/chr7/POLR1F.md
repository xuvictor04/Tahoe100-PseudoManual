---
symbol: "POLR1F"
type: "gene"
col: 2674
ensembl_id: "ENSG00000105849"
name: "RNA polymerase I subunit F"
location: "7p21.1"
module: 1
arm: "+"
pooled_cpm: 37.98
n_lines_expressing: 50
n_dd_up: 46
n_dd_down: 0
n_dd_up_clean: 24
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# POLR1F

*RNA polymerase I subunit F* — 7p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 46 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.18× (z +19.3, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 4.02× (z +15.8, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTPAP]] (+0.73, fdr 7e-06), [[PAK1IP1]] (+0.71, fdr 7e-06), [[RRP15]] (+0.70, fdr 7e-06); moves opposite to [[MBOAT7]] (-0.64, fdr 7e-06), [[KDELR1]] (-0.58, fdr 1e-05), [[CRELD1]] (-0.56, fdr 1e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 23 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 46 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2674.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.18×** | +19.3 | 0e+00 | 48/48 (A498, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.02×** | +15.8 | 0e+00 | 48/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.56×** | +15.0 | 0e+00 | 47/48 (A498, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **2.86×** | +12.4 | 2e-33 | 48/48 (PANC-1, BT-474, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.91×** | +12.2 | 6e-32 | 47/47 (KATO III, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.78×** | +12.1 | 1e-31 | 48/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **2.71×** | +11.8 | 4e-30 | 48/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.62×** | +11.4 | 3e-28 | 48/48 (A498, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **2.65×** | +10.7 | 9e-25 | 38/42 (NCI-H1792, LoVo, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **2.17×** | +9.2 | 2e-18 | 44/48 (KATO III, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.05×** | +8.5 | 1e-15 | 44/48 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.02×** | +8.3 | 3e-15 | 43/48 (A498, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.99×** | +7.8 | 2e-13 | 39/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.74×** | +6.6 | 2e-09 | 34/46 (NCI-H23, NCI-H1573, …) | all doses, flat | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.70×** | +6.3 | 1e-08 | 40/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.68×** | +5.9 | 1e-07 | 32/48 (NCI-H1792, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.41×** | +5.8 | 2e-07 | 35/48 (SNU-423, A549, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +5.3 | 3e-06 | 34/48 (RPMI-7951, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.48×** | +4.7 | 6e-05 | 29/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +4.0 | 0.001 | 23/48 (Panc 03.27, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.002 | 24/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.004 | 22/48 (PANC-1, A498, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.3 | 0.016 | 22/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +3.3 | 0.018 | 21/48 (PANC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.038 | 20/47 (LOX-IMVI, NCI-H460, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2674.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (KATO III 0.264×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 0.723× | -3.7 | 0.11 | 23/48 (SW 1271, RKO, …) | top dose only | plate-row cell shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -3.5 | 0.11 | 4/48 (NCI-H23, HT-29, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.59 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2674. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 37.8 | 9 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.08× (z +13.5) | — |
| [[A498 (line)]] | wt | 48.9 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +19.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 7.37× (z +17.0) | — |
| [[A-172 (line)]] | wt | 30.3 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.40× (z +15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.87× (z +11.2) | — |
| [[H4 (line)]] | wt | 42.0 | 7 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 7.54× (z +10.9) | — |
| [[KATO III (line)]] | alt | 48.4 | 6 (4 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.78× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 32.1 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.16× (z +13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.57× (z +11.2) | — |
| [[Hs 766T (line)]] | wt | 37.6 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.61× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 26.7 | 6 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +13.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 6.49× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 19.6 | 6 (5 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.90× (z +8.5) | — |
| [[NCI-H460 (line)]] | wt | 56.7 | 6 (4 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 3.31× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 24.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.63× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.19× (z +9.5) | — |
| [[LoVo (line)]] | wt | 34.5 | 5 (4 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.92× (z +11.2) | — |
| [[LOX-IMVI (line)]] | wt | 29.8 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.84× (z +10.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 41.4 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +13.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.96× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 24.0 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +10.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.56× (z +9.6) | — |
| [[SW480 (line)]] | alt | 43.5 | 5 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 4.00× (z +12.4) | — |
| [[AsPC-1 (line)]] | alt | 31.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.77× (z +9.1) | — |
| [[BT-474 (line)]] | alt | 46.3 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.43× (z +15.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.92× (z +11.5) | — |
| [[HEC-1-A (line)]] | alt | 42.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +13.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.87× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 24.8 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +12.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 9.20× (z +11.5) | — |
| [[NCI-H1792 (line)]] | alt | 37.6 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 7.48× (z +12.8) | — |
| [[NCI-H23 (line)]] | alt | 49.2 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.71× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.01× (z +11.4) | — |
| [[NCI-H2347 (line)]] | alt | 33.5 | 4 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.74× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +9.5) | — |
| [[SW 900 (line)]] | alt | 45.7 | 4 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.25× (z +12.4) | — |
| [[A-427 (line)]] | wt | 31.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.20× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.56× (z +8.9) | — |
| [[C32 (line)]] | wt | 33.3 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +11.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 4.71× (z +9.2) | — |
| [[HOP62 (line)]] | alt | 18.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +11.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.56× (z +9.4) | — |
| [[J82 (line)]] | alt | 29.8 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.88× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 4.01× (z +9.3) | — |
| [[SW48 (line)]] | wt | 50.6 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.22× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 5.29× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 22.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.08× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +9.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 8.47× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 44.9 | 2 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.28× (z +9.2) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.26× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 38.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.10× (z +9.9) | — |
| [[RPMI-7951 (line)]] | alt | 40.2 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.08× (z +9.5) | — |
| [[RKO (line)]] | wt | 59.8 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.96× (z +10.0) ⚠ toxic | — |
| [[SHP-77 (line)]] | alt | 67.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +9.4) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW1417 (line)]] | alt | 67.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 58.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2674), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | +0.73 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[PAK1IP1]] | +0.71 | +0.70 / +0.75 | both halves | 7e-06 | STRING 644 |
| [[RRP15]] | +0.70 | +0.74 / +0.68 | both halves | 7e-06 | STRING 600 |
| [[AASDHPPT]] | +0.65 | +0.76 / +0.72 | both halves | 7e-06 |  |
| [[N6AMT1]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[RRS1]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 | STRING 872 |
| [[NDUFAF4]] | +0.62 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[DDX20]] | +0.62 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[SRFBP1]] | +0.61 | +0.70 / +0.55 | both halves | 1e-05 | STRING 493 |
| [[UTP15]] | +0.60 | +0.69 / +0.59 | both halves | 7e-06 | STRING 573 |
| [[ZNF260]] | +0.60 | +0.72 / +0.59 | both halves | 7e-06 |  |
| [[NUFIP1]] | +0.60 | +0.54 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MBOAT7]] | -0.64 | -0.63 / -0.67 | both halves | 7e-06 |  |
| [[KDELR1]] | -0.58 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[CRELD1]] | -0.56 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[PHF1]] | -0.55 | -0.68 / -0.54 | both halves | 1e-05 | pathway: Epigenetic regulation of gene expression |
| [[SURF4]] | -0.55 | -0.63 / -0.57 | both halves | 1e-05 |  |
| [[ZCCHC17]] | -0.55 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[RABGEF1]] | -0.55 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[TPTEP2-CSNK1E]] | -0.55 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[INPP5A]] | -0.55 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[KDELR2]] | -0.54 | -0.61 / -0.56 | both halves | 1e-05 |  |
| [[OSBPL2]] | -0.54 | -0.64 / -0.57 | both halves | 9e-06 |  |
| [[CDC26]] | -0.54 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLR1F's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.620). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-17.8, -37.8); signed map (-0.0, -42.1). **Vector** length 68.2, 20.2% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +12.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.4 | +8.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.9 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +15.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.4 | +5.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.9 | +3.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +1.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.6 | +3.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -3.2 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | -2.4 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -2.4 | +3.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -0.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.4 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | RNA polymerase I subunit F |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p21.1 — chr7:19,695,461-19,709,037 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPA43, A43; previously TWISTNB |
| Gene groups (HGNC) | RNA polymerase subunits; MicroRNA protein coding host genes |
| Reactome | 9 pathways, smallest: RNA Polymerase I Transcription Termination; B-WICH complex positively regulates rRNA expression; RNA Polymerase I Promoter Escape |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3B726](https://www.uniprot.org/uniprotkb/Q3B726) (DNA-directed RNA polymerase I subunit RPA43):

> Component of RNA polymerase I (Pol I), a DNA-dependent RNA polymerase which synthesizes ribosomal RNA precursors using the four ribonucleoside triphosphates as substrates. Through its association with RRN3/TIF-IA may be involved in recruitment of Pol I to rDNA promoters.

**Summary**, from NCBI Gene [221830](https://www.ncbi.nlm.nih.gov/gene/221830):

> Involved in transcription elongation by RNA polymerase I. Located in fibrillar center and nucleoplasm. Part of RNA polymerase I complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18027) · Entrez [221830](https://www.ncbi.nlm.nih.gov/gene/221830) · UniProt [Q3B726](https://www.uniprot.org/uniprotkb/Q3B726) · Ensembl [ENSG00000105849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105849)

## Data

Gene col 2674: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2674); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2674, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2674]; `tensor/DDL_lfc|DDL_z.npy` [2674]; `embed/gene_vectors.npy` [2674]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2674 or target_col == 2674). Every well: [[POLR1F — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLR1F.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
