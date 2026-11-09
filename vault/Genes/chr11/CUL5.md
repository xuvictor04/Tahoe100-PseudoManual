---
symbol: "CUL5"
type: "gene"
col: 9273
ensembl_id: "ENSG00000166266"
name: "cullin 5"
location: "11q22.3"
module: 64
arm: "+"
pooled_cpm: 132.39
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# CUL5

*cullin 5* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.32× (z +10.4, q 1e-22, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.495× (z -26.4, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM204A]] (+0.76, fdr 7e-06), [[PGGT1B]] (+0.73, fdr 7e-06), [[MTA3]] (+0.73, fdr 7e-06); moves opposite to [[RELL1]] (-0.59, fdr 1e-05), [[CAMTA1]] (-0.55, fdr 3e-05), [[CCNYL1]] (-0.55, fdr 4e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NDUFS4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9273.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +10.4 | 1e-22 | 35/48 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +9.5 | 7e-19 | 31/48 (LS 180, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +9.1 | 1e-17 | 22/48 (NCI-H23, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.12×** | +8.8 | 1e-16 | 40/49 (SW480, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.27×** | +8.5 | 2e-15 | 31/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +7.9 | 3e-13 | 28/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.16× | +7.9 | 3e-13 | 18/48 (HT-29, KATO III, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PH-797804 (drug)]] 5 µM |  | **1.80×** | +6.9 | 3e-10 | 32/48 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.22×** | +6.1 | 8e-08 | 25/48 (AsPC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +5.4 | 4e-06 | 18/48 (LS 180, LoVo, …) | top dose only | composition shift |
| [[NG25 (drug)]] 5 µM |  | **1.45×** | +4.4 | 5e-04 | 17/47 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.13× | +4.3 | 9e-04 | 16/45 (NCI-H460, NCI-H23, …) | inconsistent across doses | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.13× | +4.3 | 9e-04 | 18/47 (SW48, C32, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.10× | +3.7 | 0.009 | 10/48 (C32, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.12× | +3.5 | 0.017 | 17/48 (HS-578T, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.024 | 12/49 (SW1417, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.071 | 5/48 (AsPC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9273.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.495×** | -26.4 | 0e+00 | 48/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.515×** | -25.0 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -21.4 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -13.4 | 9e-39 | 33/49 (A549, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.742×** | -11.2 | 4e-27 | 40/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.751×** | -10.4 | 3e-23 | 36/48 (SNU-423, C32, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.823×** | -10.3 | 4e-23 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.770×** | -9.4 | 3e-19 | 32/50 (SNU-1, SW48, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~9% of this change | **0.809×** | -8.0 | 9e-14 | 28/48 (RPMI-7951, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.814×** | -7.7 | 5e-13 | 29/48 (NCI-H460, Panc 03.27, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | **0.828×** | -6.8 | 5e-10 | 25/47 (PANC-1, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | 0.841× | -6.5 | 4e-09 | 20/48 (NCI-H1792, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | 0.851× | -5.8 | 2e-07 | 21/43 (NCI-H2030, HCT15, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | 0.877× | -4.7 | 9e-05 | 13/47 (CFPAC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.860× | -4.5 | 2e-04 | 16/49 (SW480, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.929× | -3.9 | 0.003 | 9/48 (NCI-H2347, SNU-1, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.732×** | -3.7 | 0.008 | 13/48 (NCI-H2347, Panc 03.27, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | 0.871× | -3.4 | 0.018 | 10/48 (SW 1271, A-427, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | 0.913× | -3.3 | 0.031 | 10/48 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.766×** | -3.1 | 0.050 | 12/48 (A-172, LS 180, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9273. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 196 | 1 | 6 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 2.57× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -13.1) |
| [[C-33 A (line)]] | alt | 161 | 1 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.476× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 126 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.407× (z -18.6) |
| [[Panc 03.27 (line)]] | alt | 151 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.425× (z -14.9) |
| [[A-427 (line)]] | wt | 98.0 | 1 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +12.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.475× (z -10.5) |
| [[A549 (line)]] | wt | 103 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.511× (z -13.9) |
| [[HCT15 (line)]] | alt | 212 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.437× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.502× (z -10.2) |
| [[HOP62 (line)]] | alt | 87.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.438× (z -12.6) |
| [[HS-578T (line)]] | alt | 111 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.55× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.516× (z -9.7) |
| [[KATO III (line)]] | alt | 223 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.50× (z +10.0) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.398× (z -15.9) |
| [[LoVo (line)]] | wt | 138 | 1 (1 ⚠) | 3 | [[Digitoxin (drug)]] 5 µM 1.56× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.393× (z -19.0) |
| [[NCI-H2347 (line)]] | alt | 145 | 0 | 4 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.457× (z -13.5) |
| [[RKO (line)]] | wt | 171 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.517× (z -10.6) |
| [[SNU-423 (line)]] | alt | 132 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.442× (z -13.8) |
| [[SW480 (line)]] | alt | 185 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.358× (z -22.6) |
| [[A498 (line)]] | wt | 86.7 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.489× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 106 | 0 | 3 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.474× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~36% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.564× (z -9.3) |
| [[LOX-IMVI (line)]] | wt | 154 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +11.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.576× (z -9.4) |
| [[LS 180 (line)]] | wt | 146 | 1 (1 ⚠) | 2 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.78× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.515× (z -11.4) |
| [[MIA PaCa-2 (line)]] | alt | 145 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.330× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 120 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 165 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.457× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.518× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 131 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.557× (z -9.2) ⚠ cell-cycle shift, explains ~20% of this change |
| [[PANC-1 (line)]] | alt | 178 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.592× (z -11.3) ⚠ toxic; cell-cycle shift, explains ~22% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.611× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 135 | 0 | 3 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.336× (z -14.3) ⚠ transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.482× (z -9.6) |
| [[SNU-1 (line)]] | wt | 207 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.2) ⚠ cell-cycle shift, explains ~20% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -8.7) |
| [[SW 900 (line)]] | alt | 125 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -12.9) |
| [[A-172 (line)]] | wt | 67.3 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.379× (z -12.5) |
| [[AN3 CA (line)]] | alt | 179 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.318× (z -9.8) |
| [[C32 (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -10.3) ⚠ cell-cycle shift, explains ~19% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.642× (z -8.8) |
| [[H4 (line)]] | wt | 131 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.428× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 140 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.561× (z -9.1) |
| [[Hs 766T (line)]] | wt | 121 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.499× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 83.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW1417 (line)]] | alt | 173 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.456× (z -13.8) |
| [[BT-474 (line)]] | alt | 107 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.472× (z -9.2) |
| [[COLO 205 (line)]] | alt | 109 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.360× (z -12.1) |
| [[HT-29 (line)]] | alt | 123 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.64× (z +10.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SHP-77 (line)]] | alt | 132 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.532× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 160 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 109 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 356 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9273), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM204A]] | +0.76 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[PGGT1B]] | +0.73 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[MTA3]] | +0.73 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[CC2D2A]] | +0.68 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[NUDT9]] | +0.68 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[TCTN1]] | +0.68 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[LINC01278]] | +0.67 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TMLHE]] | +0.66 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[CWC27]] | +0.65 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[TYW3]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[RBM41]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[FUBP1]] | +0.64 | +0.42 / +0.63 | both halves | 4e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RELL1]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[CAMTA1]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[CCNYL1]] | -0.55 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[LINC01128]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.53 | -0.39 / -0.49 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CUL5's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CAP2]] | B | CAP2 activity raises CUL5's level | lines that do not express CAP2 (7) vs lines expressing it (43) | 1.24× lower at baseline in the lines without CAP2 | 0.089 | ⚠ within organs, on part of the lines; also absent: SCML2, ADORA1, ASAP3 |
| [[PSMB5]] | B | PSMB5 activity lowers CUL5's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NDUFS4]] | C | CUL5's natural level strengthens NDUFS4's drug response | CUL5's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.19; direction not clear | 0.053 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.758). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-22.3, 3.8); signed map (8.8, -32.4). **Vector** length 115, 33.1% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +10.3 | +7.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.3 | +10.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +6.2 | +6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.0 | +8.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.2 | +9.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.1 | +3.7 |
|  | [[EX229 (drug)]] 5 µM |  | +4.3 | +2.8 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.5 | +0.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.0 | +2.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~22% of this change | -4.9 | -6.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.9 | -25.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.8 | -10.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -21.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.4 | -26.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.6 | -0.8 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | cullin 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:108,008,898-108,107,761 (+) |
| Ensembl biotype | protein_coding |
| Also known as | VACM-1 |
| Gene groups (HGNC) | Cullins |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 17 pathways, smallest: Evasion by RSV of host interferon responses; Inactivation of CSF3 (G-CSF) signaling; Signaling by CSF3 (G-CSF) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q93034](https://www.uniprot.org/uniprotkb/Q93034) (Cullin-5):

> Core component of multiple cullin-5-RING E3 ubiquitin-protein ligase complexes (ECS complexes, also named CRL5 complexes), which mediate the ubiquitination and subsequent proteasomal degradation of target proteins. Acts a scaffold protein that contributes to catalysis through positioning of the substrate and the ubiquitin-conjugating enzyme. The functional specificity of the E3 ubiquitin-protein ligase complex depends on the variable SOCS box-containing substrate recognition component. Acts as …

**Summary**, from NCBI Gene [8065](https://www.ncbi.nlm.nih.gov/gene/8065):

> Enables ubiquitin ligase complex scaffold activity and ubiquitin protein ligase binding activity. Involved in several processes, including negative regulation of cell-substrate junction organization; proteasome-mediated ubiquitin-dependent protein catabolic process; and protein K11-linked ubiquitination. Located in site of DNA damage. Part of Cul5-RING ubiquitin ligase complex. Is active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2556](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2556) · Entrez [8065](https://www.ncbi.nlm.nih.gov/gene/8065) · UniProt [Q93034](https://www.uniprot.org/uniprotkb/Q93034) · Ensembl [ENSG00000166266](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166266)

## Data

Gene col 9273: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9273); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9273, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9273]; `tensor/DDL_lfc|DDL_z.npy` [9273]; `embed/gene_vectors.npy` [9273]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9273 or target_col == 9273). Every well: [[CUL5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUL5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
