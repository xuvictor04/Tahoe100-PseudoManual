---
symbol: "KLHL22"
type: "gene"
col: 1828
ensembl_id: "ENSG00000099910"
name: "kelch like family member 22"
location: "22q11.21"
module: 20
arm: "-"
pooled_cpm: 37.8
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 26
n_dd_up_clean: 2
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# KLHL22

*kelch like family member 22* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.32× (z +7.3, q 1e-10, up in 26 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.33×, RKO 2.18×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 2.20×, LS 180 2.63×).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.449× (z -14.2, q 1e-42, down in 42 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.255× (z -13.1, q 2e-37, down in 46 of 49 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITCH]] (+0.61, fdr 2e-05), [[NDUFA6]] (+0.57, fdr 1e-05), [[DCAF10]] (+0.56, fdr 1e-05); moves opposite to [[DUXAP8]] (-0.55, fdr 1e-05), [[SNRNP200]] (-0.53, fdr 2e-05), [[TGOLN2]] (-0.53, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1828.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (PANC-1 3.33×, RKO 2.18×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H23 2.20×, LS 180 2.63×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +7.3 | 1e-10 | 26/48 (NCI-H23, LS 180, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.1 | 8e-05 | 22/48 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.6 | 6e-04 | 20/48 (PANC-1, RKO, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.28×** | +4.6 | 7e-04 | 20/48 (BT-474, RKO, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | 1.19× | +3.3 | 0.11 | 17/48 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.13 | 9/48 (HS-578T, SW480, …) | inconsistent across doses |  |
| [[Rifaximin (drug)]] 5 µM |  | 1.19× | +3.2 | 0.13 | 9/48 (NCI-H1792, HOP62, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.18× | +3.0 | 0.18 | 11/48 (AsPC-1, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1828.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -14.2 | 1e-42 | 42/47 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.442×** | -13.9 | 2e-41 | 34/42 (C-33 A, HCT15, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.480×** | -13.5 | 3e-39 | 34/45 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.480×** | -13.5 | 3e-39 | 40/48 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.255×** | -13.1 | 2e-37 | 46/49 (NCI-H23, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.477×** | -13.1 | 3e-37 | 31/39 (HS-578T, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.527×** | -11.8 | 4e-30 | 39/48 (LoVo, NCI-H460, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.302×** | -11.5 | 6e-29 | 40/48 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.555×** | -10.8 | 2e-25 | 39/48 (A-172, C32, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.573×** | -10.2 | 8e-23 | 36/48 (SK-MEL-2, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **0.678×** | -7.1 | 6e-11 | 30/47 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.630×** | -6.7 | 8e-10 | 33/48 (PANC-1, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.719×** | -6.0 | 6e-08 | 29/48 (C32, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.801×** | -5.7 | 4e-07 | 27/48 (SNU-423, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.690×** | -5.4 | 3e-06 | 27/48 (NCI-H1573, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.761×** | -5.0 | 2e-05 | 22/48 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.725×** | -4.7 | 9e-05 | 23/48 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.770×** | -4.5 | 2e-04 | 24/48 (HEC-1-A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.014 | 11/47 (HEC-1-A, A-172, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.819×** | -3.4 | 0.017 | 15/47 (NCI-H460, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.036 | 14/48 (NCI-H2347, SNU-423, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.842× | -3.1 | 0.036 | 16/48 (A-172, A549, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.838× | -3.1 | 0.038 | 8/48 (HS-578T, A-172, …) | top dose only | plate-row cell shift |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.857× | -2.8 | 0.095 | 10/48 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1828. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 52.5 | 0 | 8 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.223× (z -14.8) |
| [[NCI-H460 (line)]] | wt | 30.3 | 0 | 7 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.184× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.352× (z -9.7) |
| [[HS-578T (line)]] | alt | 52.7 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.0739× (z -10.3) |
| [[A498 (line)]] | wt | 37.1 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -14.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 38.4 | 0 | 5 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.135× (z -14.2) |
| [[HOP62 (line)]] | alt | 40.3 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.291× (z -10.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.302× (z -10.5) |
| [[J82 (line)]] | alt | 40.8 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.142× (z -16.5) ⚠ toxic |
| [[KATO III (line)]] | alt | 43.8 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.159× (z -8.7) |
| [[LoVo (line)]] | wt | 50.1 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 55.2 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.225× (z -13.8) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.158× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 36.5 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.20× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -15.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -10.7) |
| [[Panc 03.27 (line)]] | alt | 67.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.290× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.414× (z -9.5) |
| [[PANC-1 (line)]] | alt | 26.7 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +18.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.314× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.369× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 46.2 | 0 | 4 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.134× (z -10.9) |
| [[Hs 766T (line)]] | wt | 49.5 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.185× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 59.1 | 0 | 4 (3 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.230× (z -14.1) |
| [[SNU-1 (line)]] | wt | 53.2 | 0 | 4 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.173× (z -11.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.307× (z -11.2) |
| [[SNU-423 (line)]] | alt | 48.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.192× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.154× (z -9.0) |
| [[A549 (line)]] | wt | 45.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.131× (z -15.5) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 29.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -12.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 49.3 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0907× (z -16.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 22.4 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +9.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -9.9) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0840× (z -9.0) |
| [[SW1417 (line)]] | alt | 50.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.150× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 38.6 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.282× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 26.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.197× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.283× (z -8.9) |
| [[SW480 (line)]] | alt | 24.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.353× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.410× (z -8.6) |
| [[AN3 CA (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -8.5) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 77.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -16.6) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 31.3 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0938× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.225× (z -9.4) ⚠ cell-cycle shift, explains ~26% of this change |
| [[RKO (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 47.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 35.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1828), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*65 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITCH]] | +0.61 | +0.52 / +0.46 | both halves | 2e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation |
| [[NDUFA6]] | +0.57 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[DCAF10]] | +0.56 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Neddylation |
| [[DHRS7B]] | +0.56 | +0.46 / +0.66 | both halves | 3e-05 |  |
| [[FAM193A]] | +0.56 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[HGSNAT]] | +0.56 | +0.40 / +0.54 | both halves | 4e-05 |  |
| [[ING2-DT]] | +0.55 | +0.49 / +0.62 | both halves | 2e-05 |  |
| [[RBX1]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 | pathway: Antigen processing: Ubiquitination & Proteasome degradation; STRING 955 |
| [[UBN1]] | +0.54 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[TMEM106A]] | +0.54 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[NMNAT1]] | +0.54 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ZMYM5]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*35 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUXAP8]] | -0.55 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[SNRNP200]] | -0.53 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[TGOLN2]] | -0.53 | -0.45 / -0.57 | both halves | 3e-05 |  |
| [[APP]] | -0.53 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[MAT2A]] | -0.52 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[PFKM]] | -0.51 | -0.35 / -0.55 | both halves | 1e-04 |  |
| [[RAB3D]] | -0.51 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[G3BP1]] | -0.51 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[PRELID3B]] | -0.50 | -0.34 / -0.59 | both halves | 1e-04 |  |
| [[SOAT1]] | -0.50 | -0.42 / -0.44 | both halves | 4e-05 |  |
| [[DLD]] | -0.50 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SYNJ2BP]] | -0.50 | -0.30 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KLHL22's level | compounds that target TOP2A: 2 of 5 raise it (Doxorubicin, Idarubicin) | 40% of the class's compounds vs 0.6% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.492). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-34.8, -27.1); signed map (-2.4, 0.9). **Vector** length 93.3, 24.4% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +3.5 | +3.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +0.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +5.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.3 |
|  | [[Gemcitabine (drug)]] 0.05 µM |  | +1.9 | +1.5 |
|  | [[Resveratrol (drug)]] 5 µM |  | +1.8 | +0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | -0.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.7 | +1.5 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +1.6 | +2.0 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.3 | -13.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -7.1 | -13.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.0 | -5.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -13.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.9 | -10.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.3 | -11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -3.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | kelch like family member 22 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,441,519-20,495,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14360, KELCHL |
| Gene groups (HGNC) | Kelch like; BTB domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GT1](https://www.uniprot.org/uniprotkb/Q53GT1) (Kelch-like protein 22):

> Substrate-specific adapter of a BCR (BTB-CUL3-RBX1) E3 ubiquitin ligase complex required for chromosome alignment and localization of PLK1 at kinetochores. The BCR(KLHL22) ubiquitin ligase complex mediates monoubiquitination of PLK1, leading to PLK1 dissociation from phosphoreceptor proteins and subsequent removal from kinetochores, allowing silencing of the spindle assembly checkpoint (SAC) and chromosome segregation. Monoubiquitination of PLK1 does not lead to PLK1 degradation. The …

**Summary**, from NCBI Gene [84861](https://www.ncbi.nlm.nih.gov/gene/84861):

> Enables 14-3-3 protein binding activity and ubiquitin-like ligase-substrate adaptor activity. Involved in several processes, including cellular response to L-leucine; mitotic spindle assembly checkpoint signaling; and positive regulation of TORC1 signaling. Located in several cellular components, including intercellular bridge; lysosome; and microtubule cytoskeleton. Part of Cul3-RING ubiquitin ligase complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25888) · Entrez [84861](https://www.ncbi.nlm.nih.gov/gene/84861) · UniProt [Q53GT1](https://www.uniprot.org/uniprotkb/Q53GT1) · Ensembl [ENSG00000099910](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099910)

## Data

Gene col 1828: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1828); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1828, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1828]; `tensor/DDL_lfc|DDL_z.npy` [1828]; `embed/gene_vectors.npy` [1828]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1828 or target_col == 1828). Every well: [[KLHL22 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLHL22.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
