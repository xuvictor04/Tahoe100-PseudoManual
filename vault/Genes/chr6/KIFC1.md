---
symbol: "KIFC1"
type: "gene"
col: 14145
ensembl_id: "ENSG00000237649"
name: "kinesin family member C1"
location: "6p21.32"
module: 67
arm: "+"
pooled_cpm: 32.51
n_lines_expressing: 49
n_dd_up: 9
n_dd_down: 29
n_dd_up_clean: 1
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# KIFC1

*kinesin family member C1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.77× (z +11.8, q 3e-29, up in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~45% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 1.87× (z +3.8, q 0.010, up in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (PANC-1 4.67×, KATO III 7.44×, LS 180 5.94×, SW480 3.48×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 3.68×, KATO III 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 3.82×, KATO III 4.53×; ⚠ cell-cycle shift, explains ~38% of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.354× (z -17.0, q 0e+00, down in 43 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.636× (z -5.3, q 2e-05, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AURKB]] (+0.92, fdr 7e-06), [[SPAG5]] (+0.91, fdr 7e-06), [[TACC3]] (+0.90, fdr 7e-06).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 9 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14145.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 6 lines (PANC-1 4.67×, KATO III 7.44×, LS 180 5.94×, SW480 3.48×, …; ⚠ cell-cycle shift, explains ~45% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 3.68×, KATO III 6.49×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 3.82×, KATO III 4.53×; ⚠ cell-cycle shift, explains ~38% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.77×** | +11.8 | 3e-29 | 43/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.25×** | +9.0 | 4e-17 | 39/47 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **2.18×** | +9.0 | 4e-17 | 40/46 (PANC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.08×** | +8.2 | 4e-14 | 41/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **1.65×** | +5.8 | 9e-07 | 27/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.57×** | +5.2 | 2e-05 | 27/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **2.20×** | +4.8 | 1e-04 | 26/47 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.8 | 1e-04 | 3/47 (RKO, KATO III, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +3.8 | 0.010 | 23/47 (HS-578T, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, would explain all of this change | **1.36×** | +3.6 | 0.020 | 22/45 (HT-29, AsPC-1, …) | all doses, flat | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 13 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14145.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.354×** | -17.0 | 0e+00 | 43/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.383×** | -11.1 | 3e-26 | 41/47 (LOX-IMVI, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.436×** | -9.1 | 2e-17 | 38/47 (LOX-IMVI, NCI-H2347, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.519×** | -7.6 | 4e-12 | 31/46 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.636×** | -5.3 | 2e-05 | 27/47 (C-33 A, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Amsacrine (drug)]] 5 µM |  | **0.735×** | -5.1 | 4e-05 | 26/47 (SW48, A498, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **0.471×** | -4.6 | 4e-04 | 27/41 (NCI-H2347, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.692×** | -4.3 | 0.001 | 27/47 (LOX-IMVI, AN3 CA, …) | all doses, stronger at high dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **0.686×** | -4.2 | 0.002 | 22/47 (A498, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.735×** | -4.2 | 0.002 | 25/47 (HEC-1-A, A-427, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.705×** | -4.1 | 0.003 | 26/47 (A498, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.703×** | -4.0 | 0.004 | 23/47 (HOP62, HEC-1-A, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.576×** | -3.4 | 0.035 | 16/46 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.752×** | -3.3 | 0.037 | 19/47 (H4, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.759×** | -3.3 | 0.040 | 15/47 (A-427, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.757×** | -3.3 | 0.040 | 15/46 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.050 | 18/47 (SW48, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.758×** | -3.1 | 0.051 | 14/46 (C32, A549, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -3.1 | 0.051 | 15/47 (AN3 CA, A498, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.832×** | -3.0 | 0.060 | 18/47 (A498, H4, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.763×** | -3.0 | 0.060 | 15/46 (SNU-423, HCT15, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.609×** | -3.0 | 0.062 | 16/46 (Hs 766T, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.779×** | -2.9 | 0.078 | 20/46 (KATO III, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.83 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14145. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 24.5 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0922× (z -22.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.331× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 30.5 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.101× (z -19.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Amsacrine (drug)]] 0.5 µM 0.106× (z -13.7) |
| [[PANC-1 (line)]] | alt | 38.1 | 6 (6 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +14.3) ⚠ cell-cycle shift, explains ~45% of this change | [[Bortezomib (drug)]] 0.05 µM 0.345× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[H4 (line)]] | wt | 40.2 | 0 | 7 (6 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0763× (z -16.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.242× (z -9.2) |
| [[A-172 (line)]] | wt | 28.1 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.294× (z -10.6) |
| [[LS 180 (line)]] | wt | 21.1 | 1 (1 ⚠) | 4 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.94× (z +9.5) ⚠ cell-cycle shift, explains ~45% of this change | [[Selinexor (drug)]] 5 µM 0.116× (z -16.4) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HOP62 (line)]] | alt | 61.6 | 1 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +8.6) ⚠ cell-cycle shift, explains ~45% of this change | [[Ixazomib citrate (drug)]] 5 µM 0.225× (z -10.8) ⚠ cell-cycle shift, explains ~32% of this change |
| [[KATO III (line)]] | alt | 34.0 | 3 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 7.44× (z +12.0) ⚠ cell-cycle shift, explains ~45% of this change | [[Bortezomib (drug)]] 0.05 µM 0.224× (z -8.5) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H460 (line)]] | wt | 17.8 | 2 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.89× (z +8.7) ⚠ cell-cycle shift, explains ~54% of this change | [[Selinexor (drug)]] 5 µM 0.259× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 52.6 | 0 | 3 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.159× (z -18.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A549 (line)]] | wt | 20.2 | 0 | 3 (2 ⚠) | — | [[Amsacrine (drug)]] 0.5 µM 0.146× (z -11.8) |
| [[C32 (line)]] | wt | 27.7 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.139× (z -14.9) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.305× (z -9.0) |
| [[NCI-H2347 (line)]] | alt | 37.9 | 0 | 3 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.218× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[AN3 CA (line)]] | alt | 78.5 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.160× (z -9.0) |
| [[C-33 A (line)]] | alt | 43.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.247× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 50.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 17.9 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.250× (z -12.2) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Panc 03.27 (line)]] | alt | 30.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Selinexor (drug)]] 5 µM 0.138× (z -18.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[RPMI-7951 (line)]] | alt | 42.7 | 0 | 2 (1 ⚠) | — | [[Saquinavir (drug)]] 0.05 µM 0.131× (z -10.7) |
| [[SNU-1 (line)]] | wt | 29.2 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -9.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 14.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HCT15 (line)]] | alt | 54.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.249× (z -11.3) ⚠ cell-cycle shift, explains ~39% of this change |
| [[Hs 766T (line)]] | wt | 22.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.171× (z -8.7) ⚠ cell-cycle shift, explains ~50% of this change |
| [[HS-578T (line)]] | alt | 29.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -10.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[HT-29 (line)]] | alt | 23.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.290× (z -9.8) ⚠ cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.7 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.108× (z -13.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[J82 (line)]] | alt | 39.2 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +8.5) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[NCI-H2030 (line)]] | alt | 42.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H23 (line)]] | alt | 59.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.422× (z -9.7) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SK-MEL-2 (line)]] | alt | 44.1 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.283× (z -11.6) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SNU-423 (line)]] | alt | 40.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.200× (z -13.9) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW 900 (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.305× (z -9.0) ⚠ cell-cycle shift, explains ~39% of this change |
| [[SW48 (line)]] | wt | 34.3 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.216× (z -10.7) |
| [[SW480 (line)]] | alt | 34.5 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.48× (z +9.3) ⚠ cell-cycle shift, explains ~45% of this change | — |
| [[BT-474 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14145), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AURKB]] | +0.92 | +0.92 / +0.88 | both halves | 7e-06 | STRING 906 |
| [[SPAG5]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | STRING 866 |
| [[TACC3]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | STRING 675 |
| [[KIF22]] | +0.89 | +0.88 / +0.89 | both halves | 7e-06 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 881 |
| [[CIT]] | +0.89 | +0.87 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[DEPDC1B]] | +0.89 | +0.84 / +0.87 | both halves | 7e-06 | STRING 427 |
| [[CDCA3]] | +0.88 | +0.89 / +0.83 | both halves | 7e-06 | STRING 830 |
| [[KIF2C]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 932 |
| [[INCENP]] | +0.88 | +0.89 / +0.85 | both halves | 7e-06 | STRING 740 |
| [[RACGAP1]] | +0.88 | +0.86 / +0.87 | both halves | 7e-06 | pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 801 |
| [[NCAPH]] | +0.87 | +0.86 / +0.85 | both halves | 7e-06 | STRING 679 |
| [[KIF18B]] | +0.87 | +0.88 / +0.84 | both halves | 7e-06 | same gene group; pathway: COPI-dependent Golgi-to-ER retrograde traffic; STRING 882 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 2, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity strengthens KIFC1's drug response | lines that do not express PIMREG (5) vs lines expressing it (42) | the lines without PIMREG respond 0.66× as strongly (z diff +1.99); strongest at Ouabain (Octahydrate) 5 µM: 2.14x vs 2.84x (z diff +3.1) | 0.020 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PIMREG]] | B | PIMREG activity raises KIFC1's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 2.23× lower at baseline in the lines without PIMREG | 0.035 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[PBK]] | C | PBK activity raises KIFC1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.60× lower at baseline in the lines without PBK | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[CDCA3]] | C | CDCA3 activity raises KIFC1's level | lines that do not express CDCA3 (3) vs lines expressing it (47) | 3.01× lower at baseline in the lines without CDCA3 | 0.082 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TBC1D19, PBK, SNPH; maybe low, not absent |
| [[CDC20]] | C | CDC20 activity raises KIFC1's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 3.11× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.901). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-35.7, -54.3); signed map (-47.7, -41.9). **Vector** length 150, 51.7% of its response variance represented; |z| ≥ 3 in 1,314 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.81 to 12); *G2/M checkpoint* (hallmark, mean cos +0.80 to 9); *Mitotic Prometaphase* (reactome, mean cos +0.75 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +5.2 | +9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +5.1 | +11.8 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.0 | +5.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +4.8 | +9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.8 | +8.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +2.2 | +2.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.1 | +1.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.0 | +1.3 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -10.5 | -17.0 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | -10.3 | -9.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -9.8 | -11.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -8.3 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.0 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.8 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.0 | -4.1 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.2 | -2.5 |
|  | [[Amsacrine (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member C1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,391,823-33,409,896 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSET; previously KNSL2 |
| Gene groups (HGNC) | Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BW19](https://www.uniprot.org/uniprotkb/Q9BW19) (Kinesin-like protein KIFC1):

> Minus end-directed microtubule-dependent motor required for bipolar spindle formation. May contribute to movement of early endocytic vesicles (By similarity). Regulates cilium formation and structure (By similarity).

**Summary**, from NCBI Gene [3833](https://www.ncbi.nlm.nih.gov/gene/3833):

> Predicted to enable ATP hydrolysis activity; microtubule binding activity; and minus-end-directed microtubule motor activity. Involved in mitotic metaphase chromosome alignment and mitotic spindle assembly. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:6389](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6389) · Entrez [3833](https://www.ncbi.nlm.nih.gov/gene/3833) · UniProt [Q9BW19](https://www.uniprot.org/uniprotkb/Q9BW19) · Ensembl [ENSG00000237649](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000237649)

## Data

Gene col 14145: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14145); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14145, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14145]; `tensor/DDL_lfc|DDL_z.npy` [14145]; `embed/gene_vectors.npy` [14145]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14145 or target_col == 14145). Every well: [[KIFC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIFC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
