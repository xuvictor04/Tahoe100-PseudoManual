---
symbol: "KIF3A"
type: "gene"
col: 5208
ensembl_id: "ENSG00000131437"
name: "kinesin family member 3A"
location: "5q31.1"
module: 65
arm: "+"
pooled_cpm: 59.79
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# KIF3A

*kinesin family member 3A* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.52× (z +31.3, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.413× (z -21.9, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HERC1]] (+0.68, fdr 7e-06), [[HACE1]] (+0.68, fdr 1e-05), [[ARL3]] (+0.67, fdr 3e-05); moves opposite to [[CCDC90B-AS1]] (-0.66, fdr 2e-04), [[LINC00571]] (-0.65, fdr 5e-05), [[AKT1S1]] (-0.65, fdr 3e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[HGD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5208.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.52×** | +31.3 | 0e+00 | 48/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.48×** | +31.0 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.01×** | +27.4 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.99×** | +17.1 | 0e+00 | 44/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +13.6 | 3e-40 | 41/48 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.69×** | +13.0 | 1e-36 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.63×** | +12.6 | 2e-34 | 45/48 (LoVo, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +9.3 | 1e-18 | 33/48 (LoVo, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.39×** | +8.2 | 2e-14 | 36/48 (C32, NCI-H460, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.69×** | +6.8 | 4e-10 | 35/48 (LoVo, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.22×** | +4.9 | 4e-05 | 24/48 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +4.1 | 0.002 | 14/48 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +3.9 | 0.004 | 14/48 (C32, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.16× | +3.7 | 0.007 | 11/48 (C32, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.15× | +3.3 | 0.036 | 13/49 (BT-474, SW 900, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.11× | +3.2 | 0.042 | 11/48 (SW480, C32, …) | two highest doses | noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.058 | 10/48 (NCI-H1792, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5208.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.413×** | -21.9 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.454×** | -19.6 | 0e+00 | 45/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.488×** | -17.8 | 0e+00 | 45/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -17.0 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.550×** | -14.8 | 0e+00 | 40/48 (PANC-1, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -11.8 | 3e-30 | 41/49 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.720×** | -11.3 | 6e-28 | 30/48 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.451×** | -10.3 | 4e-23 | 34/48 (HS-578T, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.702×** | -8.4 | 2e-15 | 30/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.752×** | -7.1 | 9e-11 | 26/48 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.755×** | -7.0 | 2e-10 | 28/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.768×** | -6.5 | 3e-09 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.808×** | -5.1 | 2e-05 | 23/47 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.713×** | -4.4 | 5e-04 | 20/48 (PANC-1, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.848× | -4.1 | 0.002 | 22/48 (NCI-H460, C32, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **0.732×** | -4.0 | 0.002 | 16/48 (AsPC-1, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 0.867× | -3.3 | 0.024 | 8/48 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | 0.884× | -3.1 | 0.060 | 11/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.797×** | -2.9 | 0.080 | 12/48 (PANC-1, SW 900, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5208. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 60.6 | 4 | 15 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.33× (z +19.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.197× (z -26.1) |
| [[PANC-1 (line)]] | alt | 77.3 | 3 | 10 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.00× (z +18.7) | [[Digitoxin (drug)]] 5 µM 0.276× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.457× (z -18.4) |
| [[LoVo (line)]] | wt | 43.6 | 7 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 5.90× (z +18.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -16.2) |
| [[SW480 (line)]] | alt | 58.0 | 6 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.66× (z +20.5) | [[Digitoxin (drug)]] 5 µM 0.334× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.348× (z -14.0) |
| [[J82 (line)]] | alt | 51.9 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.25× (z +16.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -15.7) |
| [[HOP62 (line)]] | alt | 60.8 | 4 | 5 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.01× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.180× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -22.7) |
| [[HS-578T (line)]] | alt | 101 | 2 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.20× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -18.6) |
| [[HT-29 (line)]] | alt | 41.2 | 5 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.82× (z +16.5) | [[Digitoxin (drug)]] 5 µM 0.188× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.276× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 70.2 | 3 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +11.1) | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.7) |
| [[A-172 (line)]] | wt | 75.3 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.24× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.353× (z -18.1) |
| [[RKO (line)]] | wt | 69.3 | 4 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.84× (z +14.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.243× (z -14.7) |
| [[SW1417 (line)]] | alt | 58.6 | 4 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.50× (z +14.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.373× (z -11.7) |
| [[A-427 (line)]] | wt | 127 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.01× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -29.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.492× (z -13.6) |
| [[C32 (line)]] | wt | 84.7 | 1 | 6 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.23× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.287× (z -14.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -12.5) |
| [[NCI-H1573 (line)]] | alt | 56.6 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.24× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.308× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.348× (z -10.2) |
| [[SNU-423 (line)]] | alt | 41.3 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.19× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 62.1 | 5 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.39× (z +17.0) | [[Auranofin (drug)]] 5 µM 0.320× (z -13.0) |
| [[Hs 766T (line)]] | wt | 35.7 | 4 | 2 | [[Panobinostat (drug)]] 0.5 µM 6.38× (z +15.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -9.8) |
| [[LS 180 (line)]] | wt | 23.4 | 6 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 11.4× (z +15.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 55.4 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.25× (z +16.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.422× (z -8.7) |
| [[COLO 205 (line)]] | alt | 32.7 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 7.74× (z +13.1) | [[Digitoxin (drug)]] 5 µM 0.230× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 78.8 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.353× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.401× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 53.0 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.96× (z +18.9) | [[Digitoxin (drug)]] 5 µM 0.395× (z -10.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 78.5 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 16.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.1× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 110 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.37× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.228× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 49.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +16.7) | — |
| [[HepG2_C3A (line)]] | wt | 35.9 | 3 | 1 | [[Panobinostat (drug)]] 0.5 µM 6.17× (z +11.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.267× (z -8.5) |
| [[KATO III (line)]] | alt | 24.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.96× (z +15.5) | — |
| [[NCI-H1792 (line)]] | alt | 43.5 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.53× (z +11.5) | [[Harringtonine (drug)]] 5 µM 0.377× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 91.9 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 1.99× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -17.1) |
| [[SHP-77 (line)]] | alt | 74.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.59× (z +10.1) | [[Auranofin (drug)]] 5 µM 0.439× (z -8.6) |
| [[A498 (line)]] | wt | 60.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +10.4) | — |
| [[HCT15 (line)]] | alt | 55.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.14× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 39.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +11.7) | — |
| [[Panc 03.27 (line)]] | alt | 58.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.37× (z +13.8) | — |
| [[RPMI-7951 (line)]] | alt | 36.6 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.86× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 72.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.92× (z +10.1) | — |
| [[SNU-1 (line)]] | wt | 52.5 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.59× (z +9.1) | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.253× (z -9.8) |
| [[SW 900 (line)]] | alt | 44.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.90× (z +11.6) | — |
| [[SW48 (line)]] | wt | 60.9 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 4.12× (z +9.7) | [[Auranofin (drug)]] 5 µM 0.244× (z -9.7) |
| [[H4 (line)]] | wt | 52.0 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.261× (z -9.8) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 80.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0806× (z -9.2) |
| [[AN3 CA (line)]] | alt | 108 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.196× (z -10.5) |
| [[BT-474 (line)]] | alt | 32.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.61× (z +9.4) | — |
| [[SW 1271 (line)]] | alt | 120 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.174× (z -9.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 50.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 99.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5208), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HERC1]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[HACE1]] | +0.68 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ARL3]] | +0.67 | +0.44 / +0.62 | both halves | 3e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 421 |
| [[SERAC1]] | +0.67 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[KCTD6]] | +0.67 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[STX7]] | +0.66 | +0.58 / +0.45 | both halves | 3e-05 |  |
| [[REPS1]] | +0.66 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[ATG4C]] | +0.65 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[ARL6]] | +0.65 | +0.54 / +0.53 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium |
| [[ARRB2]] | +0.64 | +0.42 / +0.52 | both halves | 4e-05 | pathway: Activation of SMO; STRING 955 |
| [[ANAPC4]] | +0.64 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[WASF3]] | +0.63 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC90B-AS1]] | -0.66 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[LINC00571]] | -0.65 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[AKT1S1]] | -0.65 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[MCPH1]] | -0.65 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[PCF11]] | -0.64 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[PARD6G-AS1]] | -0.64 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[MPDU1]] | -0.64 | -0.46 / -0.50 | both halves | 3e-05 |  |
| [[FBXL19-AS1]] | -0.63 | -0.48 / -0.39 | both halves | 5e-05 |  |
| [[GLIPR1-AS1]] | -0.63 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.63 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[GTF2H1]] | -0.63 | -0.37 / -0.50 | both halves | 8e-05 |  |
| [[PTOV1-AS1]] | -0.63 | -0.48 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HGD]] | B | HGD activity lowers KIF3A's level | lines that do not express HGD (15) vs lines expressing it (35) | 1.37× higher at baseline in the lines without HGD | 0.007 | ⚠ within organs, on part of the lines; also absent: PCSK5, AQP3, FAAH2; maybe low, not absent |
| [[PLEKHA6]] | B | PLEKHA6 activity lowers KIF3A's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.54× higher at baseline in the lines without PLEKHA6 | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[TMOD2]] | B | TMOD2 activity raises KIF3A's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without TMOD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[HLA-K]] | B | HLA-K activity lowers KIF3A's level | lines that do not express HLA-K (22) vs lines expressing it (28) | 1.50× higher at baseline in the lines without HLA-K | 0.019 | ⚠ within organs, on part of the lines; also absent: ACSL5, ICAM2, ENSG00000263325 |
| [[TSPAN33]] | B | TSPAN33 activity raises KIF3A's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.50× lower at baseline in the lines without TSPAN33 | 0.057 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.678). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.4, -10.6); signed map (-32.9, -7.7). **Vector** length 114, 35.5% of its response variance represented; |z| ≥ 3 in 1,361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +6.2 | +27.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.7 | +12.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.7 | +17.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +31.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.7 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +13.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.0 | +0.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.4 | -0.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -13.3 | -14.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.7 | -1.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -8.4 | -11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -8.0 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -7.2 | -2.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -2.6 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -2.9 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.7 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 3A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,692,628-132,737,638 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLA10, KLP-20 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 22 pathways, smallest: Activation of SMO; Intraflagellar transport; Kinesins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y496](https://www.uniprot.org/uniprotkb/Q9Y496) (Kinesin-like protein KIF3A):

> Microtubule-based anterograde translocator for membranous organelles, such as primary cilium and centriole. Shows a plus end-directed microtubule sliding activity in vitro. Plays a role in primary cilia formation, probably by mediating transport of proteins into primary cilia. Mediates smoothened (SMO) translocation into primary cilia in response to hedgehog morphogens. Plays a role in centriole cohesion and subdistal appendage organization and function. Regulates the formation of the subdistal …

**Summary**, from NCBI Gene [11127](https://www.ncbi.nlm.nih.gov/gene/11127):

> Enables protein phosphatase binding activity; small GTPase binding activity; and spectrin binding activity. Involved in protein localization to cell junction and protein transport. Located in centriole; centrosome; and spindle microtubule. Part of kinesin II complex. Implicated in allergic disease and asthma. Biomarker of asthma and silicosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6319](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6319) · Entrez [11127](https://www.ncbi.nlm.nih.gov/gene/11127) · UniProt [Q9Y496](https://www.uniprot.org/uniprotkb/Q9Y496) · Ensembl [ENSG00000131437](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131437)

## Data

Gene col 5208: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5208); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5208, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5208]; `tensor/DDL_lfc|DDL_z.npy` [5208]; `embed/gene_vectors.npy` [5208]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5208 or target_col == 5208). Every well: [[KIF3A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF3A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
