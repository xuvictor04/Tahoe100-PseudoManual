---
symbol: "GOLGA4"
type: "gene"
col: 6914
ensembl_id: "ENSG00000144674"
name: "golgin A4"
location: "3p22.2"
module: 41
arm: "+"
pooled_cpm: 778.16
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# GOLGA4

*golgin A4* — 3p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.04× (z +16.3, q 0e+00, up in 46 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.69× (z +8.5, q 6e-15, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.484× (z -11.2, q 1e-26, down in 46 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.702× (z -8.0, q 2e-13, down in 42 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMF1]] (+0.76, fdr 7e-06), [[GOLGA2]] (+0.72, fdr 7e-06), [[UFL1]] (+0.69, fdr 7e-06); moves opposite to [[NUP50]] (-0.61, fdr 1e-05), [[TOR1A]] (-0.61, fdr 1e-05), [[PSME3]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6914.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.04×** | +16.3 | 0e+00 | 46/48 (A-172, NCI-H2347, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +8.5 | 6e-15 | 45/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.66×** | +8.3 | 3e-14 | 41/48 (A-172, NCI-H1573, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.54×** | +6.7 | 2e-09 | 38/48 (A-172, BT-474, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +6.5 | 1e-08 | 43/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.44×** | +5.9 | 3e-07 | 41/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.37×** | +5.1 | 3e-05 | 35/48 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.1 | 3e-05 | 37/47 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Terfenadine (drug)]] 5 µM |  | 1.20× | +4.2 | 0.002 | 22/48 (A-172, NCI-H1792, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 32/49 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 34/48 (C32, SNU-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +3.8 | 0.008 | 28/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.6 | 0.012 | 15/49 (A-172, LOX-IMVI, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.49×** | +3.4 | 0.025 | 33/48 (NCI-H2030, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | 1.16× | +3.4 | 0.025 | 10/49 (SW 1271, KATO III, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.025 | 39/48 (NCI-H2030, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.042 | 31/49 (NCI-H1792, MIA PaCa-2, …) | all doses, flat | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.085 | 29/48 (SNU-1, NCI-H1792, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 12 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6914.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -11.2 | 1e-26 | 46/47 (HT-29, SW1417, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.602×** | -8.2 | 9e-14 | 48/48 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.702×** | -8.0 | 2e-13 | 42/49 (NCI-H1792, A549, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.3 | 4e-08 | 37/48 (SW 900, HS-578T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.744×** | -4.5 | 6e-04 | 29/44 (SNU-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.760×** | -4.2 | 0.002 | 34/48 (AN3 CA, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.769×** | -4.2 | 0.002 | 30/48 (A498, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.771×** | -4.2 | 0.002 | 26/49 (SW48, SW 1271, …) | all doses, flat | cell-cycle shift (explains ~14% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.832×** | -4.2 | 0.002 | 21/48 (NCI-H2347, AsPC-1, …) | top dose only | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.765×** | -4.0 | 0.004 | 35/48 (SW48, H4, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.774×** | -3.9 | 0.004 | 30/50 (RPMI-7951, SW480, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.772×** | -3.8 | 0.006 | 35/48 (KATO III, RPMI-7951, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.8 | 0.007 | 0/50 | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.851× | -3.6 | 0.011 | 20/48 (KATO III, SW48, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.790×** | -3.6 | 0.011 | 28/48 (SNU-1, LoVo, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.794×** | -3.5 | 0.017 | 31/47 (RKO, A498, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | **0.807×** | -3.4 | 0.019 | 27/48 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.808×** | -3.4 | 0.020 | 27/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.796×** | -3.4 | 0.020 | 31/49 (A-172, KATO III, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.800×** | -3.3 | 0.026 | 28/49 (H4, LS 180, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | **0.807×** | -3.2 | 0.038 | 29/49 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.809×** | -3.1 | 0.040 | 33/48 (H4, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | 0.871× | -3.1 | 0.046 | 5/48 (NCI-H1573, LS 180, …) | top dose only |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.834× | -2.9 | 0.082 | 23/48 (COLO 205, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6914. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 552 | 12 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.58× (z +20.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.7) | — |
| [[BT-474 (line)]] | alt | 460 | 6 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +20.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.21× (z +12.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.553× (z -8.9) ⚠ toxic |
| [[A498 (line)]] | wt | 754 | 2 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +13.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.580× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 1,067 | 3 (3 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +17.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 622 | 3 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +18.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.418× (z -9.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 1,390 | 3 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.11× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 552 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +16.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.28× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 490 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +20.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +12.9) | — |
| [[SNU-1 (line)]] | wt | 999 | 3 (2 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +10.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +9.4) | [[Dinaciclib (drug)]] 5 µM 0.354× (z -11.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 748 | 4 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.10× (z +30.2) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[COLO 205 (line)]] | alt | 506 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.368× (z -10.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 850 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +15.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -12.5) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 545 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +13.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 1,139 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +10.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.328× (z -11.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 686 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.13× (z +11.1) | — |
| [[HT-29 (line)]] | alt | 823 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +13.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.269× (z -16.7) ⚠ toxic |
| [[J82 (line)]] | alt | 878 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +20.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.09× (z +8.9) | — |
| [[KATO III (line)]] | alt | 952 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.243× (z -15.8) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.6) |
| [[LoVo (line)]] | wt | 1,066 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +11.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.425× (z -10.7) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 472 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +14.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.402× (z -12.1) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 588 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +16.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.454× (z -11.5) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.596× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 1,155 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +20.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.438× (z -15.1) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 858 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +20.1) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.456× (z -8.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 467 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +18.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A549 (line)]] | wt | 800 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +14.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -12.9) |
| [[AN3 CA (line)]] | alt | 745 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +9.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 805 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.534× (z -10.0) ⚠ toxic |
| [[C32 (line)]] | wt | 772 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CFPAC-1 (line)]] | alt | 473 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.54× (z +8.7) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.530× (z -8.7) ⚠ toxic |
| [[HS-578T (line)]] | alt | 977 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +12.9) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.488× (z -8.9) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 893 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.1) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[Panc 03.27 (line)]] | alt | 792 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +13.5) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.456× (z -11.4) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 1,263 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.8) ⚠ cell-cycle shift, explains ~30% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.484× (z -8.9) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 1,034 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.6) ⚠ cell-cycle shift, explains ~30% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.605× (z -9.4) |
| [[SW 900 (line)]] | alt | 775 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.363× (z -13.4) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -9.7) |
| [[SW1417 (line)]] | alt | 1,388 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -16.1) ⚠ toxic |
| [[C-33 A (line)]] | alt | 459 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +8.9) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[CHP-212 (line)]] | wt | 756 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +8.8) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[H4 (line)]] | wt | 705 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +9.6) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[HOP62 (line)]] | alt | 692 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +13.3) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[RKO (line)]] | wt | 775 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -10.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 395 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.539× (z -8.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 1,062 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.489× (z -9.0) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 682 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.319× (z -12.9) ⚠ toxic |
| [[LS 180 (line)]] | wt | 985 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 704 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 782 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 491 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 786 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1,065 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6914), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMF1]] | +0.76 | +0.79 / +0.68 | both halves | 7e-06 | same gene group; pathway: Intra-Golgi and retrograde Golgi-to-ER traffic; STRING 795 |
| [[GOLGA2]] | +0.72 | +0.74 / +0.64 | both halves | 7e-06 | same gene group; STRING 733 |
| [[UFL1]] | +0.69 | +0.71 / +0.63 | both halves | 7e-06 |  |
| [[AKAP9]] | +0.67 | +0.71 / +0.61 | both halves | 7e-06 | STRING 430 |
| [[SEC11C]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[SRP54]] | +0.66 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[TTC3]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[LYSMD3]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[KRT10]] ⚠ | +0.65 | +0.67 / +0.52 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ARFGAP3]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[FAM114A1]] | +0.64 | +0.58 / +0.60 | both halves | 7e-06 |  |
| [[SLC17A5]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUP50]] | -0.61 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[TOR1A]] | -0.61 | -0.69 / -0.51 | both halves | 1e-05 |  |
| [[PSME3]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[SF3B4]] | -0.57 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PPIA]] | -0.56 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[SUMO3]] | -0.55 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[ZNF236]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ABCF2]] | -0.54 | -0.58 / -0.45 | both halves | 3e-05 |  |
| [[YWHAQ]] | -0.54 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[E2F3]] | -0.54 | -0.60 / -0.49 | both halves | 2e-05 |  |
| [[NADK]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GOLGA4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYTL1]] | B | SYTL1 activity lowers GOLGA4's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without SYTL1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.666). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (11.1, -38.1); signed map (-51.1, 15.4). **Vector** length 142, 66.7% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +8.9 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +6.4 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.4 | -1.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | -0.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +4.1 | +1.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.9 | +2.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.6 | +4.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -9.6 | -11.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -8.1 | -8.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.6 | +0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.3 | -6.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -6.0 | -3.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.0 | +2.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.9 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | golgin A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p22.2 — chr3:37,243,191-37,366,879 (+) |
| Ensembl biotype | protein_coding |
| Also known as | golgin-245, GOLG, GCP2, p230, golgin-240 |
| Gene groups (HGNC) | Golgins |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 7 pathways, smallest: Signaling by membrane-tethered fusions of PDGFRA or PDGFRB; Signaling by PDGFR in disease; Retrograde transport at the Trans-Golgi-Network |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13439](https://www.uniprot.org/uniprotkb/Q13439) (Golgin subfamily A member 4):

> Involved in vesicular trafficking at the Golgi apparatus level. May play a role in delivery of transport vesicles containing GPI-linked proteins from the trans-Golgi network through its interaction with MACF1. Involved in endosome-to-Golgi trafficking.

**Summary**, from NCBI Gene [2803](https://www.ncbi.nlm.nih.gov/gene/2803):

> The Golgi apparatus, which participates in glycosylation and transport of proteins and lipids in the secretory pathway, consists of a series of stacked cisternae (flattened membrane sacs). Interactions between the Golgi and microtubules are thought to be important for the reorganization of the Golgi after it fragments during mitosis. This gene encodes one of the golgins, a family of proteins localized to the Golgi. This protein has been postulated to play a role in Rab6-regulated …

**Accessions** — [HGNC:4427](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4427) · Entrez [2803](https://www.ncbi.nlm.nih.gov/gene/2803) · UniProt [Q13439](https://www.uniprot.org/uniprotkb/Q13439) · Ensembl [ENSG00000144674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144674)

## Data

Gene col 6914: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6914); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6914, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6914]; `tensor/DDL_lfc|DDL_z.npy` [6914]; `embed/gene_vectors.npy` [6914]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6914 or target_col == 6914). Every well: [[GOLGA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLGA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
