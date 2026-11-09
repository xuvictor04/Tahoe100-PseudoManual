---
symbol: "HELB"
type: "gene"
col: 4797
ensembl_id: "ENSG00000127311"
name: "DNA helicase B"
location: "12q14.3"
module: 187
arm: "+"
pooled_cpm: 54.06
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 28
n_dd_up_clean: 8
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/187"]
generated_by: "tahoemap"
---

# HELB

*DNA helicase B* — 12q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 2.17× (z +14.7, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.436× (z -16.0, q 0e+00, down in 29 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.439× (z -8.6, q 1e-15, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAPP]] (+0.62, fdr 1e-05), [[HSCB]] (+0.58, fdr 1e-05), [[CD40]] (+0.56, fdr 3e-05); moves opposite to [[MAPK1]] (-0.47, fdr 5e-05), [[FAM120A]] (-0.43, fdr 1e-04), [[SCART1]] (-0.42, fdr 2e-04).
> It is in [[Module 187]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **2.17×** | +14.7 | 0e+00 | 46/48 (LOX-IMVI, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.86×** | +12.5 | 2e-33 | 41/48 (LOX-IMVI, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.68×** | +10.5 | 2e-23 | 39/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.44×** | +7.1 | 2e-10 | 31/48 (NCI-H2347, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.50×** | +5.8 | 6e-07 | 30/49 (LOX-IMVI, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +5.6 | 3e-06 | 23/48 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.31×** | +5.4 | 5e-06 | 25/48 (A-427, H4, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.1 | 2e-05 | 22/48 (SHP-77, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +4.8 | 9e-05 | 22/43 (NCI-H460, SW1417, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.27×** | +4.8 | 1e-04 | 22/48 (RKO, NCI-H460, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | 1.16× | +4.3 | 0.001 | 18/48 (A-427, SW1417, …) | all doses, flat | low cells (technical?) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.25×** | +3.9 | 0.006 | 15/48 (PANC-1, BT-474, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.008 | 16/48 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.41×** | +3.6 | 0.012 | 12/48 (A498, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.17× | +3.1 | 0.069 | 15/47 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Hexylresorcinol (drug)]] 5 µM |  | 1.12× | +3.1 | 0.069 | 3/49 (NCI-H1573, SNU-423, …) | top dose only | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.095 | 12/48 (NCI-H23, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.436×** | -16.0 | 0e+00 | 29/43 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.477×** | -14.0 | 7e-42 | 46/48 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **0.572×** | -11.2 | 1e-26 | 40/49 (NCI-H23, A-427, …) | all doses, stronger at high dose | composition shift |
| [[TAK-733 (drug)]] 5 µM |  | **0.439×** | -8.6 | 1e-15 | 41/48 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.468×** | -7.9 | 2e-13 | 34/48 (NCI-H1792, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.476×** | -7.8 | 8e-13 | 37/48 (RKO, A549, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.485×** | -7.6 | 3e-12 | 33/48 (Hs 766T, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.508×** | -7.1 | 1e-10 | 33/48 (CHP-212, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.682×** | -7.1 | 1e-10 | 25/43 (SNU-423, A-427, …) | all doses, stronger at high dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.747×** | -5.8 | 4e-07 | 22/48 (LOX-IMVI, C-33 A, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.821×** | -5.5 | 3e-06 | 22/48 (C-33 A, CFPAC-1, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.763×** | -5.2 | 1e-05 | 28/48 (PANC-1, NCI-H23, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.787×** | -4.8 | 8e-05 | 23/48 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **0.794×** | -4.4 | 4e-04 | 22/47 (H4, SNU-423, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 0.857× | -4.3 | 6e-04 | 19/49 (CFPAC-1, A549, …) | rises with dose |  |
| [[Ixazomib (drug)]] 5 µM |  | **0.672×** | -4.1 | 0.001 | 21/48 (HCT15, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.819×** | -4.0 | 0.002 | 22/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.759×** | -3.9 | 0.003 | 17/48 (NCI-H460, SW 1271, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.762×** | -3.9 | 0.003 | 18/48 (A549, NCI-H1792, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.827×** | -3.6 | 0.008 | 14/47 (A-172, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 166 | 1 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.39× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.0533× (z -35.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 27.5 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.60× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.60× (z +10.9) | — |
| [[SW480 (line)]] | alt | 56.3 | 1 | 4 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.20× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.336× (z -12.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 42.7 | 2 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.99× (z +10.3) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[LoVo (line)]] | wt | 43.1 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.62× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.397× (z -8.8) ⚠ unreliable plate only |
| [[LOX-IMVI (line)]] | wt | 49.5 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.05× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -12.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 145 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -20.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 51.2 | 3 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.51× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.373× (z -11.2) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 95.0 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.62× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.406× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[SNU-423 (line)]] | alt | 38.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0947× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.224× (z -12.2) |
| [[A-172 (line)]] | wt | 23.7 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.40× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.26× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[HT-29 (line)]] | alt | 43.5 | 2 | 1 (1 ⚠) | [[Bortezomib (drug)]] 0.05 µM 3.21× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[NCI-H1792 (line)]] | alt | 97.8 | 0 | 3 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.143× (z -14.9) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 59.0 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 46.8 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.57× (z +9.2) | — |
| [[A549 (line)]] | wt | 89.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -22.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 79.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -13.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 59.5 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.221× (z -13.9) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 40.5 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 5 µM 0.344× (z -9.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 38.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.94× (z +9.9) | — |
| [[NCI-H1573 (line)]] | alt | 101 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -13.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 47.8 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +11.4) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 54.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.48× (z +10.2) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.306× (z -9.1) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.279× (z -12.3) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 43.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.39× (z +11.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[CFPAC-1 (line)]] | alt | 62.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 20.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.203× (z -9.1) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -9.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.196× (z -12.8) |
| [[Panc 03.27 (line)]] | alt | 26.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 63.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.183× (z -14.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 35.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.19× (z +9.3) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 62.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 43.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 50.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 66.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAPP]] | +0.62 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[HSCB]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[CD40]] | +0.56 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[BTN3A2]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[BSDC1]] | +0.55 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[PFDN4]] | +0.54 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[TBC1D15]] | +0.54 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[BTN2A3P-1]] | +0.51 | +0.47 / +0.48 | both halves | 2e-05 |  |
| [[HACL1]] | +0.50 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[CBR3]] | +0.49 | +0.36 / +0.48 | both halves | 9e-05 |  |
| [[BTN3A3]] | +0.49 | +0.50 / +0.40 | both halves | 5e-05 |  |
| [[IKZF5]] | +0.48 | +0.38 / +0.53 | both halves | 7e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK1]] | -0.47 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[FAM120A]] | -0.43 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[SCART1]] | -0.42 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[EEFSEC]] | -0.40 | -0.35 / -0.36 | both halves | 1e-04 |  |
| [[EIF4G1]] | -0.39 | -0.37 / -0.47 | both halves | 9e-05 |  |
| [[ACTB]] | -0.39 | -0.48 / -0.31 | both halves | 2e-04 |  |
| [[PDHA1]] | -0.39 | -0.24 / -0.46 | both halves | 4e-04 |  |
| [[E2F4]] | -0.39 | -0.32 / -0.37 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity lowers HELB's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 187]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (7.3, -49.7); signed map (-9.2, 10.7). **Vector** length 124, 36.0% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.1 | +14.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +10.5 | +12.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +9.4 | +10.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.9 | +5.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +5.6 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +1.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -10.1 | -14.0 |
|  | [[EX229 (drug)]] 5 µM |  | -6.8 | -7.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.6 | -8.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -5.6 | -7.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.9 | -7.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | DNA helicase B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.3 — chr12:66,302,493-66,343,643 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NG08](https://www.uniprot.org/uniprotkb/Q8NG08) (DNA helicase B):

> 5'-3' DNA helicase involved in DNA damage response by acting as an inhibitor of DNA end resection. Recruitment to single-stranded DNA (ssDNA) following DNA damage leads to inhibit the nucleases catalyzing resection, such as EXO1, BLM and DNA2, possibly via the 5'-3' ssDNA translocase activity of HELB. As cells approach S phase, DNA end resection is promoted by the nuclear export of HELB following phosphorylation. Acts independently of TP53BP1. Unwinds duplex DNA with 5'-3' polarity. Has …

**Summary**, from NCBI Gene [92797](https://www.ncbi.nlm.nih.gov/gene/92797):

> This gene encodes a DNA-dependent ATPase which catalyzes the unwinding of DNA necessary for DNA replication, repair, recombination, and transcription. This gene is thought to function specifically during the S phase entry of the cell cycle. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Feb 2016]

**Accessions** — [HGNC:17196](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17196) · Entrez [92797](https://www.ncbi.nlm.nih.gov/gene/92797) · UniProt [Q8NG08](https://www.uniprot.org/uniprotkb/Q8NG08) · Ensembl [ENSG00000127311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127311)

## Data

Gene col 4797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4797); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4797]; `tensor/DDL_lfc|DDL_z.npy` [4797]; `embed/gene_vectors.npy` [4797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4797 or target_col == 4797). Every well: [[HELB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HELB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
