---
symbol: "NIN"
type: "gene"
col: 1974
ensembl_id: "ENSG00000100503"
name: "ninein"
location: "14q22.1"
module: 118
arm: "-"
pooled_cpm: 108.03
n_lines_expressing: 49
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/118"]
generated_by: "tahoemap"
---

# NIN

*ninein* — 14q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.49× (z +10.5, q 3e-23, up in 33 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.18× (z +6.1, q 4e-07, up in 20 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 2.87×, SW1417 2.07×, HOP62 2.31×, SK-MEL-2 2.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 2.95×, SW1417 1.85×, HOP62 2.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (CFPAC-1 3.28×, NCI-H2030 1.98×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 2.27×, hTERT-HPNE 1.79×); [[Tucidinostat (drug)]] 5 µM in 2 lines (SW 900 1.84×, CFPAC-1 1.94×).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.687× (z -13.9, q 2e-41, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSX2IP]] (+0.64, fdr 1e-05), [[KIF2A]] (+0.64, fdr 7e-06), [[KPNA3]] (+0.63, fdr 7e-06); moves opposite to [[RSL1D1-DT]] (-0.66, fdr 1e-05), [[YJU2B]] (-0.59, fdr 1e-05), [[PCF11-AS1]] (-0.57, fdr 2e-05).
> It sits in the **-** arm of [[Module 118]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1974.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 6 lines (SNU-423 2.87×, SW1417 2.07×, HOP62 2.31×, SK-MEL-2 2.22×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (SNU-423 2.95×, SW1417 1.85×, HOP62 2.10×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (CFPAC-1 3.28×, NCI-H2030 1.98×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CFPAC-1 2.27×, hTERT-HPNE 1.79×); [[Tucidinostat (drug)]] 5 µM in 2 lines (SW 900 1.84×, CFPAC-1 1.94×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +10.5 | 3e-23 | 33/48 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +6.1 | 4e-07 | 20/47 (SW 900, CFPAC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.52×** | +5.8 | 2e-06 | 28/48 (CFPAC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.24×** | +5.5 | 4e-06 | 23/43 (SNU-423, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +5.4 | 7e-06 | 23/47 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.17× | +4.1 | 0.004 | 21/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.16× | +3.9 | 0.008 | 11/47 (J82, A-427, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.016 | 19/47 (NCI-H2347, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.14× | +3.5 | 0.025 | 15/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.14× | +3.5 | 0.025 | 13/47 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.3 | 0.045 | 17/44 (NCI-H1792, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 1.09× | +3.1 | 0.077 | 1/48 (H4) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.1 | 0.086 | 8/48 (NCI-H2347, SW 900, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1974.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.687×** | -13.9 | 2e-41 | 29/47 (NCI-H1573, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.434×** | -11.5 | 4e-28 | 42/48 (SW 900, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.662×** | -10.8 | 5e-25 | 33/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.676×** | -10.3 | 1e-22 | 37/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.684×** | -10.0 | 2e-21 | 31/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.779×** | -9.3 | 2e-18 | 31/47 (SW480, PANC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.731×** | -7.9 | 2e-13 | 27/46 (SNU-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.758×** | -7.3 | 2e-11 | 28/47 (SW480, SHP-77, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.783×** | -6.4 | 8e-09 | 23/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.848× | -6.1 | 5e-08 | 22/47 (NCI-H2030, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.673×** | -5.4 | 3e-06 | 27/47 (Panc 03.27, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.820×** | -5.0 | 3e-05 | 23/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.841× | -4.5 | 2e-04 | 17/47 (BT-474, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.853× | -4.0 | 0.003 | 18/47 (SW480, NCI-H2030, …) | top dose only |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.867× | -3.7 | 0.007 | 15/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.876× | -3.3 | 0.030 | 6/47 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | 0.878× | -3.1 | 0.042 | 13/46 (SW 1271, SNU-1, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | 0.848× | -3.1 | 0.051 | 11/47 (HepG2/C3A, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.854× | -3.0 | 0.074 | 11/47 (C-33 A, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1974. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 110 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -16.6) |
| [[SW480 (line)]] | alt | 142 | 0 | 9 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.598× (z -14.5) ⚠ cell-cycle shift, explains ~16% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.490× (z -14.2) |
| [[NCI-H1573 (line)]] | alt | 129 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -32.3) |
| [[NCI-H2030 (line)]] | alt | 125 | 1 (1 ⚠) | 7 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +8.9) ⚠ cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -23.0) |
| [[PANC-1 (line)]] | alt | 109 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.325× (z -18.1) |
| [[CFPAC-1 (line)]] | alt | 47.0 | 7 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.28× (z +10.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.7) | — |
| [[SW1417 (line)]] | alt | 142 | 2 (2 ⚠) | 4 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 85.5 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.9) |
| [[LOX-IMVI (line)]] | wt | 143 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -28.6) |
| [[NCI-H23 (line)]] | alt | 189 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -16.3) |
| [[RKO (line)]] | wt | 119 | 0 | 5 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -17.4) |
| [[SNU-1 (line)]] | wt | 165 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.225× (z -15.8) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.417× (z -13.6) |
| [[SW48 (line)]] | wt | 176 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -15.4) |
| [[A-427 (line)]] | wt | 131 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -19.2) |
| [[AN3 CA (line)]] | alt | 207 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.316× (z -9.9) |
| [[HepG2_C3A (line)]] | wt | 137 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.388× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.446× (z -8.6) |
| [[J82 (line)]] | alt | 151 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.464× (z -10.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.495× (z -10.1) |
| [[LoVo (line)]] | wt | 91.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.515× (z -14.1) |
| [[A549 (line)]] | wt | 124 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.548× (z -12.7) |
| [[HOP62 (line)]] | alt | 124 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +10.8) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 117 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.562× (z -9.7) |
| [[HS-578T (line)]] | alt | 84.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.537× (z -10.4) |
| [[HT-29 (line)]] | alt | 58.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.434× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 124 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.02× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.630× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 66.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.93× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 93.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +12.2) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 91.9 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 1.84× (z +10.0) | [[TAK-901 (drug)]] 5 µM 0.0928× (z -14.3) |
| [[A498 (line)]] | wt | 73.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.306× (z -9.0) |
| [[COLO 205 (line)]] | alt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 158 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +8.7) | — |
| [[LS 180 (line)]] | wt | 64.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.22× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H661 (line)]] | alt | 78.8 | 0 | 1 (1 ⚠) | — | [[Imiquimod (hydrochloride) (drug)]] 5 µM 0.0482× (z -14.1) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 108 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.01× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 143 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.496× (z -9.4) |
| [[SK-MEL-2 (line)]] | alt | 138 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +10.1) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 88.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 216 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 55.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 8.69 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 67.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 159 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1974), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSX2IP]] | +0.64 | +0.65 / +0.55 | both halves | 1e-05 | same gene group; STRING 505 |
| [[KIF2A]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 | STRING 837 |
| [[KPNA3]] | +0.63 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[NCK2]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_MITOTIC_SPINDLE |
| [[VPS13A]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CDCA7L]] | +0.61 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[R3HDM1]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[MAPK9]] | +0.57 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CEP78]] | +0.56 | +0.56 / +0.54 | both halves | 1e-05 | same gene group |
| [[SPAST]] | +0.55 | +0.46 / +0.51 | both halves | 3e-05 |  |
| [[SACS]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[EXOC2]] | +0.54 | +0.48 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSL1D1-DT]] | -0.66 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[YJU2B]] | -0.59 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[PCF11-AS1]] | -0.57 | -0.50 / -0.49 | both halves | 2e-05 |  |
| [[SYNRG]] | -0.57 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[ZNF226]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[ZSWIM3]] | -0.57 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[ZNF490]] | -0.56 | -0.51 / -0.40 | both halves | 5e-05 |  |
| [[NGDN]] | -0.55 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ZBTB8OS]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[ZNF586]] | -0.54 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[FBXL12]] | -0.54 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ANKRD42-DT]] | -0.53 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 118]]; 41 genes; this gene is in the **-** arm (projection on the module's main direction -0.592). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-6.4, -4.2); signed map (-19.3, -50.6). **Vector** length 125, 36.9% of its response variance represented; |z| ≥ 3 in 1,196 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.4 | +2.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~10% of this change | +6.4 | +5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +5.9 | +5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +4.3 | +4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.7 | +1.4 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -7.8 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.7 | -6.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -7.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.2 | -11.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -7.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -4.2 | -4.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ninein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.1 — chr14:50,719,763-50,831,162 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | EF-hand domain containing; Centriolar satellite proteins |
| Hallmark sets | KRAS_SIGNALING_UP, MITOTIC_SPINDLE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4C6](https://www.uniprot.org/uniprotkb/Q8N4C6) (Ninein):

> Centrosomal protein required in the positioning and anchorage of the microtubule minus-end in epithelial cells. May also act as a centrosome maturation factor. May play a role in microtubule nucleation, by recruiting the gamma-tubulin ring complex to the centrosome. Overexpression does not perturb nucleation or elongation of microtubules but suppresses release of microtubules. Required for centriole organization and microtubule anchoring at the mother centriole.

**Summary**, from NCBI Gene [51199](https://www.ncbi.nlm.nih.gov/gene/51199):

> This gene encodes one of the proteins important for centrosomal function. This protein is important for positioning and anchoring the microtubules minus-ends in epithelial cells. Localization of this protein to the centrosome requires three leucine zippers in the central coiled-coil domain. Multiple alternatively spliced transcript variants that encode different isoforms have been reported. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14906](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14906) · Entrez [51199](https://www.ncbi.nlm.nih.gov/gene/51199) · UniProt [Q8N4C6](https://www.uniprot.org/uniprotkb/Q8N4C6) · Ensembl [ENSG00000100503](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100503)

## Data

Gene col 1974: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1974); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1974, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1974]; `tensor/DDL_lfc|DDL_z.npy` [1974]; `embed/gene_vectors.npy` [1974]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1974 or target_col == 1974). Every well: [[NIN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
