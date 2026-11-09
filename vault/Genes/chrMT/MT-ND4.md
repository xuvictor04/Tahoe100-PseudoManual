---
symbol: "MT-ND4"
type: "gene"
col: 12720
ensembl_id: "ENSG00000198886"
name: "mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 4"
location: "mitochondria"
module: null
arm: null
pooled_cpm: 1866.13
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 11
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: false
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "noise-rna", "not-in-vector-space"]
generated_by: "tahoemap"
---

# MT-ND4

*mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 4* — mitochondria

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.52× (z +12.0, q 2e-30, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW480 4.31×, MIA PaCa-2 4.50×, NCI-H460 4.02×, LoVo 4.70×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 5.66×, SNU-1 6.50×, SW480 5.31×, NCI-H1573 5.15×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 4.14×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 0.05 µM: 0.185× (z -16.8, q 0e+00, down in 48 of 48 measured lines) ⚠ transcription drop. The strongest without an alert is [[Pentamidine (isethionate) (drug)]] 5 µM: 0.383× (z -13.5, q 5e-39, down in 45 of 48 measured lines).
> It is not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). So it has no partners and no module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12720.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 9 lines (SW480 4.31×, MIA PaCa-2 4.50×, NCI-H460 4.02×, LoVo 4.70×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (NCI-H460 5.66×, SNU-1 6.50×, SW480 5.31×, NCI-H1573 5.15×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (Panc 03.27 4.14×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.52×** | +12.0 | 2e-30 | 44/44 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +11.8 | 1e-29 | 49/49 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +10.6 | 8e-24 | 45/45 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.2 | 0.004 | 40/47 (MIA PaCa-2, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 1.80× | +3.0 | 0.28 | 26/38 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12720.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.185×** | -16.8 | 0e+00 | 48/48 (SK-MEL-2, A-427, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pentamidine (isethionate) (drug)]] 5 µM |  | **0.383×** | -13.5 | 5e-39 | 45/48 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.421×** | -8.6 | 1e-15 | 42/48 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.438×** | -8.2 | 3e-14 | 43/48 (RKO, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.568×** | -8.0 | 2e-13 | 44/49 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.469×** | -7.5 | 5e-12 | 41/48 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -6.1 | 1e-07 | 38/48 (RKO, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[crizotinib (drug)]] 5 µM |  | **0.620×** | -4.6 | 3e-04 | 44/48 (SK-MEL-2, H4, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | **0.725×** | -4.6 | 3e-04 | 41/49 (A498, SHP-77, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.711×** | -3.4 | 0.036 | 32/48 (H4, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **0.705×** | -3.4 | 0.040 | 38/48 (H4, SHP-77, …) | top dose only | plate-row cell shift; position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.739× | -3.0 | 0.12 | 37/47 (RKO, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12720. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 1,508 | 3 (3 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.22× (z +11.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.184× (z -20.3) |
| [[Hs 766T (line)]] | wt | 1,934 | 3 (3 ⚠) | 7 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +8.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.164× (z -24.1) |
| [[HOP62 (line)]] | alt | 1,117 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.47× (z +11.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.253× (z -16.1) |
| [[NCI-H460 (line)]] | wt | 2,151 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.02× (z +12.8) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.155× (z -25.2) |
| [[SW 900 (line)]] | alt | 1,755 | 3 (3 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +10.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.225× (z -19.0) |
| [[SHP-77 (line)]] | alt | 3,268 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +10.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.140× (z -19.3) ⚠ transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.308× (z -11.5) |
| [[SW480 (line)]] | alt | 1,679 | 3 (3 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.31× (z +13.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.158× (z -17.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.333× (z -14.4) |
| [[C-33 A (line)]] | alt | 1,191 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.169× (z -13.7) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.330× (z -12.1) |
| [[C32 (line)]] | wt | 1,522 | 2 (2 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.53× (z +11.0) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.191× (z -15.2) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.371× (z -12.9) |
| [[SNU-1 (line)]] | wt | 1,148 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 6.50× (z +12.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.223× (z -18.2) |
| [[SW 1271 (line)]] | alt | 973 | 1 (1 ⚠) | 6 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +9.1) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.196× (z -16.5) |
| [[SW1417 (line)]] | alt | 1,959 | 3 (3 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +9.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.184× (z -16.0) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.354× (z -9.8) |
| [[A498 (line)]] | wt | 2,586 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.02× (z +11.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.232× (z -17.5) |
| [[A549 (line)]] | wt | 2,018 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.12× (z +11.5) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.181× (z -20.6) |
| [[HS-578T (line)]] | alt | 1,345 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.89× (z +11.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.300× (z -14.6) |
| [[hTERT-HPNE (line)]] | wt | 1,005 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.06× (z +11.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.302× (z -10.2) |
| [[LS 180 (line)]] | wt | 1,701 | 3 (3 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +10.5) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.174× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 1,390 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.50× (z +12.9) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.153× (z -23.7) |
| [[NCI-H1573 (line)]] | alt | 2,095 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +11.7) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.199× (z -21.4) |
| [[PANC-1 (line)]] | alt | 2,474 | 3 (3 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.59× (z +11.4) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.201× (z -21.0) |
| [[RKO (line)]] | wt | 2,236 | 1 (1 ⚠) | 5 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.195× (z -15.5) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -15.1) |
| [[A-172 (line)]] | wt | 1,358 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.07× (z +11.2) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.313× (z -13.6) |
| [[AN3 CA (line)]] | alt | 1,959 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.73× (z +9.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.145× (z -16.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.360× (z -12.0) |
| [[BT-474 (line)]] | alt | 2,757 | 0 | 5 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.162× (z -16.5) ⚠ transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.326× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 953 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.56× (z +10.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.430× (z -10.1) |
| [[COLO 205 (line)]] | alt | 1,454 | 1 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +10.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -14.9) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.252× (z -12.0) |
| [[HT-29 (line)]] | alt | 1,203 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.94× (z +11.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.258× (z -12.4) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.395× (z -8.5) |
| [[KATO III (line)]] | alt | 2,480 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.39× (z +11.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.164× (z -17.3) ⚠ transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.308× (z -11.3) |
| [[LoVo (line)]] | wt | 1,609 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.70× (z +12.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.180× (z -14.4) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.292× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 2,612 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.39× (z +9.6) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.165× (z -21.7) |
| [[A-427 (line)]] | wt | 4,151 | 0 | 4 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -20.0) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.291× (z -15.4) |
| [[CHP-212 (line)]] | wt | 1,118 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.47× (z +10.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.192× (z -11.7) ⚠ transcription drop |
| [[HCT15 (line)]] | alt | 1,341 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.43× (z +10.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.229× (z -11.2) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.234× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 1,655 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.21× (z +10.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.194× (z -13.6) ⚠ transcription drop |
| [[J82 (line)]] | alt | 1,510 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.08× (z +9.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.192× (z -14.1) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.473× (z -9.1) |
| [[LOX-IMVI (line)]] | wt | 1,090 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.80× (z +12.3) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.209× (z -12.8) ⚠ transcription drop |
| [[NCI-H1792 (line)]] | alt | 1,108 | 2 (2 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +10.3) ⚠ toxic; transcription drop | [[Pentamidine (isethionate) (drug)]] 5 µM 0.268× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 1,433 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.25× (z +9.9) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.161× (z -16.7) ⚠ transcription drop |
| [[Panc 03.27 (line)]] | alt | 1,103 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 4.14× (z +11.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.275× (z -11.3) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 1,850 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.92× (z +11.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.208× (z -14.2) ⚠ transcription drop |
| [[AsPC-1 (line)]] | alt | 1,393 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.51× (z +9.8) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.234× (z -11.7) ⚠ transcription drop |
| [[NCI-H23 (line)]] | alt | 4,032 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.124× (z -19.5) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.364× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 2,594 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 3.05× (z +10.2) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.0973× (z -23.2) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 2,333 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.69× (z +8.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.151× (z -16.9) ⚠ transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.387× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 1,334 | 0 | 2 (1 ⚠) | — | [[Pentamidine (isethionate) (drug)]] 5 µM 0.306× (z -13.4) |
| [[NCI-H661 (line)]] | alt | 2,045 | 0 | 2 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.186× (z -11.4) ⚠ transcription drop · without an alert: [[Pentamidine (isethionate) (drug)]] 5 µM 0.340× (z -10.3) |
| [[RPMI-7951 (line)]] | alt | 987 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.18× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 1,242 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +8.5) ⚠ toxic; transcription drop | [[Docetaxel (drug)]] 0.05 µM 0.246× (z -8.8) ⚠ transcription drop |
| [[NCI-H2122 (line)]] | alt | 1,661 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 1,924 | 0 | 0 | — | — |

## Genes that move with it

Not in the vector space, so no gene relations.

## Genes that move opposite

Not in the vector space, so no gene relations.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

Not in the vector space: it is a noise-class RNA (snoRNA, mitochondrial, histone, ribosomal pseudogene or ENSG-only name). Its drug and cell-line tables above are complete all the same.

## What is on record

|  |  |
|---|---|
| Name | mitochondrially encoded NADH:ubiquinone oxidoreductase core subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | mitochondria — chrMT:10,760-12,137 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ND4, NAD4; previously MTND4, LHON |
| Gene groups (HGNC) | NADH:ubiquinone oxidoreductase core subunits; Mitochondrially encoded protein coding genes |
| Reactome | 16 pathways, smallest: FASTK family proteins regulate processing and stability of mitochondrial RNAs; tRNA processing in the mitochondrion; Mitochondrial mRNA modification |
| Matched by | ensembl_id |

**Function**, from UniProt [C0HME5](https://www.uniprot.org/uniprotkb/C0HME5) (Mitochondrial alternative ND4 protein):

> Regulates mitochondrial respiration by decreasing oxygen consumption. Also regulates reactive oxygen species homeostasis.

**Summary**, from NCBI Gene [4538](https://www.ncbi.nlm.nih.gov/gene/4538):

> Enables NADH dehydrogenase (ubiquinone) activity. Involved in mitochondrial electron transport, NADH to ubiquinone and mitochondrial respiratory chain complex I assembly. Located in mitochondrial inner membrane. Part of respiratory chain complex I. Implicated in Leber hereditary optic neuropathy; Parkinson's disease; macular degeneration; and schizophrenia. Biomarker of Alzheimer's disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7459) · Entrez [4538](https://www.ncbi.nlm.nih.gov/gene/4538) · UniProt [C0HME5](https://www.uniprot.org/uniprotkb/C0HME5) · Ensembl [ENSG00000198886](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198886)

## Data

Gene col 12720: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12720); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12720, 0 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12720]; `tensor/DDL_lfc|DDL_z.npy` [12720]; `embed/gene_vectors.npy` [12720]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12720 or target_col == 12720). Every well: [[MT-ND4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT-ND4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
