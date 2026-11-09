---
symbol: "STIM1"
type: "gene"
col: 9452
ensembl_id: "ENSG00000167323"
name: "stromal interaction molecule 1"
location: "11p15.4"
module: 186
arm: "+"
pooled_cpm: 68.97
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 7
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/186"]
generated_by: "tahoemap"
---

# STIM1

*stromal interaction molecule 1* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.75× (z +17.7, q 0e+00, up in 39 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.528× (z -20.2, q 0e+00, down in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~49% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.691× (z -8.3, q 2e-14, down in 33 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (LoVo 0.233×, A498 0.360×, NCI-H2030 0.392×, NCI-H1792 0.182×, …; ⚠ cell-cycle shift, explains ~49% of this change); [[Harringtonine (drug)]] 0.5 µM in 7 lines (LOX-IMVI 0.203×, NCI-H1573 0.177×, A498 0.400×, LoVo 0.416×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A498 0.319×, LOX-IMVI 0.198×, LS 180 0.219×; ⚠ cell-cycle shift, explains ~27% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.435×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0880×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SRPK2]] (+0.71, fdr 7e-06), [[GLB1]] (+0.64, fdr 7e-06), [[MAST2]] (+0.62, fdr 7e-06); moves opposite to [[LYSMD3]] (-0.58, fdr 1e-05), [[POLI]] (-0.56, fdr 2e-05), [[HELQ]] (-0.55, fdr 4e-05).
> It is in [[Module 186]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ADCY3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +17.7 | 0e+00 | 39/46 (NCI-H460, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.63×** | +10.9 | 2e-25 | 43/46 (PANC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.54×** | +9.7 | 4e-20 | 34/46 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.49×** | +9.0 | 3e-17 | 37/46 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +7.9 | 3e-13 | 28/46 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +7.5 | 4e-12 | 37/47 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.26×** | +7.3 | 2e-11 | 24/46 (LoVo, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +6.8 | 9e-10 | 30/46 (SHP-77, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.37×** | +6.1 | 6e-08 | 25/46 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.33×** | +6.1 | 6e-08 | 25/46 (C32, A-172, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.26×** | +5.3 | 7e-06 | 21/46 (HOP62, H4, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.8 | 7e-05 | 21/46 (RKO, NCI-H1792, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.7 | 1e-04 | 19/46 (A-427, A-172, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.6 | 2e-04 | 19/46 (C32, RKO, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.21×** | +4.2 | 9e-04 | 19/46 (NCI-H2347, SNU-423, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.23×** | +4.1 | 0.001 | 20/46 (C32, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.18× | +3.7 | 0.005 | 17/46 (NCI-H2347, SNU-423, …) | all doses, flat |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.12× | +3.7 | 0.005 | 9/46 (J82, C32, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.18× | +3.6 | 0.007 | 16/46 (SNU-423, NCI-H2347, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.008 | 10/46 (CFPAC-1, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9452.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 10 lines (LoVo 0.233×, A498 0.360×, NCI-H2030 0.392×, NCI-H1792 0.182×, …; ⚠ cell-cycle shift, explains ~49% of this change); [[Harringtonine (drug)]] 0.5 µM in 7 lines (LOX-IMVI 0.203×, NCI-H1573 0.177×, A498 0.400×, LoVo 0.416×, …); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (A498 0.319×, LOX-IMVI 0.198×, LS 180 0.219×; ⚠ cell-cycle shift, explains ~27% of this change); [[Auranofin (drug)]] 5 µM in 1 line (A-427 0.435×); [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM in 1 line (SW 1271 0.0880×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.528×** | -20.2 | 0e+00 | 39/46 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.510×** | -15.1 | 0e+00 | 40/46 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.691×** | -8.3 | 2e-14 | 33/46 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.666×** | -7.9 | 3e-13 | 30/46 (LoVo, A498, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -7.2 | 8e-11 | 32/46 (A-427, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.651×** | -4.8 | 2e-04 | 22/47 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.821×** | -4.4 | 9e-04 | 23/46 (NCI-H460, SW48, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~93% of this change | 0.842× | -3.8 | 0.009 | 20/46 (LOX-IMVI, NCI-H460, …) | top dose only | composition shift |
| [[Vilanterol (drug)]] 5 µM |  | 0.888× | -3.8 | 0.011 | 8/47 (PANC-1, Panc 03.27, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.840× | -3.6 | 0.017 | 19/43 (A498, NCI-H2030, …) | inconsistent across doses | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | 0.842× | -3.4 | 0.039 | 16/45 (SK-MEL-2, A498, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.865× | -3.3 | 0.054 | 17/46 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | 0.874× | -3.0 | 0.11 | 21/45 (SW1417, J82, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 196 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -20.3) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.400× (z -12.9) |
| [[C32 (line)]] | wt | 80.1 | 3 | 3 (3 ⚠) | [[Ponatinib (drug)]] 5 µM 2.85× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -13.8) ⚠ cell-cycle shift, explains ~49% of this change |
| [[LoVo (line)]] | wt | 55.1 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +17.6) | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -25.6) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.416× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 109 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -17.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H460 (line)]] | wt | 38.8 | 2 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +19.6) | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -14.4) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.440× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 45.3 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -16.7) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.203× (z -14.7) |
| [[LS 180 (line)]] | wt | 43.9 | 3 (2 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +17.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.219× (z -13.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[A549 (line)]] | wt | 61.3 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -13.1) ⚠ cell-cycle shift, explains ~49% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.369× (z -10.2) |
| [[COLO 205 (line)]] | alt | 34.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -14.3) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW1417 (line)]] | alt | 152 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.452× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 70.5 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.317× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.177× (z -13.0) |
| [[NCI-H23 (line)]] | alt | 42.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -13.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[PANC-1 (line)]] | alt | 125 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.84× (z +10.1) | [[Homoharringtonine (drug)]] 0.5 µM 0.473× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[RKO (line)]] | wt | 70.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +14.9) | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 99.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.51× (z +8.8) | [[Harringtonine (drug)]] 0.5 µM 0.496× (z -10.8) |
| [[A-427 (line)]] | wt | 74.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.332× (z -12.3) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.435× (z -9.3) |
| [[H4 (line)]] | wt | 40.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +10.9) | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -13.9) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HepG2_C3A (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 41.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.91× (z +10.3) | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -9.2) ⚠ cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 53.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SK-MEL-2 (line)]] | alt | 73.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.570× (z -8.7) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW48 (line)]] | wt | 75.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -14.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[A-172 (line)]] | wt | 70.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 95.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -12.4) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -10.4) ⚠ cell-cycle shift, explains ~49% of this change |
| [[HEC-1-A (line)]] | alt | 60.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +9.6) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[KATO III (line)]] | alt | 24.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.2) ⚠ cell-cycle shift, explains ~49% of this change |
| [[NCI-H2347 (line)]] | alt | 66.4 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.13× (z +9.2) | — |
| [[Panc 03.27 (line)]] | alt | 55.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.375× (z -9.6) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 41.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.01× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 91.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -10.1) ⚠ cell-cycle shift, explains ~49% of this change |
| [[SW 1271 (line)]] | alt | 59.2 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0880× (z -8.8) |
| [[BT-474 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 54.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 94.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 68.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRPK2]] | +0.71 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[GLB1]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[MAST2]] | +0.62 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[BMPR1A]] | +0.62 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[SGPP1]] | +0.61 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[SLC41A3]] | +0.60 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[HACD3]] | +0.60 | +0.66 / +0.45 | both halves | 3e-05 |  |
| [[MFSD14B]] | +0.59 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[NFATC3]] | +0.59 | +0.67 / +0.49 | both halves | 1e-05 | pathway: Signaling by the B Cell Receptor (BCR); STRING 448 |
| [[CCNY]] | +0.58 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN17]] | +0.58 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[FAR1]] | +0.58 | +0.58 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LYSMD3]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[POLI]] | -0.56 | -0.61 / -0.47 | both halves | 2e-05 |  |
| [[HELQ]] | -0.55 | -0.63 / -0.42 | both halves | 4e-05 |  |
| [[MYSM1]] | -0.55 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[TCEANC]] | -0.53 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[GORAB]] | -0.53 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[ZBTB1]] | -0.53 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[ZNF638]] | -0.52 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ZNF554]] | -0.52 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[GOLGA1]] | -0.52 | -0.64 / -0.36 | both halves | 9e-05 |  |
| [[METTL25B]] | -0.52 | -0.64 / -0.28 | both halves | 3e-04 |  |
| [[ZNF776]] | -0.51 | -0.49 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY3]] | B | ADCY3 activity raises STIM1's level | lines that do not express ADCY3 (5) vs lines expressing it (45) | 1.48× lower at baseline in the lines without ADCY3 | 0.014 | ⚠ within organs, on part of the lines; also absent: PPP2R3A, TBC1D19, SSBP2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 186]]; 20 genes; every member is in the + arm (projection on the module's main direction 0.622). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.4, -7.8); signed map (-45.3, -6.6). **Vector** length 107, 28.7% of its response variance represented; |z| ≥ 3 in 1,173 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +5.9 | +5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | +4.5 | +6.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +17.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.2 | +6.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[Neratinib (drug)]] 5 µM |  | +2.6 | +3.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.6 | +3.0 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.5 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -11.8 | -20.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -9.7 | -15.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.8 | -7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -6.2 | -7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.3 | -3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.4 | -3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | +2.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | stromal interaction molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:3,854,527-4,093,210 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GOK, D11S4896E |
| Gene groups (HGNC) | Sterile alpha motif domain containing; MicroRNA protein coding host genes; Stromal interaction molecule family |
| Reactome | 10 pathways, smallest: Elevation of cytosolic Ca2+ levels; Platelet calcium homeostasis; Antigen activates B Cell Receptor (BCR) leading to generation of second messengers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13586](https://www.uniprot.org/uniprotkb/Q13586) (Stromal interaction molecule 1):

> Acts as a Ca(2+) sensor that gates two major inward rectifying Ca(2+) channels at the plasma membrane: Ca(2+) release-activated Ca(2+) (CRAC) channels and arachidonate-regulated Ca(2+)-selective (ARC) channels. Plays a role in mediating store-operated Ca(2+) entry (SOCE), a Ca(2+) influx following depletion of intracellular Ca(2+) stores. Upon Ca(2+) depletion, translocates from the endoplasmic reticulum to the plasma membrane where it activates CRAC channel pore-forming subunits ORA1, ORA2 and …

**Summary**, from NCBI Gene [6786](https://www.ncbi.nlm.nih.gov/gene/6786):

> This gene encodes a type 1 transmembrane protein that mediates Ca2+ influx after depletion of intracellular Ca2+ stores by gating of store-operated Ca2+ influx channels (SOCs). It is one of several genes located in the imprinted gene domain of 11p15.5, an important tumor-suppressor gene region. Alterations in this region have been associated with the Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocrotical carcinoma, and lung, ovarian, and breast cancer. This gene may play a …

**Accessions** — [HGNC:11386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11386) · Entrez [6786](https://www.ncbi.nlm.nih.gov/gene/6786) · UniProt [Q13586](https://www.uniprot.org/uniprotkb/Q13586) · Ensembl [ENSG00000167323](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167323)

## Data

Gene col 9452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9452); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9452]; `tensor/DDL_lfc|DDL_z.npy` [9452]; `embed/gene_vectors.npy` [9452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9452 or target_col == 9452). Every well: [[STIM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STIM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
