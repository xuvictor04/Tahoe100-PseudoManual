---
symbol: "VPS36"
type: "gene"
col: 5811
ensembl_id: "ENSG00000136100"
name: "vacuolar protein sorting 36 homolog"
location: "13q14.3"
module: 25
arm: "+"
pooled_cpm: 56.97
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# VPS36

*vacuolar protein sorting 36 homolog* — 13q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.78× (z +16.7, q 0e+00, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 5 µM: 1.13× (z +4.8, q 1e-04, up in 9 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 2.46×, PANC-1 2.08×, SW480 1.83×, NCI-H23 2.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (HT-29 3.14×, PANC-1 2.20×, HCT15 3.63×, HEC-1-A 1.96×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.83×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.488× (z -20.8, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NAE1]] (+0.66, fdr 7e-06), [[PTAR1]] (+0.65, fdr 2e-05), [[DCAF17]] (+0.64, fdr 3e-05); moves opposite to [[ZKSCAN5]] (-0.58, fdr 1e-05), [[ZNF324]] (-0.53, fdr 2e-05), [[ZNF432]] (-0.53, fdr 2e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5811.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (HEC-1-A 2.46×, PANC-1 2.08×, SW480 1.83×, NCI-H23 2.33×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (HT-29 3.14×, PANC-1 2.20×, HCT15 3.63×, HEC-1-A 1.96×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A-427 2.83×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +16.7 | 0e+00 | 41/49 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.81×** | +16.5 | 0e+00 | 38/42 (HT-29, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.45×** | +9.9 | 6e-21 | 27/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.23×** | +5.8 | 1e-06 | 21/47 (LOX-IMVI, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +4.8 | 1e-04 | 9/48 (A-172, C32, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 1.12× | +4.6 | 4e-04 | 13/48 (SNU-423, Panc 03.27, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.17× | +4.5 | 6e-04 | 19/48 (LoVo, NCI-H2030, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.17× | +4.4 | 7e-04 | 14/48 (LoVo, A498, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +4.1 | 0.003 | 14/48 (CFPAC-1, AsPC-1, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.15× | +4.0 | 0.004 | 7/47 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.14× | +3.8 | 0.007 | 9/48 (NCI-H1573, NCI-H23, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.27×** | +3.7 | 0.012 | 8/43 (CFPAC-1, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.13× | +3.5 | 0.024 | 12/47 (C32, LS 180, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.027 | 10/48 (C32, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.12× | +3.4 | 0.027 | 11/48 (HCT15, CFPAC-1, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.036 | 11/48 (NCI-H23, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.11× | +3.0 | 0.090 | 6/49 (KATO III, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Verteporfin (drug)]] 5 µM |  | 1.11× | +3.0 | 0.090 | 10/47 (J82, BT-474, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.05 µM |  | 1.11× | +2.9 | 0.098 | 2/48 (HT-29, SK-MEL-2) | inconsistent across doses |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 1.11× | +2.9 | 0.098 | 4/47 (SNU-1, HEC-1-A, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | 1.11× | +2.9 | 0.098 | 7/47 (HT-29, NCI-H460, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5811.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.488×** | -20.8 | 0e+00 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.492×** | -20.6 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.515×** | -19.3 | 0e+00 | 45/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.641×** | -18.2 | 0e+00 | 40/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.637×** | -13.1 | 3e-37 | 44/48 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.775×** | -10.5 | 1e-23 | 29/48 (A-427, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.700×** | -10.4 | 3e-23 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.809×** | -8.7 | 2e-16 | 25/48 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.745×** | -8.2 | 1e-14 | 28/50 (PANC-1, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.804×** | -6.1 | 7e-08 | 23/47 (SW480, A498, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.829×** | -5.5 | 3e-06 | 16/48 (SW480, J82, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.843× | -5.0 | 3e-05 | 18/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.734×** | -4.7 | 1e-04 | 21/49 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.846× | -4.7 | 1e-04 | 22/48 (NCI-H1573, NCI-H460, …) | top dose only | composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.863× | -4.3 | 7e-04 | 14/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.05 µM |  | 0.871× | -4.0 | 0.002 | 8/48 (SW480, LS 180, …) | all doses, stronger at high dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.918× | -3.5 | 0.013 | 10/48 (A498, HT-29, …) | top dose only |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.895× | -3.2 | 0.035 | 10/47 (SW 1271, PANC-1, …) | two highest doses |  |
| [[Cytarabine (drug)]] 0.05 µM |  | 0.891× | -3.1 | 0.050 | 8/48 (LS 180, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.818×** | -3.0 | 0.057 | 16/49 (PANC-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5811. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 71.1 | 2 (2 ⚠) | 8 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.20× (z +12.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.425× (z -19.2) |
| [[NCI-H460 (line)]] | wt | 53.7 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.496× (z -14.3) |
| [[SW480 (line)]] | alt | 94.6 | 1 (1 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +10.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.400× (z -15.3) |
| [[HEC-1-A (line)]] | alt | 72.5 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.46× (z +12.2) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.562× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 42.4 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.13× (z +8.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -12.6) |
| [[A498 (line)]] | wt | 47.3 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.8) |
| [[HT-29 (line)]] | alt | 77.8 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.14× (z +12.8) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -10.3) |
| [[LoVo (line)]] | wt | 76.0 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 1.73× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.435× (z -13.4) |
| [[MIA PaCa-2 (line)]] | alt | 74.7 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -22.2) |
| [[NCI-H1573 (line)]] | alt | 86.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -16.1) |
| [[A-427 (line)]] | wt | 48.4 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 2.83× (z +9.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.362× (z -10.4) |
| [[A549 (line)]] | wt | 49.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -12.6) |
| [[KATO III (line)]] | alt | 84.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.366× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 66.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.378× (z -11.6) |
| [[LS 180 (line)]] | wt | 78.4 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -9.9) |
| [[SW1417 (line)]] | alt | 56.4 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -11.8) |
| [[SW48 (line)]] | wt | 104 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -10.0) |
| [[HCT15 (line)]] | alt | 63.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 65.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +9.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -11.0) |
| [[SNU-1 (line)]] | wt | 106 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.342× (z -10.3) |
| [[AN3 CA (line)]] | alt | 61.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 48.1 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.381× (z -9.3) |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.314× (z -9.0) |
| [[CHP-212 (line)]] | wt | 49.8 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.266× (z -8.7) |
| [[HOP62 (line)]] | alt | 31.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.43× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 34.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.449× (z -8.8) |
| [[SNU-423 (line)]] | alt | 35.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.45× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 38.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 47.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 67.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 35.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 44.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5811), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAE1]] | +0.66 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[PTAR1]] | +0.65 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[DCAF17]] | +0.64 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[NELFCD]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[TNPO1]] | +0.64 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[RAB11FIP2]] | +0.63 | +0.55 / +0.71 | both halves | 1e-05 |  |
| [[VRK2]] | +0.62 | +0.70 / +0.54 | both halves | 1e-05 |  |
| [[USP46]] | +0.62 | +0.46 / +0.64 | both halves | 2e-05 |  |
| [[TSEN15]] | +0.62 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MRPL42]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[NUDT3]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[PPA2]] | +0.59 | +0.42 / +0.61 | both halves | 4e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZKSCAN5]] | -0.58 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[ZNF324]] | -0.53 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[ZNF432]] | -0.53 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[MAP3K9-DT]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[TUBA4A]] | -0.52 | -0.33 / -0.63 | both halves | 1e-04 | pathway: HCMV Infection |
| [[DOK3]] | -0.52 | -0.50 / -0.46 | both halves | 3e-05 |  |
| [[ZNF200]] | -0.52 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[TRPT1]] | -0.52 | -0.22 / -0.62 | both halves | 6e-04 |  |
| [[SLC16A3]] | -0.52 | -0.39 / -0.57 | both halves | 6e-05 |  |
| [[BIN3]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[TGFB1]] | -0.51 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TTLL3]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises VPS36's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.509). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-29.0, -15.2); signed map (-11.6, -40.7). **Vector** length 98.2, 23.7% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.1 | +16.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.1 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +9.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.5 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +4.1 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.0 | +4.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.0 | +4.8 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.3 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.7 | -3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -10.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.2 | -13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.0 | -18.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -3.0 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Filgotinib (drug)]] 0.05 µM |  | -1.9 | -1.6 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | vacuolar protein sorting 36 homolog |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q14.3 — chr13:52,412,602-52,450,634 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-145, Eap45; previously C13orf9 |
| Gene groups (HGNC) | ESCRT-II |
| Reactome | 6 pathways, smallest: Endosomal Sorting Complex Required For Transport (ESCRT); HCMV Late Events; HCMV Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86VN1](https://www.uniprot.org/uniprotkb/Q86VN1) (Vacuolar protein-sorting-associated protein 36):

> Component of the ESCRT-II complex (endosomal sorting complex required for transport II), which is required for multivesicular body (MVB) formation and sorting of endosomal cargo proteins into MVBs. The MVB pathway mediates delivery of transmembrane proteins into the lumen of the lysosome for degradation. The ESCRT-II complex is probably involved in the recruitment of the ESCRT-III complex. Its ability to bind ubiquitin probably plays a role in endosomal sorting of ubiquitinated cargo proteins …

**Summary**, from NCBI Gene [51028](https://www.ncbi.nlm.nih.gov/gene/51028):

> This gene encodes a protein that is a subunit of the endosomal sorting complex required for transport II (ESCRT-II). This protein complex functions in sorting of ubiquitinated membrane proteins during endocytosis. A similar protein complex in rat is associated with RNA polymerase elongation factor II. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:20312](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20312) · Entrez [51028](https://www.ncbi.nlm.nih.gov/gene/51028) · UniProt [Q86VN1](https://www.uniprot.org/uniprotkb/Q86VN1) · Ensembl [ENSG00000136100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136100)

## Data

Gene col 5811: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5811); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5811, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5811]; `tensor/DDL_lfc|DDL_z.npy` [5811]; `embed/gene_vectors.npy` [5811]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5811 or target_col == 5811). Every well: [[VPS36 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VPS36.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
