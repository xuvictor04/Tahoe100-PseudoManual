---
symbol: "ZGRF1"
type: "gene"
col: 6205
ensembl_id: "ENSG00000138658"
name: "zinc finger GRF-type containing 1"
location: "4q25"
module: 6
arm: "+"
pooled_cpm: 29.37
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 23
n_dd_up_clean: 10
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# ZGRF1

*zinc finger GRF-type containing 1* — 4q25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (19 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.81× (z +10.9, q 5e-25, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (11 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.687× (z -10.7, q 5e-24, down in 31 of 48 measured lines) ⚠ cell-cycle shift, explains ~40% of this change. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.690× (z -10.6, q 7e-24, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD5]] (+0.91, fdr 7e-06), [[POLQ]] (+0.89, fdr 7e-06), [[RAD51AP1]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[FAM111B]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 22 with an alert ⚠; shown: the 15 strongest and the 14 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.81×** | +10.9 | 5e-25 | 35/48 (J82, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.59×** | +9.4 | 2e-18 | 34/48 (A549, SW48, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +8.3 | 2e-14 | 29/48 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **1.50×** | +7.9 | 4e-13 | 26/48 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.42×** | +7.1 | 1e-10 | 30/48 (RKO, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.42×** | +6.8 | 7e-10 | 24/48 (SW480, RKO, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.40×** | +6.8 | 7e-10 | 25/48 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.42×** | +6.8 | 7e-10 | 27/48 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.36×** | +6.3 | 3e-08 | 21/48 (NCI-H460, SW480, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.23×** | +6.0 | 1e-07 | 22/48 (NCI-H460, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.32×** | +5.6 | 1e-06 | 21/48 (NCI-H23, HEC-1-A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.31×** | +5.5 | 2e-06 | 22/47 (NCI-H23, RKO, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.30×** | +5.3 | 6e-06 | 19/48 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.31×** | +5.2 | 8e-06 | 22/48 (C32, NCI-H2347, …) | top dose only | composition shift |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.28×** | +5.0 | 2e-05 | 13/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.30×** | +5.0 | 2e-05 | 16/48 (NCI-H460, CFPAC-1, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +4.4 | 2e-04 | 11/48 (PANC-1, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +4.3 | 4e-04 | 14/48 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.25×** | +4.2 | 7e-04 | 13/48 (LS 180, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Methotrexate (drug)]] 0.5 µM |  | **1.22×** | +4.1 | 0.001 | 10/48 (HT-29, NCI-H460, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.001 | 19/48 (PANC-1, SW1417, …) | top dose only |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.20×** | +3.7 | 0.004 | 12/48 (Hs 766T, HCT15, …) | inconsistent across doses |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.004 | 7/48 (HOP62, A-427, …) | top dose only | plate-row cell shift |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | 1.20× | +3.5 | 0.009 | 8/48 (CFPAC-1, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Methotrexate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.011 | 6/48 (LS 180, SW480, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.019 | 11/47 (SW480, A549, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.021 | 15/48 (PANC-1, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.028 | 3/48 (SW480, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.11× | +3.0 | 0.036 | 4/48 (A498, HCT15, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 14 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.687×** | -10.7 | 5e-24 | 31/48 (A498, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.690×** | -10.6 | 7e-24 | 40/48 (RPMI-7951, SHP-77, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.629×** | -9.4 | 1e-18 | 31/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.680×** | -7.8 | 8e-13 | 25/48 (HOP62, RPMI-7951, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.688×** | -7.6 | 5e-12 | 30/48 (A498, HCT15, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.805×** | -6.2 | 5e-08 | 23/48 (KATO III, COLO 205, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.734×** | -5.9 | 3e-07 | 22/48 (KATO III, H4, …) | all doses, flat |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.671×** | -5.8 | 6e-07 | 20/48 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.824×** | -5.5 | 2e-06 | 21/48 (HCT15, RKO, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.764×** | -5.4 | 3e-06 | 21/48 (HCT15, NCI-H460, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.631×** | -4.9 | 6e-05 | 20/48 (SW1417, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.640×** | -4.7 | 1e-04 | 15/47 (KATO III, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.795×** | -4.6 | 2e-04 | 14/48 (SNU-1, KATO III, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.649×** | -4.6 | 2e-04 | 17/48 (HEC-1-A, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.798×** | -4.6 | 2e-04 | 17/48 (A-427, LOX-IMVI, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.674×** | -4.2 | 0.001 | 15/48 (HEC-1-A, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.815×** | -4.1 | 0.001 | 15/47 (HOP62, LS 180, …) | two highest doses | low cells (technical?) |
| [[Entrectinib (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.002 | 10/48 (Panc 03.27, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.829×** | -3.8 | 0.004 | 15/48 (A-427, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.834× | -3.5 | 0.010 | 12/48 (HEC-1-A, SNU-423, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.841× | -3.5 | 0.011 | 11/47 (PANC-1, NCI-H1573, …) | two highest doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.891× | -3.3 | 0.022 | 13/48 (NCI-H1792, hTERT-HPNE, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.735×** | -3.2 | 0.025 | 8/48 (SW480, CHP-212, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.75 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 45.5 | 0 | 6 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.205× (z -16.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.385× (z -9.9) |
| [[H4 (line)]] | wt | 32.2 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.100× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 34.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -10.3) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-427 (line)]] | wt | 39.5 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.380× (z -10.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.342× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 77.6 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LS 180 (line)]] | wt | 18.7 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.154× (z -15.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.351× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 21.3 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +12.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HOP62 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.309× (z -9.5) ⚠ cell-cycle shift, explains ~34% of this change |
| [[HT-29 (line)]] | alt | 27.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.430× (z -8.7) ⚠ cell-cycle shift, explains ~40% of this change |
| [[KATO III (line)]] | alt | 31.0 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.288× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[LOX-IMVI (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.314× (z -9.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[NCI-H2030 (line)]] | alt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +11.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H23 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 40.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 1 | — | [[Tucidinostat (drug)]] 5 µM 0.351× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 67.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 30.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD5]] | +0.91 | +0.91 / +0.90 | both halves | 7e-06 | STRING 780 |
| [[POLQ]] | +0.89 | +0.90 / +0.88 | both halves | 7e-06 |  |
| [[RAD51AP1]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[BRIP1]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[BRCA1]] | +0.87 | +0.83 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[KIF24]] | +0.87 | +0.79 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[DTL]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 |  |
| [[FANCD2]] | +0.86 | +0.90 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[WDHD1]] | +0.85 | +0.85 / +0.84 | both halves | 7e-06 |  |
| [[PLK4]] | +0.85 | +0.86 / +0.85 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.85 | +0.83 / +0.85 | both halves | 7e-06 |  |
| [[FANCI]] | +0.85 | +0.83 / +0.86 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM111B]] | B | FAM111B activity raises ZGRF1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without FAM111B | 0.049 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers ZGRF1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GPR19]] | B | GPR19 activity raises ZGRF1's level | lines that do not express GPR19 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without GPR19 | 0.060 | ⚠ within organs, on part of the lines; also absent: DBNDD1, GPR137B, ERO1B; maybe low, not absent; its own permutation p |
| [[BRME1]] | C | BRME1 activity raises ZGRF1's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 1.95× lower at baseline in the lines without BRME1 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens ZGRF1's drug response | recorded loss-of-function mutation of TP53 in 31 lines vs 17 not recorded | the TP53-altered lines respond 0.86× as strongly (z diff +0.34); rises at some drug-doses, falls at others (74% from rises): Selinexor 5 µM: 0.73x vs 0.47x (z diff +2.6); Panobinostat 5 µM: 1.32x vs 1.88x (z diff +2.0); Belinostat 5 µM: 1.41x vs 1.92x (z diff +1.6) | 0.689 over the table, 0.043 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; both ways; rises at some drug-doses, falls at others; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.833). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.2, -47.1); signed map (-40.7, -45.0). **Vector** length 134, 39.5% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.63 to 65); *DNA strand elongation* (reactome, mean cos +0.68 to 28); *DNA Replication* (reactome, mean cos +0.67 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +4.4 | +6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +10.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +3.7 | +6.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | +3.7 | +7.9 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | +3.5 | +4.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +5.0 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.6 | +3.7 |
|  | [[Entecavir (monohydrate) (drug)]] 5 µM |  | +2.5 | +3.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.4 | +1.9 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -7.6 | -10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.4 | -10.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -6.1 | -7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -5.6 | -7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.8 | -6.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.4 | -5.5 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.9 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger GRF-type containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q25 — chr4:112,539,333-112,636,995 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11331; previously C4orf21 |
| Gene groups (HGNC) | Zinc fingers GRF-type; UPF1 like RNA helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86YA3](https://www.uniprot.org/uniprotkb/Q86YA3) (5'-3' DNA helicase ZGRF1):

> 5'-3' DNA helicase which is recruited to sites of DNA damage and promotes repair of replication-blocking DNA lesions through stimulation of homologous recombination (HR). Promotes HR by directly stimulating RAD51-mediated strand exchange activity. Not required to load RAD51 at sites of DNA damage but promotes recombinational repair after RAD51 recruitment. Also promotes HR by positively regulating EXO1-mediated DNA end resection of double-strand breaks. Required for recruitment of replication …

**Summary**, from NCBI Gene [55345](https://www.ncbi.nlm.nih.gov/gene/55345):

> The encoded protein contains GRF zinc finger (zf-GRF) and transmembrane domains. GRF zinc fingers are found in a number of DNA-binding proteins. Alternative splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:25654](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25654) · Entrez [55345](https://www.ncbi.nlm.nih.gov/gene/55345) · UniProt [Q86YA3](https://www.uniprot.org/uniprotkb/Q86YA3) · Ensembl [ENSG00000138658](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138658)

## Data

Gene col 6205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6205); `tables/drug_effects.parquet` (73 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6205]; `tensor/DDL_lfc|DDL_z.npy` [6205]; `embed/gene_vectors.npy` [6205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6205 or target_col == 6205). Every well: [[ZGRF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZGRF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
