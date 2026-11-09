---
symbol: "SMIM14"
type: "gene"
col: 8752
ensembl_id: "ENSG00000163683"
name: "small integral membrane protein 14"
location: "4p14"
module: 69
arm: "+"
pooled_cpm: 94.22
n_lines_expressing: 50
n_dd_up: 34
n_dd_down: 26
n_dd_up_clean: 28
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# SMIM14

*small integral membrane protein 14* — 4p14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.40× (z +18.9, q 0e+00, up in 45 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.266× (z -20.2, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.482× (z -11.2, q 2e-26, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC186]] (+0.72, fdr 7e-06), [[UBN2]] (+0.71, fdr 1e-05), [[CREBRF]] (+0.67, fdr 1e-05); moves opposite to [[POP1]] (-0.66, fdr 8e-06), [[PDSS1]] (-0.66, fdr 1e-05), [[NOL10]] (-0.64, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8752.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +18.9 | 0e+00 | 45/49 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.37×** | +12.7 | 2e-34 | 44/48 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.20×** | +11.6 | 1e-28 | 42/50 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.60×** | +7.2 | 1e-10 | 28/47 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +6.8 | 1e-09 | 25/39 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.28×** | +5.3 | 8e-06 | 27/48 (HOP62, SNU-423, …) | rises with dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.3 | 8e-06 | 32/48 (HOP62, A-427, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.41×** | +5.2 | 1e-05 | 37/49 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 2e-05 | 27/48 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +5.1 | 2e-05 | 25/48 (BT-474, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 6e-05 | 27/48 (AsPC-1, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +4.5 | 3e-04 | 24/48 (SK-MEL-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +4.5 | 3e-04 | 23/49 (SW480, PANC-1, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +4.5 | 3e-04 | 30/47 (A549, NCI-H460, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.35×** | +4.5 | 3e-04 | 29/48 (A549, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.33×** | +4.3 | 6e-04 | 25/48 (SK-MEL-2, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +4.2 | 1e-03 | 21/48 (CFPAC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.001 | 24/48 (NCI-H460, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8752.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.266×** | -20.2 | 0e+00 | 48/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.482×** | -11.2 | 2e-26 | 41/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 5 µM |  | **0.262×** | -10.7 | 2e-24 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.289×** | -9.9 | 5e-21 | 46/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.290×** | -9.9 | 5e-21 | 45/48 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.340×** | -8.6 | 7e-16 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.356×** | -8.2 | 1e-14 | 42/48 (LS 180, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.360×** | -8.2 | 2e-14 | 42/49 (HT-29, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.367×** | -8.0 | 8e-14 | 42/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -7.2 | 4e-11 | 34/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.522×** | -7.1 | 7e-11 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.621×** | -6.9 | 3e-10 | 36/48 (BT-474, HT-29, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -6.5 | 4e-09 | 31/47 (HCT15, SW 900, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.702×** | -5.4 | 3e-06 | 32/48 (KATO III, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.708×** | -5.0 | 2e-05 | 27/47 (BT-474, Panc 03.27, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.713×** | -4.9 | 4e-05 | 29/48 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.743×** | -4.5 | 2e-04 | 28/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8752. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 226 | 0 | 14 (5 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.167× (z -20.3) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 0.351× (z -11.9) |
| [[PANC-1 (line)]] | alt | 95.1 | 2 (2 ⚠) | 10 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.69× (z +11.4) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.139× (z -22.7) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.299× (z -13.9) |
| [[SW 900 (line)]] | alt | 226 | 2 | 9 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +9.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -18.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.162× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 101 | 3 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +16.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -19.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.109× (z -10.9) |
| [[NCI-H460 (line)]] | wt | 72.9 | 0 | 9 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0929× (z -27.1) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.310× (z -13.3) |
| [[HOP62 (line)]] | alt | 72.8 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +21.0) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +18.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -13.4) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 224 | 1 (1 ⚠) | 6 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -11.8) ⚠ unreliable plate only · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.323× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 86.0 | 6 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +12.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 172 | 2 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.08× (z +9.1) | [[Ixazomib citrate (drug)]] 5 µM 0.229× (z -13.1) |
| [[A498 (line)]] | wt | 167 | 0 | 6 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.180× (z -19.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0938× (z -13.8) |
| [[Panc 03.27 (line)]] | alt | 93.0 | 3 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.286× (z -12.4) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 0.177× (z -9.0) |
| [[SW480 (line)]] | alt | 57.5 | 4 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +15.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -16.5) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.396× (z -8.9) |
| [[A-172 (line)]] | wt | 73.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.294× (z -12.3) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 67.4 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.345× (z -9.5) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 110 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.7) | [[PH-797804 (drug)]] 5 µM 0.145× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 50.7 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +11.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.198× (z -11.7) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 79.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +16.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -12.6) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 110 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.96× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.248× (z -11.4) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 110 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.197× (z -11.0) ⚠ unreliable plate only · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.252× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 45.6 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +18.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.129× (z -14.9) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 58.5 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -15.2) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 83.2 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +18.0) | — |
| [[LoVo (line)]] | wt | 107 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -15.9) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 25.4 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.96× (z +13.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.229× (z -9.0) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 92.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -12.2) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 79.6 | 2 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 5.02× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -11.6) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 65.5 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.270× (z -11.5) ⚠ unreliable plate only |
| [[C-33 A (line)]] | alt | 45.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.21× (z +10.2) | — |
| [[COLO 205 (line)]] | alt | 173 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +8.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.302× (z -10.9) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 75.5 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.186× (z -10.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0534× (z -9.8) |
| [[Hs 766T (line)]] | wt | 93.3 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.164× (z -15.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.121× (z -9.4) |
| [[HS-578T (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -14.7) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 60.6 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.89× (z +11.3) | — |
| [[J82 (line)]] | alt | 33.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +12.8) | — |
| [[NCI-H2030 (line)]] | alt | 103 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.199× (z -16.1) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.384× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 171 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.00× (z +10.3) | — |
| [[RKO (line)]] | wt | 31.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 67.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +10.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.290× (z -9.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 54.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.215× (z -12.3) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 98.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.8) | — |
| [[NCI-H1792 (line)]] | alt | 82.1 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.177× (z -15.2) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 24.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.19× (z +10.6) | — |
| [[SW 1271 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -10.0) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8752), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*41 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC186]] | +0.72 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[UBN2]] | +0.71 | +0.56 / +0.73 | both halves | 1e-05 |  |
| [[CREBRF]] | +0.67 | +0.56 / +0.68 | both halves | 1e-05 |  |
| [[BET1]] | +0.66 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.64 | +0.47 / +0.72 | both halves | 2e-05 |  |
| [[TCP11L2]] | +0.64 | +0.36 / +0.71 | both halves | 1e-04 |  |
| [[JMY]] | +0.64 | +0.39 / +0.73 | both halves | 5e-05 |  |
| [[ERO1B]] | +0.63 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLU7]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[NBR1]] | +0.62 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.62 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CYLD]] | +0.62 | +0.46 / +0.60 | both halves | 2e-05 |  |

## Genes that move opposite

*59 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP1]] | -0.66 | -0.58 / -0.67 | both halves | 8e-06 |  |
| [[PDSS1]] | -0.66 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[NOL10]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[MRPS27]] | -0.64 | -0.56 / -0.66 | both halves | 1e-05 |  |
| [[MRPL4]] | -0.64 | -0.69 / -0.52 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.64 | -0.52 / -0.68 | both halves | 1e-05 |  |
| [[NLE1]] | -0.63 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[PHB1]] | -0.63 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[SORD]] | -0.63 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[CCT2]] | -0.63 | -0.54 / -0.58 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.63 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[POLR3H]] | -0.61 | -0.58 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises SMIM14's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.74× lower at baseline in the lines without AGR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[PRKCH-AS1]] | B | PRKCH-AS1 activity raises SMIM14's level | lines that do not express PRKCH-AS1 (34) vs lines expressing it (16) | 1.87× lower at baseline in the lines without PRKCH-AS1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TMEM30B, TMPRSS2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers SMIM14's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TFR2]] | B | TFR2 activity raises SMIM14's level | lines that do not express TFR2 (10) vs lines expressing it (40) | 1.41× lower at baseline in the lines without TFR2 | 0.097 | ⚠ within organs, on part of the lines; also absent: KRTAP5-AS1, EFNA2, AP1G2; maybe low, not absent |
| [[TESK2]] | C | TESK2 activity raises SMIM14's level | lines that do not express TESK2 (3) vs lines expressing it (46) | 2.72× lower at baseline in the lines without TESK2 | 0.029 | ⚠ few lines (3 vs 46); across organs; also absent: SYNPO2, SLC9A3, SFXN3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.6, -44.7); signed map (-13.1, 9.7). **Vector** length 144, 52.3% of its response variance represented; |z| ≥ 3 in 1,720 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +12.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.4 | +5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.8 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.5 | +5.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +3.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.8 | +4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +4.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.8 | -20.2 |
|  | [[EX229 (drug)]] 5 µM |  | -11.7 | -10.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -10.4 | -9.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.1 | -8.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -9.5 | -9.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -8.4 | -8.6 |

## What is on record

|  |  |
|---|---|
| Name | small integral membrane protein 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p14 — chr4:39,546,336-39,638,902 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13289; previously C4orf34 |
| Matched by | ensembl_id |

UniProt [Q96QK8](https://www.uniprot.org/uniprotkb/Q96QK8) carries no function annotation.

**Summary**, from NCBI Gene [201895](https://www.ncbi.nlm.nih.gov/gene/201895):

> Predicted to act upstream of or within blastocyst hatching. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27321](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27321) · Entrez [201895](https://www.ncbi.nlm.nih.gov/gene/201895) · UniProt [Q96QK8](https://www.uniprot.org/uniprotkb/Q96QK8) · Ensembl [ENSG00000163683](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163683)

## Data

Gene col 8752: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8752); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8752, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8752]; `tensor/DDL_lfc|DDL_z.npy` [8752]; `embed/gene_vectors.npy` [8752]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8752 or target_col == 8752). Every well: [[SMIM14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMIM14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
