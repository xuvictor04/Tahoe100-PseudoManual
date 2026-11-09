---
symbol: "MAP3K3"
type: "gene"
col: 12730
ensembl_id: "ENSG00000198909"
name: "mitogen-activated protein kinase kinase kinase 3"
location: "17q23.3"
module: 145
arm: "+"
pooled_cpm: 40.37
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/145"]
generated_by: "tahoemap"
---

# MAP3K3

*mitogen-activated protein kinase kinase kinase 3* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.91× (z +20.5, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.474× (z -16.8, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 0.659× (z -13.3, q 4e-38, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPSB3]] (+0.74, fdr 7e-06), [[MXD4]] (+0.73, fdr 7e-06), [[SRGAP2D]] (+0.72, fdr 7e-06); moves opposite to [[GTF2H3]] (-0.67, fdr 7e-06), [[ZNF300]] (-0.65, fdr 4e-05), [[KICS2]] (-0.63, fdr 1e-05).
> It is in [[Module 145]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SRGAP2C]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12730.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +20.5 | 0e+00 | 42/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.42×** | +19.9 | 0e+00 | 48/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +19.7 | 0e+00 | 46/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.18×** | +17.5 | 0e+00 | 47/48 (CFPAC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.72×** | +12.1 | 7e-32 | 42/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.71×** | +12.0 | 2e-31 | 42/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.97×** | +8.0 | 1e-13 | 37/48 (HEC-1-A, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.39×** | +7.4 | 1e-11 | 26/48 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.26×** | +7.3 | 2e-11 | 23/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.71×** | +6.3 | 1e-08 | 32/48 (J82, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.0 | 8e-08 | 22/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +5.8 | 2e-07 | 28/48 (SW480, C32, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.6 | 7e-07 | 23/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.25×** | +5.1 | 2e-05 | 22/47 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.9 | 3e-05 | 21/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.21×** | +4.3 | 8e-04 | 19/48 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12730.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.474×** | -16.8 | 0e+00 | 47/48 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.464×** | -16.6 | 0e+00 | 30/39 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.481×** | -15.2 | 0e+00 | 34/45 (SW480, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.514×** | -15.0 | 0e+00 | 35/45 (NCI-H1792, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.659×** | -13.3 | 4e-38 | 43/48 (Panc 03.27, MIA PaCa-2, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.587×** | -12.0 | 4e-31 | 36/48 (A-172, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.646×** | -9.8 | 8e-21 | 31/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.479×** | -8.6 | 4e-16 | 37/48 (SW480, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.488×** | -8.4 | 2e-15 | 37/47 (SW480, A-427, …) | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.697×** | -8.1 | 2e-14 | 30/48 (MIA PaCa-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.514×** | -7.8 | 3e-13 | 33/47 (RKO, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.519×** | -7.7 | 6e-13 | 34/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.706×** | -7.2 | 2e-11 | 27/47 (HS-578T, A549, …) | all doses, flat | low cells (technical?) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.542×** | -7.2 | 2e-11 | 33/48 (SW480, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.734×** | -7.0 | 1e-10 | 29/48 (HT-29, SHP-77, …) | top dose only |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.616×** | -5.7 | 4e-07 | 28/46 (SNU-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.633×** | -5.4 | 3e-06 | 21/49 (HS-578T, HOP62, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.797×** | -4.9 | 3e-05 | 19/48 (PANC-1, NCI-H661, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.768×** | -4.2 | 6e-04 | 16/48 (SW1417, LOX-IMVI, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12730. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 54.2 | 7 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +15.6) | [[Dinaciclib (drug)]] 5 µM 0.277× (z -16.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 40.9 | 5 | 3 (3 ⚠) | [[Belinostat (drug)]] 5 µM 2.93× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.4 | 8 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +23.2) | — |
| [[LOX-IMVI (line)]] | wt | 49.8 | 2 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.1) | [[Harringtonine (drug)]] 0.5 µM 0.344× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 30.7 | 3 | 4 (3 ⚠) | [[Belinostat (drug)]] 5 µM 3.01× (z +10.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.284× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.470× (z -10.4) |
| [[A-172 (line)]] | wt | 53.8 | 1 | 5 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -17.5) |
| [[MIA PaCa-2 (line)]] | alt | 60.6 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +9.2) | [[Selinexor (drug)]] 5 µM 0.461× (z -10.4) |
| [[SW1417 (line)]] | alt | 46.4 | 2 | 4 (4 ⚠) | [[Belinostat (drug)]] 5 µM 2.58× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 45.5 | 1 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +15.0) | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.356× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 44.9 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +11.1) | [[Selinexor (drug)]] 5 µM 0.451× (z -10.8) |
| [[PANC-1 (line)]] | alt | 26.9 | 2 | 3 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.44× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.426× (z -9.5) |
| [[C32 (line)]] | wt | 39.2 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 20.4 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.19× (z +12.7) | — |
| [[HOP62 (line)]] | alt | 66.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.471× (z -8.9) |
| [[HS-578T (line)]] | alt | 54.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.395× (z -9.1) |
| [[KATO III (line)]] | alt | 36.8 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.60× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.352× (z -9.2) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 16.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +14.6) | — |
| [[LS 180 (line)]] | wt | 16.5 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.90× (z +11.9) | — |
| [[A549 (line)]] | wt | 45.9 | 1 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.0) | [[Dinaciclib (drug)]] 0.5 µM 0.310× (z -10.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.389× (z -8.6) |
| [[C-33 A (line)]] | alt | 39.9 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.82× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -14.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 35.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.215× (z -13.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 61.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +11.0) | [[Docetaxel (drug)]] 0.05 µM 0.317× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~11% of this change |
| [[J82 (line)]] | alt | 63.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.411× (z -11.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 35.7 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.157× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.5 | 2 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.92× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.204× (z -9.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 48.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.74× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.275× (z -10.7) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 54.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.175× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.493× (z -9.5) |
| [[AN3 CA (line)]] | alt | 66.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -9.4) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 43.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 47.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.155× (z -17.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 55.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.348× (z -8.9) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 64.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.305× (z -12.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 49.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -13.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.1) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.2) | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0722× (z -8.8) |
| [[SHP-77 (line)]] | alt | 45.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -14.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.241× (z -9.1) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 60.7 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0658× (z -10.5) |
| [[BT-474 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 53.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12730), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB3]] | +0.74 | +0.58 / +0.71 | both halves | 7e-06 |  |
| [[MXD4]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 |  |
| [[SRGAP2D]] | +0.72 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[ULK1]] | +0.70 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[FBXL20]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RPS6KA5]] | +0.68 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[RNF38]] | +0.67 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TAF5]] | +0.66 | +0.44 / +0.74 | both halves | 3e-05 |  |
| [[RAB40C]] | +0.66 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[CMC2]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[LINC01881]] | +0.65 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[SRGAP2B]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | -0.67 | -0.59 / -0.68 | both halves | 7e-06 |  |
| [[ZNF300]] | -0.65 | -0.41 / -0.63 | both halves | 4e-05 |  |
| [[KICS2]] | -0.63 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TRMO]] | -0.60 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[PUS7L]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[NRAS]] | -0.60 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[GUF1]] | -0.60 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[MRRF]] | -0.59 | -0.42 / -0.60 | both halves | 4e-05 |  |
| [[ZNF460]] | -0.59 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[RRP15]] | -0.59 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[SMIM15]] | -0.59 | -0.47 / -0.57 | both halves | 2e-05 |  |
| [[UTP20]] | -0.59 | -0.47 / -0.56 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRGAP2C]] | B | SRGAP2C activity raises MAP3K3's level | lines that do not express SRGAP2C (5) vs lines expressing it (45) | 1.81× lower at baseline in the lines without SRGAP2C | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TGFBR2, PRDM2, APC; also absent: FAM72B, LINC02798, DNAJB5; its own permutation p |
| [[TOP2A]] | B | TOP2A activity lowers MAP3K3's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 145]]; 31 genes; every member is in the + arm (projection on the module's main direction 0.839). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.21; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.4, -42.7); signed map (-21.5, 11.3). **Vector** length 121, 36.4% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.7 | +12.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.3 | +19.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +20.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.5 | +12.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.4 | +6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +8.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.9 | +5.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.3 | +2.8 |
| fall | [[Selinexor (drug)]] 5 µM |  | -11.6 | -13.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.6 | -16.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -8.9 | -12.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.4 | -15.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -7.8 | -8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.5 | -9.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -7.2 | -8.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.0 | -7.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -6.8 | -8.6 |
|  | [[EX229 (drug)]] 5 µM |  | -6.3 | -7.7 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,622,415-63,696,305 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MAPKKK3; previously MEKK3 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; STE11 kinase family |
| Reactome | 4 pathways, smallest: Interleukin-1 signaling; Interleukin-1 family signaling; Signaling by Interleukins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99759](https://www.uniprot.org/uniprotkb/Q99759) (Mitogen-activated protein kinase kinase kinase 3):

> Component of a protein kinase signal transduction cascade. Mediates activation of the NF-kappa-B, AP1 and DDIT3 transcriptional regulators.

**Summary**, from NCBI Gene [4215](https://www.ncbi.nlm.nih.gov/gene/4215):

> This gene product is a 626-amino acid polypeptide that is 96.5% identical to mouse Mekk3. Its catalytic domain is closely related to those of several other kinases, including mouse Mekk2, tobacco NPK, and yeast Ste11. Northern blot analysis revealed a 4.6-kb transcript that appears to be ubiquitously expressed. This protein directly regulates the stress-activated protein kinase (SAPK) and extracellular signal-regulated protein kinase (ERK) pathways by activating SEK and MEK1/2 respectively; it …

**Accessions** — [HGNC:6855](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6855) · Entrez [4215](https://www.ncbi.nlm.nih.gov/gene/4215) · UniProt [Q99759](https://www.uniprot.org/uniprotkb/Q99759) · Ensembl [ENSG00000198909](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198909)

## Data

Gene col 12730: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12730); `tables/drug_effects.parquet` (61 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12730, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12730]; `tensor/DDL_lfc|DDL_z.npy` [12730]; `embed/gene_vectors.npy` [12730]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12730 or target_col == 12730). Every well: [[MAP3K3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
