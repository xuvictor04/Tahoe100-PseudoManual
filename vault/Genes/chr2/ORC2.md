---
symbol: "ORC2"
type: "gene"
col: 3739
ensembl_id: "ENSG00000115942"
name: "origin recognition complex subunit 2"
location: "2q33.1"
module: 156
arm: "+"
pooled_cpm: 103.66
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/156"]
generated_by: "tahoemap"
---

# ORC2

*origin recognition complex subunit 2* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.28× (z +8.3, q 8e-14, up in 30 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 1.40× (z +6.1, q 2e-07, up in 22 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AsPC-1 2.49×, SW 900 1.90×, HS-578T 1.87×, SHP-77 1.55×, …; ⚠ cell-cycle shift, explains ~75% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 2.88×; ⚠ cell-cycle shift, explains ~56% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (PANC-1 2.40×); [[TAK-901 (drug)]] 5 µM in 1 line (HEC-1-A 2.67×).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.580× (z -18.2, q 0e+00, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.721× (z -10.9, q 1e-25, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (C-33 A 0.0938×, NCI-H1573 0.205×, NCI-H23 0.303×, PANC-1 0.423×, …; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 6 lines (NCI-H1573 0.424×, AsPC-1 0.317×, PANC-1 0.540×, NCI-H460 0.564×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.371×, HEC-1-A 0.298×, NCI-H1573 0.321×, PANC-1 0.478×, …; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.593×, NCI-H1573 0.574×); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.193×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TYW1]] (+0.61, fdr 7e-06), [[GTF3C2]] (+0.60, fdr 8e-06), [[CCDC138]] (+0.60, fdr 1e-05); moves opposite to [[NOTCH2NLC]] (-0.60, fdr 1e-05), [[TEX261]] (-0.55, fdr 2e-05), [[EMD]] (-0.55, fdr 2e-05).
> It is in [[Module 156]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[LGALS3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 9 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3739.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (AsPC-1 2.49×, SW 900 1.90×, HS-578T 1.87×, SHP-77 1.55×, …; ⚠ cell-cycle shift, explains ~75% of this change); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (HS-578T 2.88×; ⚠ cell-cycle shift, explains ~56% of this change); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 1.77×; ⚠ cell-cycle shift, explains ~0% of this change); [[PH-797804 (drug)]] 5 µM in 1 line (PANC-1 2.40×); [[TAK-901 (drug)]] 5 µM in 1 line (HEC-1-A 2.67×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.28×** | +8.3 | 8e-14 | 30/47 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +7.2 | 2e-10 | 25/48 (NCI-H2347, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.22×** | +7.0 | 6e-10 | 25/48 (HT-29, HCT15, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.40×** | +6.1 | 2e-07 | 22/49 (HEC-1-A, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.16× | +5.3 | 2e-05 | 16/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.29×** | +4.7 | 3e-04 | 17/38 (SK-MEL-2, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | 1.14× | +4.4 | 7e-04 | 18/48 (HS-578T, AsPC-1, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.012 | 15/48 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 1.11× | +3.5 | 0.025 | 15/48 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.14× | +3.4 | 0.032 | 12/47 (HEC-1-A, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.10× | +3.2 | 0.060 | 12/48 (NCI-H2030, SW1417, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | 1.13× | +3.2 | 0.062 | 12/48 (HT-29, C32, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.09× | +3.2 | 0.069 | 2/48 (SW1417, KATO III) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | 1.19× | +3.1 | 0.069 | 13/49 (A498, Hs 766T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.06× | +3.1 | 0.071 | 16/49 (AsPC-1, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3739.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (C-33 A 0.0938×, NCI-H1573 0.205×, NCI-H23 0.303×, PANC-1 0.423×, …; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 5 µM in 6 lines (NCI-H1573 0.424×, AsPC-1 0.317×, PANC-1 0.540×, NCI-H460 0.564×, …); [[Dinaciclib (drug)]] 0.5 µM in 5 lines (SW480 0.371×, HEC-1-A 0.298×, NCI-H1573 0.321×, PANC-1 0.478×, …; ⚠ toxic; transcription drop); [[Harringtonine (drug)]] 0.5 µM in 2 lines (NCI-H460 0.593×, NCI-H1573 0.574×); [[Atazanavir (sulfate) (drug)]] 5 µM in 1 line (NCI-H596 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.580×** | -18.2 | 0e+00 | 35/44 (C-33 A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.617×** | -16.8 | 0e+00 | 46/49 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.681×** | -11.6 | 7e-29 | 29/45 (LS 180, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.721×** | -10.9 | 1e-25 | 31/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.811×** | -10.2 | 1e-22 | 22/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.763×** | -9.4 | 5e-19 | 30/48 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.771×** | -9.0 | 1e-17 | 30/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.784×** | -8.4 | 2e-15 | 28/48 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.804×** | -7.3 | 2e-11 | 28/47 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.867× | -4.9 | 4e-05 | 18/48 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.871× | -4.2 | 0.002 | 17/47 (NCI-H460, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.887× | -4.1 | 0.002 | 14/48 (HEC-1-A, MIA PaCa-2, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.888× | -4.0 | 0.003 | 12/47 (A549, NCI-H2030, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.898× | -3.7 | 0.007 | 13/47 (hTERT-HPNE, SW48, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.898× | -3.7 | 0.008 | 11/48 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 0.896× | -3.7 | 0.009 | 7/47 (C32, NCI-H23, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.897× | -3.6 | 0.010 | 11/48 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 0.938× | -3.1 | 0.059 | 1/48 (CHP-212) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 0.915× | -3.1 | 0.060 | 9/49 (A-427, NCI-H23, …) | rises with dose |  |
| [[OTS514 (drug)]] 5 µM |  | 0.846× | -3.0 | 0.068 | 14/46 (SHP-77, C32, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 111 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -23.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.424× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 126 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.520× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.564× (z -10.2) |
| [[PANC-1 (line)]] | alt | 120 | 1 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 2.40× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.423× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.540× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 127 | 1 (1 ⚠) | 4 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +14.9) ⚠ cell-cycle shift, explains ~75% of this change | [[Dinaciclib (drug)]] 5 µM 0.237× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -12.8) |
| [[HEC-1-A (line)]] | alt | 130 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 2.67× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -20.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 110 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -12.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 176 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -14.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 155 | 1 (1 ⚠) | 2 (2 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 1.80× (z +9.1) ⚠ toxic; cell-cycle shift, explains ~29% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.475× (z -12.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 110 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -12.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW480 (line)]] | alt | 140 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.371× (z -23.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 108 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.600× (z -10.5) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.527× (z -8.9) |
| [[COLO 205 (line)]] | alt | 80.9 | 0 | 2 (2 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0747× (z -14.4) ⚠ toxic |
| [[H4 (line)]] | wt | 114 | 0 | 2 (2 ⚠) | — | [[Bortezomib (drug)]] 5 µM 0.145× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HCT15 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.458× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Allantoin (drug)]] 0.5 µM 0.459× (z -8.8) |
| [[HS-578T (line)]] | alt | 63.0 | 2 (2 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.4) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[J82 (line)]] | alt | 89.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.523× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 99.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.77× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.456× (z -12.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 136 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.303× (z -17.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 76.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.362× (z -12.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 125 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.435× (z -11.6) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[SHP-77 (line)]] | alt | 126 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.55× (z +8.6) ⚠ cell-cycle shift, explains ~75% of this change | [[Dinaciclib (drug)]] 5 µM 0.344× (z -14.1) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 79.4 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +10.0) ⚠ cell-cycle shift, explains ~75% of this change | [[Harringtonine (drug)]] 5 µM 0.414× (z -9.3) |
| [[A549 (line)]] | wt | 99.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.606× (z -10.3) ⚠ cell-cycle shift, explains ~75% of this change |
| [[BT-474 (line)]] | alt | 72.1 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.170× (z -10.1) ⚠ toxic |
| [[C-33 A (line)]] | alt | 135 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0938× (z -28.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 101 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.551× (z -10.7) ⚠ cell-cycle shift, explains ~15% of this change |
| [[CFPAC-1 (line)]] | alt | 69.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.63× (z +8.6) ⚠ cell-cycle shift, explains ~75% of this change | — |
| [[KATO III (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.452× (z -10.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 91.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -13.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.499× (z -9.7) ⚠ cell-cycle shift, explains ~17% of this change |
| [[NCI-H596 (line)]] | alt | 98.5 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.193× (z -9.3) |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.431× (z -9.6) ⚠ transcription drop |
| [[SNU-1 (line)]] | wt | 125 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -9.5) ⚠ cell-cycle shift, explains ~75% of this change |
| [[SW 1271 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.100× (z -12.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 83.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 97.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 74.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 85.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 63.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 113 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 65.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 95.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 95.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 119 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | +0.61 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[GTF3C2]] | +0.60 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[CCDC138]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[INTS9]] | +0.58 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[METTL16]] | +0.58 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[HIRA]] | +0.58 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[AGAP4]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[TFCP2]] | +0.57 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NUP160]] | +0.56 | +0.57 / +0.58 | both halves | 1e-05 | pathway: Cell Cycle Checkpoints |
| [[IQCB1]] | +0.56 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[KNOP1]] | +0.56 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[INTS4]] | +0.56 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLC]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TEX261]] | -0.55 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[EMD]] | -0.55 | -0.46 / -0.57 | both halves | 2e-05 |  |
| [[PNPLA2]] | -0.54 | -0.60 / -0.46 | both halves | 2e-05 |  |
| [[CHMP4B]] | -0.54 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[TFE3]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[PTBP3]] | -0.51 | -0.35 / -0.57 | both halves | 1e-04 |  |
| [[AFF4]] | -0.51 | -0.33 / -0.59 | both halves | 1e-04 |  |
| [[FAM199X]] | -0.50 | -0.30 / -0.59 | both halves | 2e-04 |  |
| [[CPEB2]] | -0.50 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[TPPP]] | -0.49 | -0.55 / -0.46 | both halves | 2e-05 |  |
| [[TP53INP2]] | -0.49 | -0.56 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LGALS3]] | B | LGALS3 activity lowers ORC2's level | lines that do not express LGALS3 (11) vs lines expressing it (39) | 1.38× higher at baseline in the lines without LGALS3 | 0.025 | ⚠ within organs, on part of the lines; also absent: TNS3, STAT5A, ADGRG1 |
| [[KHDC1]] | B | KHDC1 activity lowers ORC2's level | lines that do not express KHDC1 (15) vs lines expressing it (35) | 1.17× higher at baseline in the lines without KHDC1 | 0.095 | ⚠ within organs, on part of the lines; also absent: KHDC1-AS1, MAP9, C15orf48 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 156]]; 28 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-25.3, -8.3); signed map (-42.7, -21.0). **Vector** length 112, 27.4% of its response variance represented; |z| ≥ 3 in 1,032 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | +6.3 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | +4.9 | +7.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~4% of this change | +4.1 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +3.9 | +7.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +3.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | +2.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +1.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.3 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.8 | -16.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -6.4 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -18.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -10.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.7 | -3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | -2.6 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -0.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.5 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | origin recognition complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,908,977-200,963,680 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ORC2L |
| Gene groups (HGNC) | Origin recognition complex |
| Hallmark sets | E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 19 pathways, smallest: CDC6 association with the ORC:origin complex; E2F-enabled inhibition of pre-replication complex formation; E2F mediated regulation of DNA replication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13416](https://www.uniprot.org/uniprotkb/Q13416) (Origin recognition complex subunit 2):

> Component of the origin recognition complex (ORC) that binds origins of replication. DNA-binding is ATP-dependent. The specific DNA sequences that define origins of replication have not been identified yet. ORC is required to assemble the pre-replication complex necessary to initiate DNA replication. Binds histone H3 and H4 trimethylation marks H3K9me3, H3K20me3 and H4K27me3. Stabilizes LRWD1, by protecting it from ubiquitin-mediated proteasomal degradation. Also stabilizes ORC3.

**Summary**, from NCBI Gene [4999](https://www.ncbi.nlm.nih.gov/gene/4999):

> The origin recognition complex (ORC) is a highly conserved six subunits protein complex essential for the initiation of the DNA replication in eukaryotic cells. Studies in yeast demonstrated that ORC binds specifically to origins of replication and serves as a platform for the assembly of additional initiation factors such as Cdc6 and Mcm proteins. The protein encoded by this gene is a subunit of the ORC complex. This protein forms a core complex with ORC3, -4, and -5. It also interacts with …

**Accessions** — [HGNC:8488](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8488) · Entrez [4999](https://www.ncbi.nlm.nih.gov/gene/4999) · UniProt [Q13416](https://www.uniprot.org/uniprotkb/Q13416) · Ensembl [ENSG00000115942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115942)

## Data

Gene col 3739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3739); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3739]; `tensor/DDL_lfc|DDL_z.npy` [3739]; `embed/gene_vectors.npy` [3739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3739 or target_col == 3739). Every well: [[ORC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ORC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
