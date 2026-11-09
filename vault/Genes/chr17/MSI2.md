---
symbol: "MSI2"
type: "gene"
col: 7754
ensembl_id: "ENSG00000153944"
name: "musashi RNA binding protein 2"
location: "17q22"
module: 29
arm: "+"
pooled_cpm: 284.93
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# MSI2

*musashi RNA binding protein 2* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Anethole trithione (drug)]] 5 µM: 1.18× (z +5.1, q 2e-04, up in 14 of 46 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 4 lines (A498 3.74×, A549 2.12×, NCI-H1573 2.03×, HOP62 2.17×; ⚠ cell-cycle shift, explains ~35% of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 1.28×, HOP62 1.26×; ⚠ position not correctable); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A498 3.87×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.20×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 1.58×).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.482× (z -22.4, q 0e+00, down in 38 of 46 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.394× (z -20.2, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LAPTM4B]] (+0.60, fdr 1e-05), [[NFIA]] (+0.56, fdr 3e-05), [[PON2]] (+0.54, fdr 1e-05); moves opposite to [[ZNF674]] (-0.54, fdr 2e-05), [[BTG1]] (-0.54, fdr 3e-05), [[HMGN2P46]] (-0.53, fdr 3e-05).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → cells under [[Clofarabine (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7754.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 8 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Ixazomib citrate (drug)]] 5 µM in 4 lines (A498 3.74×, A549 2.12×, NCI-H1573 2.03×, HOP62 2.17×; ⚠ cell-cycle shift, explains ~35% of this change); [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 1.28×, HOP62 1.26×; ⚠ position not correctable); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (A498 3.87×); [[Ponatinib (drug)]] 5 µM in 1 line (C32 2.20×); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A498 1.58×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | 1.18× | +5.1 | 2e-04 | 14/46 (HEC-1-A, SHP-77, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.21×** | +4.1 | 0.010 | 24/46 (A498, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.20×** | +4.0 | 0.014 | 22/46 (A498, A-172, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.19× | +3.6 | 0.042 | 21/47 (SNU-423, J82, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.5 | 0.046 | 20/46 (HOP62, PANC-1, …) | rises with dose |  |
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.046 | 12/46 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.17× | +3.4 | 0.046 | 16/46 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |
| [[Folic acid (drug)]] 5 µM |  | 1.11× | +3.3 | 0.076 | 4/46 (LS 180, COLO 205, …) | rises with dose |  |
| [[Minodronic acid (drug)]] 0.05 µM |  | 1.17× | +3.2 | 0.076 | 15/46 (HS-578T, Panc 03.27, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.16× | +3.2 | 0.091 | 14/47 (J82, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Budesonide (drug)]] 5 µM |  | 1.15× | +3.0 | 0.12 | 18/46 (HOP62, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 14 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.482×** | -22.4 | 0e+00 | 38/46 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.394×** | -20.2 | 0e+00 | 41/46 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.424×** | -18.6 | 0e+00 | 43/46 (SW480, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -17.5 | 0e+00 | 40/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.533×** | -13.7 | 2e-40 | 40/46 (SW480, LoVo, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.540×** | -12.9 | 7e-36 | 40/45 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.605×** | -10.5 | 8e-24 | 30/46 (NCI-H460, A549, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.715×** | -10.3 | 4e-23 | 28/47 (HepG2/C3A, SW480, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.634×** | -9.9 | 3e-21 | 36/46 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.706×** | -7.5 | 3e-12 | 32/46 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -6.0 | 9e-08 | 29/46 (SW480, CHP-212, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.784×** | -5.3 | 6e-06 | 24/46 (SK-MEL-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~65% of this change | **0.788×** | -5.2 | 1e-05 | 30/46 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.637×** | -5.1 | 1e-05 | 33/46 (SW 900, HepG2/C3A, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.808×** | -4.6 | 1e-04 | 25/47 (KATO III, RKO, …) | top dose only |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.876× | -4.1 | 0.002 | 3/47 (RKO, HS-578T, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.830×** | -3.9 | 0.003 | 18/46 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.904× | -3.1 | 0.041 | 14/47 (KATO III, CHP-212, …) | all doses, flat |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.869× | -3.1 | 0.045 | 20/46 (PANC-1, CHP-212, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 907 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -20.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.147× (z -20.2) |
| [[SK-MEL-2 (line)]] | alt | 729 | 0 | 10 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.198× (z -18.3) |
| [[A549 (line)]] | wt | 270 | 1 (1 ⚠) | 8 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.12× (z +10.0) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -22.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.311× (z -15.5) |
| [[COLO 205 (line)]] | alt | 753 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -31.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 293 | 0 | 9 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 188 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -26.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.283× (z -20.3) |
| [[A-172 (line)]] | wt | 501 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.227× (z -14.4) |
| [[A498 (line)]] | wt | 122 | 6 (4 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.87× (z +18.5) | [[Homoharringtonine (drug)]] 5 µM 0.469× (z -14.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.528× (z -8.7) |
| [[SW480 (line)]] | alt | 541 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -23.2) |
| [[HepG2_C3A (line)]] | wt | 635 | 0 | 7 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.248× (z -18.5) |
| [[KATO III (line)]] | alt | 381 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -14.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.296× (z -12.0) |
| [[LOX-IMVI (line)]] | wt | 245 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -14.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 135 | 2 (2 ⚠) | 5 (1 ⚠) | [[Bortezomib (drug)]] 5 µM 4.30× (z +9.8) ⚠ toxic; cell-cycle shift, explains ~91% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -18.1) |
| [[SW 900 (line)]] | alt | 229 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -21.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.258× (z -18.2) |
| [[C32 (line)]] | wt | 269 | 1 | 5 (2 ⚠) | [[Ponatinib (drug)]] 5 µM 2.20× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -16.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.515× (z -11.4) |
| [[CHP-212 (line)]] | wt | 839 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.396× (z -12.9) |
| [[hTERT-HPNE (line)]] | wt | 204 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 217 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.182× (z -22.7) |
| [[SHP-77 (line)]] | alt | 440 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.375× (z -14.0) |
| [[SW1417 (line)]] | alt | 340 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -16.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.293× (z -14.8) |
| [[HS-578T (line)]] | alt | 189 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -14.6) |
| [[HT-29 (line)]] | alt | 289 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.325× (z -14.5) |
| [[MIA PaCa-2 (line)]] | alt | 177 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.378× (z -12.1) |
| [[NCI-H23 (line)]] | alt | 174 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.291× (z -14.7) |
| [[PANC-1 (line)]] | alt | 104 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -24.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -16.7) |
| [[RKO (line)]] | wt | 245 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.439× (z -10.5) |
| [[A-427 (line)]] | wt | 256 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.373× (z -14.0) |
| [[H4 (line)]] | wt | 178 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +8.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 348 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.424× (z -13.0) |
| [[HOP62 (line)]] | alt | 172 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.17× (z +8.8) ⚠ cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -13.1) |
| [[LS 180 (line)]] | wt | 379 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -16.1) |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.0) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.277× (z -15.5) |
| [[SNU-1 (line)]] | wt | 473 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.345× (z -11.9) |
| [[SW48 (line)]] | wt | 382 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.230× (z -14.1) |
| [[AsPC-1 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.494× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.371× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.319× (z -13.7) |
| [[J82 (line)]] | alt | 119 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 1.99× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.583× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 190 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -13.6) |
| [[SW 1088 (line)]] | alt | 126 | 0 | 2 | — | [[Silodosin (drug)]] 0.05 µM 0.0673× (z -10.0) |
| [[AN3 CA (line)]] | alt | 302 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.2) |
| [[BT-474 (line)]] | alt | 484 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -9.9) |
| [[SNU-423 (line)]] | alt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.308× (z -11.1) |
| [[C-33 A (line)]] | alt | 253 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 405 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 65.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 345 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*58 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LAPTM4B]] | +0.60 | +0.66 / +0.49 | both halves | 1e-05 |  |
| [[NFIA]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PON2]] | +0.54 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[PLBD1]] | +0.54 | +0.39 / +0.60 | both halves | 5e-05 |  |
| [[STT3B]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[PFKM]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[MEST]] | +0.53 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[GSTK1]] | +0.52 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[NAA50]] | +0.52 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[GSR]] | +0.52 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[OSBPL1A]] | +0.52 | +0.48 / +0.42 | both halves | 4e-05 |  |
| [[RAVER2]] | +0.51 | +0.53 / +0.44 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*42 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF674]] | -0.54 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[BTG1]] | -0.54 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[HMGN2P46]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[RSPH3]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[FOXD1]] | -0.51 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[MFAP1]] | -0.50 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[DNTTIP1]] | -0.50 | -0.39 / -0.42 | both halves | 6e-05 |  |
| [[BCL10]] | -0.50 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ZNF699]] | -0.49 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[RAP2B]] | -0.49 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[BCL2A1]] | -0.49 | -0.40 / -0.47 | both halves | 4e-05 |  |
| [[HELQ]] | -0.49 | -0.58 / -0.55 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Clofarabine (drug)]] 0.5 µM | C | MSI2's natural level raises the cells' numbers under Clofarabine 0.5 µM (protects the cells) | MSI2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.61 | 0.470 over the table, 0.074 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.510). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-26.3, -19.9); signed map (-21.1, -41.2). **Vector** length 122, 38.6% of its response variance represented; |z| ≥ 3 in 1,648 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +12.7 | -1.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +11.1 | -2.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +9.0 | -1.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +6.8 | +4.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +5.7 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.7 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +4.5 | +2.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.1 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.8 | -20.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.9 | -9.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.2 | -7.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -3.9 | -10.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.8 | -2.8 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -3.7 | -1.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.6 | -3.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.5 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | musashi RNA binding protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:57,255,851-57,684,689 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | RNA binding motif containing; Musashi RNA binding protein family |
| Reactome | 5 pathways, smallest: RHOBTB2 GTPase cycle; RHOBTB GTPase Cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DH6](https://www.uniprot.org/uniprotkb/Q96DH6) (RNA-binding protein Musashi homolog 2):

> RNA binding protein that regulates the expression of target mRNAs at the translation level. May play a role in the proliferation and maintenance of stem cells in the central nervous system (By similarity).

**Summary**, from NCBI Gene [124540](https://www.ncbi.nlm.nih.gov/gene/124540):

> This gene encodes an RNA-binding protein that is a member of the Musashi protein family. The encoded protein is transcriptional regulator that targets genes involved in development and cell cycle regulation. Mutations in this gene are associated with poor prognosis in certain types of cancers. This gene has also been shown to be rearranged in certain cancer cells. [provided by RefSeq, Apr 2016]

**Accessions** — [HGNC:18585](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18585) · Entrez [124540](https://www.ncbi.nlm.nih.gov/gene/124540) · UniProt [Q96DH6](https://www.uniprot.org/uniprotkb/Q96DH6) · Ensembl [ENSG00000153944](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000153944)

## Data

Gene col 7754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7754); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7754]; `tensor/DDL_lfc|DDL_z.npy` [7754]; `embed/gene_vectors.npy` [7754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7754 or target_col == 7754). Every well: [[MSI2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MSI2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
