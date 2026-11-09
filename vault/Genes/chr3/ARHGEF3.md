---
symbol: "ARHGEF3"
type: "gene"
col: 8820
ensembl_id: "ENSG00000163947"
name: "Rho guanine nucleotide exchange factor 3"
location: "3p14.3"
module: 31
arm: "+"
pooled_cpm: 117.35
n_lines_expressing: 46
n_dd_up: 10
n_dd_down: 26
n_dd_up_clean: 8
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 23
direction_downstream: 1
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ARHGEF3

*Rho guanine nucleotide exchange factor 3* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.52× (z +8.9, q 4e-16, up in 22 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.420× (z -17.4, q 0e+00, down in 33 of 39 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.588× (z -11.1, q 2e-26, down in 37 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TJP2]] (+0.63, fdr 1e-05), [[RHPN2]] (+0.62, fdr 1e-05), [[PIM1]] (+0.55, fdr 3e-05); moves opposite to [[MSANTD2]] (-0.59, fdr 1e-05), [[CNRIP1]] (-0.49, fdr 1e-04), [[ITGB3BP]] (-0.48, fdr 4e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[SKAP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[KIAA1522]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.52×** | +8.9 | 4e-16 | 22/44 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.39×** | +7.0 | 9e-10 | 25/44 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +6.8 | 2e-09 | 23/44 (HOP62, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.27×** | +5.0 | 6e-05 | 20/44 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.25×** | +4.6 | 4e-04 | 20/44 (Hs 766T, HEC-1-A, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.23×** | +4.4 | 0.001 | 21/45 (A-172, HS-578T, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.24×** | +4.3 | 0.001 | 21/43 (C32, BT-474, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.005 | 19/46 (C32, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.14× | +3.9 | 0.007 | 18/44 (LS 180, HEC-1-A, …) | all doses, flat | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +3.8 | 0.008 | 15/44 (A-172, HS-578T, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.027 | 14/45 (SHP-77, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.12× | +3.3 | 0.039 | 12/44 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.039 | 16/44 (J82, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | 1.17× | +3.3 | 0.045 | 10/45 (HEC-1-A, LoVo, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | 1.17× | +3.2 | 0.051 | 15/43 (SW48, MIA PaCa-2, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.054 | 14/43 (SW48, SW480, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.15× | +3.0 | 0.090 | 15/43 (C32, BT-474, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | **1.31×** | +3.0 | 0.090 | 19/45 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.10× | +2.9 | 0.090 | 6/44 (KATO III, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 17 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8820.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.420×** | -17.4 | 0e+00 | 33/39 (NCI-H1792, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.452×** | -16.6 | 0e+00 | 34/45 (NCI-H1792, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.469×** | -14.6 | 0e+00 | 31/41 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.588×** | -11.1 | 2e-26 | 37/44 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.595×** | -10.9 | 2e-25 | 33/44 (LS 180, KATO III, …) | rises with dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.708×** | -10.2 | 2e-22 | 26/44 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.640×** | -9.3 | 8e-19 | 28/44 (LS 180, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -9.2 | 3e-18 | 26/45 (SNU-423, SW1417, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.440×** | -9.0 | 2e-17 | 36/45 (LoVo, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.697×** | -7.2 | 2e-11 | 25/43 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.700×** | -7.2 | 4e-11 | 30/44 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.711×** | -6.9 | 3e-10 | 29/46 (SNU-423, PANC-1, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~41% of this change | **0.716×** | -6.7 | 8e-10 | 28/43 (LoVo, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.728×** | -6.6 | 1e-09 | 23/44 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.559×** | -6.4 | 8e-09 | 20/33 (Panc 03.27, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.562×** | -6.3 | 1e-08 | 31/44 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.785×** | -5.0 | 1e-05 | 23/44 (SNU-423, A498, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.783×** | -4.7 | 6e-05 | 18/43 (A549, SW48, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.814×** | -4.3 | 5e-04 | 22/44 (SNU-423, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.825×** | -4.0 | 0.001 | 19/43 (MIA PaCa-2, SNU-423, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.880× | -3.7 | 0.004 | 13/45 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.886× | -3.6 | 0.008 | 13/44 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.843× | -3.4 | 0.013 | 17/44 (MIA PaCa-2, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.861× | -3.1 | 0.036 | 15/44 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.815×** | -3.0 | 0.043 | 14/44 (MIA PaCa-2, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 302 | 0 | 17 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -25.7) |
| [[SW48 (line)]] | wt | 242 | 1 | 11 (9 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.45× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0824× (z -23.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -15.1) |
| [[KATO III (line)]] | alt | 203 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -21.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.135× (z -11.8) |
| [[Panc 03.27 (line)]] | alt | 478 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.115× (z -27.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -15.9) |
| [[LS 180 (line)]] | wt | 162 | 0 | 10 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -23.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.142× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 142 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.354× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.476× (z -9.9) |
| [[LoVo (line)]] | wt | 128 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -20.0) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.194× (z -11.9) |
| [[MIA PaCa-2 (line)]] | alt | 130 | 0 | 9 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.187× (z -14.9) |
| [[NCI-H1792 (line)]] | alt | 247 | 0 | 9 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -28.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -15.6) |
| [[SW1417 (line)]] | alt | 194 | 0 | 9 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -20.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -20.3) |
| [[COLO 205 (line)]] | alt | 267 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.173× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -10.9) |
| [[PANC-1 (line)]] | alt | 90.2 | 0 | 8 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -14.9) |
| [[SW480 (line)]] | alt | 187 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -12.3) |
| [[A498 (line)]] | wt | 72.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.493× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 313 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.386× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 141 | 0 | 4 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.231× (z -13.8) ⚠ toxic |
| [[J82 (line)]] | alt | 110 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +16.8) ⚠ cell-cycle shift, explains ~71% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1573 (line)]] | alt | 58.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -13.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[A-427 (line)]] | wt | 75.7 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.126× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.0) |
| [[A549 (line)]] | wt | 92.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -17.5) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 95.4 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.451× (z -12.2) |
| [[BT-474 (line)]] | alt | 98.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.261× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -9.0) |
| [[HOP62 (line)]] | alt | 46.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.76× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 82.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.209× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 66.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[AN3 CA (line)]] | alt | 117 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0797× (z -8.5) |
| [[C32 (line)]] | wt | 95.4 | 2 | 0 | [[Cobimetinib (drug)]] 5 µM 3.14× (z +9.8) | — |
| [[HCT15 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.334× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 95.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 49.7 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +9.1) | [[Lonafarnib (drug)]] 5 µM 0.0956× (z -11.0) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 51.5 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +9.6) | — |
| [[A-172 (line)]] | wt | 50.9 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.28× (z +10.8) | — |
| [[CHP-212 (line)]] | wt | 66.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.25× (z +12.9) ⚠ cell-cycle shift, explains ~71% of this change | — |
| [[HT-29 (line)]] | alt | 102 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.342× (z -10.2) ⚠ toxic |
| [[RKO (line)]] | wt | 63.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.365× (z -9.6) |
| [[RPMI-7951 (line)]] | alt | 46.1 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 59.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.352× (z -9.3) |
| [[C-33 A (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 97.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 74.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.7 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TJP2]] | +0.63 | +0.68 / +0.51 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[RHPN2]] | +0.62 | +0.54 / +0.54 | both halves | 1e-05 | pathway: RHOA GTPase cycle |
| [[PIM1]] | +0.55 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[FA2H]] | +0.55 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[DTX2]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[EPB41]] | +0.54 | +0.47 / +0.58 | both halves | 2e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[NR6A1]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[SPNS2]] | +0.52 | +0.39 / +0.46 | both halves | 5e-05 |  |
| [[RAB11FIP1]] | +0.52 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[SPATA13]] | +0.52 | +0.49 / +0.43 | both halves | 3e-05 | same gene group |
| [[SYNGR2]] | +0.52 | +0.39 / +0.47 | both halves | 5e-05 |  |
| [[UBE2H]] | +0.52 | +0.52 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSANTD2]] | -0.59 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[CNRIP1]] | -0.49 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[ITGB3BP]] | -0.48 | -0.40 / -0.45 | both halves | 4e-05 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[PRIMPOL]] | -0.47 | -0.33 / -0.45 | both halves | 1e-04 |  |
| [[ANGEL2]] | -0.47 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[STXBP5-AS1]] | -0.46 | -0.41 / -0.34 | both halves | 1e-04 |  |
| [[TSTD2]] | -0.45 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[DNAAF10]] | -0.45 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[PSKH1]] | -0.44 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[CLMP]] | -0.44 | -0.37 / -0.48 | both halves | 8e-05 |  |
| [[LINC01355]] | -0.44 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[ZNF142]] | -0.44 | -0.40 / -0.37 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 21, C 2. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SKAP1]] | B | SKAP1 activity raises ARHGEF3's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.86× lower at baseline in the lines without SKAP1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1 |
| [[AFAP1L2]] | B | AFAP1L2 activity raises ARHGEF3's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without AFAP1L2 | 0.011 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH |
| [[CLDN4]] | B | CLDN4 activity raises ARHGEF3's level | lines that do not express CLDN4 (26) vs lines expressing it (24) | 2.49× lower at baseline in the lines without CLDN4 | 0.013 | ⚠ within organs, on part of the lines; also absent: CDH1, SCNN1A, ITGB6 |
| [[CLIC5]] | B | CLIC5 activity raises ARHGEF3's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without CLIC5 | 0.013 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[PADI1]] | B | PADI1 activity raises ARHGEF3's level | lines that do not express PADI1 (34) vs lines expressing it (16) | 2.38× lower at baseline in the lines without PADI1 | 0.016 | ⚠ within organs, on part of the lines; also absent: CLIC5, LINC01559, EPS8L3 |
| [[ST14]] | B | ST14 activity raises ARHGEF3's level | lines that do not express ST14 (32) vs lines expressing it (18) | 2.44× lower at baseline in the lines without ST14 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1 |
| [[FA2H]] | B | FA2H activity raises ARHGEF3's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without FA2H | 0.025 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[GPRC5A]] | B | GPRC5A activity raises ARHGEF3's level | lines that do not express GPRC5A (12) vs lines expressing it (38) | 2.15× lower at baseline in the lines without GPRC5A | 0.028 | ⚠ within organs, on part of the lines; also absent: TESMIN, PSORS1C1, ITGA3 |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ARHGEF3's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 2.33× lower at baseline in the lines without TMPRSS4 | 0.041 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[KIAA1522]] | B | KIAA1522 activity raises ARHGEF3's level | lines that do not express KIAA1522 (5) vs lines expressing it (45) | 2.80× lower at baseline in the lines without KIAA1522 | 0.042 | ⚠ across organs; also absent: ENSG00000257489, TRIB3, PBX4 |
| [[CDH1]] | B | CDH1 activity raises ARHGEF3's level | lines that do not express CDH1 (31) vs lines expressing it (19) | 2.41× lower at baseline in the lines without CDH1 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ST14, LAD1, KDF1 |
| [[ELF3]] | B | ELF3 activity raises ARHGEF3's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.19× lower at baseline in the lines without ELF3 | 0.055 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIAA1522]] | C | ARHGEF3 activity raises KIAA1522's level | lines that do not express ARHGEF3 (4) vs lines expressing it (46) | 3.72× lower at baseline in the lines without ARHGEF3 | 0.088 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SLC45A4, PPP1R13L, ENSG00000257489; maybe low, not absent |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-5.9, 34.2); signed map (-18.3, 33.9). **Vector** length 110, 33.0% of its response variance represented; |z| ≥ 3 in 1,525 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.8 | +6.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.8 | +7.0 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~79% of this change | +3.6 | +3.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.5 | +4.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.5 | +8.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +3.8 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.7 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.4 | -9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -6.3 | -17.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.7 | -7.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -5.2 | -16.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.2 | -11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.9 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.4 | -3.6 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.7 | -1.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -2.7 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:56,727,418-57,079,329 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STA3, XPLN, GEF3, DKFZP434F2429 |
| Gene groups (HGNC) | Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR81](https://www.uniprot.org/uniprotkb/Q9NR81) (Rho guanine nucleotide exchange factor 3):

> Acts as a guanine nucleotide exchange factor (GEF) for RhoA and RhoB GTPases.

**Summary**, from NCBI Gene [50650](https://www.ncbi.nlm.nih.gov/gene/50650):

> Rho-like GTPases are involved in a variety of cellular processes, and they are activated by binding GTP and inactivated by conversion of GTP to GDP by their intrinsic GTPase activity. Guanine nucleotide exchange factors (GEFs) accelerate the GTPase activity of Rho GTPases by catalyzing their release of bound GDP. This gene encodes a guanine nucleotide exchange factor, which specifically activates two members of the Rho GTPase family: RHOA and RHOB, both of which have a role in bone cell …

**Accessions** — [HGNC:683](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:683) · Entrez [50650](https://www.ncbi.nlm.nih.gov/gene/50650) · UniProt [Q9NR81](https://www.uniprot.org/uniprotkb/Q9NR81) · Ensembl [ENSG00000163947](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163947)

## Data

Gene col 8820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8820); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8820]; `tensor/DDL_lfc|DDL_z.npy` [8820]; `embed/gene_vectors.npy` [8820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8820 or target_col == 8820). Every well: [[ARHGEF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
