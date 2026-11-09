---
symbol: "SLU7"
type: "gene"
col: 8969
ensembl_id: "ENSG00000164609"
name: "spliceosome associated SLU7"
location: "5q33.3"
module: 74
arm: "+"
pooled_cpm: 89.07
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 16
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# SLU7

*spliceosome associated SLU7* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +17.4, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +11.8, q 1e-29, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.353× (z -15.3, q 0e+00, down in 46 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.449× (z -6.4, q 5e-08, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCC2]] (+0.85, fdr 7e-06), [[SYF2]] (+0.81, fdr 7e-06), [[NBR1]] (+0.77, fdr 7e-06); moves opposite to [[CS]] (-0.66, fdr 9e-06), [[HEATR3]] (-0.65, fdr 1e-05), [[TFDP1]] (-0.63, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8969.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.26×** | +17.4 | 0e+00 | 46/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +11.8 | 1e-29 | 48/49 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.03×** | +10.9 | 3e-25 | 44/48 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.87×** | +9.3 | 3e-18 | 44/48 (HOP62, NCI-H2347, …) | rises with dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +7.4 | 1e-11 | 37/48 (BT-474, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +6.7 | 2e-09 | 44/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +6.6 | 4e-09 | 45/48 (HOP62, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +6.5 | 5e-09 | 43/47 (HT-29, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.51×** | +6.4 | 1e-08 | 34/48 (LoVo, AsPC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.2 | 3e-08 | 36/48 (A549, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.48×** | +6.0 | 9e-08 | 40/48 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +5.1 | 1e-05 | 35/50 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.8 | 6e-05 | 32/48 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +4.4 | 5e-04 | 25/48 (NCI-H2347, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.002 | 25/48 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.024 | 20/48 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.024 | 21/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.053 | 23/48 (KATO III, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.085 | 22/48 (NCI-H2030, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8969.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.353×** | -15.3 | 0e+00 | 46/48 (NCI-H2347, LOX-IMVI, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.449×** | -6.4 | 5e-08 | 44/48 (Hs 766T, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.464×** | -6.1 | 2e-07 | 41/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.479×** | -5.9 | 6e-07 | 39/48 (AsPC-1, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.488×** | -5.7 | 1e-06 | 37/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.495×** | -5.6 | 2e-06 | 44/48 (SW1417, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.05 µM |  | **0.691×** | -5.3 | 9e-06 | 38/48 (AsPC-1, Hs 766T, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | **0.829×** | -4.0 | 0.005 | 25/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.832×** | -3.9 | 0.006 | 21/48 (SW 900, HT-29, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.579×** | -3.7 | 0.015 | 29/48 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8969. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 66.3 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +20.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +15.6) | — |
| [[LoVo (line)]] | wt | 79.0 | 5 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +16.3) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.322× (z -11.9) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 133 | 5 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Selinexor (drug)]] 5 µM 1.85× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -15.6) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 72.8 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.56× (z +16.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.294× (z -11.0) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 67.1 | 5 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.54× (z +11.2) | — |
| [[NCI-H460 (line)]] | wt | 80.6 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.29× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.359× (z -10.0) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 87.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +15.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.55× (z +10.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.342× (z -11.7) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 82.6 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +15.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.97× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 81.9 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +10.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.336× (z -11.1) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 85.8 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +22.9) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.76× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.391× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 78.1 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.71× (z +18.5) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.32× (z +8.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.360× (z -9.9) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 96.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.8) | [[Lonafarnib (drug)]] 5 µM 0.139× (z -10.1) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 76.0 | 3 (2 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.390× (z -10.6) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 122 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.308× (z -12.9) ⚠ unreliable plate only |
| [[AsPC-1 (line)]] | alt | 114 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.7) ⚠ cell-cycle shift, explains ~46% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.246× (z -14.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.438× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 85.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -10.7) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 96.4 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +13.8) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.95× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -10.3) ⚠ unreliable plate only |
| [[HT-29 (line)]] | alt | 77.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +13.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 2.50× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.312× (z -11.8) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 79.0 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.381× (z -8.6) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 84.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.6) ⚠ cell-cycle shift, explains ~46% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -10.5) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 80.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +15.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.52× (z +9.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.214× (z -15.4) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 79.1 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -10.3) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 82.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.4) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.329× (z -11.4) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 164 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +12.6) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.382× (z -8.8) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 112 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +9.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.408× (z -9.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 78.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +9.8) | — |
| [[COLO 205 (line)]] | alt | 89.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +12.5) ⚠ cell-cycle shift, explains ~31% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -11.1) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 104 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.292× (z -11.7) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 73.3 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +14.2) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +9.3) | — |
| [[NCI-H23 (line)]] | alt | 90.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.8) ⚠ cell-cycle shift, explains ~31% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.358× (z -9.3) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 88.4 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.13× (z +10.1) | — |
| [[SHP-77 (line)]] | alt | 88.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.388× (z -9.2) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 113 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.8) ⚠ cell-cycle shift, explains ~31% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.343× (z -11.6) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 113 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.35× (z +9.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.359× (z -10.9) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 89.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +9.3) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[AN3 CA (line)]] | alt | 101 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.206× (z -9.3) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.257× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 76.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -9.3) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 79.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.65× (z +8.8) | — |
| [[SW48 (line)]] | wt | 54.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[CHP-212 (line)]] | wt | 83.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 68.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 96.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 99.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 85.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8969), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCC2]] | +0.85 | +0.80 / +0.85 | both halves | 7e-06 |  |
| [[SYF2]] | +0.81 | +0.73 / +0.85 | both halves | 7e-06 | same gene group; pathway: Processing of Capped Intron-Containing Pre-mRNA; STRING 995 |
| [[NBR1]] | +0.77 | +0.75 / +0.80 | both halves | 7e-06 |  |
| [[RB1CC1]] | +0.77 | +0.57 / +0.82 | both halves | 9e-06 |  |
| [[CREBRF]] | +0.76 | +0.60 / +0.80 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.75 | +0.48 / +0.81 | both halves | 2e-05 |  |
| [[CIR1]] | +0.75 | +0.68 / +0.80 | both halves | 7e-06 | STRING 547 |
| [[BOD1L1]] | +0.73 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[TBC1D15]] | +0.73 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[EAPP]] | +0.72 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[RSF1]] | +0.72 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[PAIP2]] | +0.71 | +0.40 / +0.80 | both halves | 5e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CS]] | -0.66 | -0.57 / -0.69 | both halves | 9e-06 |  |
| [[HEATR3]] | -0.65 | -0.56 / -0.60 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.63 | -0.69 / -0.56 | both halves | 1e-05 |  |
| [[CAD]] | -0.61 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[PPP5C]] | -0.60 | -0.66 / -0.51 | both halves | 1e-05 |  |
| [[FAR1]] | -0.59 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[LMNB2]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[BOP1]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[GOT2]] | -0.58 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[NME1]] | -0.58 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[POLR3G]] | -0.58 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[POFUT1]] | -0.58 | -0.42 / -0.60 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLU7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -45.4); signed map (-14.0, 9.1). **Vector** length 117, 41.3% of its response variance represented; |z| ≥ 3 in 1,150 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +4.6 | +17.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.4 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.1 | +10.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.0 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +7.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +2.9 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -15.5 | -15.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.2 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -9.0 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -8.5 | -5.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.5 | -5.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.3 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | spliceosome associated SLU7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:160,401,641-160,421,711 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 9G8 |
| Gene groups (HGNC) | NTC associated proteins; Spliceosomal C complex; Spliceosomal P complex; U11 small nuclear ribonucleoprotein |
| Reactome | 7 pathways, smallest: Transport of Mature mRNA derived from an Intron-Containing Transcript; Transport of Mature Transcript to Cytoplasm; mRNA 3'-end processing |
| Matched by | ensembl_id |

**Function**, from UniProt [O95391](https://www.uniprot.org/uniprotkb/O95391) (Pre-mRNA-splicing factor SLU7):

> Required for pre-mRNA splicing as component of the spliceosome. Participates in the second catalytic step of pre-mRNA splicing, when the free hydroxyl group of exon I attacks the 3'-splice site to generate spliced mRNA and the excised lariat intron. Required for holding exon 1 properly in the spliceosome and for correct AG identification when more than one possible AG exists in 3'-splicing site region. May be involved in the activation of proximal AG. Probably also involved in alternative …

**Summary**, from NCBI Gene [10569](https://www.ncbi.nlm.nih.gov/gene/10569):

> Pre-mRNA splicing occurs in two sequential transesterification steps. The protein encoded by this gene is a splicing factor that has been found to be essential during the second catalytic step in the pre-mRNA splicing process. It associates with the spliceosome and contains a zinc knuckle motif that is found in other splicing factors and is involved in protein-nucleic acid and protein-protein interactions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:16939](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16939) · Entrez [10569](https://www.ncbi.nlm.nih.gov/gene/10569) · UniProt [O95391](https://www.uniprot.org/uniprotkb/O95391) · Ensembl [ENSG00000164609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164609)

## Data

Gene col 8969: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8969); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8969, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8969]; `tensor/DDL_lfc|DDL_z.npy` [8969]; `embed/gene_vectors.npy` [8969]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8969 or target_col == 8969). Every well: [[SLU7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLU7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
