---
symbol: "ATG4C"
type: "gene"
col: 4646
ensembl_id: "ENSG00000125703"
name: "autophagy related 4C cysteine peptidase"
location: "1p31.3"
module: 65
arm: "+"
pooled_cpm: 26.62
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# ATG4C

*autophagy related 4C cysteine peptidase* — 1p31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.65× (z +21.7, q 0e+00, up in 46 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.269× (z -29.2, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARL6]] (+0.81, fdr 7e-06), [[HACE1]] (+0.81, fdr 7e-06), [[POT1]] (+0.79, fdr 7e-06); moves opposite to [[AKT1S1]] (-0.71, fdr 1e-05), [[MMADHC-DT]] (-0.71, fdr 1e-05), [[LINC00571]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PLEKHA6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4646.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.65×** | +21.7 | 0e+00 | 46/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +19.2 | 0e+00 | 45/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.28×** | +18.4 | 0e+00 | 46/47 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.75×** | +12.4 | 2e-33 | 42/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +11.4 | 8e-28 | 37/47 (NCI-H2347, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +8.7 | 2e-16 | 35/47 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.03×** | +8.2 | 1e-14 | 35/47 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.4 | 1e-11 | 28/47 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Afatinib (drug)]] 5 µM |  | **1.23×** | +4.6 | 2e-04 | 10/47 (SNU-423, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.16× | +4.6 | 3e-04 | 12/47 (KATO III, RPMI-7951, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.22×** | +4.4 | 6e-04 | 12/47 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.002 | 16/47 (HOP62, A-172, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.20×** | +4.1 | 0.002 | 11/47 (NCI-H2347, A-427, …) | all doses, stronger at high dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +4.0 | 0.003 | 5/47 (HOP62, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 15/46 (C32, NCI-H2347, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 15 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4646.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.269×** | -29.2 | 0e+00 | 45/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.272×** | -29.0 | 0e+00 | 39/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.343×** | -23.8 | 0e+00 | 44/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.426×** | -19.0 | 0e+00 | 43/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.560×** | -18.2 | 0e+00 | 34/46 (SW 900, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.492×** | -15.2 | 0e+00 | 36/46 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.511×** | -13.8 | 1e-41 | 27/41 (SW480, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -13.2 | 5e-38 | 37/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.585×** | -11.9 | 6e-31 | 28/43 (C32, C-33 A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.374×** | -11.4 | 1e-28 | 38/47 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.605×** | -11.2 | 2e-27 | 30/47 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.641×** | -9.9 | 2e-21 | 28/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.672×** | -8.9 | 4e-17 | 29/47 (SW480, RPMI-7951, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -7.2 | 3e-11 | 21/37 (SHP-77, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.585×** | -6.2 | 2e-08 | 14/29 (SW 900, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.777×** | -5.6 | 7e-07 | 19/47 (NCI-H460, HCT15, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.623×** | -5.5 | 1e-06 | 24/47 (RPMI-7951, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.787×** | -5.0 | 1e-05 | 21/47 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.818×** | -4.3 | 4e-04 | 15/46 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.874× | -4.2 | 5e-04 | 12/47 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.840× | -3.9 | 0.002 | 13/46 (HS-578T, RKO, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4646. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.3 | 2 | 13 (6 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.29× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.108× (z -25.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -22.0) |
| [[PANC-1 (line)]] | alt | 35.0 | 3 | 12 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.68× (z +12.1) | [[Digitoxin (drug)]] 5 µM 0.104× (z -27.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.127× (z -25.2) |
| [[SW480 (line)]] | alt | 27.7 | 3 | 7 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.79× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0473× (z -31.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.192× (z -18.5) |
| [[LS 180 (line)]] | wt | 24.4 | 3 | 6 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.77× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.0823× (z -19.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -13.9) |
| [[A498 (line)]] | wt | 21.8 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.00× (z +11.8) | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -12.7) |
| [[SW 900 (line)]] | alt | 29.8 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -20.1) |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.113× (z -17.1) |
| [[A-172 (line)]] | wt | 17.7 | 3 | 3 | [[Panobinostat (drug)]] 0.5 µM 5.24× (z +11.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -9.5) |
| [[H4 (line)]] | wt | 45.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.153× (z -12.5) |
| [[HS-578T (line)]] | alt | 35.3 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 23.1 | 0 | 6 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.247× (z -11.5) |
| [[SNU-1 (line)]] | wt | 28.1 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0267× (z -20.5) |
| [[Hs 766T (line)]] | wt | 26.5 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.96× (z +9.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.161× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 31.4 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -10.6) |
| [[A-427 (line)]] | wt | 40.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.523× (z -8.6) |
| [[C32 (line)]] | wt | 35.3 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0490× (z -21.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.193× (z -11.7) |
| [[J82 (line)]] | alt | 19.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -12.9) |
| [[LoVo (line)]] | wt | 19.6 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.269× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.82× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.285× (z -9.1) |
| [[NCI-H1573 (line)]] | alt | 23.5 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 3.16× (z +8.6) | [[Digitoxin (drug)]] 5 µM 0.207× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.225× (z -11.1) |
| [[SHP-77 (line)]] | alt | 56.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.141× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.323× (z -10.2) |
| [[SNU-423 (line)]] | alt | 19.1 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -9.7) |
| [[C-33 A (line)]] | alt | 49.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0938× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 18.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -9.7) |
| [[COLO 205 (line)]] | alt | 24.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -12.7) |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -12.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.0 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.38× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0838× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -12.4) |
| [[RKO (line)]] | wt | 21.3 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0472× (z -18.2) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.196× (z -10.1) |
| [[RPMI-7951 (line)]] | alt | 37.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.8) |
| [[A549 (line)]] | wt | 16.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.240× (z -9.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 29.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.96× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 22.7 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.110× (z -12.1) |
| [[LOX-IMVI (line)]] | wt | 27.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 17.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.156× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.441× (z -8.8) |
| [[SW48 (line)]] | wt | 29.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.130× (z -11.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0513× (z -12.2) |
| [[BT-474 (line)]] | alt | 11.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0670× (z -12.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.264× (z -10.4) |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.194× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -8.8) |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.294× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.182× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4646), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARL6]] | +0.81 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[HACE1]] | +0.81 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[POT1]] | +0.79 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.78 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.78 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[ANAPC4]] | +0.73 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[VDAC3]] | +0.73 | +0.66 / +0.58 | both halves | 8e-06 | pathway: Autophagy |
| [[ABHD10]] | +0.72 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[POGLUT2]] | +0.72 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[PRRC1]] | +0.71 | +0.62 / +0.50 | both halves | 1e-05 |  |
| [[MMS19]] | +0.71 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[SDHAF3]] | +0.70 | +0.51 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKT1S1]] | -0.71 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | -0.71 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[LINC00571]] | -0.70 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.70 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[PPP3CB-AS1]] | -0.69 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[PSMD6-AS1]] | -0.69 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[SPON1-AS1]] | -0.68 | -0.65 / -0.40 | both halves | 5e-05 |  |
| [[WSB2]] | -0.68 | -0.49 / -0.63 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | -0.67 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CDKN2B-AS1]] | -0.67 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.66 | -0.50 / -0.36 | both halves | 1e-04 |  |
| [[AVEN]] | -0.66 | -0.50 / -0.52 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEKHA6]] | B | PLEKHA6 activity lowers ATG4C's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.52× higher at baseline in the lines without PLEKHA6 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[GATA2-AS1]] | B | GATA2-AS1 activity raises ATG4C's level | lines that do not express GATA2-AS1 (10) vs lines expressing it (40) | 1.35× lower at baseline in the lines without GATA2-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GATA2 |
| [[HLTF]] | B | HLTF activity raises ATG4C's level | lines that do not express HLTF (8) vs lines expressing it (42) | 1.52× lower at baseline in the lines without HLTF | 0.027 | ⚠ within organs, on part of the lines; also absent: HDGFL3, ZNF512B, FERMT2 |
| [[ZHX2]] | B | ZHX2 activity lowers ATG4C's level | lines that do not express ZHX2 (7) vs lines expressing it (43) | 1.49× higher at baseline in the lines without ZHX2 | 0.077 | ⚠ within organs, on part of the lines; also absent: NIBAN2, SMOX, NDRG1 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers ATG4C's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers ATG4C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[POGLUT2]] | C | POGLUT2 activity raises ATG4C's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[WARS2-AS1]] | C | WARS2-AS1 activity raises ATG4C's level | lines that do not express WARS2-AS1 (3) vs lines expressing it (47) | 2.11× lower at baseline in the lines without WARS2-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: WWOX, MPP4, CDHR3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.831). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (3.0, -10.7); signed map (-32.9, -7.9). **Vector** length 87.1, 21.5% of its response variance represented; |z| ≥ 3 in 1,334 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +4.4 | +18.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | +21.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.8 | +12.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +19.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +11.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +8.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +4.6 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +3.8 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.8 | +0.7 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.2 | -13.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -18.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -7.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.6 | -19.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -4.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.9 | -8.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.5 | -1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | autophagy related 4C cysteine peptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p31.3 — chr1:62,784,132-62,865,516 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14867, AUTL3; previously AUTL1, APG4C |
| Gene groups (HGNC) | Autophagy related; Autophagy related 4 family cysteine peptidases |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DT6](https://www.uniprot.org/uniprotkb/Q96DT6) (Cysteine protease ATG4C):

> Cysteine protease that plays a key role in autophagy by mediating both proteolytic activation and delipidation of ATG8 family proteins. The protease activity is required for proteolytic activation of ATG8 family proteins: cleaves the C-terminal amino acid of ATG8 proteins MAP1LC3 and GABARAPL2, to reveal a C-terminal glycine. Exposure of the glycine at the C-terminus is essential for ATG8 proteins conjugation to phosphatidylethanolamine (PE) and insertion to membranes, which is necessary for …

**Summary**, from NCBI Gene [84938](https://www.ncbi.nlm.nih.gov/gene/84938):

> Autophagy is the process by which endogenous proteins and damaged organelles are destroyed intracellularly. Autophagy is postulated to be essential for cell homeostasis and cell remodeling during differentiation, metamorphosis, non-apoptotic cell death, and aging. Reduced levels of autophagy have been described in some malignant tumors, and a role for autophagy in controlling the unregulated cell growth linked to cancer has been proposed. This gene encodes a member of the autophagin protein …

**Accessions** — [HGNC:16040](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16040) · Entrez [84938](https://www.ncbi.nlm.nih.gov/gene/84938) · UniProt [Q96DT6](https://www.uniprot.org/uniprotkb/Q96DT6) · Ensembl [ENSG00000125703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125703)

## Data

Gene col 4646: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4646); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4646, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4646]; `tensor/DDL_lfc|DDL_z.npy` [4646]; `embed/gene_vectors.npy` [4646]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4646 or target_col == 4646). Every well: [[ATG4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATG4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
