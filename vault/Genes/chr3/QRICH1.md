---
symbol: "QRICH1"
type: "gene"
col: 12556
ensembl_id: "ENSG00000198218"
name: "glutamine rich 1"
location: "3p21.31"
module: 156
arm: "+"
pooled_cpm: 100.14
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 6
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# QRICH1

*glutamine rich 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.78× (z +15.6, q 0e+00, up in 47 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.338× (z -24.2, q 0e+00, down in 48 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.554× (z -13.2, q 1e-37, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAA60]] (+0.66, fdr 1e-05), [[VPS51]] (+0.66, fdr 7e-06), [[TMEM87A]] (+0.66, fdr 7e-06); moves opposite to [[FAM199X]] (-0.54, fdr 2e-04), [[EFR3A]] (-0.53, fdr 3e-05), [[SPTBN1]] (-0.52, fdr 3e-04).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12556.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.78×** | +15.6 | 0e+00 | 47/49 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.93×** | +12.6 | 9e-34 | 45/48 (SW480, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +11.5 | 3e-28 | 44/48 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +10.4 | 5e-23 | 41/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +8.9 | 7e-17 | 41/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.49×** | +8.9 | 7e-17 | 41/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.24×** | +4.9 | 7e-05 | 28/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.23×** | +4.3 | 0.001 | 25/48 (HEC-1-A, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.5 | 0.026 | 13/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12556.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.338×** | -24.2 | 0e+00 | 48/49 (Panc 03.27, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.331×** | -23.8 | 0e+00 | 43/44 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.405×** | -18.7 | 0e+00 | 44/45 (SNU-423, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.554×** | -13.2 | 1e-37 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.590×** | -11.8 | 5e-30 | 47/48 (A498, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.602×** | -11.3 | 9e-28 | 45/48 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.725×** | -10.2 | 2e-22 | 44/48 (NCI-H460, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.675×** | -8.8 | 1e-16 | 45/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -6.8 | 5e-10 | 27/48 (NCI-H23, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.748×** | -6.5 | 5e-09 | 34/49 (SK-MEL-2, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.741×** | -6.4 | 6e-09 | 25/50 (HEC-1-A, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | **0.787×** | -5.1 | 1e-05 | 25/47 (BT-474, H4, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.670×** | -4.7 | 1e-04 | 31/49 (NCI-H460, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.812×** | -4.6 | 1e-04 | 23/48 (AsPC-1, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -4.2 | 8e-04 | 23/48 (J82, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.843× | -3.8 | 0.005 | 20/48 (J82, C32, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.039 | 20/47 (HS-578T, C32, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12556. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 97.6 | 4 (1 ⚠) | 7 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.448× (z -11.7) |
| [[HEC-1-A (line)]] | alt | 126 | 3 | 5 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 4.76× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.315× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -11.1) |
| [[LS 180 (line)]] | wt | 92.8 | 5 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.30× (z +14.6) | [[Dinaciclib (drug)]] 0.5 µM 0.236× (z -17.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 77.2 | 5 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +14.0) | [[Dinaciclib (drug)]] 0.5 µM 0.373× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.542× (z -9.3) |
| [[SW480 (line)]] | alt | 119 | 6 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.194× (z -25.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 86.7 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.368× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.411× (z -12.5) |
| [[LOX-IMVI (line)]] | wt | 89.4 | 4 (1 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -12.3) |
| [[AsPC-1 (line)]] | alt | 112 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.488× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 95.6 | 2 (1 ⚠) | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.467× (z -9.1) |
| [[SW1417 (line)]] | alt | 160 | 2 | 4 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.264× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.509× (z -8.9) |
| [[C-33 A (line)]] | alt | 132 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.34× (z +8.5) | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.459× (z -8.6) |
| [[HOP62 (line)]] | alt | 102 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.78× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.540× (z -8.5) |
| [[HS-578T (line)]] | alt | 90.7 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.46× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.205× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -9.4) |
| [[LoVo (line)]] | wt | 120 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.72× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.325× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 59.5 | 3 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.39× (z +10.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.01× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -11.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 103 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.23× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.0992× (z -27.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 121 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.322× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.414× (z -9.5) |
| [[A-172 (line)]] | wt | 80.9 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.294× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.441× (z -10.9) |
| [[A-427 (line)]] | wt | 121 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.14× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.244× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.526× (z -8.6) |
| [[HT-29 (line)]] | alt | 67.6 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.09× (z +8.8) | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -14.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 87.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.1) |
| [[NCI-H23 (line)]] | alt | 114 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.312× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.350× (z -13.4) |
| [[NCI-H2347 (line)]] | alt | 134 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.333× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.562× (z -8.9) |
| [[RKO (line)]] | wt | 104 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.33× (z +12.5) | [[Dinaciclib (drug)]] 0.05 µM 0.320× (z -11.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 117 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.288× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.462× (z -9.4) |
| [[SW 900 (line)]] | alt | 119 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.209× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.444× (z -9.3) |
| [[HCT15 (line)]] | alt | 156 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -19.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 95.5 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.69× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 91.8 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.472× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.265× (z -13.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 92.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.0981× (z -26.1) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 116 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.32× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.127× (z -19.2) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 84.2 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.132× (z -20.1) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 78.8 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0822× (z -12.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 111 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -14.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 75.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.8× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -10.2) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 78.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -13.6) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 81.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.58× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.189× (z -18.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 128 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.253× (z -17.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 113 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.65× (z +9.0) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -14.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 79.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -12.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0927× (z -15.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 73.1 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.73× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 61.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -9.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 78.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 97.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 98.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 84.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12556), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAA60]] | +0.66 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[VPS51]] | +0.66 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[TMEM87A]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[LRRC41]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[AKAP8]] | +0.65 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[METTL16]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CCDC12]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[APPBP2]] | +0.64 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[TFCP2]] | +0.63 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[AKAP8L]] | +0.63 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[MBTD1]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ZNF200]] | +0.61 | +0.41 / +0.59 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM199X]] | -0.54 | -0.32 / -0.57 | both halves | 2e-04 |  |
| [[EFR3A]] | -0.53 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SPTBN1]] | -0.52 | -0.27 / -0.46 | both halves | 3e-04 |  |
| [[IDH3A]] | -0.51 | -0.61 / -0.44 | both halves | 3e-05 |  |
| [[OCRL]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers QRICH1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.792). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-33.6, -10.2); signed map (-4.8, -9.7). **Vector** length 106, 34.8% of its response variance represented; |z| ≥ 3 in 1,250 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +9.1 | +1.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +8.3 | +1.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.8 | +15.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.3 | +12.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | -0.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +1.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | -2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.7 | +1.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.4 | +2.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -10.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~16% of this change | -5.0 | -5.1 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -3.9 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.6 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.6 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | glutamine rich 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:49,029,707-49,094,363 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20259, VERBRAS, AB-DIP |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2TAL8](https://www.uniprot.org/uniprotkb/Q2TAL8) (Transcriptional regulator QRICH1):

> Transcriptional regulator that acts as a mediator of the integrated stress response (ISR) through transcriptional control of protein homeostasis under conditions of ER stress. Controls the outcome of the unfolded protein response (UPR) which is an ER-stress response pathway. ER stress induces QRICH1 translation by a ribosome translation re-initiation mechanism in response to EIF2S1/eIF-2-alpha phosphorylation, and stress-induced QRICH1 regulates a transcriptional program associated with protein …

**Summary**, from NCBI Gene [54870](https://www.ncbi.nlm.nih.gov/gene/54870):

> Enables DNA binding activity. Involved in intracellular signal transduction; positive regulation of DNA-templated transcription; and positive regulation of apoptotic process. Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24713](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24713) · Entrez [54870](https://www.ncbi.nlm.nih.gov/gene/54870) · UniProt [Q2TAL8](https://www.uniprot.org/uniprotkb/Q2TAL8) · Ensembl [ENSG00000198218](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198218)

## Data

Gene col 12556: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12556); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12556, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12556]; `tensor/DDL_lfc|DDL_z.npy` [12556]; `embed/gene_vectors.npy` [12556]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12556 or target_col == 12556). Every well: [[QRICH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/QRICH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
