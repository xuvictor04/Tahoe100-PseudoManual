---
symbol: "CPEB3"
type: "gene"
col: 2891
ensembl_id: "ENSG00000107864"
name: "cytoplasmic polyadenylation element binding protein 3"
location: "10q23.32"
module: 69
arm: "+"
pooled_cpm: 64.76
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 21
n_dd_up_clean: 18
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CPEB3

*cytoplasmic polyadenylation element binding protein 3* — 10q23.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.71× (z +14.1, q 3e-42, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.388× (z -17.9, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.450× (z -7.4, q 2e-11, down in 34 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MKRN1]] (+0.65, fdr 1e-05), [[ELF2]] (+0.62, fdr 2e-05), [[YPEL2]] (+0.61, fdr 1e-05); moves opposite to [[EEFSEC]] (-0.57, fdr 1e-05), [[POLR1A]] (-0.56, fdr 2e-05), [[TMEM185B]] (-0.56, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +14.1 | 3e-42 | 39/49 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +7.1 | 4e-10 | 33/48 (HOP62, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +6.7 | 3e-09 | 31/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.41×** | +6.6 | 7e-09 | 30/49 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +6.5 | 7e-09 | 29/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.3 | 2e-08 | 27/48 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +5.8 | 4e-07 | 30/48 (RKO, HOP62, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.39×** | +5.6 | 1e-06 | 26/48 (RKO, PANC-1, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +5.4 | 3e-06 | 29/49 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +5.3 | 8e-06 | 27/48 (RKO, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.9 | 4e-05 | 23/47 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.29×** | +4.8 | 8e-05 | 23/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.29×** | +4.7 | 1e-04 | 22/50 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 23/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.27×** | +4.4 | 5e-04 | 24/47 (AsPC-1, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +4.0 | 0.002 | 20/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 19/50 (A-427, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.24×** | +3.6 | 0.009 | 10/49 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.009 | 16/49 (AsPC-1, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.388×** | -17.9 | 0e+00 | 47/48 (NCI-H460, SW480, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -15.9 | 0e+00 | 35/42 (NCI-H2030, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.491×** | -13.5 | 3e-39 | 43/49 (Panc 03.27, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.592×** | -9.2 | 5e-18 | 35/44 (AN3 CA, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.450×** | -7.4 | 2e-11 | 34/48 (NCI-H460, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.457×** | -7.2 | 5e-11 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.701×** | -6.7 | 1e-09 | 32/48 (NCI-H1792, KATO III, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.487×** | -6.6 | 2e-09 | 29/48 (NCI-H460, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.493×** | -6.5 | 5e-09 | 36/48 (NCI-H1792, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.718×** | -6.3 | 2e-08 | 26/48 (AsPC-1, SNU-423, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.545×** | -5.6 | 1e-06 | 32/48 (NCI-H460, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.767×** | -4.8 | 6e-05 | 22/48 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.775×** | -4.8 | 6e-05 | 25/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.773×** | -4.5 | 2e-04 | 24/47 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 5 µM |  | 0.859× | -3.9 | 0.003 | 11/48 (HT-29, HCT15, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.816×** | -3.9 | 0.004 | 17/48 (SW1417, LS 180, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | **0.826×** | -3.6 | 0.008 | 10/48 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.826×** | -3.6 | 0.008 | 18/49 (HT-29, LS 180, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.026 | 11/46 (A498, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.847× | -3.2 | 0.037 | 15/49 (HT-29, A498, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.852× | -3.0 | 0.052 | 11/48 (HEC-1-A, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 61.9 | 5 (4 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -19.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 69.6 | 2 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.433× (z -11.1) |
| [[CFPAC-1 (line)]] | alt | 89.0 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -13.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 32.5 | 4 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +12.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.341× (z -9.5) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 86.2 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.253× (z -16.1) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 117 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0765× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.399× (z -8.7) |
| [[SW1417 (line)]] | alt | 97.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -12.1) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 117 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -12.3) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 48.0 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.0487× (z -23.1) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 69.8 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.73× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.296× (z -15.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.451× (z -9.8) |
| [[A-172 (line)]] | wt | 51.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.148× (z -16.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.307× (z -12.9) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 53.2 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.217× (z -13.3) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 60.6 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.8) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.0822× (z -27.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 71.8 | 3 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.23× (z +11.1) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.16× (z +10.9) | — |
| [[SNU-423 (line)]] | alt | 46.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -9.0) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 113 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0836× (z -13.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 41.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.50× (z +9.4) ⚠ toxic | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.319× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 102 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.95× (z +8.9) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 144 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.196× (z -11.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 103 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.287× (z -10.1) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 52.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.178× (z -14.1) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 86.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -11.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 44.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -9.5) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 57.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.254× (z -9.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 30.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[CHP-212 (line)]] | wt | 46.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0913× (z -10.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 39.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 90.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.216× (z -10.0) ⚠ toxic; transcription drop |
| [[NCI-H661 (line)]] | alt | 66.5 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.101× (z -9.9) |
| [[SNU-1 (line)]] | wt | 35.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +9.0) | — |
| [[SW48 (line)]] | wt | 58.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -12.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 74.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MKRN1]] | +0.65 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[ELF2]] | +0.62 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[YPEL2]] | +0.61 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[TMEM59]] | +0.60 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[UBR2]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SGK3]] | +0.60 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[IFT20]] | +0.59 | +0.51 / +0.61 | both halves | 1e-05 |  |
| [[MICA]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[CIR1]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[PDCL]] | +0.57 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[TFG]] | +0.57 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[IST1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEFSEC]] | -0.57 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.56 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[TMEM185B]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[EIF4G1]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[SMARCA4]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PURB]] | -0.55 | -0.45 / -0.58 | both halves | 3e-05 |  |
| [[BRD9]] | -0.55 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[ZNF121]] | -0.55 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 | same gene group |
| [[REXO1]] | -0.54 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[DDX10]] | -0.54 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[THOC6]] | -0.53 | -0.48 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.601). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.6, -41.2); signed map (-16.0, 11.1). **Vector** length 119, 35.6% of its response variance represented; |z| ≥ 3 in 1,431 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.9 | +6.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.6 | +4.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.3 | +5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.1 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +6.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.9 | +3.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -9.7 | -17.9 |
|  | [[EX229 (drug)]] 5 µM |  | -5.8 | -6.6 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.8 | -6.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.5 | -7.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -4.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.3 | -7.4 |

## What is on record

|  |  |
|---|---|
| Name | cytoplasmic polyadenylation element binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.32 — chr10:92,046,692-92,291,078 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0940 |
| Gene groups (HGNC) | RNA binding motif containing |
| Hallmark sets | KRAS_SIGNALING_DN |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NE35](https://www.uniprot.org/uniprotkb/Q8NE35) (Cytoplasmic polyadenylation element-binding protein 3):

> Sequence-specific RNA-binding protein which acts as a translational repressor in the basal unstimulated state but, following neuronal stimulation, acts as a translational activator (By similarity). In contrast to CPEB1, does not bind to the cytoplasmic polyadenylation element (CPE), a uridine-rich sequence element within the mRNA 3'-UTR, but binds to a U-rich loop within a stem-loop structure (By similarity). Required for the consolidation and maintenance of hippocampal-based long term memory …

**Summary**, from NCBI Gene [22849](https://www.ncbi.nlm.nih.gov/gene/22849):

> Enables mRNA 3'-UTR binding activity and translation factor activity, RNA binding. Involved in cellular response to amino acid stimulus and regulation of gene expression. Located in cytoplasm; neuron projection; and nucleus. Part of CCR4-NOT complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:21746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21746) · Entrez [22849](https://www.ncbi.nlm.nih.gov/gene/22849) · UniProt [Q8NE35](https://www.uniprot.org/uniprotkb/Q8NE35) · Ensembl [ENSG00000107864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107864)

## Data

Gene col 2891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2891); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2891]; `tensor/DDL_lfc|DDL_z.npy` [2891]; `embed/gene_vectors.npy` [2891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2891 or target_col == 2891). Every well: [[CPEB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CPEB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
