---
symbol: "CBR4"
type: "gene"
col: 6994
ensembl_id: "ENSG00000145439"
name: "carbonyl reductase 4"
location: "4q32.3"
module: 15
arm: "+"
pooled_cpm: 61.69
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# CBR4

*carbonyl reductase 4* — 4q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.69× (z +15.7, q 0e+00, up in 38 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.351× (z -22.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 17 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSDL2-AS1]] (+0.63, fdr 1e-05), [[POLR1HASP]] (+0.62, fdr 1e-05), [[C2orf76]] (+0.60, fdr 3e-05); moves opposite to [[DNAJB1]] (-0.56, fdr 7e-05), [[GPRIN1]] (-0.54, fdr 2e-04), [[RAB39A]] (-0.52, fdr 6e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6994.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.69×** | +15.7 | 0e+00 | 38/49 (AsPC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.11×** | +15.2 | 0e+00 | 44/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +11.6 | 9e-29 | 43/50 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.37×** | +9.5 | 5e-19 | 39/48 (J82, RKO, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +9.4 | 7e-19 | 31/48 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +7.4 | 2e-11 | 37/48 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +7.0 | 2e-10 | 25/42 (AsPC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.26×** | +6.9 | 5e-10 | 31/48 (HEC-1-A, SW1417, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.36×** | +6.5 | 4e-09 | 32/48 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +5.3 | 7e-06 | 22/48 (A498, SW1417, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.26×** | +4.9 | 5e-05 | 24/48 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +4.4 | 4e-04 | 23/48 (KATO III, A-172, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.22×** | +4.0 | 0.003 | 22/47 (A-172, SW480, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.004 | 19/49 (SW480, NCI-H1792, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.17× | +3.2 | 0.047 | 12/48 (KATO III, SNU-423, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.064 | 7/48 (CFPAC-1, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.1 | 0.064 | 6/48 (HEC-1-A, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6994.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.351×** | -22.1 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.408×** | -18.9 | 0e+00 | 46/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.413×** | -18.7 | 0e+00 | 46/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.464×** | -16.2 | 0e+00 | 47/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.546×** | -12.8 | 2e-35 | 43/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.566×** | -11.5 | 8e-29 | 34/47 (LoVo, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.584×** | -11.3 | 7e-28 | 40/48 (PANC-1, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.388×** | -10.4 | 1e-23 | 45/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -9.3 | 9e-19 | 39/48 (MIA PaCa-2, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.703×** | -7.2 | 5e-11 | 32/48 (PANC-1, RPMI-7951, …) | rises with dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.717×** | -6.6 | 2e-09 | 35/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.553×** | -6.5 | 3e-09 | 27/45 (PANC-1, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.765×** | -5.6 | 7e-07 | 26/48 (SW480, NCI-H23, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.720×** | -4.6 | 1e-04 | 23/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.865× | -4.3 | 6e-04 | 6/49 (CFPAC-1, C32, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.829×** | -4.0 | 0.002 | 18/48 (CFPAC-1, HS-578T, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.769×** | -4.0 | 0.002 | 19/49 (PANC-1, SHP-77, …) | all doses, flat | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.003 | 14/48 (Hs 766T, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.857× | -3.3 | 0.029 | 15/47 (LOX-IMVI, NCI-H2030, …) | two highest doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.853× | -3.2 | 0.031 | 13/48 (NCI-H460, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6994. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 66.0 | 0 | 11 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -28.0) |
| [[SW480 (line)]] | alt | 75.5 | 3 | 7 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.16× (z +15.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -25.6) |
| [[NCI-H460 (line)]] | wt | 49.7 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.298× (z -14.4) |
| [[J82 (line)]] | alt | 46.2 | 1 (1 ⚠) | 6 (2 ⚠) | [[Selinexor (drug)]] 5 µM 1.98× (z +9.1) ⚠ cell-cycle shift, explains ~45% of this change | [[Digitoxin (drug)]] 5 µM 0.234× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -13.7) |
| [[LoVo (line)]] | wt | 86.6 | 2 (1 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.24× (z +15.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.86× (z +11.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.242× (z -18.1) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.303× (z -15.9) |
| [[MIA PaCa-2 (line)]] | alt | 47.9 | 3 | 4 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.46× (z +13.3) | [[PH-797804 (drug)]] 5 µM 0.0980× (z -11.2) |
| [[COLO 205 (line)]] | alt | 96.0 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.174× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.290× (z -12.3) |
| [[HEC-1-A (line)]] | alt | 74.0 | 3 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +13.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.360× (z -11.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.406× (z -10.6) |
| [[HOP62 (line)]] | alt | 72.1 | 1 | 5 (2 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.63× (z +12.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.206× (z -16.4) |
| [[HT-29 (line)]] | alt | 44.8 | 3 | 3 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +12.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.318× (z -11.0) |
| [[LS 180 (line)]] | wt | 78.4 | 2 | 4 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +9.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -18.1) |
| [[HCT15 (line)]] | alt | 84.4 | 0 | 5 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.239× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 94.9 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.348× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 65.8 | 3 | 2 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +12.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.423× (z -8.7) |
| [[RKO (line)]] | wt | 52.2 | 3 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.0) | [[Digitoxin (drug)]] 5 µM 0.150× (z -16.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 92.3 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.505× (z -9.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.398× (z -9.4) |
| [[A498 (line)]] | wt | 57.7 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.48× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.552× (z -9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.443× (z -9.2) |
| [[H4 (line)]] | wt | 64.2 | 1 | 3 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +8.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 64.4 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.173× (z -13.4) |
| [[Hs 766T (line)]] | wt | 71.9 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +11.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.385× (z -9.6) |
| [[KATO III (line)]] | alt | 82.7 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.146× (z -21.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -15.2) |
| [[AN3 CA (line)]] | alt | 90.5 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0573× (z -15.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.136× (z -11.5) |
| [[AsPC-1 (line)]] | alt | 26.3 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +16.7) | — |
| [[BT-474 (line)]] | alt | 64.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.182× (z -13.4) |
| [[C32 (line)]] | wt | 119 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 49.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +13.8) | — |
| [[NCI-H23 (line)]] | alt | 47.9 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.09× (z +9.8) | [[Digitoxin (drug)]] 0.5 µM 0.294× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 78.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.406× (z -9.8) |
| [[SNU-423 (line)]] | alt | 44.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -12.5) |
| [[SW 900 (line)]] | alt | 36.6 | 1 | 2 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +8.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.247× (z -10.0) |
| [[A-427 (line)]] | wt | 42.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.405× (z -8.6) |
| [[C-33 A (line)]] | alt | 101 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.230× (z -13.4) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 109 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -8.5) |
| [[HS-578T (line)]] | alt | 42.1 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.268× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.321× (z -9.0) |
| [[hTERT-HPNE (line)]] | wt | 59.1 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.263× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 52.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +12.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +9.4) | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 2 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.303× (z -10.3) |
| [[SW1417 (line)]] | alt | 49.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +15.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.350× (z -10.9) |
| [[A549 (line)]] | wt | 40.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H596 (line)]] | alt | 65.7 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 5 µM 0.117× (z -9.3) |
| [[SHP-77 (line)]] | alt | 42.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.299× (z -9.9) |
| [[SNU-1 (line)]] | wt | 46.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.190× (z -10.5) |
| [[SW 1271 (line)]] | alt | 57.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0595× (z -10.6) |
| [[SW48 (line)]] | wt | 56.7 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 81.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6994), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSDL2-AS1]] | +0.63 | +0.68 / +0.52 | both halves | 1e-05 |  |
| [[POLR1HASP]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[C2orf76]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[RNF170]] | +0.60 | +0.61 / +0.36 | both halves | 9e-05 |  |
| [[MAILR]] | +0.59 | +0.73 / +0.38 | both halves | 7e-05 |  |
| [[SLC30A9]] | +0.58 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[TBCK]] | +0.57 | +0.63 / +0.40 | both halves | 4e-05 |  |
| [[TRIM66]] | +0.56 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[TP53]] | +0.56 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[SMIM19]] | +0.56 | +0.62 / +0.30 | both halves | 2e-04 |  |
| [[TRAPPC6B]] | +0.55 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[LINC01376]] | +0.55 | +0.64 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB1]] | -0.56 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[GPRIN1]] | -0.54 | -0.46 / -0.32 | both halves | 2e-04 |  |
| [[RAB39A]] | -0.52 | -0.38 / -0.41 | both halves | 6e-05 |  |
| [[ETNK2]] | -0.51 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[SIPA1]] | -0.51 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[CAMK2G]] | -0.51 | -0.61 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[GIPC1]] | -0.51 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[TSPAN33]] | -0.50 | -0.44 / -0.11 | ⚠ not reproduced | 0.002 |  |
| [[SLC39A3]] | -0.50 | -0.37 / -0.26 | both halves | 3e-04 |  |
| [[GPR153]] | -0.49 | -0.31 / -0.35 | both halves | 2e-04 |  |
| [[NAA40]] | -0.49 | -0.46 / -0.23 | both halves | 5e-04 |  |
| [[MAST3]] | -0.49 | -0.50 / -0.15 | ⚠ one half (not replicated) | 0.001 |  |
| [[SNN]] | -0.49 | -0.41 / -0.22 | both halves | 6e-04 |  |
| [[PRR5]] | -0.49 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[ZDHHC18]] | -0.49 | -0.40 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CBR4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.477). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.3, 20.1); signed map (24.3, -10.7). **Vector** length 70.6, 17.6% of its response variance represented; |z| ≥ 3 in 1,331 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +15.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +3.0 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.0 | +2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +6.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -4.9 | -12.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.8 | +7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -5.6 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -4.7 | -6.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.4 | -6.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -11.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | +2.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | carbonyl reductase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.3 — chr4:168,863,770-169,010,275 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14431, SDR45C1 |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: Fatty acyl-CoA biosynthesis; Fatty acid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4T8](https://www.uniprot.org/uniprotkb/Q8N4T8) (3-oxoacyl-[acyl-carrier-protein] reductase):

> Component of the heterotetramer complex KAR (3-ketoacyl-[acyl carrier protein] reductase or 3-ketoacyl-[ACP] reductase) that forms part of the mitochondrial fatty acid synthase (mtFAS). Beta-subunit of the KAR heterotetramer complex, responsible for the 3-ketoacyl-ACP reductase activity of the mtFAS, reduces 3-oxoacyl-[ACP] to (3R)-hydroxyacyl-[ACP] in a NADPH-dependent manner with no chain length preference, thereby participating in mitochondrial fatty acid biosynthesis. The homotetramer has …

**Summary**, from NCBI Gene [84869](https://www.ncbi.nlm.nih.gov/gene/84869):

> Enables several functions, including 3-oxoacyl-[acyl-carrier-protein] reductase (NADPH) activity; NADPH binding activity; and NADPH dehydrogenase (quinone) activity. Involved in several processes, including daunorubicin metabolic process; doxorubicin metabolic process; and protein tetramerization. Located in mitochondrial matrix. Part of oxidoreductase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25891](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25891) · Entrez [84869](https://www.ncbi.nlm.nih.gov/gene/84869) · UniProt [Q8N4T8](https://www.uniprot.org/uniprotkb/Q8N4T8) · Ensembl [ENSG00000145439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145439)

## Data

Gene col 6994: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6994); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6994, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6994]; `tensor/DDL_lfc|DDL_z.npy` [6994]; `embed/gene_vectors.npy` [6994]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6994 or target_col == 6994). Every well: [[CBR4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBR4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
