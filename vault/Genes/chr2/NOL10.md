---
symbol: "NOL10"
type: "gene"
col: 3718
ensembl_id: "ENSG00000115761"
name: "nucleolar protein 10"
location: "2p25.1"
module: 33
arm: "+"
pooled_cpm: 110.87
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 8
n_dd_up_clean: 16
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NOL10

*nucleolar protein 10* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.71× (z +19.7, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.673× (z -16.3, q 0e+00, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PUM3]] (+0.76, fdr 7e-06), [[HEATR1]] (+0.76, fdr 7e-06), [[DIS3L2]] (+0.75, fdr 7e-06); moves opposite to [[SMIM14]] (-0.64, fdr 7e-06), [[HLA-A]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.71×** | +19.7 | 0e+00 | 47/49 (PANC-1, SW480, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.94×** | +16.2 | 0e+00 | 45/48 (MIA PaCa-2, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.65×** | +14.5 | 1e-45 | 44/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.58×** | +13.2 | 1e-37 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +10.7 | 2e-24 | 39/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +10.4 | 2e-23 | 37/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +9.1 | 6e-18 | 33/48 (SHP-77, NCI-H1792, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +8.8 | 9e-17 | 31/38 (SW480, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +8.7 | 2e-16 | 34/48 (SHP-77, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.32×** | +8.1 | 3e-14 | 30/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.69×** | +7.9 | 1e-13 | 38/45 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +7.8 | 3e-13 | 41/48 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +7.5 | 2e-12 | 30/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.29×** | +7.3 | 1e-11 | 30/48 (SHP-77, NCI-H2347, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.60×** | +7.1 | 5e-11 | 41/48 (PANC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +7.0 | 7e-11 | 27/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.38×** | +6.6 | 2e-09 | 37/49 (PANC-1, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.48×** | +5.9 | 1e-07 | 29/48 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.22×** | +5.7 | 3e-07 | 24/48 (NCI-H1573, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.28×** | +5.1 | 7e-06 | 25/48 (PANC-1, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.36×** | +4.6 | 1e-04 | 23/48 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.36×** | +4.6 | 1e-04 | 24/48 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.673×** | -16.3 | 0e+00 | 40/49 (A498, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -8.7 | 7e-16 | 23/48 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -8.7 | 7e-16 | 32/50 (HOP62, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.738×** | -8.5 | 4e-15 | 29/48 (HOP62, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.773×** | -7.4 | 2e-11 | 27/49 (SW 900, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.825×** | -5.5 | 4e-06 | 22/48 (RKO, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.828×** | -5.3 | 1e-05 | 22/44 (LS 180, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | 0.834× | -5.3 | 1e-05 | 20/48 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.842× | -5.0 | 4e-05 | 22/48 (SW1417, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | 0.837× | -5.0 | 4e-05 | 22/47 (A-427, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.866× | -4.2 | 0.001 | 15/49 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.886× | -4.1 | 0.002 | 9/48 (MIA PaCa-2, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.873× | -3.9 | 0.004 | 16/47 (A-427, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.891× | -3.8 | 0.005 | 11/48 (A-427, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.876× | -3.7 | 0.008 | 15/48 (A-427, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | 0.850× | -3.4 | 0.026 | 17/47 (A498, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | 0.852× | -3.3 | 0.028 | 14/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 128 | 10 (3 ⚠) | 1 | [[PH-797804 (drug)]] 5 µM 4.81× (z +14.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.579× (z -14.0) |
| [[NCI-H1573 (line)]] | alt | 104 | 9 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.02× (z +15.8) | — |
| [[SW480 (line)]] | alt | 94.1 | 7 (3 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 4.21× (z +14.4) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.617× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 216 | 3 (1 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 136 | 3 | 3 | [[TAK-901 (drug)]] 0.05 µM 2.39× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -14.3) |
| [[SHP-77 (line)]] | alt | 212 | 5 (4 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.90× (z +11.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.33× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 127 | 4 (3 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.04× (z +10.3) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 3.61× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -10.2) |
| [[HOP62 (line)]] | alt | 97.6 | 2 | 3 | [[TAK-901 (drug)]] 5 µM 5.66× (z +13.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -12.0) |
| [[NCI-H23 (line)]] | alt | 184 | 4 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.53× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.559× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 111 | 5 (3 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.76× (z +14.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 3.95× (z +10.4) | — |
| [[A-427 (line)]] | wt | 188 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.01× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 2.96× (z +9.2) | — |
| [[A498 (line)]] | wt | 119 | 2 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.85× (z +10.7) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 2.67× (z +8.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -16.2) |
| [[HT-29 (line)]] | alt | 82.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.88× (z +10.6) | — |
| [[LoVo (line)]] | wt | 101 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.02× (z +12.4) | — |
| [[LS 180 (line)]] | wt | 95.8 | 1 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.09× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.398× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 139 | 3 (1 ⚠) | 0 | [[PH-797804 (drug)]] 5 µM 7.64× (z +15.0) | — |
| [[RKO (line)]] | wt | 170 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.52× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -14.7) |
| [[SK-MEL-2 (line)]] | alt | 130 | 2 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.62× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.444× (z -9.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 92.8 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.08× (z +8.8) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -15.1) |
| [[C-33 A (line)]] | alt | 128 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 5.10× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -11.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 118 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.42× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -9.2) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 104 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 4.10× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 81.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 77.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.12× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 135 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.75× (z +9.3) | — |
| [[SW1417 (line)]] | alt | 132 | 1 (1 ⚠) | 1 | [[c-Kit-IN-1 (drug)]] 0.05 µM 1.73× (z +8.8) ⚠ unreliable plate only | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.623× (z -10.7) |
| [[A-172 (line)]] | wt | 71.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -12.9) |
| [[AN3 CA (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 93.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 4.35× (z +11.5) | — |
| [[COLO 205 (line)]] | alt | 76.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.57× (z +9.0) | — |
| [[HepG2_C3A (line)]] | wt | 99.8 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.43× (z +8.5) ⚠ toxic; cell-cycle shift, explains ~17% of this change | — |
| [[J82 (line)]] | alt | 70.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -12.8) |
| [[KATO III (line)]] | alt | 109 | 1 | 0 | [[PH-797804 (drug)]] 5 µM 3.27× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 69.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -12.2) |
| [[SNU-1 (line)]] | wt | 128 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.2) |
| [[SNU-423 (line)]] | alt | 82.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -10.1) |
| [[SW48 (line)]] | wt | 135 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -12.5) |
| [[BT-474 (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 119 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 86.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 78.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 96.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 87.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PUM3]] | +0.76 | +0.69 / +0.82 | both halves | 7e-06 | STRING 850 |
| [[HEATR1]] | +0.76 | +0.71 / +0.79 | both halves | 7e-06 | STRING 998 |
| [[DIS3L2]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 | STRING 536 |
| [[NAA25]] | +0.75 | +0.72 / +0.81 | both halves | 7e-06 |  |
| [[WDR3]] | +0.74 | +0.76 / +0.69 | both halves | 7e-06 | same gene group; STRING 998 |
| [[PDCD11]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 | STRING 997 |
| [[POLR1A]] | +0.74 | +0.67 / +0.78 | both halves | 7e-06 | STRING 706 |
| [[MRPS27]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[MDN1]] | +0.73 | +0.64 / +0.78 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.72 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[CHCHD6]] | +0.72 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[TSEN2]] | +0.71 | +0.64 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMIM14]] | -0.64 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[HLA-A]] | -0.61 | -0.50 / -0.59 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises NOL10's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SATB1]] | B | SATB1 activity lowers NOL10's level | lines that do not express SATB1 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without SATB1 | 0.041 | ⚠ within organs, on part of the lines; also absent: STING1, EFNB2, NR3C2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.791). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-11.5, -35.3); signed map (-9.8, -49.3). **Vector** length 118, 38.1% of its response variance represented; |z| ≥ 3 in 1,444 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.54 to 8); *Major pathway of rRNA processing in the nucleolus and cytosol* (reactome, mean cos +0.56 to 10); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.56 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.6 | +14.5 |
|  | [[EX229 (drug)]] 5 µM |  | +6.7 | +7.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.3 | +9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.1 | +16.2 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +19.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.7 | +7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +5.1 | +4.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.6 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -16.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -8.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | +0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.5 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -8.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -5.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -2.8 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.6 | -5.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.5 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | nucleolar protein 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:10,562,347-10,689,987 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14075; previously PQBP5 |
| Gene groups (HGNC) | WD repeat domain containing |
| Matched by | ensembl_id |

UniProt [Q9BSC4](https://www.uniprot.org/uniprotkb/Q9BSC4) carries no function annotation.

**Summary**, from NCBI Gene [79954](https://www.ncbi.nlm.nih.gov/gene/79954):

> Enables RNA binding activity. Predicted to be involved in maturation of SSU-rRNA from tricistronic rRNA transcript (SSU-rRNA, 5.8S rRNA, LSU-rRNA). Located in nucleolus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25862) · Entrez [79954](https://www.ncbi.nlm.nih.gov/gene/79954) · UniProt [Q9BSC4](https://www.uniprot.org/uniprotkb/Q9BSC4) · Ensembl [ENSG00000115761](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115761)

## Data

Gene col 3718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3718); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3718]; `tensor/DDL_lfc|DDL_z.npy` [3718]; `embed/gene_vectors.npy` [3718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3718 or target_col == 3718). Every well: [[NOL10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOL10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
