---
symbol: "GAB2"
type: "gene"
col: 415
ensembl_id: "ENSG00000033327"
name: "GRB2 associated binding protein 2"
location: "11q14.1"
module: 115
arm: "+"
pooled_cpm: 67.15
n_lines_expressing: 48
n_dd_up: 27
n_dd_down: 23
n_dd_up_clean: 18
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/115"]
generated_by: "tahoemap"
---

# GAB2

*GRB2 associated binding protein 2* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.10× (z +14.0, q 5e-42, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (16 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.438× (z -15.7, q 0e+00, down in 40 of 46 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.438× (z -15.1, q 0e+00, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EXOC6B]] (+0.64, fdr 7e-06), [[SERAC1]] (+0.61, fdr 7e-06), [[SPIRE1]] (+0.59, fdr 1e-05); moves opposite to [[PER2]] (-0.53, fdr 1e-05), [[DDX39B]] (-0.53, fdr 2e-05), [[LINS1]] (-0.51, fdr 3e-05).
> It is in [[Module 115]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MTOR]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Menadione (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 415.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.10×** | +14.0 | 5e-42 | 38/45 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.95×** | +12.7 | 2e-34 | 37/46 (PANC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.77×** | +10.2 | 2e-22 | 39/46 (C32, HT-29, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.37×** | +8.2 | 3e-14 | 28/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.39×** | +6.3 | 4e-08 | 28/46 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.42×** | +6.2 | 4e-08 | 29/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +6.2 | 6e-08 | 30/45 (A549, SW480, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +6.1 | 1e-07 | 26/45 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +5.9 | 3e-07 | 25/46 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +5.4 | 4e-06 | 26/45 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 1e-04 | 25/47 (C32, PANC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | **1.30×** | +4.7 | 1e-04 | 23/47 (MIA PaCa-2, HOP62, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.28×** | +4.6 | 2e-04 | 21/45 (KATO III, NCI-H460, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.6 | 2e-04 | 19/46 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.25×** | +4.2 | 1e-03 | 20/45 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.69×** | +4.1 | 0.001 | 21/48 (NCI-H460, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **1.68×** | +4.1 | 0.002 | 17/46 (LS 180, HEC-1-A, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.003 | 21/45 (SW480, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Rapamycin (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.004 | 16/45 (Panc 03.27, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.62×** | +3.8 | 0.004 | 18/47 (LS 180, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 19 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 415.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.438×** | -15.7 | 0e+00 | 40/46 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.438×** | -15.1 | 0e+00 | 36/48 (NCI-H2347, SW 900, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.430×** | -14.8 | 0e+00 | 30/41 (C-33 A, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.574×** | -14.7 | 0e+00 | 36/46 (PANC-1, SW 900, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change | **0.474×** | -14.2 | 1e-43 | 37/44 (LoVo, C-33 A, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.470×** | -13.8 | 2e-41 | 37/45 (SW48, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.497×** | -13.3 | 3e-38 | 38/45 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.491×** | -13.0 | 1e-36 | 32/40 (SNU-423, C-33 A, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.623×** | -12.5 | 3e-34 | 32/47 (NCI-H2347, CHP-212, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.706×** | -9.1 | 5e-18 | 31/46 (NCI-H2347, NCI-H661, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.634×** | -8.7 | 2e-16 | 31/45 (LoVo, NCI-H23, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.387×** | -7.5 | 4e-12 | 33/47 (PANC-1, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.680×** | -7.1 | 7e-11 | 27/46 (HEC-1-A, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.703×** | -6.7 | 8e-10 | 28/46 (C-33 A, LoVo, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.735×** | -5.5 | 1e-06 | 27/46 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.636×** | -3.6 | 0.009 | 12/44 (HCT15, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.841× | -3.1 | 0.053 | 16/45 (AsPC-1, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Sulfatinib (drug)]] 5 µM |  | 0.851× | -3.0 | 0.068 | 13/46 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.689×** | -2.9 | 0.071 | 16/45 (HS-578T, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 0.858× | -2.9 | 0.071 | 10/45 (A498, AsPC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **0.811×** | -2.8 | 0.089 | 9/46 (LS 180, SW1417, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 0.865× | -2.8 | 0.098 | 7/46 (SHP-77, RKO, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 5 µM |  | 0.901× | -2.8 | 0.098 | 6/46 (NCI-H460, H4, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.902× | -2.8 | 0.098 | 10/46 (A498, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 415. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 65.5 | 3 (1 ⚠) | 11 (9 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.75× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -20.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.427× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 119 | 0 | 11 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.204× (z -24.6) |
| [[C-33 A (line)]] | alt | 336 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0876× (z -25.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 50.1 | 1 | 8 (8 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.51× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.273× (z -12.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[LoVo (line)]] | wt | 129 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.178× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~67% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.581× (z -9.6) |
| [[SW1417 (line)]] | alt | 96.8 | 0 | 9 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -11.8) |
| [[SW480 (line)]] | alt | 69.8 | 2 | 6 (6 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.33× (z +10.2) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.169× (z -21.7) ⚠ cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 86.9 | 4 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.67× (z +12.4) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -9.4) |
| [[HT-29 (line)]] | alt | 54.8 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.62× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[LS 180 (line)]] | wt | 86.1 | 2 | 4 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.69× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SW48 (line)]] | wt | 102 | 0 | 6 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -13.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 55.5 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -19.9) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -12.6) |
| [[CHP-212 (line)]] | wt | 247 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0754× (z -21.2) |
| [[HS-578T (line)]] | alt | 48.5 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.222× (z -13.2) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -8.5) |
| [[NCI-H1792 (line)]] | alt | 83.4 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -13.2) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.420× (z -11.2) |
| [[SW 900 (line)]] | alt | 95.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -20.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -14.8) |
| [[CFPAC-1 (line)]] | alt | 25.4 | 4 (2 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.49× (z +11.0) | — |
| [[Hs 766T (line)]] | wt | 77.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.190× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.7) |
| [[J82 (line)]] | alt | 83.4 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -10.1) |
| [[KATO III (line)]] | alt | 81.4 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.24× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.251× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H661 (line)]] | alt | 244 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.311× (z -10.6) |
| [[RKO (line)]] | wt | 88.6 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.195× (z -14.8) ⚠ toxic; cell-cycle shift, explains ~37% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.7) |
| [[SNU-423 (line)]] | alt | 60.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0499× (z -22.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[A549 (line)]] | wt | 61.3 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -18.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HepG2_C3A (line)]] | wt | 121 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.300× (z -11.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.437× (z -11.0) |
| [[LOX-IMVI (line)]] | wt | 38.7 | 2 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.09× (z +8.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.372× (z -8.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.105× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[A-172 (line)]] | wt | 82.5 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -9.6) |
| [[A-427 (line)]] | wt | 71.2 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -10.4) |
| [[H4 (line)]] | wt | 30.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.85× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0895× (z -17.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 34.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.50× (z +11.0) | — |
| [[Panc 03.27 (line)]] | alt | 68.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -19.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 77.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.391× (z -10.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 45.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.306× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[BT-474 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -9.2) ⚠ cell-cycle shift, explains ~50% of this change |
| [[hTERT-HPNE (line)]] | wt | 64.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[SHP-77 (line)]] | alt | 108 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.390× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[AN3 CA (line)]] | alt | 88.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 76.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 415), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EXOC6B]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SERAC1]] | +0.61 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[SPIRE1]] | +0.59 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ST6GALNAC6]] | +0.58 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A29]] | +0.58 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[PACC1]] | +0.58 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[TANGO2]] | +0.57 | +0.62 / +0.46 | both halves | 2e-05 |  |
| [[LDAF1]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[EVI5]] | +0.56 | +0.57 / +0.47 | both halves | 2e-05 |  |
| [[ANO10]] | +0.56 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[BLVRA]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[CDYL]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PER2]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[DDX39B]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[LINS1]] | -0.51 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[COG4]] | -0.51 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[EP300]] | -0.51 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[HNRNPUL1]] | -0.50 | -0.45 / -0.40 | both halves | 5e-05 |  |
| [[SKA2]] | -0.50 | -0.57 / -0.35 | both halves | 1e-04 |  |
| [[CBX5]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[KIAA0753]] | -0.50 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[PRKAR1A]] | -0.49 | -0.44 / -0.41 | both halves | 4e-05 | pathway: Intracellular signaling by second messengers |
| [[SNHG31]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[COQ9]] | -0.49 | -0.51 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers GAB2's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, GSK1059615, Rapamycin, Sapanisertib) | 62% of the class's compounds vs 4.8% of all compounds | 0.020 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises GAB2's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LRP3]] | B | LRP3 activity raises GAB2's level | lines that do not express LRP3 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without LRP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: ACBD7, SNTA1, TMCC2; maybe low, not absent |
| [[PLEKHO1]] | B | PLEKHO1 activity raises GAB2's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 1.46× lower at baseline in the lines without PLEKHO1 | 0.093 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Menadione (drug)]] 0.5 µM | C | GAB2's natural level raises the cells' numbers under Menadione 0.5 µM (protects the cells) | GAB2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.73 | 0.250 over the table, 0.009 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 115]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.530). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (0.6, 1.9); signed map (-27.4, 4.4). **Vector** length 132, 41.2% of its response variance represented; |z| ≥ 3 in 1,414 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +12.0 | +14.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.5 | +12.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +10.4 | +10.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +7.4 | +8.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +6.5 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +5.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.9 | +5.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.6 | +6.1 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.9 | -15.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | -6.6 | -13.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.7 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -5.7 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -15.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -9.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -2.9 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.3 | +0.3 |
|  | [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | GRB2 associated binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:78,215,293-78,418,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0571 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 40 pathways, smallest: STAT5 Activation; STAT5 activation downstream of FLT3 ITD mutants; Interleukin-15 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQC2](https://www.uniprot.org/uniprotkb/Q9UQC2) (GRB2-associated-binding protein 2):

> Adapter protein which acts downstream of several membrane receptors including cytokine, antigen, hormone, cell matrix and growth factor receptors to regulate multiple signaling pathways. Regulates osteoclast differentiation mediating the TNFRSF11A/RANK signaling. In allergic response, it plays a role in mast cells activation and degranulation through PI-3-kinase regulation. Also involved in the regulation of cell proliferation and hematopoiesis.

**Summary**, from NCBI Gene [9846](https://www.ncbi.nlm.nih.gov/gene/9846):

> This gene is a member of the GRB2-associated binding protein (GAB) gene family. These proteins contain pleckstrin homology (PH) domain, and bind SHP2 tyrosine phosphatase and GRB2 adapter protein. They act as adapters for transmitting various signals in response to stimuli through cytokine and growth factor receptors, and T- and B-cell antigen receptors. The protein encoded by this gene is the principal activator of phosphatidylinositol-3 kinase in response to activation of the high affinity …

**Accessions** — [HGNC:14458](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14458) · Entrez [9846](https://www.ncbi.nlm.nih.gov/gene/9846) · UniProt [Q9UQC2](https://www.uniprot.org/uniprotkb/Q9UQC2) · Ensembl [ENSG00000033327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000033327)

## Data

Gene col 415: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 415); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 415, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 415]; `tensor/DDL_lfc|DDL_z.npy` [415]; `embed/gene_vectors.npy` [415]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 415 or target_col == 415). Every well: [[GAB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
