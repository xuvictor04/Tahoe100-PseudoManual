---
symbol: "GAN"
type: "gene"
col: 15355
ensembl_id: "ENSG00000261609"
name: "gigaxonin"
location: "16q23.2"
module: 180
arm: "+"
pooled_cpm: 113.12
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 6
n_dd_up_clean: 21
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# GAN

*gigaxonin* — 16q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.16× (z +17.7, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.597× (z -11.0, q 2e-25, down in 39 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.508× (z -8.2, q 6e-14, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LMBR1]] (+0.61, fdr 8e-06), [[KLHL29]] (+0.58, fdr 1e-05), [[PPFIA1]] (+0.58, fdr 1e-05); moves opposite to [[SMG7]] (-0.63, fdr 1e-05), [[HNRNPD]] (-0.61, fdr 1e-05), [[DMAP1]] (-0.58, fdr 1e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HMGN5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15355.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.16×** | +17.7 | 0e+00 | 48/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +17.3 | 0e+00 | 39/48 (NCI-H1573, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +15.9 | 0e+00 | 48/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +14.2 | 2e-43 | 46/48 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +10.8 | 5e-25 | 34/49 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +8.9 | 6e-17 | 33/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.44×** | +8.3 | 6e-15 | 30/48 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +8.1 | 3e-14 | 34/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +7.9 | 2e-13 | 38/48 (SNU-423, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +7.7 | 6e-13 | 34/48 (LOX-IMVI, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +7.6 | 2e-12 | 36/48 (BT-474, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.36×** | +7.0 | 9e-11 | 34/48 (BT-474, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +6.3 | 1e-08 | 29/48 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.32×** | +6.1 | 5e-08 | 30/50 (NCI-H460, PANC-1, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.30×** | +6.1 | 5e-08 | 29/48 (NCI-H1573, H4, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.61×** | +5.7 | 3e-07 | 35/48 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.19× | +5.6 | 6e-07 | 21/49 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.57×** | +5.4 | 2e-06 | 30/48 (PANC-1, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15355.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.597×** | -11.0 | 2e-25 | 39/45 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.648×** | -10.0 | 3e-21 | 37/49 (NCI-H23, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.508×** | -8.2 | 6e-14 | 37/49 (NCI-H1573, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.713×** | -7.5 | 9e-12 | 29/44 (J82, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.771×** | -5.8 | 9e-07 | 30/48 (LoVo, KATO III, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.944× | -4.6 | 4e-04 | 4/50 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.840× | -4.0 | 0.004 | 21/49 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.739×** | -3.6 | 0.018 | 19/49 (AsPC-1, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 0.874× | -3.6 | 0.018 | 13/48 (MIA PaCa-2, HepG2/C3A, …) | all doses, flat | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | 0.860× | -3.5 | 0.026 | 16/48 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.901× | -3.4 | 0.038 | 5/48 (MIA PaCa-2, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.901× | -3.3 | 0.048 | 13/49 (MIA PaCa-2, SW480, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.870× | -3.2 | 0.054 | 12/49 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 0.05 µM |  | 0.864× | -3.2 | 0.056 | 12/48 (RPMI-7951, SW480, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.876× | -3.1 | 0.080 | 10/49 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.877× | -3.1 | 0.080 | 15/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.879× | -3.0 | 0.082 | 15/49 (MIA PaCa-2, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.880× | -3.0 | 0.098 | 13/47 (NCI-H460, A-172, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15355. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 104 | 7 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -12.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 117 | 7 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +27.9) | [[TAK-901 (drug)]] 5 µM 0.230× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 76.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +11.1) | — |
| [[SW480 (line)]] | alt | 177 | 6 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +20.2) | [[Dinaciclib (drug)]] 0.05 µM 0.401× (z -11.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 212 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.76× (z +11.0) | [[Adagrasib (drug)]] 0.05 µM 0.636× (z -16.9) ⚠ position not correctable |
| [[A549 (line)]] | wt | 91.8 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.34× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.449× (z -10.4) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 122 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.88× (z +12.2) | — |
| [[Hs 766T (line)]] | wt | 83.8 | 4 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.37× (z +14.4) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -10.8) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 74.8 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.52× (z +13.2) | — |
| [[SNU-1 (line)]] | wt | 84.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.358× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 125 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.55× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.487× (z -8.6) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 78.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.47× (z +20.9) | — |
| [[HS-578T (line)]] | alt | 99.7 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +10.3) | [[Lonafarnib (drug)]] 5 µM 0.258× (z -8.7) ⚠ toxic |
| [[J82 (line)]] | alt | 109 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -13.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 204 | 1 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 74.0 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +14.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.377× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 55.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +14.4) | — |
| [[HEC-1-A (line)]] | alt | 81.9 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.453× (z -10.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 136 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.422× (z -9.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 64.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.282× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 118 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +12.5) | — |
| [[NCI-H23 (line)]] | alt | 110 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.09× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -13.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 119 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.71× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.466× (z -8.9) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 71.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.67× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 84.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +15.9) | — |
| [[SW1417 (line)]] | alt | 118 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.19× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 144 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.417× (z -9.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 93.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.25× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -8.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 106 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.46× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 116 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +19.6) | — |
| [[KATO III (line)]] | alt | 175 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.00× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -8.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 185 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.413× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Belumosudil (drug)]] 5 µM 0.492× (z -9.4) |
| [[Panc 03.27 (line)]] | alt | 84.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.411× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 80.5 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +10.3) | [[TAK-901 (drug)]] 5 µM 0.163× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 137 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.02× (z +9.6) | — |
| [[A-427 (line)]] | wt | 99.8 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.18× (z +9.0) | — |
| [[AN3 CA (line)]] | alt | 106 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.263× (z -9.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.331× (z -12.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +15.1) | — |
| [[RKO (line)]] | wt | 81.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.415× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 123 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.164× (z -9.2) |
| [[CHP-212 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15355), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*48 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMBR1]] | +0.61 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[KLHL29]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 | same gene group |
| [[PPFIA1]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[GPR89B]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[ARFGEF3]] | +0.57 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[SNX14]] | +0.56 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[ZXDC]] | +0.56 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[TPTEP2-CSNK1E]] | +0.56 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[DNAJC5]] | +0.55 | +0.37 / +0.55 | both halves | 8e-05 | same gene group |
| [[AXIN1]] | +0.55 | +0.39 / +0.50 | both halves | 6e-05 |  |
| [[MIB1]] | +0.54 | +0.59 / +0.58 | both halves | 7e-06 | same gene group |
| [[SNX25]] | +0.54 | +0.42 / +0.47 | both halves | 4e-05 |  |

## Genes that move opposite

*52 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMG7]] | -0.63 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[HNRNPD]] | -0.61 | -0.56 / -0.63 | both halves | 1e-05 |  |
| [[DMAP1]] | -0.58 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[TSPYL4]] | -0.58 | -0.57 / -0.47 | both halves | 2e-05 |  |
| [[LUC7L2]] | -0.57 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[SH3BGRL]] | -0.56 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[DHX9]] | -0.56 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[VAPA]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[ZBTB17]] | -0.56 | -0.53 / -0.63 | both halves | 1e-05 | same gene group |
| [[TTC30A]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[TTC31]] | -0.56 | -0.48 / -0.60 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HMGN5]] | B | HMGN5 activity lowers GAN's level | lines that do not express HMGN5 (7) vs lines expressing it (43) | 1.35× higher at baseline in the lines without HMGN5 | 0.058 | ⚠ within organs, on part of the lines; also absent: SH3BGRL; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.511). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-21.0, 2.0); signed map (-19.0, 44.1). **Vector** length 116, 37.1% of its response variance represented; |z| ≥ 3 in 1,475 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +10.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +5.3 | +5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.2 | +7.9 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +4.2 | +4.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +7.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.0 | +3.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +4.6 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -12.5 | -8.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -8.5 | -1.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.1 | -11.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.2 | -5.8 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -3.6 | -3.4 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -3.5 | -3.3 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -3.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | gigaxonin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q23.2 — chr16:81,314,944-81,390,809 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GAN1, KLHL16, GIG |
| Gene groups (HGNC) | Kelch like; BTB domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H2C0](https://www.uniprot.org/uniprotkb/Q9H2C0) (Gigaxonin):

> Probable cytoskeletal component that directly or indirectly plays an important role in neurofilament architecture. May act as a substrate-specific adapter of an E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Controls degradation of TBCB. Controls degradation of MAP1B and MAP1S, and is critical for neuronal maintenance and survival.

**Summary**, from NCBI Gene [8139](https://www.ncbi.nlm.nih.gov/gene/8139):

> This gene encodes a member of the cytoskeletal BTB/kelch (Broad-Complex, Tramtrack and Bric a brac) repeat family. The encoded protein plays a role in neurofilament architecture and is involved in mediating the ubiquitination and degradation of some proteins. Defects in this gene are a cause of giant axonal neuropathy (GAN). [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:4137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4137) · Entrez [8139](https://www.ncbi.nlm.nih.gov/gene/8139) · UniProt [Q9H2C0](https://www.uniprot.org/uniprotkb/Q9H2C0) · Ensembl [ENSG00000261609](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261609)

## Data

Gene col 15355: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15355); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15355, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15355]; `tensor/DDL_lfc|DDL_z.npy` [15355]; `embed/gene_vectors.npy` [15355]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15355 or target_col == 15355). Every well: [[GAN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
