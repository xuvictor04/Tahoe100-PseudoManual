---
symbol: "MAGI1"
type: "gene"
col: 7501
ensembl_id: "ENSG00000151276"
name: "membrane associated guanylate kinase, WW and PDZ domain containing 1"
location: "3p14.1"
module: 160
arm: "+"
pooled_cpm: 265.88
n_lines_expressing: 47
n_dd_up: 10
n_dd_down: 30
n_dd_up_clean: 10
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# MAGI1

*membrane associated guanylate kinase, WW and PDZ domain containing 1* — 3p14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.96× (z +12.4, q 1e-32, up in 40 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.483× (z -12.9, q 2e-35, down in 35 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.524× (z -11.9, q 2e-30, down in 30 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TCF7L2]] (+0.60, fdr 1e-05), [[USP6NL]] (+0.60, fdr 1e-05), [[STIM2]] (+0.59, fdr 1e-05); moves opposite to [[RNF14]] (-0.57, fdr 1e-05), [[ZNF621]] (-0.54, fdr 2e-05), [[DDX59]] (-0.52, fdr 4e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[MAP3K4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7501.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +12.4 | 1e-32 | 40/45 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +12.1 | 2e-31 | 40/45 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.92×** | +12.1 | 3e-31 | 42/45 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +11.8 | 8e-30 | 38/45 (J82, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.67×** | +9.4 | 5e-19 | 40/45 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +6.8 | 1e-09 | 24/45 (A-172, J82, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.99×** | +6.6 | 3e-09 | 36/46 (J82, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 4e-04 | 25/46 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.029 | 21/45 (NCI-H1792, C32, …) | top dose only |  |
| [[BAY1125976 (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.038 | 20/45 (LoVo, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7501.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.483×** | -12.9 | 2e-35 | 35/41 (SK-MEL-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.502×** | -12.2 | 5e-32 | 36/44 (KATO III, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.524×** | -11.9 | 2e-30 | 30/45 (NCI-H2030, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.557×** | -10.0 | 2e-21 | 31/42 (SNU-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -9.3 | 1e-18 | 33/46 (Panc 03.27, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.654×** | -7.8 | 4e-13 | 33/45 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.703×** | -6.5 | 7e-09 | 31/45 (RKO, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -6.4 | 1e-08 | 28/45 (SK-MEL-2, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -6.3 | 2e-08 | 27/45 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.709×** | -6.0 | 1e-07 | 30/45 (SK-MEL-2, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.544×** | -5.9 | 2e-07 | 37/45 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.735×** | -5.7 | 6e-07 | 26/45 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.560×** | -5.6 | 1e-06 | 27/36 (NCI-H2030, C32, …) | top dose only | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | **0.814×** | -5.3 | 4e-06 | 26/45 (PANC-1, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.759×** | -5.1 | 1e-05 | 24/45 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.599×** | -4.9 | 2e-05 | 31/45 (LoVo, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.609×** | -4.8 | 5e-05 | 33/45 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.723×** | -4.7 | 7e-05 | 28/45 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.781×** | -4.6 | 1e-04 | 27/45 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.720×** | -4.3 | 4e-04 | 25/45 (LoVo, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.812×** | -3.8 | 0.003 | 22/45 (RKO, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **0.698×** | -3.5 | 0.013 | 21/45 (LoVo, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.818×** | -3.4 | 0.014 | 21/44 (C32, NCI-H1792, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7501. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 103 | 12 (5 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 6.67× (z +19.3) | [[Selinexor (drug)]] 5 µM 0.428× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Dexamethasone (drug)]] 0.5 µM 0.425× (z -8.7) |
| [[RKO (line)]] | wt | 205 | 7 (2 ⚠) | 7 (3 ⚠) | [[Panobinostat (drug)]] 0.05 µM 3.07× (z +12.1) | [[Homoharringtonine (drug)]] 0.05 µM 0.322× (z -12.3) |
| [[SK-MEL-2 (line)]] | alt | 574 | 0 | 13 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0754× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -17.5) |
| [[J82 (line)]] | alt | 153 | 11 (3 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.30× (z +19.2) | [[Dinaciclib (drug)]] 5 µM 0.429× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 112 | 6 | 6 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.19× (z +14.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.355× (z -13.4) |
| [[NCI-H2030 (line)]] | alt | 451 | 0 | 11 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -25.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -17.9) |
| [[LoVo (line)]] | wt | 322 | 6 (2 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.69× (z +11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[BAY1125976 (drug)]] 5 µM 3.84× (z +10.8) | [[Auranofin (drug)]] 5 µM 0.415× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 366 | 5 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +23.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Belinostat (drug)]] 5 µM 1.72× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.442× (z -11.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 269 | 4 | 5 (3 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.53× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -20.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -16.0) |
| [[hTERT-HPNE (line)]] | wt | 105 | 8 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 10.7× (z +17.8) | — |
| [[LOX-IMVI (line)]] | wt | 136 | 6 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.35× (z +18.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.408× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 304 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.276× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -12.1) |
| [[SW480 (line)]] | alt | 437 | 0 | 8 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.303× (z -15.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.444× (z -11.7) |
| [[A549 (line)]] | wt | 92.7 | 7 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.05 µM 3.50× (z +11.9) | — |
| [[HOP62 (line)]] | alt | 96.4 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 8.77× (z +18.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 4 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.47× (z +12.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.358× (z -10.0) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.386× (z -9.7) |
| [[Panc 03.27 (line)]] | alt | 608 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.455× (z -9.2) |
| [[RPMI-7951 (line)]] | alt | 148 | 7 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.75× (z +15.4) | — |
| [[SW48 (line)]] | wt | 310 | 6 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.58× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -8.9) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 115 | 4 (2 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.53× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.508× (z -8.9) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.524× (z -8.5) |
| [[C32 (line)]] | wt | 204 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -12.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.214× (z -11.9) |
| [[KATO III (line)]] | alt | 698 | 0 | 6 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -17.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 427 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -17.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.328× (z -16.6) |
| [[SNU-1 (line)]] | wt | 436 | 2 (2 ⚠) | 4 (4 ⚠) | [[Harringtonine (drug)]] 5 µM 2.40× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 81.0 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.40× (z +12.7) | — |
| [[HS-578T (line)]] | alt | 389 | 2 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.63× (z +10.6) | [[Homoharringtonine (drug)]] 0.5 µM 0.411× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 420 | 0 | 5 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.308× (z -12.6) ⚠ toxic · without an alert: [[Phenylephrine (hydrochloride) (drug)]] 5 µM 0.411× (z -9.9) |
| [[A-427 (line)]] | wt | 241 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 1.98× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.215× (z -19.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 151 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.16× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 298 | 2 | 2 (2 ⚠) | [[Belinostat (drug)]] 5 µM 2.10× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.307× (z -15.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 278 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.352× (z -11.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.439× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 279 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -23.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.194× (z -16.8) |
| [[SNU-423 (line)]] | alt | 234 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.48× (z +13.8) | — |
| [[HepG2_C3A (line)]] | wt | 862 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.175× (z -17.1) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.359× (z -10.4) |
| [[LS 180 (line)]] | wt | 425 | 1 | 2 (2 ⚠) | [[BAY1125976 (drug)]] 5 µM 4.90× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -14.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 519 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -16.0) ⚠ toxic |
| [[SW 900 (line)]] | alt | 322 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.281× (z -12.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 247 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.317× (z -9.4) |
| [[CHP-212 (line)]] | wt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -11.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 287 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.54× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 213 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.213× (z -8.9) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 274 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0610× (z -12.0) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 43.4 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 41.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 262 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 48.2 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 258 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 74.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7501), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF7L2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[USP6NL]] | +0.60 | +0.54 / +0.60 | both halves | 1e-05 |  |
| [[STIM2]] | +0.59 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[LRP6]] | +0.58 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZNF704]] | +0.57 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[IGF1R]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[OSBPL10]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[SPATA13]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[MAML3]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ARHGAP26]] | +0.55 | +0.46 / +0.56 | both halves | 3e-05 |  |
| [[IFFO2]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[PHLPP1]] | +0.53 | +0.51 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF14]] | -0.57 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[ZNF621]] | -0.54 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[DDX59]] | -0.52 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[PAAF1]] | -0.51 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[MTERF4]] | -0.51 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[KRBOX4]] | -0.49 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[PIGC]] | -0.49 | -0.47 / -0.38 | both halves | 6e-05 |  |
| [[CIAO3]] | -0.48 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LVRN]] | -0.48 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[MTRF1]] | -0.48 | -0.42 / -0.40 | both halves | 4e-05 |  |
| [[FAM149B1]] | -0.48 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[ZDHHC6]] | -0.48 | -0.53 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers MAGI1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers MAGI1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[NOS1AP]] | B | NOS1AP activity raises MAGI1's level | lines that do not express NOS1AP (9) vs lines expressing it (41) | 2.37× lower at baseline in the lines without NOS1AP | 0.091 | ⚠ within organs, on part of the lines; also absent: ENSG00000254706, C1orf226, CMTM8; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K4]] | C | MAGI1 activity raises MAP3K4's level | lines that do not express MAGI1 (3) vs lines expressing it (47) | 1.76× lower at baseline in the lines without MAGI1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PXYLP1, YPEL2, TMEM229B; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.380). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-6.2, 38.0); signed map (-2.9, 27.3). **Vector** length 130, 44.7% of its response variance represented; |z| ≥ 3 in 1,756 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +7.2 | +9.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +7.1 | +12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.9 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +6.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.3 | +6.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +3.1 | +2.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +2.3 | +2.4 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +2.1 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.9 | -12.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.3 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -6.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.6 | -5.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -4.6 | -2.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -4.2 | -0.4 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -4.2 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | membrane associated guanylate kinase, WW and PDZ domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.1 — chr3:65,353,525-66,038,918 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BAP1, MAGI-1, TNRC19, AIP3, WWP3; previously BAIAP1 |
| Gene groups (HGNC) | Membrane associated guanylate kinases; PDZ domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QZ7](https://www.uniprot.org/uniprotkb/Q96QZ7) (Membrane-associated guanylate kinase, WW and PDZ domain-containing protein 1):

> Plays a role in coupling actin fibers to cell junctions in endothelial cells, via its interaction with AMOTL2 and CDH5 (By similarity). May regulate acid-induced ASIC3 currents by modulating its expression at the cell surface (By similarity).

**Summary**, from NCBI Gene [9223](https://www.ncbi.nlm.nih.gov/gene/9223):

> The protein encoded by this gene is a member of the membrane-associated guanylate kinase homologue (MAGUK) family. MAGUK proteins participate in the assembly of multiprotein complexes on the inner surface of the plasma membrane at regions of cell-cell contact. The product of this gene may play a role as scaffolding protein at cell-cell junctions. Alternatively spliced transcript variants encoding different isoforms have been identified. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:946](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:946) · Entrez [9223](https://www.ncbi.nlm.nih.gov/gene/9223) · UniProt [Q96QZ7](https://www.uniprot.org/uniprotkb/Q96QZ7) · Ensembl [ENSG00000151276](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151276)

## Data

Gene col 7501: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7501); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7501, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7501]; `tensor/DDL_lfc|DDL_z.npy` [7501]; `embed/gene_vectors.npy` [7501]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7501 or target_col == 7501). Every well: [[MAGI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAGI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
