---
symbol: "TM7SF3"
type: "gene"
col: 738
ensembl_id: "ENSG00000064115"
name: "transmembrane 7 superfamily member 3"
location: "12p11.23"
module: 65
arm: "+"
pooled_cpm: 65.02
n_lines_expressing: 50
n_dd_up: 31
n_dd_down: 23
n_dd_up_clean: 22
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# TM7SF3

*transmembrane 7 superfamily member 3* — 12p11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +17.6, q 0e+00, up in 39 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Radotinib (drug)]] 5 µM: 1.38× (z +10.8, q 7e-25, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.665× (z -13.5, q 5e-39, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALDH7A1]] (+0.67, fdr 9e-06), [[SDHAF3]] (+0.65, fdr 7e-06), [[PRMT9]] (+0.64, fdr 7e-06); moves opposite to [[CDR2]] (-0.62, fdr 1e-05), [[KCNJ14]] (-0.61, fdr 1e-05), [[TUT7]] (-0.57, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 738.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +17.6 | 0e+00 | 39/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +15.3 | 0e+00 | 32/42 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.77×** | +12.4 | 8e-33 | 34/45 (NCI-H1573, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.38×** | +10.8 | 7e-25 | 42/48 (AsPC-1, NCI-H1792, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +10.7 | 7e-25 | 37/48 (SW 900, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +10.7 | 8e-25 | 41/48 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.53×** | +10.0 | 1e-21 | 31/48 (J82, HOP62, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.51×** | +9.7 | 3e-20 | 32/48 (HOP62, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.46×** | +8.8 | 8e-17 | 30/48 (J82, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **1.48×** | +8.8 | 8e-17 | 35/47 (A-172, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +8.3 | 7e-15 | 33/48 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.36×** | +7.2 | 3e-11 | 32/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.24×** | +7.1 | 7e-11 | 24/48 (NCI-H460, LOX-IMVI, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +6.2 | 2e-08 | 31/48 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.65×** | +6.2 | 3e-08 | 31/49 (PANC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.57×** | +5.5 | 1e-06 | 23/47 (HepG2/C3A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +5.3 | 4e-06 | 23/47 (SW480, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.48×** | +4.8 | 4e-05 | 23/49 (A498, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 0.5 µM |  | **1.33×** | +4.8 | 4e-05 | 21/49 (PANC-1, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.22×** | +4.7 | 7e-05 | 17/48 (HOP62, NCI-H1573, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **1.21×** | +4.5 | 2e-04 | 18/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bentamapimod (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 7/48 (PANC-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 738.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.665×** | -13.5 | 5e-39 | 31/48 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.574×** | -13.0 | 2e-36 | 39/48 (SNU-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.610×** | -11.6 | 8e-29 | 37/48 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.623×** | -11.1 | 2e-26 | 41/48 (SW480, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.637×** | -10.6 | 4e-24 | 29/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.659×** | -9.8 | 1e-20 | 37/48 (SW1417, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.739×** | -7.1 | 1e-10 | 32/47 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.757×** | -6.5 | 5e-09 | 23/48 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.769×** | -6.2 | 4e-08 | 29/48 (NCI-H23, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.771×** | -6.1 | 6e-08 | 25/47 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.775×** | -6.0 | 1e-07 | 27/48 (NCI-H23, LOX-IMVI, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.728×** | -6.0 | 1e-07 | 27/48 (SK-MEL-2, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.783×** | -5.7 | 4e-07 | 23/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.780×** | -5.6 | 8e-07 | 23/47 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.849× | -5.4 | 2e-06 | 20/49 (NCI-H23, KATO III, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.796×** | -5.4 | 3e-06 | 18/48 (NCI-H460, NCI-H2347, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.819×** | -4.7 | 9e-05 | 21/47 (SNU-423, SK-MEL-2, …) | rises with dose | low cells (technical?) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.824×** | -4.6 | 2e-04 | 19/47 (NCI-H23, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.31 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 738. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 66.7 | 3 (3 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.81× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -26.0) |
| [[HOP62 (line)]] | alt | 73.9 | 5 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.79× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 40.0 | 2 (1 ⚠) | 5 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.05× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -15.1) |
| [[LoVo (line)]] | wt | 59.1 | 2 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.73× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -19.5) |
| [[SW480 (line)]] | alt | 135 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 1.96× (z +9.3) ⚠ toxic; transcription drop | [[Auranofin (drug)]] 5 µM 0.351× (z -15.2) |
| [[J82 (line)]] | alt | 33.2 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.15× (z +9.5) ⚠ cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H1573 (line)]] | alt | 41.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.45× (z +14.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.8) |
| [[A-172 (line)]] | wt | 58.9 | 3 (2 ⚠) | 1 | [[TAK-901 (drug)]] 5 µM 7.44× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -9.2) |
| [[C32 (line)]] | wt | 90.4 | 1 | 3 | [[Amsacrine (drug)]] 5 µM 2.33× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.300× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 103 | 1 | 3 | [[Selinexor (drug)]] 5 µM 1.75× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -18.8) |
| [[NCI-H1792 (line)]] | alt | 44.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.74× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -11.0) |
| [[SW1417 (line)]] | alt | 54.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -11.9) |
| [[A498 (line)]] | wt | 94.6 | 1 | 1 | [[TAK-901 (drug)]] 5 µM 11.2× (z +12.6) | [[Auranofin (drug)]] 5 µM 0.422× (z -8.6) |
| [[Hs 766T (line)]] | wt | 39.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.48× (z +9.4) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.434× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 55.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.2) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 77.7 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.03× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 56.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 117 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.398× (z -11.0) |
| [[RKO (line)]] | wt | 46.2 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.38× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 36.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.251× (z -9.8) |
| [[SNU-1 (line)]] | wt | 44.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.145× (z -12.8) |
| [[SW 900 (line)]] | alt | 86.5 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 2.11× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.368× (z -8.9) |
| [[A-427 (line)]] | wt | 130 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.30× (z +10.4) | — |
| [[A549 (line)]] | wt | 89.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.7) |
| [[C-33 A (line)]] | alt | 60.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.83× (z +9.0) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 37.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.70× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 58.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.03× (z +9.0) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 34.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.1) |
| [[KATO III (line)]] | alt | 46.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 38.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 105 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.18× (z +9.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 45.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 40.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.28× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 110 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.157× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 95.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 65.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 738), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH7A1]] | +0.67 | +0.57 / +0.71 | both halves | 9e-06 |  |
| [[SDHAF3]] | +0.65 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[PRMT9]] | +0.64 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[ZNF30]] | +0.64 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[CROT]] | +0.64 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SLC25A12]] | +0.64 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[BBS2]] | +0.63 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[CMBL]] | +0.63 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[SCP2]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[CAT]] | +0.63 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[ORC4]] | +0.62 | +0.70 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDR2]] | -0.62 | -0.55 / -0.62 | both halves | 1e-05 |  |
| [[KCNJ14]] | -0.61 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[TUT7]] | -0.57 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[FAM120B]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CRK]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LINC02798]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[WNT2B]] | -0.56 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.55 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[MYH3]] | -0.55 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.55 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[LRP2BP-AS1]] | -0.54 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[TUBA1C]] | -0.54 | -0.46 / -0.57 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers TM7SF3's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 5.6% of all compounds | 0.063 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FDXR]] | B | FDXR activity raises TM7SF3's level | lines that do not express FDXR (8) vs lines expressing it (42) | 1.57× lower at baseline in the lines without FDXR | 0.083 | ⚠ within organs, on part of the lines; also absent: GRIN2C, MCM10; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.690). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.9, -8.7); signed map (-31.9, -13.0). **Vector** length 133, 42.1% of its response variance represented; |z| ≥ 3 in 1,484 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.7 | +4.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +7.9 | +10.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.8 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +10.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.9 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +6.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -11.2 | -11.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -10.3 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.8 | -13.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.4 | -13.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.7 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.1 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -5.4 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane 7 superfamily member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p11.23 — chr12:26,971,579-27,014,434 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 7TM uncharacterized proteins |
| Hallmark sets | P53_PATHWAY |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS93](https://www.uniprot.org/uniprotkb/Q9NS93) (Transmembrane 7 superfamily member 3):

> Involved in the inhibition of cytokine-induced death of pancreatic beta cells. Involved in the promotion of insulin secretion from pancreatic beta cells. Is a downstream transcriptional target of p53/TP53, and acts as a pro-survival homeostatic factor that attenuates the development of cellular stress. Maintains protein homeostasis and promotes cell survival through attenuation of endoplasmic reticulum (ER) stress and the subsequent induction of unfolded protein response (UPR).

**Summary**, from NCBI Gene [51768](https://www.ncbi.nlm.nih.gov/gene/51768):

> Involved in cellular response to unfolded protein; negative regulation of programmed cell death; and positive regulation of insulin secretion. Located in cytosol; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23049](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23049) · Entrez [51768](https://www.ncbi.nlm.nih.gov/gene/51768) · UniProt [Q9NS93](https://www.uniprot.org/uniprotkb/Q9NS93) · Ensembl [ENSG00000064115](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064115)

## Data

Gene col 738: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 738); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 738, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 738]; `tensor/DDL_lfc|DDL_z.npy` [738]; `embed/gene_vectors.npy` [738]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 738 or target_col == 738). Every well: [[TM7SF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TM7SF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
