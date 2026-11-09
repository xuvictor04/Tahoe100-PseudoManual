---
symbol: "CENPK"
type: "gene"
col: 4418
ensembl_id: "ENSG00000123219"
name: "centromere protein K"
location: "5q12.3"
module: 6
arm: "+"
pooled_cpm: 58.25
n_lines_expressing: 48
n_dd_up: 24
n_dd_down: 24
n_dd_up_clean: 7
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# CENPK

*centromere protein K* — 5q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (17 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.94× (z +11.6, q 2e-28, up in 36 of 46 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change. The strongest without an alert is [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM: 1.26× (z +4.0, q 0.003, up in 13 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.506× (z -16.9, q 0e+00, down in 38 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FANCI]] (+0.95, fdr 7e-06), [[MELK]] (+0.93, fdr 7e-06), [[POLQ]] (+0.92, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 22 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4418.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | **1.94×** | +11.6 | 2e-28 | 36/46 (NCI-H2347, A549, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.93×** | +11.5 | 4e-28 | 40/46 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **1.94×** | +11.2 | 9e-27 | 31/40 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.85×** | +10.8 | 5e-25 | 38/46 (LoVo, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change | **1.72×** | +8.8 | 2e-16 | 27/41 (NCI-H2347, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +8.2 | 2e-14 | 34/46 (LoVo, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.35×** | +5.3 | 1e-05 | 24/46 (MIA PaCa-2, SW480, …) | two highest doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.22×** | +5.0 | 4e-05 | 20/46 (A549, HT-29, …) | rises with dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | 1.19× | +4.3 | 0.001 | 18/46 (HT-29, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.27×** | +4.2 | 0.002 | 21/45 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.29×** | +4.2 | 0.002 | 23/46 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **1.26×** | +4.0 | 0.003 | 13/46 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.27×** | +4.0 | 0.003 | 20/46 (SW 900, HS-578T, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.26×** | +3.8 | 0.005 | 17/46 (SW 900, SW480, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.25×** | +3.8 | 0.005 | 16/46 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.3 | 0.026 | 15/46 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.026 | 15/46 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.13× | +3.1 | 0.048 | 7/46 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.1 | 0.051 | 10/46 (A-427, SW1417, …) | top dose only | plate-row cell shift |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.20×** | +3.0 | 0.055 | 10/46 (SW480, HT-29, …) | rises with dose |  |
| [[Irinotecan (drug)]] 0.5 µM |  | **1.27×** | +3.0 | 0.057 | 10/46 (SW480, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.38×** | +2.8 | 0.089 | 10/46 (A549, AsPC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4418.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.506×** | -16.9 | 0e+00 | 38/46 (H4, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.457×** | -12.8 | 3e-35 | 36/46 (SNU-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.430×** | -7.4 | 2e-11 | 32/46 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.577×** | -6.9 | 9e-10 | 30/46 (SW480, KATO III, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.464×** | -6.7 | 2e-09 | 31/46 (SW480, J82, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.772×** | -6.4 | 1e-08 | 24/46 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Harringtonine (drug)]] 5 µM |  | **0.690×** | -6.3 | 3e-08 | 29/46 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.705×** | -5.8 | 6e-07 | 26/46 (A498, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.722×** | -5.0 | 4e-05 | 25/46 (A-172, HCT15, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.823×** | -4.9 | 7e-05 | 22/46 (COLO 205, HCT15, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.580×** | -4.8 | 9e-05 | 24/43 (SNU-423, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.796×** | -4.5 | 3e-04 | 20/46 (A-427, HEC-1-A, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[palbociclib (drug)]] 5 µM |  | **0.601×** | -4.5 | 3e-04 | 19/45 (SW480, PANC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.776×** | -4.5 | 3e-04 | 21/46 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.777×** | -4.4 | 4e-04 | 23/46 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.849× | -4.1 | 0.002 | 15/46 (NCI-H23, CFPAC-1, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.642×** | -3.9 | 0.003 | 21/45 (A-427, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.810×** | -3.7 | 0.007 | 17/46 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.867× | -3.5 | 0.012 | 21/46 (HCT15, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.803×** | -3.4 | 0.023 | 14/45 (SW48, A-172, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.031 | 15/46 (RKO, KATO III, …) | top dose only |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.815×** | -3.1 | 0.041 | 11/46 (Hs 766T, COLO 205, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.93 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4418. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 68.7 | 0 | 8 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.265× (z -15.5) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.280× (z -14.8) |
| [[H4 (line)]] | wt | 65.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0247× (z -30.3) |
| [[A-427 (line)]] | wt | 92.8 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -19.7) |
| [[HEC-1-A (line)]] | alt | 115 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -18.8) |
| [[A-172 (line)]] | wt | 97.5 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.338× (z -12.1) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.412× (z -9.9) |
| [[A549 (line)]] | wt | 38.0 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.27× (z +11.5) ⚠ cell-cycle shift, explains ~95% of this change | — |
| [[LoVo (line)]] | wt | 43.4 | 3 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.48× (z +10.4) ⚠ cell-cycle shift, explains ~95% of this change | [[Selinexor (drug)]] 5 µM 0.424× (z -10.1) ⚠ cell-cycle shift, explains ~53% of this change |
| [[LS 180 (line)]] | wt | 39.4 | 1 (1 ⚠) | 3 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.00× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | [[Selinexor (drug)]] 5 µM 0.243× (z -13.4) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.385× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 77.5 | 1 (1 ⚠) | 3 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.80× (z +8.6) ⚠ cell-cycle shift, explains ~96% of this change | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -13.6) |
| [[HT-29 (line)]] | alt | 50.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -9.3) |
| [[KATO III (line)]] | alt | 54.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 52.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.09× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~98% of this change | — |
| [[PANC-1 (line)]] | alt | 72.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.15× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -11.2) |
| [[SNU-1 (line)]] | wt | 34.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0678× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0770× (z -13.3) |
| [[SW480 (line)]] | alt | 95.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -16.9) |
| [[HCT15 (line)]] | alt | 80.7 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.303× (z -12.0) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HOP62 (line)]] | alt | 41.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -14.1) |
| [[J82 (line)]] | alt | 123 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 57.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -10.2) |
| [[AN3 CA (line)]] | alt | 70.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -12.4) |
| [[CHP-212 (line)]] | wt | 30.7 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.0741× (z -9.0) |
| [[COLO 205 (line)]] | alt | 50.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.181× (z -8.9) |
| [[Hs 766T (line)]] | wt | 52.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 26.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -9.7) |
| [[NCI-H23 (line)]] | alt | 67.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.480× (z -9.5) |
| [[NCI-H460 (line)]] | wt | 51.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 65.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.396× (z -9.6) ⚠ cell-cycle shift, explains ~53% of this change |
| [[SW1417 (line)]] | alt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.3) |
| [[SW48 (line)]] | wt | 39.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 34.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.4 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 44.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 63.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 82.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 72.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4418), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FANCI]] | +0.95 | +0.94 / +0.94 | both halves | 7e-06 | STRING 407 |
| [[MELK]] | +0.93 | +0.94 / +0.92 | both halves | 7e-06 | STRING 652 |
| [[POLQ]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[FANCB]] | +0.92 | +0.93 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[NCAPG2]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | STRING 568 |
| [[SPC24]] | +0.91 | +0.92 / +0.87 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 685 |
| [[EXO1]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 472 |
| [[FANCA]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[WDHD1]] | +0.90 | +0.87 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[GINS1]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | STRING 479 |
| [[SPC25]] | +0.89 | +0.92 / +0.87 | both halves | 7e-06 | pathway: Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal; STRING 649 |
| [[RAD51]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | STRING 448 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 7, C 9. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises CENPK's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.93× lower at baseline in the lines without CDC25A | 0.016 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises CENPK's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without TCF19 | 0.019 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises CENPK's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.79× lower at baseline in the lines without E2F2 | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TOP1]] | B | TOP1 activity lowers CENPK's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 4.2% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[E2F8]] | B | E2F8 activity raises CENPK's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.98× lower at baseline in the lines without E2F8 | 0.054 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises CENPK's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.99× lower at baseline in the lines without CDCA7 | 0.061 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises CENPK's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.56× lower at baseline in the lines without FAM111B | 0.079 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[ZNF367]] | C | ZNF367 activity raises CENPK's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without ZNF367 | 0.021 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CENPK's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.55× lower at baseline in the lines without AURKB | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent; co-absent with the target |
| [[PKMYT1]] | C | PKMYT1 activity raises CENPK's level | lines that do not express PKMYT1 (3) vs lines expressing it (47) | 3.07× lower at baseline in the lines without PKMYT1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: AURKB, TCF19, SMARCD3; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MYBL2]] | C | MYBL2 activity raises CENPK's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.48× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MCM10]] | C | MCM10 activity raises CENPK's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without MCM10 | 0.072 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.932). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.6, -46.3); signed map (-39.1, -43.7). **Vector** length 157, 55.7% of its response variance represented; |z| ≥ 3 in 1,373 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.69 to 65); *DNA strand elongation* (reactome, mean cos +0.74 to 28); *DNA Replication* (reactome, mean cos +0.73 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | +5.9 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | +5.5 | +10.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.1 | +2.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~95% of this change | +4.9 | +11.5 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | +4.5 | +5.0 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.5 | +3.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +3.2 | +3.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +3.0 | +3.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +2.9 | +4.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.8 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.5 | -12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -9.2 | -16.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -8.0 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | -6.4 | -5.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.7 | -1.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -4.8 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.7 | -4.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | -4.5 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein K |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q12.3 — chr5:65,517,766-65,563,168 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FKSG14, SOLT, CENP-K |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 20 pathways, smallest: Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly; Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BS16](https://www.uniprot.org/uniprotkb/Q9BS16) (Centromere protein K):

> Component of the CENPA-CAD (nucleosome distal) complex, a complex recruited to centromeres which is involved in assembly of kinetochore proteins, mitotic progression and chromosome segregation. May be involved in incorporation of newly synthesized CENPA into centromeres via its interaction with the CENPA-NAC complex. Acts in coordination with KNL1 to recruit the NDC80 complex to the outer kinetochore.

**Summary**, from NCBI Gene [64105](https://www.ncbi.nlm.nih.gov/gene/64105):

> CENPK is a subunit of a CENPH (MIM 605607)-CENPI (MIM 300065)-associated centromeric complex that targets CENPA (MIM 117139) to centromeres and is required for proper kinetochore function and mitotic progression (Okada et al., 2006 [PubMed 16622420]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:29479](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29479) · Entrez [64105](https://www.ncbi.nlm.nih.gov/gene/64105) · UniProt [Q9BS16](https://www.uniprot.org/uniprotkb/Q9BS16) · Ensembl [ENSG00000123219](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123219)

## Data

Gene col 4418: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4418); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4418, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4418]; `tensor/DDL_lfc|DDL_z.npy` [4418]; `embed/gene_vectors.npy` [4418]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4418 or target_col == 4418). Every well: [[CENPK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
