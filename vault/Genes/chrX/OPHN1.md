---
symbol: "OPHN1"
type: "gene"
col: 1260
ensembl_id: "ENSG00000079482"
name: "oligophrenin 1"
location: "Xq12"
module: 8
arm: "+"
pooled_cpm: 72.95
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 32
n_dd_up_clean: 5
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# OPHN1

*oligophrenin 1* — Xq12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (4 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.49× (z +10.8, q 3e-24, up in 36 of 47 measured lines) ⚠ cell-cycle shift, explains ~53% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.29× (z +4.8, q 2e-04, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (20 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.401× (z -17.4, q 0e+00, down in 40 of 47 measured lines) ⚠ cell-cycle shift, explains ~27% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.625× (z -8.9, q 4e-17, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DAB2IP]] (+0.49, fdr 3e-05), [[TANC1]] (+0.48, fdr 3e-05), [[TPD52L1]] (+0.48, fdr 3e-05); moves opposite to [[TPT1-AS1]] (-0.52, fdr 3e-05), [[ADGRL1-AS1]] (-0.47, fdr 9e-05), [[SLC28A2-AS1]] (-0.46, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TGFBR3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1260.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.49×** | +10.8 | 3e-24 | 36/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.40×** | +6.5 | 3e-08 | 35/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.36×** | +5.8 | 1e-06 | 30/47 (LS 180, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.29×** | +4.8 | 2e-04 | 25/47 (NCI-H1573, AsPC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.6 | 5e-04 | 26/47 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.24×** | +4.0 | 0.007 | 17/49 (AsPC-1, NCI-H1573, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.012 | 16/47 (SNU-423, A-172, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.021 | 19/46 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.023 | 14/47 (AsPC-1, NCI-H1573, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.023 | 20/46 (AsPC-1, NCI-H1573, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 1.19× | +3.3 | 0.052 | 17/47 (AsPC-1, LoVo, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.064 | 13/47 (J82, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 21 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1260.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.401×** | -17.4 | 0e+00 | 40/47 (SW480, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.458×** | -14.8 | 0e+00 | 43/46 (KATO III, RKO, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.623×** | -12.7 | 1e-34 | 37/47 (SK-MEL-2, A549, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.524×** | -12.3 | 1e-32 | 36/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.529×** | -12.1 | 1e-31 | 37/47 (SW480, KATO III, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.625×** | -8.9 | 4e-17 | 35/47 (SW480, C32, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.637×** | -8.6 | 8e-16 | 31/47 (A549, SW 900, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~55% of this change | **0.682×** | -7.3 | 3e-11 | 32/47 (LOX-IMVI, H4, …) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.485×** | -7.2 | 4e-11 | 32/48 (SNU-1, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.691×** | -7.0 | 1e-10 | 31/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.774×** | -6.9 | 3e-10 | 28/48 (C32, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change | **0.701×** | -6.6 | 1e-09 | 28/48 (LOX-IMVI, C32, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **0.697×** | -6.6 | 2e-09 | 25/42 (KATO III, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | **0.699×** | -6.5 | 3e-09 | 30/47 (SK-MEL-2, A549, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.725×** | -6.1 | 4e-08 | 26/47 (C32, SK-MEL-2, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.551×** | -5.9 | 1e-07 | 28/47 (AN3 CA, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.780×** | -4.7 | 7e-05 | 22/47 (C32, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.802×** | -4.2 | 7e-04 | 21/47 (J82, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.798×** | -4.1 | 9e-04 | 21/46 (HT-29, C32, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.805×** | -4.0 | 0.001 | 23/46 (C32, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.863× | -4.0 | 0.002 | 17/48 (C32, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.795×** | -3.9 | 0.002 | 24/47 (C32, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.010 | 19/47 (MIA PaCa-2, A549, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.889× | -3.2 | 0.028 | 4/48 (SW480, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.853× | -3.0 | 0.042 | 17/47 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.754×** | -2.8 | 0.083 | 15/47 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 0.902× | -2.8 | 0.090 | 2/48 (LS 180, SW48) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1260. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 204 | 0 | 25 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -18.9) |
| [[KATO III (line)]] | alt | 87.4 | 0 | 12 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.138× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 211 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -23.5) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -14.4) |
| [[SW480 (line)]] | alt | 61.6 | 0 | 9 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -22.6) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.271× (z -15.1) |
| [[A549 (line)]] | wt | 77.0 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -20.3) ⚠ cell-cycle shift, explains ~65% of this change |
| [[COLO 205 (line)]] | alt | 42.1 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.0) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 56.8 | 0 | 8 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.187× (z -12.7) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.358× (z -11.0) |
| [[SNU-1 (line)]] | wt | 77.0 | 0 | 8 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -14.6) ⚠ cell-cycle shift, explains ~65% of this change |
| [[LOX-IMVI (line)]] | wt | 196 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.284× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.564× (z -9.6) |
| [[LoVo (line)]] | wt | 39.7 | 1 (1 ⚠) | 5 (5 ⚠) | [[Selinexor (drug)]] 5 µM 2.03× (z +10.5) ⚠ cell-cycle shift, explains ~53% of this change | [[Digitoxin (drug)]] 5 µM 0.299× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SW 900 (line)]] | alt | 55.4 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.237× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 54.7 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.298× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[AsPC-1 (line)]] | alt | 38.4 | 2 | 2 (2 ⚠) | [[Cobimetinib (drug)]] 5 µM 3.56× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -11.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H1792 (line)]] | alt | 48.4 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 90.2 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.397× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[PANC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.59× (z +8.9) ⚠ cell-cycle shift, explains ~53% of this change | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -9.0) |
| [[A-427 (line)]] | wt | 65.5 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AN3 CA (line)]] | alt | 176 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -11.4) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0618× (z -10.6) |
| [[HCT15 (line)]] | alt | 46.2 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -12.7) ⚠ toxic; cell-cycle shift, explains ~55% of this change |
| [[Hs 766T (line)]] | wt | 89.9 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.291× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -9.5) |
| [[HS-578T (line)]] | alt | 37.5 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.248× (z -11.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[HT-29 (line)]] | alt | 82.7 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.180× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 68.7 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -13.5) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -11.9) |
| [[LS 180 (line)]] | wt | 47.8 | 2 (1 ⚠) | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.3) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +9.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -11.1) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 71.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -19.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 75.2 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.282× (z -10.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 99.3 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -15.9) |
| [[A498 (line)]] | wt | 49.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -19.8) ⚠ cell-cycle shift, explains ~65% of this change |
| [[CFPAC-1 (line)]] | alt | 51.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -12.7) ⚠ cell-cycle shift, explains ~65% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 100 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +13.4) ⚠ cell-cycle shift, explains ~65% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.432× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~79% of this change |
| [[NCI-H596 (line)]] | alt | 72.9 | 2 | 0 | [[Atazanavir (sulfate) (drug)]] 0.05 µM 14.6× (z +14.2) | — |
| [[SNU-423 (line)]] | alt | 70.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -11.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[C-33 A (line)]] | alt | 54.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.253× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[HEC-1-A (line)]] | alt | 50.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.344× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change |
| [[HOP62 (line)]] | alt | 43.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 2.35× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H1573 (line)]] | alt | 38.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -10.7) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H2030 (line)]] | alt | 49.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -9.5) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H2347 (line)]] | alt | 86.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.368× (z -13.7) |
| [[SW 1271 (line)]] | alt | 66.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0725× (z -10.5) ⚠ cell-cycle shift, explains ~25% of this change |
| [[SW48 (line)]] | wt | 71.1 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.276× (z -8.6) |
| [[BT-474 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 62.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 142 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 78.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.4 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 43.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1260), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DAB2IP]] | +0.49 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[TANC1]] | +0.48 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[TPD52L1]] | +0.48 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[EPS8]] | +0.48 | +0.44 / +0.40 | both halves | 4e-05 |  |
| [[USP54]] | +0.47 | +0.35 / +0.44 | both halves | 1e-04 |  |
| [[SAMD12]] | +0.47 | +0.47 / +0.38 | both halves | 7e-05 |  |
| [[MANSC1]] | +0.47 | +0.49 / +0.36 | both halves | 1e-04 |  |
| [[INPP4B]] | +0.46 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[PUM1]] | +0.46 | +0.37 / +0.38 | both halves | 7e-05 |  |
| [[KCTD3]] | +0.46 | +0.49 / +0.36 | both halves | 1e-04 | pathway: CDC42 GTPase cycle |
| [[RAVER2]] | +0.45 | +0.47 / +0.39 | both halves | 6e-05 |  |
| [[SH3BGRL2]] | +0.45 | +0.47 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPT1-AS1]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[ADGRL1-AS1]] | -0.47 | -0.36 / -0.38 | both halves | 9e-05 |  |
| [[SLC28A2-AS1]] | -0.46 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CRYGS]] | -0.44 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[CCM2]] | -0.43 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TMEM225B]] | -0.42 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MFSD11]] | -0.42 | -0.26 / -0.35 | both halves | 4e-04 |  |
| [[EGFR]] | -0.41 | -0.43 / -0.38 | both halves | 7e-05 |  |
| [[TRIOBP]] | -0.41 | -0.38 / -0.38 | both halves | 6e-05 |  |
| [[PPP1R13L]] | -0.41 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[GOSR2]] | -0.40 | -0.32 / -0.44 | both halves | 2e-04 |  |
| [[TNXB]] | -0.39 | -0.25 / -0.42 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGFBR3]] | B | TGFBR3 activity strengthens OPHN1's drug response | lines that do not express TGFBR3 (5) vs lines expressing it (43) | the lines without TGFBR3 respond 0.71× as strongly (z diff +2.65); strongest at Homoharringtonine 5 µM: 0.93x vs 0.55x (z diff +4.6) | 0.068 | ⚠ within organs, on part of the lines; also absent: LRP1, AMN; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.308). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.0, 43.6); signed map (57.5, -4.3). **Vector** length 78.2, 18.3% of its response variance represented; |z| ≥ 3 in 1,481 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +8.3 | +10.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +5.4 | +5.8 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.4 | +6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.8 | -2.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~55% of this change | +2.4 | -5.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +3.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.1 | -0.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.7 | +2.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.7 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.5 | +2.2 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.8 | -8.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -6.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.1 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.1 | -12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -2.0 | -4.7 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -1.1 | -1.1 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.0 | -2.5 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.0 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | oligophrenin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq12 — chrX:67,949,349-68,433,913 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OPN1, ARHGAP41; previously MRX60 |
| Gene groups (HGNC) | AH/BAR family Rho GTPase activating proteins |
| Hallmark sets | HEDGEHOG_SIGNALING, MITOTIC_SPINDLE |
| Reactome | 13 pathways, smallest: RHOJ GTPase cycle; RHOQ GTPase cycle; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O60890](https://www.uniprot.org/uniprotkb/O60890) (Oligophrenin-1):

> Stimulates GTP hydrolysis of members of the Rho family. Its action on RHOA activity and signaling is implicated in growth and stabilization of dendritic spines, and therefore in synaptic function. Critical for the stabilization of AMPA receptors at postsynaptic sites. Critical for the regulation of synaptic vesicle endocytosis at presynaptic terminals. Required for the localization of NR1D1 to dendrites, can suppress its repressor activity and protect it from proteasomal degradation (By …

**Summary**, from NCBI Gene [4983](https://www.ncbi.nlm.nih.gov/gene/4983):

> This gene encodes a Rho-GTPase-activating protein that promotes GTP hydrolysis of Rho subfamily members. Rho proteins are important mediators of intracellular signal transduction, which affects cell migration and cell morphogenesis. Mutations in this gene are responsible for OPHN1-related X-linked cognitive disability with cerebellar hypoplasia and distinctive facial dysmorhphism. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8148](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8148) · Entrez [4983](https://www.ncbi.nlm.nih.gov/gene/4983) · UniProt [O60890](https://www.uniprot.org/uniprotkb/O60890) · Ensembl [ENSG00000079482](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000079482)

## Data

Gene col 1260: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1260); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1260, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1260]; `tensor/DDL_lfc|DDL_z.npy` [1260]; `embed/gene_vectors.npy` [1260]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1260 or target_col == 1260). Every well: [[OPHN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OPHN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
