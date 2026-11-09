---
symbol: "ZNF337-AS1"
type: "gene"
col: 13133
ensembl_id: "ENSG00000213742"
name: "ZNF337 antisense RNA 1"
location: "20p11.21"
module: 124
arm: "+"
pooled_cpm: 31.32
n_lines_expressing: 49
n_dd_up: 24
n_dd_down: 20
n_dd_up_clean: 19
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/124"]
generated_by: "tahoemap"
---

# ZNF337-AS1

*ZNF337 antisense RNA 1* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.11× (z +21.0, q 0e+00, up in 44 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.411× (z -11.6, q 1e-28, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (57 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 43 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BDNF-AS]] (+0.77, fdr 3e-05), [[PBLD]] (+0.77, fdr 0.001, ⚠ one half only (not replicated)), [[HEXIM2-AS1]] (+0.76, fdr 2e-05), [[ANKRD17-DT]] (+0.76, fdr 3e-05); moves opposite to [[MAST3]] (-0.72, fdr 7e-04), [[SLC27A1]] (-0.70, fdr 8e-04, ⚠ one half only (not replicated)), [[ANKRD27]] (-0.70, fdr 0.002, ⚠ one half only (not replicated)), [[CAMK2G]] (-0.70, fdr 2e-04), [[SH3PXD2B]] (-0.68, fdr 6e-04).
> It sits in the **+** arm of [[Module 124]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 5 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.11×** | +21.0 | 0e+00 | 44/46 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.28×** | +10.4 | 8e-23 | 38/46 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +7.8 | 1e-12 | 37/47 (LOX-IMVI, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.72×** | +6.8 | 1e-09 | 30/45 (HT-29, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.6 | 6e-09 | 36/47 (A-172, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +5.9 | 4e-07 | 34/46 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +5.9 | 4e-07 | 28/46 (NCI-H2030, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.4 | 5e-06 | 29/46 (LoVo, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.50×** | +5.3 | 7e-06 | 32/46 (HOP62, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.2 | 1e-05 | 21/35 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.47×** | +5.0 | 3e-05 | 20/42 (AsPC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.006 | 23/47 (COLO 205, PANC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.34×** | +3.8 | 0.007 | 18/47 (A549, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.007 | 18/47 (LoVo, SW 900, …) | all doses, stronger at high dose |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.33×** | +3.7 | 0.007 | 16/47 (NCI-H2030, NCI-H460, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.009 | 19/46 (SW480, HepG2/C3A, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.31×** | +3.6 | 0.012 | 23/47 (PANC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Amsacrine (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.013 | 14/47 (A549, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.21×** | +3.5 | 0.016 | 16/47 (SW480, RKO, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.016 | 17/46 (HOP62, NCI-H2030, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.411×** | -11.6 | 1e-28 | 41/46 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.433×** | -11.0 | 2e-25 | 42/46 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.442×** | -10.7 | 2e-24 | 40/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.459×** | -10.2 | 3e-22 | 38/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.279×** | -8.7 | 3e-16 | 34/45 (Panc 03.27, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.293×** | -8.4 | 4e-15 | 38/47 (PANC-1, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.565×** | -7.5 | 7e-12 | 31/47 (PANC-1, RKO, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.600×** | -6.3 | 2e-08 | 33/47 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.614×** | -6.1 | 5e-08 | 26/45 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.413×** | -6.1 | 8e-08 | 26/41 (C-33 A, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.637×** | -5.9 | 2e-07 | 25/47 (NCI-H460, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.644×** | -5.8 | 4e-07 | 31/46 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.479×** | -5.0 | 2e-05 | 29/44 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.701×** | -4.6 | 1e-04 | 27/47 (BT-474, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.729×** | -4.1 | 0.001 | 23/46 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.001 | 23/47 (NCI-H661, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.834× | -3.4 | 0.025 | 19/47 (KATO III, SW480, …) | rises with dose |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.782×** | -3.2 | 0.040 | 16/46 (AN3 CA, SW 900, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.790×** | -3.1 | 0.059 | 18/46 (HEC-1-A, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.48 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 64.1 | 1 | 9 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.76× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.295× (z -13.3) |
| [[BT-474 (line)]] | alt | 52.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.221× (z -10.8) |
| [[HepG2_C3A (line)]] | wt | 40.5 | 2 (1 ⚠) | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.51× (z +13.8) | [[Digitoxin (drug)]] 5 µM 0.244× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.244× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 39.7 | 2 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.247× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.315× (z -9.4) |
| [[SW480 (line)]] | alt | 39.9 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.97× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.283× (z -11.6) |
| [[KATO III (line)]] | alt | 53.1 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.270× (z -11.7) |
| [[A-427 (line)]] | wt | 32.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.226× (z -11.6) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 0.135× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 44.1 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.03× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.284× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.138× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 30.5 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.127× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.355× (z -8.9) |
| [[A498 (line)]] | wt | 24.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +11.3) | — |
| [[A549 (line)]] | wt | 35.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +10.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.245× (z -9.4) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 24.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +10.8) | [[Digitoxin (drug)]] 5 µM 0.204× (z -8.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 24.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.50× (z +13.0) | — |
| [[Hs 766T (line)]] | wt | 33.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +11.4) | [[Ixazomib citrate (drug)]] 5 µM 0.234× (z -9.4) |
| [[HS-578T (line)]] | alt | 16.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.53× (z +13.8) | — |
| [[HT-29 (line)]] | alt | 20.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +10.1) | — |
| [[LoVo (line)]] | wt | 21.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +12.1) | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.53× (z +15.3) | — |
| [[LS 180 (line)]] | wt | 19.4 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 42.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.6) | [[Ixazomib citrate (drug)]] 5 µM 0.256× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 20.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.94× (z +15.0) | — |
| [[NCI-H23 (line)]] | alt | 25.6 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.214× (z -10.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +9.2) | [[PH-797804 (drug)]] 5 µM 0.0261× (z -11.5) |
| [[RKO (line)]] | wt | 67.7 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +14.6) | [[Ixazomib citrate (drug)]] 5 µM 0.339× (z -9.2) |
| [[SW1417 (line)]] | alt | 54.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.4) |
| [[A-172 (line)]] | wt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.43× (z +15.4) | — |
| [[AsPC-1 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +12.5) | — |
| [[C32 (line)]] | wt | 23.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.57× (z +13.7) | — |
| [[H4 (line)]] | wt | 15.0 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 26.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.37× (z +10.6) | — |
| [[NCI-H2347 (line)]] | alt | 9.29 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 30.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 27.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 18.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.76× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 36 of them with an alert (⚠; 36 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BDNF-AS]] | +0.77 | +0.83 / +0.44 | both halves | 3e-05 | same gene group |
| [[PBLD]] | +0.77 | +0.81 / +0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[HEXIM2-AS1]] | +0.76 | +0.72 / +0.48 | both halves | 2e-05 | same gene group |
| [[ANKRD17-DT]] | +0.76 | +0.80 / +0.43 | both halves | 3e-05 |  |
| [[RFX3-DT]] | +0.76 | +0.83 / +0.21 | both halves | 7e-04 |  |
| [[MAD2L1-DT]] | +0.76 | +0.82 / +0.26 | both halves | 3e-04 |  |
| [[SEPTIN7-DT]] | +0.75 | +0.77 / +0.34 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | +0.75 | +0.72 / +0.33 | both halves | 1e-04 | same gene group |
| [[PCBP1-AS1]] | +0.74 | +0.74 / +0.29 | both halves | 2e-04 | same gene group |
| [[ST7L]] | +0.74 | +0.80 / +0.28 | both halves | 3e-04 |  |
| [[MFF-DT]] | +0.74 | +0.75 / +0.17 | ⚠ one half (not replicated) | 0.001 |  |
| [[GABPB1-AS1]] | +0.74 | +0.71 / +0.49 | both halves | 1e-05 | same gene group |
| [[RXYLT1]] | +0.74 | +0.80 / +0.36 | both halves | 1e-04 |  |
| [[RAB30-DT]] | +0.74 | +0.81 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | -0.72 | -0.66 / -0.21 | both halves | 7e-04 |  |
| [[SLC27A1]] | -0.70 | -0.68 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[ANKRD27]] | -0.70 | -0.73 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[CAMK2G]] | -0.70 | -0.64 / -0.30 | both halves | 2e-04 |  |
| [[TSPAN33]] | -0.68 | -0.55 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[SH3PXD2B]] | -0.68 | -0.69 / -0.21 | both halves | 6e-04 |  |
| [[FCHO1]] | -0.67 | -0.54 / -0.24 | both halves | 4e-04 |  |
| [[DOK4]] | -0.67 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[GNAI2]] | -0.65 | -0.59 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[USP35]] | -0.65 | -0.68 / -0.36 | both halves | 1e-04 |  |
| [[YIF1B]] | -0.65 | -0.62 / +0.03 | ⚠ one half (not replicated) | 1.00 |  |
| [[MGST3]] | -0.64 | -0.59 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZNF337-AS1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 4.8% of all compounds | 0.005 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TSPAN33]] | B | TSPAN33 activity raises ZNF337-AS1's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.64× lower at baseline in the lines without TSPAN33 | 0.045 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[PRKAR1B]] | B | PRKAR1B activity raises ZNF337-AS1's level | lines that do not express PRKAR1B (6) vs lines expressing it (44) | 1.81× lower at baseline in the lines without PRKAR1B | 0.056 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers ZNF337-AS1's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.8% of all compounds | 0.0995 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 124]]; 39 genes; this gene is in the **+** arm (projection on the module's main direction 0.790). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (1.6, 7.7); signed map (25.3, -9.1). **Vector** length 97.0, 27.5% of its response variance represented; |z| ≥ 3 in 1,257 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +10.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +21.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.9 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +7.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.2 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.2 | +3.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.6 | +3.9 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -8.0 | -1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.8 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.7 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.7 | +0.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.5 | -1.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.1 | +1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.6 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.4 | -8.7 |

## What is on record

|  |  |
|---|---|
| Name | ZNF337 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20p11.21 — chr20:25,624,045-25,689,032 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40759) · Entrez [102724826](https://www.ncbi.nlm.nih.gov/gene/102724826) · Ensembl [ENSG00000213742](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213742)

## Data

Gene col 13133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13133); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13133]; `tensor/DDL_lfc|DDL_z.npy` [13133]; `embed/gene_vectors.npy` [13133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13133 or target_col == 13133). Every well: [[ZNF337-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF337-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
