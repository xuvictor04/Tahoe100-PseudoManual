---
symbol: "KAZN"
type: "gene"
col: 12117
ensembl_id: "ENSG00000189337"
name: "kazrin, periplakin interacting protein"
location: "1p36.21"
module: 37
arm: "+"
pooled_cpm: 94.87
n_lines_expressing: 45
n_dd_up: 12
n_dd_down: 19
n_dd_up_clean: 11
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# KAZN

*kazrin, periplakin interacting protein* — 1p36.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +16.9, q 0e+00, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.380× (z -21.6, q 0e+00, down in 37 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 0.530× (z -14.7, q 0e+00, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02885]] (+0.61, fdr 1e-04), [[LVRN]] (+0.60, fdr 7e-06), [[SNX31]] (+0.59, fdr 7e-06); moves opposite to [[ZNF708]] (-0.48, fdr 9e-05), [[MCRS1]] (-0.48, fdr 2e-04), [[MRPS18A]] (-0.47, fdr 5e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LINC01482]] → it (grade B ⚠); 8 go from it, the strongest it → [[LINC00595]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12117.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +16.9 | 0e+00 | 38/43 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +15.6 | 0e+00 | 31/44 (A498, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **2.89×** | +12.9 | 1e-35 | 36/44 (SW48, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +10.1 | 6e-22 | 30/43 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +9.5 | 4e-19 | 32/44 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +7.3 | 3e-11 | 23/43 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +5.5 | 3e-06 | 20/42 (C-33 A, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.26×** | +5.5 | 3e-06 | 23/43 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.56×** | +5.4 | 4e-06 | 22/44 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +4.7 | 2e-04 | 21/43 (C32, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.4 | 5e-04 | 19/45 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.1 | 0.002 | 17/43 (KATO III, NCI-H1573, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.19× | +4.1 | 0.002 | 12/43 (NCI-H1573, NCI-H2030, …) | inconsistent across doses |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.005 | 15/44 (SW480, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.16× | +3.3 | 0.034 | 13/42 (LoVo, A-172, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.16× | +3.3 | 0.035 | 11/44 (A-427, HepG2/C3A, …) | top dose only |  |
| [[Torkinib (drug)]] 0.05 µM |  | 1.15× | +3.1 | 0.069 | 7/43 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.14× | +3.0 | 0.086 | 8/43 (H4, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 13 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12117.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.380×** | -21.6 | 0e+00 | 37/42 (HEC-1-A, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.530×** | -14.7 | 0e+00 | 35/43 (COLO 205, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.505×** | -8.3 | 3e-14 | 29/44 (HEC-1-A, SK-MEL-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.798×** | -7.3 | 3e-11 | 25/43 (SNU-423, Hs 766T, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.737×** | -7.1 | 2e-10 | 22/43 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.750×** | -6.6 | 3e-09 | 24/43 (COLO 205, SW 1088, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **0.760×** | -6.3 | 2e-08 | 25/43 (PANC-1, KATO III, …) | all doses, flat | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.761×** | -6.3 | 2e-08 | 21/43 (PANC-1, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.768×** | -6.1 | 7e-08 | 23/43 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -5.9 | 3e-07 | 22/43 (KATO III, LS 180, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **0.786×** | -5.6 | 1e-06 | 21/43 (KATO III, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.808×** | -4.9 | 5e-05 | 20/43 (NCI-H2030, SW 900, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.807×** | -4.8 | 9e-05 | 20/43 (NCI-H2030, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.813×** | -4.6 | 2e-04 | 14/42 (LS 180, AN3 CA, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.767×** | -4.4 | 5e-04 | 9/43 (SNU-423, LS 180, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.822×** | -4.2 | 1e-03 | 19/42 (NCI-H23, HCT15, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.834× | -4.2 | 1e-03 | 15/42 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.881× | -4.1 | 0.001 | 10/44 (HEC-1-A, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.731×** | -3.8 | 0.004 | 15/43 (HEC-1-A, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.854× | -3.6 | 0.007 | 16/43 (A549, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | 0.855× | -3.6 | 0.007 | 11/44 (HOP62, COLO 205, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.855× | -3.5 | 0.011 | 8/44 (SW 900, A549, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12117. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 518 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.295× (z -15.6) |
| [[C32 (line)]] | wt | 75.0 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.03× (z +21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.25× (z +13.8) | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[KATO III (line)]] | alt | 78.6 | 4 (1 ⚠) | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.32× (z +13.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.198× (z -18.0) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.386× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 204 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +18.6) | [[Ponatinib (drug)]] 5 µM 0.299× (z -13.6) |
| [[HS-578T (line)]] | alt | 173 | 1 | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.29× (z +10.6) | [[Dinaciclib (drug)]] 0.5 µM 0.283× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.371× (z -8.9) |
| [[HT-29 (line)]] | alt | 58.1 | 3 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.02× (z +10.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -13.6) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.358× (z -9.7) |
| [[LS 180 (line)]] | wt | 231 | 1 (1 ⚠) | 6 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.38× (z +9.5) ⚠ cell-cycle shift, explains ~93% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.215× (z -16.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.306× (z -12.9) |
| [[PANC-1 (line)]] | alt | 90.8 | 2 | 5 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.77× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.372× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.484× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 76.2 | 3 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.54× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.340× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.431× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 379 | 0 | 5 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.257× (z -19.4) ⚠ toxic · without an alert: [[PH-797804 (drug)]] 5 µM 0.206× (z -12.2) |
| [[NCI-H460 (line)]] | wt | 54.8 | 5 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 2.96× (z +15.2) | — |
| [[RKO (line)]] | wt | 92.9 | 2 (1 ⚠) | 3 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +11.3) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.350× (z -9.1) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.366× (z -9.0) |
| [[SW480 (line)]] | alt | 60.8 | 3 (1 ⚠) | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.24× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.285× (z -11.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.350× (z -10.3) |
| [[Hs 766T (line)]] | wt | 37.2 | 1 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +9.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.244× (z -9.7) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.275× (z -9.2) |
| [[SNU-423 (line)]] | alt | 140 | 1 | 3 | [[Tucidinostat (drug)]] 5 µM 2.31× (z +11.3) | [[Selinexor (drug)]] 5 µM 0.523× (z -8.8) |
| [[C-33 A (line)]] | alt | 55.9 | 3 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.30× (z +13.0) ⚠ toxic · without an alert: [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.9) | — |
| [[HCT15 (line)]] | alt | 185 | 1 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.03× (z +8.6) ⚠ toxic | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.148× (z -14.8) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.262× (z -10.8) |
| [[LoVo (line)]] | wt | 89.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +17.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.309× (z -9.4) ⚠ toxic |
| [[SW 900 (line)]] | alt | 97.2 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +10.9) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.191× (z -14.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 96.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.69× (z +9.1) ⚠ cell-cycle shift, explains ~68% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.362× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 56.0 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.72× (z +8.5) | [[Dinaciclib (drug)]] 0.05 µM 0.161× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~77% of this change |
| [[A498 (line)]] | wt | 41.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +20.7) | — |
| [[AN3 CA (line)]] | alt | 609 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 124 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0702× (z -17.4) ⚠ toxic · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.146× (z -13.1) |
| [[HOP62 (line)]] | alt | 49.6 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.50× (z +10.4) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.326× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 99.8 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 1.74× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 130 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.239× (z -14.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 97.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +12.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.302× (z -9.2) ⚠ toxic |
| [[A549 (line)]] | wt | 38.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +11.6) | — |
| [[CFPAC-1 (line)]] | alt | 25.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.11× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[CHP-212 (line)]] | wt | 46.3 | 0 | 1 | — | [[Elimusertib hydrochloride (drug)]] 0.05 µM 0.0664× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 82.5 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.258× (z -10.7) ⚠ cell-cycle shift, explains ~68% of this change |
| [[SW1417 (line)]] | alt | 37.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.13× (z +8.7) | — |
| [[SW48 (line)]] | wt | 143 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -14.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 175 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.1 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 90.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 346 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 85.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12117), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02885]] | +0.61 | +0.35 / +0.60 | both halves | 1e-04 |  |
| [[LVRN]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[SNX31]] | +0.59 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.58 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CD247]] | +0.57 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[CAMTA1]] | +0.57 | +0.46 / +0.60 | both halves | 2e-05 |  |
| [[C1QTNF7-AS1]] | +0.56 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[GRK3]] | +0.56 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[LINC00595]] | +0.55 | +0.38 / +0.68 | both halves | 7e-05 |  |
| [[C1QTNF7]] | +0.55 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[FLJ40194]] | +0.55 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[MGC4859]] | +0.55 | +0.46 / +0.65 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF708]] | -0.48 | -0.37 / -0.49 | both halves | 9e-05 |  |
| [[MCRS1]] | -0.48 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[MRPS18A]] | -0.47 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[POLR3F]] | -0.46 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[ZNF576]] | -0.45 | -0.18 / -0.47 | ⚠ not reproduced | 0.001 |  |
| [[DNAJC14]] | -0.44 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ZNF613]] | -0.44 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[EXO5]] | -0.44 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[CENPBD1P]] | -0.43 | -0.26 / -0.52 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC01482]] | B | LINC01482 activity raises KAZN's level | lines that do not express LINC01482 (5) vs lines expressing it (45) | 3.35× lower at baseline in the lines without LINC01482 | 0.042 | ⚠ within organs, on part of the lines; also absent: MAP7D2, SLC35F4, ENSG00000226965; maybe low, not absent |
| [[MGC4859]] | B | MGC4859 activity raises KAZN's level | lines that do not express MGC4859 (8) vs lines expressing it (42) | 3.38× lower at baseline in the lines without MGC4859 | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC00922, LINC01811, LINC00276; maybe low, not absent |
| [[LINC02885]] | B | LINC02885 activity raises KAZN's level | lines that do not express LINC02885 (15) vs lines expressing it (35) | 2.15× lower at baseline in the lines without LINC02885 | 0.047 | ⚠ within organs, on part of the lines; also absent: LINC01399, PCDHB2, ENSG00000258168; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers KAZN's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[LINC00504]] | B | LINC00504 activity raises KAZN's level | lines that do not express LINC00504 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without LINC00504 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000287598, LINC02930, ENSG00000287474 |
| [[LINC00595]] | B | LINC00595 activity raises KAZN's level | lines that do not express LINC00595 (9) vs lines expressing it (41) | 2.43× lower at baseline in the lines without LINC00595 | 0.090 | ⚠ within organs, on part of the lines; also absent: SUSD4, EBF4, SLC17A7; maybe low, not absent |
| [[FRZB]] | C | FRZB activity raises KAZN's level | lines that do not express FRZB (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without FRZB | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: EFCAB3P1, ENSG00000287621, ENSG00000229195; maybe low, not absent |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00595]] | B | KAZN activity raises LINC00595's level | lines that do not express KAZN (5) vs lines expressing it (45) | 3.22× lower at baseline in the lines without KAZN | 0.007 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[CAMTA1]] | B | KAZN activity raises CAMTA1's level | lines that do not express KAZN (5) vs lines expressing it (45) | 1.74× lower at baseline in the lines without KAZN | 0.013 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[PLD5P1]] | B | KAZN activity raises PLD5P1's level | lines that do not express KAZN (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without KAZN | 0.048 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[LINC02885]] | B | KAZN activity raises LINC02885's level | lines that do not express KAZN (5) vs lines expressing it (45) | 2.57× lower at baseline in the lines without KAZN | 0.061 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[ZNF473CR]] | B | KAZN activity raises ZNF473CR's level | lines that do not express KAZN (5) vs lines expressing it (45) | 1.46× lower at baseline in the lines without KAZN | 0.070 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[C1QTNF7-AS1]] | B | KAZN activity raises C1QTNF7-AS1's level | lines that do not express KAZN (5) vs lines expressing it (45) | 2.41× lower at baseline in the lines without KAZN | 0.073 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[LINC02641]] | B | KAZN activity raises LINC02641's level | lines that do not express KAZN (5) vs lines expressing it (45) | 3.62× lower at baseline in the lines without KAZN | 0.084 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent |
| [[C1QTNF7-AS1]] | C | KAZN activity strengthens C1QTNF7-AS1's drug response | lines that do not express KAZN (4) vs lines expressing it (42) | the lines without KAZN respond 0.43× as strongly (z diff +3.24); strongest at Idarubicin (hydrochloride) 5 µM: 1.14x vs 0.52x (z diff +7.2) | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAH6, SLC1A4, ENSG00000197332; maybe low, not absent; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.540). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.5, -19.2); signed map (7.7, 7.1). **Vector** length 102, 24.5% of its response variance represented; |z| ≥ 3 in 1,336 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +10.3 | +16.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.1 | +5.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.9 | -1.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.4 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +7.2 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.9 | +2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.5 | +12.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.1 | -14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.3 | -21.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -2.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.8 | -7.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -0.9 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -2.3 | -5.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.3 | -0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -2.1 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | kazrin, periplakin interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.21 — chr1:13,892,792-15,118,043 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1026, KAZRIN, FLJ43806; previously C1orf196 |
| Gene groups (HGNC) | Sterile alpha motif domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q674X7](https://www.uniprot.org/uniprotkb/Q674X7) (Kazrin):

> Component of the cornified envelope of keratinocytes. May be involved in the interplay between adherens junctions and desmosomes. The function in the nucleus is not known.

**Summary**, from NCBI Gene [23254](https://www.ncbi.nlm.nih.gov/gene/23254):

> This gene encodes a protein that plays a role in desmosome assembly, cell adhesion, cytoskeletal organization, and epidermal differentiation. This protein co-localizes with desmoplakin and the cytolinker protein periplakin. In general, this protein localizes to the nucleus, desmosomes, cell membrane, and cortical actin-based structures. Some isoforms of this protein also associate with microtubules. Alternative splicing results in multiple transcript variants encoding distinct isoforms. …

**Accessions** — [HGNC:29173](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29173) · Entrez [23254](https://www.ncbi.nlm.nih.gov/gene/23254) · UniProt [Q674X7](https://www.uniprot.org/uniprotkb/Q674X7) · Ensembl [ENSG00000189337](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189337)

## Data

Gene col 12117: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12117); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12117, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12117]; `tensor/DDL_lfc|DDL_z.npy` [12117]; `embed/gene_vectors.npy` [12117]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12117 or target_col == 12117). Every well: [[KAZN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KAZN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
