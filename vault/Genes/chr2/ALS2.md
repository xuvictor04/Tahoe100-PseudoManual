---
symbol: "ALS2"
type: "gene"
col: 32
ensembl_id: "ENSG00000003393"
name: "alsin Rho guanine nucleotide exchange factor ALS2"
location: "2q33.1"
module: 57
arm: "-"
pooled_cpm: 78.44
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 3
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# ALS2

*alsin Rho guanine nucleotide exchange factor ALS2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.17× (z +22.9, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.712× (z -6.9, q 3e-09, down in 29 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (KATO III 0.0694×, C-33 A 0.132×, SK-MEL-2 0.172×, AN3 CA 0.0913×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Hs 766T 0.178×, A-427 0.308×, C-33 A 0.300×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.378×, NCI-H1573 0.358×, NCI-H1792 0.376×; ⚠ toxic; transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H596 0.218×); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.228×).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREM]] (+0.67, fdr 1e-05), [[RHBDD3]] (+0.64, fdr 1e-05), [[CDK12]] (+0.58, fdr 3e-04); moves opposite to [[ALDH7A1]] (-0.57, fdr 6e-04), [[ELP1]] (-0.55, fdr 2e-04), [[ORC4]] (-0.54, fdr 4e-04).
> It sits in the **-** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[POGLUT2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 32.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.17×** | +22.9 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.51×** | +19.3 | 0e+00 | 48/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.42×** | +18.5 | 0e+00 | 47/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.27×** | +17.2 | 0e+00 | 47/48 (A498, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.12×** | +13.9 | 4e-42 | 46/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.93×** | +13.8 | 2e-41 | 42/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.84×** | +12.8 | 1e-35 | 45/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +12.7 | 3e-35 | 38/49 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.82×** | +12.5 | 3e-34 | 45/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.63×** | +10.2 | 1e-22 | 38/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.60×** | +9.9 | 3e-21 | 37/48 (SNU-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.63×** | +9.8 | 6e-21 | 40/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.49×** | +8.1 | 3e-14 | 39/48 (C32, HOP62, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +7.4 | 4e-12 | 39/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.93×** | +6.7 | 1e-09 | 40/49 (AsPC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 3e-08 | 34/48 (AsPC-1, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.5 | 1e-06 | 30/48 (SNU-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 32.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (KATO III 0.0694×, C-33 A 0.132×, SK-MEL-2 0.172×, AN3 CA 0.0913×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (Hs 766T 0.178×, A-427 0.308×, C-33 A 0.300×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (NCI-H460 0.378×, NCI-H1573 0.358×, NCI-H1792 0.376×; ⚠ toxic; transcription drop); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (NCI-H596 0.218×); [[Atazanavir (sulfate) (drug)]] 0.05 µM in 1 line (NCI-H596 0.228×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.712×** | -6.9 | 3e-09 | 29/44 (KATO III, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.712×** | -6.3 | 8e-08 | 29/45 (Hs 766T, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.753×** | -6.0 | 4e-07 | 32/49 (NCI-H460, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~74% of this change | 0.838× | -3.8 | 0.024 | 21/48 (SW480, CHP-212, …) | inconsistent across doses | low cells (technical?) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | 0.851× | -3.4 | 0.067 | 18/47 (A-427, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 0.727× | -3.3 | 0.10 | 17/45 (AsPC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 0.863× | -3.1 | 0.14 | 14/48 (SK-MEL-2, hTERT-HPNE, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 0.862× | -3.0 | 0.18 | 15/48 (NCI-H2030, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 32. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 38.0 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 62.0 | 10 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +18.1) | — |
| [[NCI-H460 (line)]] | wt | 109 | 8 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -12.7) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 60.2 | 8 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +11.7) | — |
| [[SW480 (line)]] | alt | 71.3 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +18.0) | — |
| [[COLO 205 (line)]] | alt | 78.2 | 7 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.15× (z +11.2) | — |
| [[LoVo (line)]] | wt | 60.8 | 6 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.461× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 66.5 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.376× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 32.0 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +14.9) | — |
| [[PANC-1 (line)]] | alt | 113 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +21.0) | — |
| [[SW1417 (line)]] | alt | 80.0 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +15.1) | — |
| [[A498 (line)]] | wt | 71.5 | 6 | 0 | [[Panobinostat (drug)]] 5 µM 3.46× (z +15.0) | — |
| [[KATO III (line)]] | alt | 55.8 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.83× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.0694× (z -26.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 84.7 | 4 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.00× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.310× (z -13.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 75.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.172× (z -17.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 87.7 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.17× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 57.3 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 54.0 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 57.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 3.22× (z +11.4) | — |
| [[J82 (line)]] | alt | 83.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +16.0) | — |
| [[NCI-H23 (line)]] | alt | 113 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.419× (z -10.7) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 94.2 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +10.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.85× (z +8.9) | — |
| [[H4 (line)]] | wt | 81.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +12.6) | — |
| [[HepG2_C3A (line)]] | wt | 89.2 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.22× (z +10.6) | — |
| [[Hs 766T (line)]] | wt | 50.6 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -14.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 64.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.52× (z +12.7) | — |
| [[hTERT-HPNE (line)]] | wt | 58.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 95.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.367× (z -10.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 62.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +10.9) | — |
| [[RKO (line)]] | wt | 99.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +15.0) | — |
| [[RPMI-7951 (line)]] | alt | 68.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.35× (z +11.6) | — |
| [[SNU-1 (line)]] | wt | 80.5 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.25× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.221× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 77.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 2.79× (z +11.8) | — |
| [[A549 (line)]] | wt | 75.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.40× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 122 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.381× (z -10.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 40.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.14× (z +9.1) | — |
| [[C-33 A (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -19.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 106 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +18.2) | — |
| [[NCI-H596 (line)]] | alt | 74.5 | 0 | 2 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.218× (z -10.7) |
| [[SW48 (line)]] | wt | 48.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -8.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.308× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 116 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0913× (z -15.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 80.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +9.5) | — |
| [[SHP-77 (line)]] | alt | 60.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 133 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +9.0) | — |
| [[CHP-212 (line)]] | wt | 78.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 32), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREM]] | +0.67 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[RHBDD3]] | +0.64 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[CDK12]] | +0.58 | +0.68 / +0.27 | both halves | 3e-04 |  |
| [[SLC38A6]] | +0.57 | +0.67 / +0.34 | both halves | 1e-04 |  |
| [[SLC66A1]] | +0.56 | +0.63 / +0.42 | both halves | 4e-05 |  |
| [[TBCA]] | +0.56 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[MAFG]] | +0.55 | +0.68 / +0.28 | both halves | 3e-04 |  |
| [[RABEP1]] | +0.55 | +0.68 / +0.49 | both halves | 1e-05 | pathway: Rab regulation of trafficking; STRING 502 |
| [[FBXO30]] | +0.54 | +0.65 / +0.27 | both halves | 3e-04 |  |
| [[FTX]] | +0.54 | +0.63 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[HTATIP2]] | +0.53 | +0.64 / +0.27 | both halves | 3e-04 |  |
| [[MRPL45P2]] | +0.53 | +0.64 / +0.32 | both halves | 2e-04 |  |
| [[PSMA4]] | +0.53 | +0.63 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH7A1]] | -0.57 | -0.56 / -0.22 | both halves | 6e-04 |  |
| [[ELP1]] | -0.55 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[ORC4]] | -0.54 | -0.62 / -0.25 | both halves | 4e-04 |  |
| [[CYB5A]] | -0.54 | -0.53 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ANAPC5]] | -0.53 | -0.63 / -0.27 | both halves | 3e-04 |  |
| [[NUDT21]] | -0.53 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[ABHD10]] | -0.52 | -0.64 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[SDHAF3]] | -0.52 | -0.60 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[MMUT]] | -0.52 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[PRMT9]] | -0.52 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[H3-3A]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FRG1DP]] | -0.51 | -0.39 / -0.36 | both halves | 1e-04 |  |
| [[MCMBP]] | -0.51 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[LRRC1]] | -0.50 | -0.53 / -0.24 | both halves | 4e-04 |  |
| [[PPP1CB]] | -0.48 | -0.54 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POGLUT2]] | C | POGLUT2 activity raises ALS2's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without POGLUT2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **-** arm (projection on the module's main direction -0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-16.4, 11.2); signed map (21.2, -24.6). **Vector** length 73.5, 19.2% of its response variance represented; |z| ≥ 3 in 1,272 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +8.0 | +13.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.9 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.6 | +12.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.1 | +7.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +2.9 | +9.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.5 | +4.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.1 | +3.1 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -4.0 | +19.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.5 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | +17.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.4 | +18.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Gemcitabine (drug)]] 0.5 µM |  | -1.2 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | alsin Rho guanine nucleotide exchange factor ALS2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:201,700,267-201,782,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ALS2CR6 |
| Gene groups (HGNC) | Dbl family Rho GEFs; VPS9 domain containing; MORN repeat containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 8 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96Q42](https://www.uniprot.org/uniprotkb/Q96Q42) (Alsin):

> May act as a GTPase regulator. Controls survival and growth of spinal motoneurons (By similarity).

**Summary**, from NCBI Gene [57679](https://www.ncbi.nlm.nih.gov/gene/57679):

> The protein encoded by this gene contains an ATS1/RCC1-like domain, a RhoGEF domain, and a vacuolar protein sorting 9 (VPS9) domain, all of which are guanine-nucleotide exchange factors that activate members of the Ras superfamily of GTPases. The protein functions as a guanine nucleotide exchange factor for the small GTPase RAB5. The protein localizes with RAB5 on early endosomal compartments, and functions as a modulator for endosomal dynamics. Mutations in this gene result in several forms of …

**Accessions** — [HGNC:443](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:443) · Entrez [57679](https://www.ncbi.nlm.nih.gov/gene/57679) · UniProt [Q96Q42](https://www.uniprot.org/uniprotkb/Q96Q42) · Ensembl [ENSG00000003393](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000003393)

## Data

Gene col 32: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 32); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 32, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 32]; `tensor/DDL_lfc|DDL_z.npy` [32]; `embed/gene_vectors.npy` [32]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 32 or target_col == 32). Every well: [[ALS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
