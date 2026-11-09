---
symbol: "MLEC"
type: "gene"
col: 3179
ensembl_id: "ENSG00000110917"
name: "malectin"
location: "12q24.31"
module: 42
arm: "+"
pooled_cpm: 172.26
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 13
n_dd_up_clean: 6
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/042"]
generated_by: "tahoemap"
---

# MLEC

*malectin* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.56× (z +19.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.509× (z -14.2, q 5e-43, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[P3H1]] (+0.81, fdr 7e-06), [[TMED4]] (+0.78, fdr 7e-06), [[PDIA6]] (+0.78, fdr 7e-06); moves opposite to [[ZNF480]] (-0.69, fdr 7e-06), [[ZNF594]] (-0.69, fdr 7e-06), [[GLRX2]] (-0.69, fdr 7e-06).
> It is in [[Module 042]], a single-armed module (UPR ER).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 14 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3179.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.56×** | +19.9 | 0e+00 | 48/49 (NCI-H460, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.28×** | +12.9 | 1e-35 | 47/48 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.23×** | +12.5 | 1e-33 | 47/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | **2.20×** | +12.3 | 2e-32 | 47/49 (SNU-423, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **2.22×** | +12.0 | 7e-31 | 43/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **2.13×** | +11.8 | 3e-30 | 47/48 (LOX-IMVI, AsPC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.77×** | +8.5 | 1e-15 | 45/50 (NCI-H460, A-172, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.62×** | +7.3 | 3e-11 | 37/48 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~70% of this change | **1.64×** | +7.2 | 5e-11 | 38/45 (SNU-423, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **1.52×** | +6.3 | 2e-08 | 39/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.49×** | +6.2 | 3e-08 | 42/48 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.0 | 8e-08 | 31/48 (A-172, BT-474, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.39×** | +5.2 | 9e-06 | 37/48 (HepG2/C3A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.34×** | +4.6 | 2e-04 | 32/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.73×** | +4.5 | 3e-04 | 40/49 (LOX-IMVI, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.012 | 27/48 (A549, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.033 | 32/48 (SNU-423, H4, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.051 | 22/49 (LoVo, KATO III, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠; shown: the 15 strongest. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3179.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.509×** | -14.2 | 5e-43 | 45/48 (A-172, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.408×** | -13.5 | 8e-39 | 47/48 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.519×** | -10.2 | 3e-22 | 44/48 (A498, AN3 CA, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.596×** | -8.1 | 1e-13 | 42/48 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.656×** | -6.6 | 5e-09 | 39/48 (LS 180, A-172, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.903× | -5.4 | 6e-06 | 1/50 (CHP-212) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.730×** | -4.7 | 2e-04 | 39/47 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.765×** | -4.2 | 0.002 | 35/48 (LS 180, hTERT-HPNE, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.756×** | -4.1 | 0.002 | 27/47 (A498, RKO, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.768×** | -4.1 | 0.002 | 31/49 (C32, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.627×** | -3.8 | 0.007 | 33/49 (J82, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.786×** | -3.7 | 0.008 | 25/47 (SK-MEL-2, COLO 205, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.848× | -3.5 | 0.017 | 22/48 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.662×** | -3.4 | 0.031 | 29/50 (J82, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 0.855× | -3.3 | 0.039 | 19/48 (LS 180, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.64 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3179. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 119 | 9 (7 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +17.3) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -24.4) |
| [[KATO III (line)]] | alt | 235 | 6 (5 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.67× (z +12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -17.5) |
| [[LS 180 (line)]] | wt | 508 | 3 (3 ⚠) | 8 (3 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -17.5) |
| [[PANC-1 (line)]] | alt | 161 | 8 (7 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 3.05× (z +13.8) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -15.8) |
| [[A549 (line)]] | wt | 130 | 8 (6 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +19.5) | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 146 | 8 (7 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +20.9) | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 155 | 6 (5 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 135 | 9 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.41× (z +15.9) | — |
| [[RKO (line)]] | wt | 178 | 6 (5 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.03× (z +17.2) | [[Harringtonine (drug)]] 5 µM 0.224× (z -16.5) |
| [[SNU-423 (line)]] | alt | 84.4 | 9 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.79× (z +16.7) | — |
| [[SW480 (line)]] | alt | 122 | 9 (8 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +18.2) | — |
| [[A498 (line)]] | wt | 271 | 3 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.87× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -19.0) |
| [[J82 (line)]] | alt | 166 | 5 (4 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 182 | 4 (3 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +15.8) | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -14.3) |
| [[NCI-H460 (line)]] | wt | 121 | 8 (7 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +22.5) | — |
| [[Panc 03.27 (line)]] | alt | 79.0 | 7 (6 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +16.1) | [[Harringtonine (drug)]] 5 µM 0.409× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 128 | 6 (5 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 4.21× (z +14.7) ⚠ cell-cycle shift, explains ~51% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +13.5) | [[Harringtonine (drug)]] 0.5 µM 0.437× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 129 | 4 (3 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +14.5) | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -11.2) |
| [[HOP62 (line)]] | alt | 166 | 5 (4 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 197 | 2 (1 ⚠) | 5 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +11.6) | [[Harringtonine (drug)]] 5 µM 0.296× (z -11.8) |
| [[NCI-H1792 (line)]] | alt | 136 | 7 (6 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +14.0) | — |
| [[NCI-H2030 (line)]] | alt | 158 | 5 (4 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +13.1) | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -12.2) |
| [[SK-MEL-2 (line)]] | alt | 150 | 5 (4 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +14.6) | [[Harringtonine (drug)]] 5 µM 0.227× (z -15.5) |
| [[SW1417 (line)]] | alt | 237 | 5 (4 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.591× (z -9.3) |
| [[A-427 (line)]] | wt | 120 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -18.0) |
| [[Hs 766T (line)]] | wt | 95.9 | 6 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 184 | 3 (2 ⚠) | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +12.7) | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -15.0) |
| [[HepG2_C3A (line)]] | wt | 133 | 4 (3 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +13.4) | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -12.1) |
| [[LoVo (line)]] | wt | 284 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +15.3) | [[Harringtonine (drug)]] 5 µM 0.204× (z -17.4) |
| [[NCI-H23 (line)]] | alt | 196 | 3 (2 ⚠) | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -16.8) |
| [[C-33 A (line)]] | alt | 136 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +10.5) | [[Harringtonine (drug)]] 5 µM 0.411× (z -8.8) |
| [[C32 (line)]] | wt | 226 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +11.0) | [[Homoharringtonine (drug)]] 0.05 µM 0.392× (z -8.6) |
| [[H4 (line)]] | wt | 242 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -16.2) |
| [[SW 900 (line)]] | alt | 203 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -9.9) |
| [[BT-474 (line)]] | alt | 129 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.92× (z +14.6) | — |
| [[COLO 205 (line)]] | alt | 236 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +9.6) | — |
| [[HT-29 (line)]] | alt | 211 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.567× (z -9.1) |
| [[SHP-77 (line)]] | alt | 154 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +10.3) | — |
| [[SW48 (line)]] | wt | 152 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +15.5) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -8.8) |
| [[AN3 CA (line)]] | alt | 161 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.5) | [[Homoharringtonine (drug)]] 0.5 µM 0.0819× (z -18.2) |
| [[NCI-H1573 (line)]] | alt | 148 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.05× (z +9.7) | [[Harringtonine (drug)]] 5 µM 0.253× (z -13.1) |
| [[RPMI-7951 (line)]] | alt | 158 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.65× (z +13.5) | [[Harringtonine (drug)]] 5 µM 0.285× (z -12.3) |
| [[CHP-212 (line)]] | wt | 144 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 185 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.1) | — |
| [[SNU-1 (line)]] | wt | 174 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +13.8) | — |
| [[SW 1088 (line)]] | alt | 216 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 166 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 138 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3179), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[P3H1]] | +0.81 | +0.79 / +0.77 | both halves | 7e-06 |  |
| [[TMED4]] | +0.78 | +0.78 / +0.72 | both halves | 7e-06 |  |
| [[PDIA6]] | +0.78 | +0.81 / +0.73 | both halves | 7e-06 |  |
| [[PDIA3]] | +0.76 | +0.81 / +0.75 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PDIA4]] | +0.73 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[HSP90B1]] | +0.71 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[SDHA]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[DDOST]] | +0.70 | +0.75 / +0.67 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 984 |
| [[TM9SF2]] | +0.69 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[GLG1]] | +0.69 | +0.74 / +0.63 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.69 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[RPN2]] | +0.69 | +0.67 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 991 |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF480]] | -0.69 | -0.67 / -0.63 | both halves | 7e-06 |  |
| [[ZNF594]] | -0.69 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[GLRX2]] | -0.69 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[KCNMB3]] | -0.68 | -0.64 / -0.64 | both halves | 7e-06 |  |
| [[METTL18]] | -0.67 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[NT5C]] | -0.65 | -0.60 / -0.63 | both halves | 7e-06 |  |
| [[THG1L]] | -0.64 | -0.67 / -0.50 | both halves | 1e-05 |  |
| [[MRPL58]] | -0.63 | -0.67 / -0.58 | both halves | 7e-06 |  |
| [[TIAM2]] | -0.63 | -0.61 / -0.55 | both halves | 1e-05 |  |
| [[MAPK1IP1L]] | -0.63 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[TRMT10B]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[ZSCAN29]] | -0.63 | -0.65 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MLEC's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 042]] — UPR ER; 103 genes; every member is in the + arm (projection on the module's main direction 0.783). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.8, -19.5); signed map (-55.1, 6.1). **Vector** length 145, 57.9% of its response variance represented; |z| ≥ 3 in 1,416 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *UPR ER* (control, mean cos +0.61 to 11); *Maturation of DENV proteins* (reactome, mean cos +0.59 to 11); *Dengue Virus Genome Translation and Replication* (reactome, mean cos +0.58 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.7 | +19.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | +5.6 | +11.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | +5.5 | +4.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +5.0 | +8.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +4.4 | +7.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +4.5 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +2.7 | +1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | +2.4 | +1.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -16.2 | -13.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -14.5 | -10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -14.3 | -14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -13.5 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -10.2 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -6.0 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -3.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | malectin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:120,687,149-120,701,859 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously KIAA0152 |
| Reactome | 4 pathways, smallest: N-glycan trimming in the ER and Calnexin/Calreticulin cycle; Asparagine N-linked glycosylation; Neutrophil degranulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14165](https://www.uniprot.org/uniprotkb/Q14165) (Malectin):

> Carbohydrate-binding protein with a strong ligand preference for Glc2-N-glycan. May play a role in the early steps of protein N-glycosylation (By similarity).

**Summary**, from NCBI Gene [9761](https://www.ncbi.nlm.nih.gov/gene/9761):

> This gene encodes the carbohydrate-binding protein malectin which is a Type I membrane-anchored endoplasmic reticulum protein. This protein has an affinity for Glc2Man9GlcNAc2 (G2M9) N-glycans and is involved in regulating glycosylation in the endoplasmic reticulum. This protein has also been shown to interact with ribophorin I and may be involved in the directing the degradation of misfolded proteins. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2015]

**Accessions** — [HGNC:28973](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28973) · Entrez [9761](https://www.ncbi.nlm.nih.gov/gene/9761) · UniProt [Q14165](https://www.uniprot.org/uniprotkb/Q14165) · Ensembl [ENSG00000110917](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110917)

## Data

Gene col 3179: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3179); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3179, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3179]; `tensor/DDL_lfc|DDL_z.npy` [3179]; `embed/gene_vectors.npy` [3179]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3179 or target_col == 3179). Every well: [[MLEC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MLEC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
