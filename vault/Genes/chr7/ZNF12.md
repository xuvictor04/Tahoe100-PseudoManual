---
symbol: "ZNF12"
type: "gene"
col: 8977
ensembl_id: "ENSG00000164631"
name: "zinc finger protein 12"
location: "7p22.1"
module: 17
arm: "+"
pooled_cpm: 60.76
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# ZNF12

*zinc finger protein 12* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 1.65× (z +11.0, q 3e-25, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.524× (z -13.8, q 2e-40, down in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.785× (z -5.2, q 2e-05, down in 23 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-172 0.0462×, SK-MEL-2 0.123×, A498 0.230×, RPMI-7951 0.162×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 0.352×, CHP-212 0.0776×, KATO III 0.345×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.284×, PANC-1 0.546×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.393×, AN3 CA 0.171×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0777×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0953×).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB26]] (+0.64, fdr 1e-05), [[ZNF112]] (+0.63, fdr 1e-05), [[ZNF84]] (+0.61, fdr 3e-05); moves opposite to [[ITSN1]] (-0.50, fdr 1e-04), [[CLEC16A]] (-0.48, fdr 1e-04), [[CYFIP1]] (-0.48, fdr 1e-04).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8977.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +11.0 | 3e-25 | 42/48 (LoVo, SW480, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.51×** | +9.1 | 3e-17 | 32/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.17×** | +8.9 | 8e-17 | 41/49 (A498, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +8.6 | 8e-16 | 33/47 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.06×** | +8.3 | 8e-15 | 39/48 (KATO III, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +7.8 | 4e-13 | 34/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.3 | 2e-11 | 26/37 (SW480, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +6.5 | 7e-09 | 26/45 (A549, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +6.4 | 8e-09 | 24/48 (A498, NCI-H460, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +6.1 | 5e-08 | 29/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.30×** | +5.7 | 7e-07 | 27/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.9 | 4e-05 | 22/48 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +4.4 | 5e-04 | 21/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 23/48 (SW 900, BT-474, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.21×** | +4.1 | 0.002 | 22/48 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.14× | +3.9 | 0.003 | 8/48 (PANC-1, A549, …) | inconsistent across doses | position effect removed |
| [[Isocorydine (drug)]] 0.5 µM |  | 1.19× | +3.8 | 0.005 | 19/48 (SW480, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.18× | +3.3 | 0.025 | 17/47 (MIA PaCa-2, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.041 | 12/48 (HEC-1-A, KATO III, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 11 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8977.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 7 lines (A-172 0.0462×, SK-MEL-2 0.123×, A498 0.230×, RPMI-7951 0.162×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (A498 0.352×, CHP-212 0.0776×, KATO III 0.345×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (RKO 0.284×, PANC-1 0.546×; ⚠ cell-cycle shift, explains ~0% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (PANC-1 0.393×, AN3 CA 0.171×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (CHP-212 0.0777×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0953×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -13.8 | 2e-40 | 34/44 (A-172, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.654×** | -9.4 | 2e-18 | 31/49 (A498, CHP-212, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.714×** | -7.5 | 2e-11 | 37/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.755×** | -6.2 | 6e-08 | 33/48 (A498, PANC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.769×** | -5.6 | 2e-06 | 27/48 (A-427, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.785×** | -5.2 | 2e-05 | 23/48 (PANC-1, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.820×** | -4.4 | 9e-04 | 23/48 (PANC-1, A498, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.834× | -3.9 | 0.007 | 20/50 (SK-MEL-2, NCI-H23, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | 0.835× | -3.9 | 0.007 | 21/47 (C32, SHP-77, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | 0.891× | -3.6 | 0.015 | 14/49 (A498, SNU-423, …) | top dose only | position effect removed |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | 0.860× | -3.4 | 0.038 | 11/48 (SNU-1, NCI-H23, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.861× | -3.3 | 0.038 | 13/48 (RKO, A498, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.907× | -3.1 | 0.088 | 18/48 (RKO, PANC-1, …) | top dose only | composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8977. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 65.7 | 6 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.01× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.345× (z -12.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 54.7 | 7 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.92× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.76× (z +13.4) | — |
| [[SW480 (line)]] | alt | 62.4 | 7 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.61× (z +14.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +14.7) | — |
| [[A498 (line)]] | wt | 86.0 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -20.3) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 82.1 | 2 (1 ⚠) | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +9.9) | [[Harringtonine (drug)]] 5 µM 0.393× (z -13.5) |
| [[SK-MEL-2 (line)]] | alt | 93.0 | 1 (1 ⚠) | 3 (3 ⚠) | [[Harringtonine (drug)]] 0.5 µM 2.27× (z +8.7) ⚠ cell-cycle shift, explains ~6% of this change | [[Dinaciclib (drug)]] 5 µM 0.123× (z -21.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 60.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0776× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0777× (z -13.4) |
| [[RKO (line)]] | wt | 61.3 | 2 (2 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.88× (z +10.0) ⚠ toxic | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 101 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.122× (z -13.0) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.171× (z -10.5) |
| [[HS-578T (line)]] | alt | 39.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 7.38× (z +9.7) | — |
| [[LoVo (line)]] | wt | 48.5 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.33× (z +10.0) | — |
| [[LS 180 (line)]] | wt | 39.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.09× (z +10.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 103 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.07× (z +8.5) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.274× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 48.4 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.80× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 90.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.162× (z -16.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 66.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -11.3) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 80.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.197× (z -13.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 63.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0462× (z -29.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 45.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.56× (z +11.4) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 57.9 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[C32 (line)]] | wt | 57.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.331× (z -10.4) ⚠ toxic; cell-cycle shift, explains ~8% of this change |
| [[COLO 205 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -10.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 72.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.325× (z -8.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 47.7 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.51× (z +9.2) ⚠ toxic | — |
| [[J82 (line)]] | alt | 62.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.259× (z -14.2) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 49.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.414× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.46× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 61.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.419× (z -8.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 87.1 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0953× (z -10.1) |
| [[A-427 (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 101 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 55.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 48.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 63.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 89.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 62.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 55.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 86.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 74.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 52.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8977), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 12 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB26]] | +0.64 | +0.52 / +0.69 | both halves | 1e-05 | same gene group |
| [[ZNF112]] | +0.63 | +0.53 / +0.67 | both halves | 1e-05 | same gene group |
| [[ZNF84]] | +0.61 | +0.46 / +0.67 | both halves | 3e-05 | same gene group |
| [[C2orf49]] | +0.59 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[TRIT1]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[JRK]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 |  |
| [[PMS2CL]] | +0.55 | +0.63 / +0.45 | both halves | 3e-05 | ⚠ same locus (28.4 kb: neighbours can correlate without regulation) |
| [[ZKSCAN8]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 | same gene group |
| [[COA5]] | +0.53 | +0.34 / +0.54 | both halves | 1e-04 |  |
| [[SNRNP35]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[DYNLT2]] | +0.53 | +0.30 / +0.57 | both halves | 2e-04 |  |
| [[SEC31B]] | +0.52 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[MAFIP]] | +0.52 | +0.42 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITSN1]] | -0.50 | -0.33 / -0.57 | both halves | 1e-04 |  |
| [[CLEC16A]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[CYFIP1]] | -0.48 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[SNTB2]] | -0.44 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[FRYL]] | -0.44 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[NPIPB5]] | -0.44 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[EHBP1]] | -0.44 | -0.39 / -0.38 | both halves | 6e-05 |  |
| [[PDLIM5]] | -0.43 | -0.33 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises ZNF12's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ACTG1P17]] | C | ACTG1P17's natural level strengthens ZNF12's drug response | ACTG1P17's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.07; direction not clear | 0.060 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.207). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-41.1, 15.7); signed map (-16.1, -17.8). **Vector** length 92.5, 21.0% of its response variance represented; |z| ≥ 3 in 952 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.4 | +11.0 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.9 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.5 | +8.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.7 | +4.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.8 | +8.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | -0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.2 | +3.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +0.5 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~8% of this change | -6.5 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.2 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | -3.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.3 | -3.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.3 | -9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.3 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -1.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:6,688,433-6,706,947 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KOX3, GIOT-3; previously ZNF325 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17014](https://www.uniprot.org/uniprotkb/P17014) (Zinc finger protein 12):

> Transcriptional repressor which suppresses activation protein 1 (AP-1)- and serum response element (SRE)-mediated transcriptional activity.

**Summary**, from NCBI Gene [7559](https://www.ncbi.nlm.nih.gov/gene/7559):

> This gene is a member of the krueppel C2H2-type zinc-finger protein family and encodes a protein with eight C2H2-type zinc fingers and a KRAB domain. This nuclear protein is involved in developmental control of gene expression. Alternate transcriptional splice variants, encoding different isoforms, have been characterized. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12902](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12902) · Entrez [7559](https://www.ncbi.nlm.nih.gov/gene/7559) · UniProt [P17014](https://www.uniprot.org/uniprotkb/P17014) · Ensembl [ENSG00000164631](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164631)

## Data

Gene col 8977: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8977); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8977, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8977]; `tensor/DDL_lfc|DDL_z.npy` [8977]; `embed/gene_vectors.npy` [8977]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8977 or target_col == 8977). Every well: [[ZNF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
