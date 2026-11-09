---
symbol: "SRGAP3"
type: "gene"
col: 12158
ensembl_id: "ENSG00000196220"
name: "SLIT-ROBO Rho GTPase activating protein 3"
location: "3p25.3"
module: 26
arm: "+"
pooled_cpm: 33.25
n_lines_expressing: 48
n_dd_up: 40
n_dd_down: 26
n_dd_up_clean: 36
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# SRGAP3

*SLIT-ROBO Rho GTPase activating protein 3* — 3p25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.35× (z +24.3, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.460× (z -11.1, q 7e-26, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.461× (z -11.0, q 7e-26, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGO1-AS1]] (+0.74, fdr 7e-06), [[ITFG2-AS1]] (+0.72, fdr 7e-06), [[DNAH12]] (+0.68, fdr 1e-05); moves opposite to [[GTF2E2]] (-0.66, fdr 7e-05), [[HERC2P9]] (-0.64, fdr 7e-05), [[ZNF496]] (-0.59, fdr 3e-05).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 4 with an alert ⚠; shown: the 15 strongest. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.35×** | +24.3 | 0e+00 | 44/46 (A-172, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +19.6 | 0e+00 | 37/45 (NCI-H1792, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +16.7 | 0e+00 | 41/45 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.10×** | +16.1 | 0e+00 | 41/46 (SW1417, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.00×** | +15.7 | 0e+00 | 42/46 (NCI-H460, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.56×** | +13.4 | 5e-39 | 39/46 (A-172, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.54×** | +12.8 | 1e-35 | 42/46 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +12.5 | 4e-34 | 40/46 (SW1417, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.24×** | +11.5 | 9e-29 | 36/46 (SW1417, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.69×** | +10.6 | 2e-24 | 38/46 (A-172, HOP62, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.94×** | +9.4 | 2e-19 | 39/46 (A-172, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.81×** | +8.4 | 2e-15 | 31/45 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.75×** | +8.0 | 5e-14 | 36/46 (KATO III, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +7.6 | 1e-12 | 32/46 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.08×** | +6.7 | 9e-10 | 28/46 (SW1417, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -11.1 | 7e-26 | 36/45 (SW1417, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.461×** | -11.0 | 7e-26 | 37/46 (PANC-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.479×** | -10.5 | 2e-23 | 37/46 (SW1417, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.506×** | -9.7 | 4e-20 | 32/46 (H4, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.520×** | -9.3 | 1e-18 | 36/46 (RPMI-7951, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.561×** | -8.2 | 2e-14 | 29/46 (SW480, PANC-1, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.553×** | -8.1 | 4e-14 | 28/45 (hTERT-HPNE, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.718×** | -6.7 | 2e-09 | 30/46 (MIA PaCa-2, Panc 03.27, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.658×** | -6.0 | 1e-07 | 26/46 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.677×** | -5.6 | 1e-06 | 24/46 (Panc 03.27, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.712×** | -4.7 | 2e-04 | 22/45 (A-427, LoVo, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.737×** | -4.3 | 6e-04 | 17/46 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.747×** | -4.2 | 0.001 | 19/46 (Panc 03.27, A-427, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.738×** | -4.1 | 0.002 | 22/46 (HS-578T, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.753×** | -4.0 | 0.002 | 19/45 (Panc 03.27, HT-29, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.643×** | -4.0 | 0.002 | 19/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.554×** | -4.0 | 0.002 | 17/46 (HOP62, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Crizotinib (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -3.6 | 0.008 | 12/46 (A549, C32, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.769×** | -3.5 | 0.012 | 16/45 (C32, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 25.3 | 10 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.8× (z +21.1) | — |
| [[SW1417 (line)]] | alt | 36.4 | 6 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.28× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.108× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -10.7) |
| [[SW480 (line)]] | alt | 26.9 | 6 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.57× (z +12.2) | [[Digitoxin (drug)]] 5 µM 0.275× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.308× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 19.1 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.81× (z +16.1) | — |
| [[PANC-1 (line)]] | alt | 11.2 | 6 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.65× (z +13.4) | [[Digitoxin (drug)]] 0.5 µM 0.198× (z -10.0) |
| [[HOP62 (line)]] | alt | 31.5 | 6 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +14.2) | — |
| [[LOX-IMVI (line)]] | wt | 8.61 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +16.1) | — |
| [[RKO (line)]] | wt | 11.1 | 5 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 25.9× (z +12.8) | [[Digitoxin (drug)]] 5 µM 0.112× (z -8.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 31.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +12.6) | — |
| [[C32 (line)]] | wt | 54.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +16.6) | — |
| [[HEC-1-A (line)]] | alt | 86.1 | 5 | 0 | [[Auranofin (drug)]] 5 µM 3.37× (z +11.7) | — |
| [[HS-578T (line)]] | alt | 51.1 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +11.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.153× (z -11.3) ⚠ toxic |
| [[KATO III (line)]] | alt | 45.1 | 2 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.69× (z +10.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 2.31× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 22.9 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.68× (z +16.4) | [[Digitoxin (drug)]] 5 µM 0.215× (z -10.2) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 19.6 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.36× (z +14.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.110× (z -11.5) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 15.0 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.5× (z +14.9) | [[Digitoxin (drug)]] 5 µM 0.0719× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Simotinib (drug)]] 0.05 µM 0.0825× (z -9.3) |
| [[Hs 766T (line)]] | wt | 83.7 | 2 | 2 (2 ⚠) | [[Triamcinolone (drug)]] 5 µM 2.75× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 23.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +24.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 8.43× (z +10.3) | — |
| [[NCI-H2347 (line)]] | alt | 15.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.60× (z +15.0) | — |
| [[Panc 03.27 (line)]] | alt | 23.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +12.7) | [[Digitoxin (drug)]] 5 µM 0.221× (z -9.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 69.9 | 2 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +12.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.236× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -8.5) |
| [[A549 (line)]] | wt | 16.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +9.9) | — |
| [[hTERT-HPNE (line)]] | wt | 86.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -12.1) ⚠ toxic |
| [[LS 180 (line)]] | wt | 159 | 1 (1 ⚠) | 2 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.78× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 36.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.7× (z +27.1) | — |
| [[RPMI-7951 (line)]] | alt | 42.2 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.29× (z +15.0) | [[Ixazomib citrate (drug)]] 5 µM 0.139× (z -11.4) |
| [[A498 (line)]] | wt | 16.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.88× (z +9.3) | — |
| [[BT-474 (line)]] | alt | 61.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +11.0) | [[Digitoxin (drug)]] 0.5 µM 0.212× (z -9.0) |
| [[CFPAC-1 (line)]] | alt | 17.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.24× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 39.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +13.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.172× (z -8.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 15.5 | 2 | 0 | [[Auranofin (drug)]] 5 µM 7.78× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 27.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.132× (z -10.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 26.4 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +11.9) | — |
| [[SW 900 (line)]] | alt | 16.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +13.8) | — |
| [[SW48 (line)]] | wt | 99.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.244× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 23.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.81× (z +9.4) | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.108× (z -10.5) |
| [[AN3 CA (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.82 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 45.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.28 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGO1-AS1]] | +0.74 | +0.84 / +0.63 | both halves | 7e-06 |  |
| [[ITFG2-AS1]] | +0.72 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[DNAH12]] | +0.68 | +0.77 / +0.53 | both halves | 1e-05 |  |
| [[MGAM]] | +0.66 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[PKN2-AS1]] | +0.66 | +0.80 / +0.42 | both halves | 4e-05 |  |
| [[KCNAB1]] | +0.66 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[PSMD7-DT]] | +0.66 | +0.75 / +0.53 | both halves | 1e-05 |  |
| [[MAILR]] | +0.66 | +0.83 / +0.41 | both halves | 4e-05 |  |
| [[EPM2A-DT]] | +0.65 | +0.73 / +0.42 | both halves | 4e-05 |  |
| [[OXA1L-DT]] | +0.65 | +0.80 / +0.37 | both halves | 9e-05 |  |
| [[AK9]] | +0.64 | +0.78 / +0.46 | both halves | 3e-05 |  |
| [[CFAP418-AS1]] | +0.64 | +0.70 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2E2]] | -0.66 | -0.71 / -0.38 | both halves | 7e-05 |  |
| [[HERC2P9]] | -0.64 | -0.58 / -0.37 | both halves | 7e-05 |  |
| [[ZNF496]] | -0.59 | -0.68 / -0.43 | both halves | 3e-05 |  |
| [[FAM20B]] | -0.58 | -0.70 / -0.41 | both halves | 4e-05 |  |
| [[HERC2P2]] | -0.58 | -0.45 / -0.33 | both halves | 1e-04 |  |
| [[NTAQ1]] | -0.57 | -0.54 / -0.36 | both halves | 9e-05 |  |
| [[TEX2]] | -0.57 | -0.52 / -0.23 | both halves | 5e-04 |  |
| [[HERC2P3]] | -0.56 | -0.49 / -0.32 | both halves | 2e-04 |  |
| [[TTLL4]] | -0.56 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[NR2C1]] | -0.55 | -0.64 / -0.20 | ⚠ one half (not replicated) | 7e-04 |  |
| [[PACC1]] | -0.55 | -0.68 / -0.00 | ⚠ one half (not replicated) | 0.009 |  |
| [[HERC2]] | -0.54 | -0.46 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SRGAP3's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.0% of all compounds | 0.009 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[LINC00276]] | B | LINC00276 activity raises SRGAP3's level | lines that do not express LINC00276 (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without LINC00276 | 0.035 | ⚠ within organs, on part of the lines; also absent: LINC02932, MGC4859, RBFOX1; maybe low, not absent |
| [[LINC02343]] | B | LINC02343 activity raises SRGAP3's level | lines that do not express LINC02343 (7) vs lines expressing it (43) | 2.26× lower at baseline in the lines without LINC02343 | 0.060 | ⚠ within organs, on part of the lines; also absent: PRAF2; maybe low, not absent |
| [[LINC02940]] | B | LINC02940 activity raises SRGAP3's level | lines that do not express LINC02940 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without LINC02940 | 0.077 | ⚠ within organs, on part of the lines; also absent: LINC02641; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.649). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.6, 18.4); signed map (29.3, -6.2). **Vector** length 85.4, 23.4% of its response variance represented; |z| ≥ 3 in 1,571 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.9 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +19.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +12.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +8.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +12.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.4 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +9.4 |
| fall | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -0.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.0 | +11.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.5 | +15.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -8.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.5 | -6.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.3 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.1 | -4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | SLIT-ROBO Rho GTPase activating protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.3 — chr3:8,980,591-9,363,053 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0411, MEGAP, WRP, ARHGAP14; previously SRGAP2 |
| Gene groups (HGNC) | F-BAR domain containing; AH/BAR family Rho GTPase activating proteins; SH3 domain containing |
| Reactome | 9 pathways, smallest: Inactivation of CDC42 and RAC1; CDC42 GTPase cycle; RAC1 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O43295](https://www.uniprot.org/uniprotkb/O43295) (SLIT-ROBO Rho GTPase-activating protein 3):

> GTPase-activating protein for RAC1 and perhaps Cdc42, but not for RhoA small GTPase. May attenuate RAC1 signaling in neurons.

**Summary**, from NCBI Gene [9901](https://www.ncbi.nlm.nih.gov/gene/9901):

> Predicted to enable GTPase activator activity. Predicted to be involved in negative regulation of cell migration; nervous system development; and regulation of postsynapse assembly. Is active in postsynapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19744](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19744) · Entrez [9901](https://www.ncbi.nlm.nih.gov/gene/9901) · UniProt [O43295](https://www.uniprot.org/uniprotkb/O43295) · Ensembl [ENSG00000196220](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196220)

## Data

Gene col 12158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12158); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12158]; `tensor/DDL_lfc|DDL_z.npy` [12158]; `embed/gene_vectors.npy` [12158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12158 or target_col == 12158). Every well: [[SRGAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SRGAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
