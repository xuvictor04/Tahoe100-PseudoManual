---
symbol: "RAD50"
type: "gene"
col: 3469
ensembl_id: "ENSG00000113522"
name: "RAD50 double strand break repair protein"
location: "5q31.1"
module: 28
arm: "+"
pooled_cpm: 139.64
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 20
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/028"]
generated_by: "tahoemap"
---

# RAD50

*RAD50 double strand break repair protein* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.97× (z +13.1, q 2e-36, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.499× (z -13.4, q 3e-38, down in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.513× (z -12.9, q 2e-35, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCDC25]] (+0.75, fdr 7e-06), [[TRMT13]] (+0.75, fdr 7e-06), [[MTIF2]] (+0.75, fdr 7e-06); moves opposite to [[KLHL25]] (-0.64, fdr 1e-05), [[GNB2]] (-0.63, fdr 1e-05), [[SNHG30]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 028]] (Intraflagellar transport).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3469.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.97×** | +13.1 | 2e-36 | 47/48 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +9.8 | 2e-20 | 43/49 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +9.7 | 6e-20 | 35/44 (A-427, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +7.4 | 2e-11 | 27/48 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.38×** | +6.2 | 5e-08 | 37/48 (A-427, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.32×** | +5.0 | 6e-05 | 26/45 (RKO, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | 1.19× | +4.7 | 2e-04 | 19/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.7 | 2e-04 | 29/48 (NCI-H1573, HS-578T, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.58×** | +4.7 | 2e-04 | 32/48 (SW480, COLO 205, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.24×** | +4.2 | 0.002 | 23/48 (HS-578T, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.007 | 24/48 (KATO III, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **1.21×** | +3.7 | 0.009 | 21/48 (A549, A-172, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.43×** | +3.6 | 0.012 | 23/48 (NCI-H1573, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.013 | 22/48 (NCI-H1573, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +3.4 | 0.022 | 21/48 (KATO III, A-172, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3469.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.499×** | -13.4 | 3e-38 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.513×** | -12.9 | 2e-35 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.528×** | -12.3 | 2e-32 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.584×** | -10.4 | 5e-23 | 41/48 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.594×** | -10.0 | 1e-21 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.628×** | -8.5 | 3e-15 | 42/48 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.700×** | -6.9 | 6e-10 | 32/48 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.524×** | -6.5 | 5e-09 | 36/45 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.795×** | -6.2 | 3e-08 | 31/49 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.741×** | -5.5 | 2e-06 | 29/47 (HCT15, LoVo, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.745×** | -5.4 | 3e-06 | 30/47 (SNU-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.779×** | -4.8 | 8e-05 | 28/48 (COLO 205, SW480, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.780×** | -4.8 | 9e-05 | 28/48 (PANC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.633×** | -4.6 | 2e-04 | 26/48 (A-427, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.642×** | -4.5 | 3e-04 | 29/49 (A-427, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.673×** | -4.0 | 0.002 | 28/48 (KATO III, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.822×** | -3.8 | 0.005 | 26/48 (HCT15, A-172, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.767×** | -3.6 | 0.008 | 24/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3469. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 257 | 1 | 9 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.96× (z +12.6) | [[Digitoxin (drug)]] 5 µM 0.264× (z -24.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.284× (z -23.5) |
| [[MIA PaCa-2 (line)]] | alt | 258 | 0 | 8 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -14.9) |
| [[NCI-H23 (line)]] | alt | 205 | 2 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +18.5) | [[Dinaciclib (drug)]] 5 µM 0.0805× (z -34.9) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.391× (z -13.5) |
| [[SW480 (line)]] | alt | 154 | 1 | 7 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.06× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.310× (z -18.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.316× (z -18.5) |
| [[HCT15 (line)]] | alt | 295 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.371× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.442× (z -11.5) |
| [[SNU-1 (line)]] | wt | 197 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.310× (z -13.6) |
| [[A-427 (line)]] | wt | 203 | 3 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +15.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +12.3) | [[PH-797804 (drug)]] 5 µM 0.251× (z -10.8) |
| [[HT-29 (line)]] | alt | 101 | 3 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.39× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.17× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.353× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.460× (z -9.2) |
| [[KATO III (line)]] | alt | 134 | 2 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 1.97× (z +8.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.380× (z -11.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.422× (z -11.1) |
| [[LoVo (line)]] | wt | 162 | 1 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.59× (z +14.4) | [[Digitoxin (drug)]] 5 µM 0.400× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.474× (z -11.3) |
| [[SHP-77 (line)]] | alt | 134 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.382× (z -11.3) |
| [[NCI-H2347 (line)]] | alt | 65.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +11.0) | — |
| [[RKO (line)]] | wt | 114 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +8.8) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.348× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.361× (z -11.3) |
| [[SNU-423 (line)]] | alt | 154 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +19.3) | [[Ixazomib citrate (drug)]] 5 µM 0.478× (z -8.7) |
| [[AN3 CA (line)]] | alt | 154 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -12.0) |
| [[CFPAC-1 (line)]] | alt | 61.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.6) | — |
| [[COLO 205 (line)]] | alt | 185 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -12.1) |
| [[H4 (line)]] | wt | 164 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.424× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 221 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.600× (z -9.8) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.505× (z -9.2) |
| [[HS-578T (line)]] | alt | 142 | 3 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.12× (z +13.5) | — |
| [[LOX-IMVI (line)]] | wt | 99.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.418× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 110 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.60× (z +11.3) | — |
| [[NCI-H2030 (line)]] | alt | 106 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.6) | [[Digitoxin (drug)]] 5 µM 0.408× (z -9.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 219 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.85× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 72.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 74.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.9) | — |
| [[Hs 766T (line)]] | wt | 150 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.3) | [[Ixazomib citrate (drug)]] 5 µM 0.401× (z -10.5) |
| [[J82 (line)]] | alt | 82.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -9.3) |
| [[NCI-H1792 (line)]] | alt | 50.0 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.30× (z +9.3) | — |
| [[NCI-H460 (line)]] | wt | 122 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +9.9) | [[Digitoxin (drug)]] 5 µM 0.436× (z -10.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.382× (z -10.5) |
| [[A498 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.595× (z -9.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A549 (line)]] | wt | 165 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -9.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[BT-474 (line)]] | alt | 56.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.345× (z -8.6) |
| [[C-33 A (line)]] | alt | 154 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.12× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 98.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -8.7) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.344× (z -10.5) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 91.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.448× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 114 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.20× (z +8.6) | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.100× (z -10.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 75.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.461× (z -8.5) |
| [[SW48 (line)]] | wt | 166 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.337× (z -9.6) |
| [[C32 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 121 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 64.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3469), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC25]] | +0.75 | +0.80 / +0.70 | both halves | 7e-06 |  |
| [[TRMT13]] | +0.75 | +0.83 / +0.65 | both halves | 7e-06 |  |
| [[MTIF2]] | +0.75 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[USP40]] | +0.74 | +0.84 / +0.59 | both halves | 7e-06 |  |
| [[NOL8]] | +0.72 | +0.82 / +0.63 | both halves | 7e-06 |  |
| [[DARS1]] | +0.72 | +0.75 / +0.60 | both halves | 7e-06 |  |
| [[ZMYM4]] | +0.72 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[NOP14]] | +0.71 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[AASDHPPT]] | +0.70 | +0.80 / +0.55 | both halves | 1e-05 |  |
| [[ICE2]] | +0.70 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[RPL7L1]] | +0.70 | +0.83 / +0.55 | both halves | 1e-05 |  |
| [[GUF1]] | +0.69 | +0.77 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL25]] | -0.64 | -0.54 / -0.54 | both halves | 1e-05 |  |
| [[GNB2]] | -0.63 | -0.69 / -0.50 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.62 | -0.68 / -0.45 | both halves | 3e-05 |  |
| [[UBTD1]] | -0.62 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[ASB16-AS1]] | -0.62 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SAP130]] | -0.61 | -0.69 / -0.49 | both halves | 1e-05 |  |
| [[MBOAT7]] | -0.61 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[CD81]] | -0.60 | -0.68 / -0.47 | both halves | 2e-05 |  |
| [[TOR1B]] | -0.60 | -0.53 / -0.54 | both halves | 1e-05 |  |
| [[UBE2G1]] | -0.60 | -0.69 / -0.42 | both halves | 4e-05 |  |
| [[TPST2]] | -0.59 | -0.75 / -0.44 | both halves | 3e-05 | pathway: Differentiation of T cells |
| [[RNF38]] | -0.59 | -0.68 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 028]] — Intraflagellar transport; 154 genes; this gene is in the **+** arm (projection on the module's main direction 0.760). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-23.1, 7.7); signed map (10.9, -25.6). **Vector** length 132, 46.9% of its response variance represented; |z| ≥ 3 in 1,208 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +15.7 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +13.4 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +9.7 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.2 | +4.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +8.6 | +6.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.0 | +3.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.8 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.7 | +1.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -8.0 | -6.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.1 | -5.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.5 | -10.4 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -5.1 | -6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.9 | -8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -6.9 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.1 | -3.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -2.1 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.3 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | RAD50 double strand break repair protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,556,019-132,646,349 (+) |
| Ensembl biotype | protein_coding |
| Also known as | hRad50, RAD50-2 |
| Gene groups (HGNC) | BRCA1 C complex; MRN complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 42 pathways, smallest: Sensing of DNA Double Strand Breaks; HDR through MMEJ (alt-NHEJ); Impaired BRCA2 binding to PALB2 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92878](https://www.uniprot.org/uniprotkb/Q92878) (DNA repair protein RAD50):

> Component of the MRN complex, which plays a central role in double-strand break (DSB) repair, DNA recombination, maintenance of telomere integrity and meiosis. The MRN complex is involved in the repair of DNA double-strand breaks (DSBs) via homologous recombination (HR), an error-free mechanism which primarily occurs during S and G2 phases. The complex (1) mediates the end resection of damaged DNA, which generates proper single-stranded DNA, a key initial steps in HR, and is (2) required for …

**Summary**, from NCBI Gene [10111](https://www.ncbi.nlm.nih.gov/gene/10111):

> The protein encoded by this gene is highly similar to Saccharomyces cerevisiae Rad50, a protein involved in DNA double-strand break repair. This protein forms a complex with MRE11 and NBS1. The protein complex binds to DNA and displays numerous enzymatic activities that are required for nonhomologous joining of DNA ends. This protein, cooperating with its partners, is important for DNA double-strand break repair, cell cycle checkpoint activation, telomere maintenance, and meiotic recombination. …

**Accessions** — [HGNC:9816](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9816) · Entrez [10111](https://www.ncbi.nlm.nih.gov/gene/10111) · UniProt [Q92878](https://www.uniprot.org/uniprotkb/Q92878) · Ensembl [ENSG00000113522](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113522)

## Data

Gene col 3469: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3469); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3469, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3469]; `tensor/DDL_lfc|DDL_z.npy` [3469]; `embed/gene_vectors.npy` [3469]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3469 or target_col == 3469). Every well: [[RAD50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAD50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
