---
symbol: "MAP2K5"
type: "gene"
col: 6061
ensembl_id: "ENSG00000137764"
name: "mitogen-activated protein kinase kinase 5"
location: "15q23"
module: 74
arm: "+"
pooled_cpm: 105.05
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 49
n_dd_up_clean: 5
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# MAP2K5

*mitogen-activated protein kinase kinase 5* — 15q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.31× (z +5.5, q 3e-05, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (22 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.445× (z -24.1, q 0e+00, down in 44 of 48 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.349× (z -21.3, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BCAS3]] (+0.61, fdr 1e-05), [[SNX13]] (+0.59, fdr 1e-05), [[NIPBL]] (+0.58, fdr 3e-05); moves opposite to [[CEP295NL]] (-0.59, fdr 1e-05), [[NES]] (-0.52, fdr 2e-05), [[ZNF697]] (-0.52, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6061.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +5.5 | 3e-05 | 30/47 (SW480, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.27×** | +4.9 | 3e-04 | 30/50 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.5 | 0.001 | 29/48 (KATO III, J82, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +4.2 | 0.003 | 16/48 (SW480, SHP-77, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.21×** | +4.1 | 0.005 | 20/48 (A498, A549, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.16× | +4.0 | 0.006 | 15/49 (SW480, NCI-H2347, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.15× | +3.9 | 0.008 | 14/48 (SW480, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.012 | 18/48 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.019 | 13/48 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | 1.17× | +3.6 | 0.019 | 19/49 (SW480, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.023 | 19/48 (KATO III, SW480, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.35×** | +3.3 | 0.038 | 18/50 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.038 | 16/48 (SW480, RKO, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.038 | 16/48 (SW480, C32, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.046 | 15/47 (SW480, C32, …) | rises with dose |  |
| [[RMC-6236 (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.089 | 11/48 (SW480, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 54 in all, 23 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 22 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6061.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.445×** | -24.1 | 0e+00 | 44/48 (PANC-1, C32, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.360×** | -21.5 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.349×** | -21.3 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.380×** | -20.4 | 0e+00 | 45/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.382×** | -20.3 | 0e+00 | 46/49 (CHP-212, NCI-H23, …) | all doses, flat | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.402×** | -19.2 | 0e+00 | 44/48 (SW480, C32, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.430×** | -17.8 | 0e+00 | 46/48 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.417×** | -17.7 | 0e+00 | 42/44 (PANC-1, AN3 CA, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.436×** | -17.5 | 0e+00 | 47/48 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.414×** | -17.2 | 0e+00 | 41/45 (SW480, A549, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.447×** | -16.9 | 0e+00 | 45/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.461×** | -16.3 | 0e+00 | 46/48 (SW480, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.524×** | -13.1 | 2e-37 | 44/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.530×** | -12.8 | 1e-35 | 46/48 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -12.6 | 1e-34 | 39/48 (PANC-1, C32, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -11.1 | 3e-27 | 43/49 (LOX-IMVI, NCI-H460, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.370×** | -11.0 | 2e-26 | 42/49 (PANC-1, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -10.0 | 5e-22 | 40/48 (PANC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.668×** | -8.5 | 7e-16 | 36/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.790×** | -7.0 | 9e-11 | 28/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.540×** | -6.8 | 3e-10 | 40/48 (PANC-1, CHP-212, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.552×** | -6.5 | 2e-09 | 41/48 (Hs 766T, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.654×** | -6.4 | 4e-09 | 44/48 (PANC-1, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.744×** | -6.2 | 1e-08 | 30/48 (KATO III, SW480, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.591×** | -5.8 | 2e-07 | 34/48 (NCI-H460, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.596×** | -5.7 | 2e-07 | 33/48 (NCI-H460, COLO 205, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.40 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6061. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 115 | 0 | 23 (16 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -26.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.153× (z -25.0) |
| [[PANC-1 (line)]] | alt | 113 | 0 | 22 (14 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -33.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.159× (z -28.3) |
| [[NCI-H1573 (line)]] | alt | 183 | 0 | 18 (13 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.314× (z -17.6) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.337× (z -16.6) |
| [[LOX-IMVI (line)]] | wt | 157 | 0 | 17 (14 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -20.3) |
| [[C32 (line)]] | wt | 130 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -28.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.193× (z -19.9) |
| [[LoVo (line)]] | wt | 207 | 0 | 16 (11 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.275× (z -19.3) |
| [[SW480 (line)]] | alt | 84.3 | 0 | 15 (11 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -25.7) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.223× (z -22.1) |
| [[SNU-423 (line)]] | alt | 76.9 | 0 | 14 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -28.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -16.3) |
| [[KATO III (line)]] | alt | 113 | 0 | 13 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.162× (z -22.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.297× (z -14.7) |
| [[MIA PaCa-2 (line)]] | alt | 90.5 | 0 | 13 (8 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -21.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.238× (z -15.0) |
| [[NCI-H23 (line)]] | alt | 138 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -20.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.281× (z -16.3) |
| [[A549 (line)]] | wt | 128 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -27.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.113× (z -24.8) |
| [[HT-29 (line)]] | alt | 75.9 | 0 | 12 (9 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -20.5) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.248× (z -14.8) |
| [[LS 180 (line)]] | wt | 121 | 0 | 12 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.167× (z -22.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.264× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 12 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.212× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.230× (z -18.5) |
| [[HCT15 (line)]] | alt | 122 | 0 | 11 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -11.5) |
| [[Hs 766T (line)]] | wt | 73.1 | 0 | 11 (9 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.269× (z -11.8) ⚠ unreliable plate only · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.392× (z -8.8) |
| [[J82 (line)]] | alt | 73.5 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -20.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.272× (z -12.4) |
| [[SNU-1 (line)]] | wt | 142 | 0 | 11 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.281× (z -11.9) |
| [[A-172 (line)]] | wt | 82.1 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -22.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -14.0) |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -25.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.205× (z -15.3) |
| [[SW 900 (line)]] | alt | 73.8 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -19.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.156× (z -16.2) |
| [[SW1417 (line)]] | alt | 95.0 | 0 | 9 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -17.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.389× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -18.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.407× (z -12.1) |
| [[HOP62 (line)]] | alt | 83.4 | 0 | 8 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -15.1) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 171 | 0 | 8 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.224× (z -13.6) |
| [[RKO (line)]] | wt | 94.1 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[SHP-77 (line)]] | alt | 101 | 0 | 8 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.353× (z -11.9) |
| [[COLO 205 (line)]] | alt | 119 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.229× (z -15.2) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.346× (z -11.0) |
| [[SW48 (line)]] | wt | 123 | 0 | 7 (6 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.228× (z -12.9) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.307× (z -10.3) |
| [[A-427 (line)]] | wt | 71.6 | 0 | 6 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -15.8) |
| [[A498 (line)]] | wt | 61.2 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -27.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.141× (z -20.0) |
| [[Panc 03.27 (line)]] | alt | 104 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.355× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 147 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 105 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -27.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.218× (z -15.8) |
| [[AN3 CA (line)]] | alt | 146 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0684× (z -18.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.159× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 86.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -18.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.326× (z -11.1) |
| [[HS-578T (line)]] | alt | 56.2 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -14.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.270× (z -12.1) |
| [[C-33 A (line)]] | alt | 142 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.280× (z -14.7) |
| [[AsPC-1 (line)]] | alt | 43.8 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.232× (z -10.8) ⚠ cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 47.2 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.241× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.300× (z -9.0) |
| [[H4 (line)]] | wt | 92.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.334× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 74.2 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.187× (z -13.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0373× (z -22.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW 1271 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0364× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 55.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.535× (z -8.9) |
| [[SW 1088 (line)]] | alt | 85.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0775× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6061), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCAS3]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[SNX13]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[NIPBL]] | +0.58 | +0.45 / +0.55 | both halves | 3e-05 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[BRWD1]] | +0.58 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[ARID1B]] | +0.57 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[CTPS2]] | +0.57 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[TBC1D5]] | +0.56 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TDRD3]] | +0.55 | +0.67 / +0.49 | both halves | 1e-05 |  |
| [[SETD2]] | +0.55 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[TBCK]] | +0.55 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[NCOR1]] | +0.55 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TNKS]] | +0.55 | +0.39 / +0.60 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEP295NL]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NES]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[ZNF697]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ACTN1]] | -0.52 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[CACNB1]] | -0.51 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[TRPV2]] | -0.51 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[DCBLD2]] | -0.50 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[CDC42EP2]] | -0.50 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[ANXA5]] | -0.49 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[CORO1C]] | -0.48 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[GDPD5]] | -0.47 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[CCNYL1]] | -0.47 | -0.48 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-24.1, 29.7); signed map (6.3, -13.9). **Vector** length 81.0, 29.4% of its response variance represented; |z| ≥ 3 in 1,749 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +5.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.5 | +2.6 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.3 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.3 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.2 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +3.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -7.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.5 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | -4.7 | -17.2 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -19.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.4 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.1 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q23 — chr15:67,542,703-67,807,117 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MEK5, MAPKK5, HsT17454; previously PRKMK5 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 3 pathways, smallest: Signaling by NTRK1 (TRKA); Signaling by NTRKs; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13163](https://www.uniprot.org/uniprotkb/Q13163) (Dual specificity mitogen-activated protein kinase kinase 5):

> Acts as a scaffold for the formation of a ternary MAP3K2/MAP3K3-MAP3K5-MAPK7 signaling complex. Activation of this pathway appears to play a critical role in protecting cells from stress-induced apoptosis, neuronal survival and cardiac development and angiogenesis. As part of the MAPK/ERK signaling pathway, acts as a negative regulator of apoptosis in cardiomyocytes via promotion of STUB1/CHIP-mediated ubiquitination and degradation of ICER-type isoforms of CREM (By similarity).

**Summary**, from NCBI Gene [5607](https://www.ncbi.nlm.nih.gov/gene/5607):

> The protein encoded by this gene is a dual specificity protein kinase that belongs to the MAP kinase kinase family. This kinase specifically interacts with and activates MAPK7/ERK5. This kinase itself can be phosphorylated and activated by MAP3K3/MEKK3, as well as by atypical protein kinase C isoforms (aPKCs). The signal cascade mediated by this kinase is involved in growth factor stimulated cell proliferation and muscle cell differentiation. Three alternatively spliced transcript variants of …

**Accessions** — [HGNC:6845](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6845) · Entrez [5607](https://www.ncbi.nlm.nih.gov/gene/5607) · UniProt [Q13163](https://www.uniprot.org/uniprotkb/Q13163) · Ensembl [ENSG00000137764](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137764)

## Data

Gene col 6061: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6061); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6061, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6061]; `tensor/DDL_lfc|DDL_z.npy` [6061]; `embed/gene_vectors.npy` [6061]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6061 or target_col == 6061). Every well: [[MAP2K5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
