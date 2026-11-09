---
symbol: "SLC38A2"
type: "gene"
col: 5540
ensembl_id: "ENSG00000134294"
name: "solute carrier family 38 member 2"
location: "12q13.11"
module: 113
arm: "+"
pooled_cpm: 413.06
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 35
n_dd_up_clean: 6
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# SLC38A2

*solute carrier family 38 member 2* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 1.33× (z +5.7, q 8e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 35 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.524× (z -18.0, q 0e+00, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SGK1]] (+0.59, fdr 1e-05), [[ZNF281]] (+0.53, fdr 3e-05), [[ZSWIM6]] (+0.52, fdr 8e-05); moves opposite to [[UBA5]] (-0.53, fdr 4e-05), [[ATPAF1]] (-0.49, fdr 1e-04), [[MIR34AHG]] (-0.45, fdr 5e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[DUSP4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5540.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 8e-06 | 30/48 (COLO 205, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +5.1 | 1e-04 | 30/48 (COLO 205, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.9 | 2e-04 | 1/50 (HOP62) | inconsistent across doses |  |
| [[Gefitinib (drug)]] 5 µM |  | **1.25×** | +4.4 | 0.002 | 33/48 (SNU-1, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.003 | 26/47 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 1.16× | +4.1 | 0.004 | 19/49 (Hs 766T, A-172, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.22×** | +3.9 | 0.007 | 26/48 (LS 180, SNU-1, …) | all doses, flat |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.007 | 30/47 (SK-MEL-2, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.30×** | +3.7 | 0.013 | 27/48 (HS-578T, SW 900, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.6 | 0.020 | 31/45 (LoVo, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~7% of this change | 1.20× | +3.5 | 0.020 | 22/47 (SNU-1, SW480, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.024 | 24/48 (AsPC-1, CFPAC-1, …) | all doses, flat | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.20× | +3.5 | 0.024 | 22/47 (HOP62, J82, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.19× | +3.4 | 0.029 | 21/48 (AN3 CA, NCI-H23, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +3.4 | 0.029 | 22/48 (A498, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.18× | +3.2 | 0.040 | 22/47 (MIA PaCa-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.18× | +3.2 | 0.041 | 21/48 (SW480, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 35 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5540.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.524×** | -18.0 | 0e+00 | 39/48 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.534×** | -17.5 | 0e+00 | 43/49 (HepG2/C3A, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.415×** | -16.7 | 0e+00 | 42/44 (SNU-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.479×** | -14.5 | 1e-45 | 45/49 (MIA PaCa-2, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.515×** | -13.1 | 4e-37 | 47/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.534×** | -11.9 | 1e-30 | 38/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.538×** | -11.8 | 5e-30 | 41/48 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.560×** | -11.4 | 2e-28 | 47/48 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.563×** | -10.9 | 8e-26 | 38/50 (MIA PaCa-2, NCI-H23, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.596×** | -10.2 | 1e-22 | 43/48 (MIA PaCa-2, NCI-H2030, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.577×** | -10.0 | 6e-22 | 36/45 (HepG2/C3A, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.614×** | -9.6 | 3e-20 | 44/48 (HepG2/C3A, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.628×** | -9.2 | 2e-18 | 37/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~36% of this change | **0.626×** | -8.9 | 2e-17 | 40/47 (MIA PaCa-2, HepG2/C3A, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.444×** | -8.4 | 2e-15 | 47/48 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.478×** | -7.6 | 9e-13 | 43/48 (MIA PaCa-2, SW480, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.484×** | -7.5 | 2e-12 | 43/48 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.500×** | -7.2 | 3e-11 | 45/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.625×** | -6.6 | 1e-09 | 43/48 (MIA PaCa-2, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.546×** | -6.2 | 1e-08 | 39/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -5.4 | 2e-06 | 28/48 (SW48, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -4.5 | 1e-04 | 26/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.655×** | -4.4 | 3e-04 | 32/49 (HepG2/C3A, A-172, …) | rises with dose | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.735×** | -4.3 | 3e-04 | 38/49 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5540. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 1,599 | 0 | 29 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.167× (z -29.9) |
| [[MIA PaCa-2 (line)]] | alt | 851 | 2 (1 ⚠) | 19 (9 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 1.79× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -26.1) |
| [[AsPC-1 (line)]] | alt | 608 | 4 (2 ⚠) | 14 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +12.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.76× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.385× (z -14.9) |
| [[A-172 (line)]] | wt | 294 | 0 | 14 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -26.7) |
| [[SNU-1 (line)]] | wt | 727 | 5 (2 ⚠) | 9 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.40× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.130× (z -26.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.452× (z -15.2) |
| [[NCI-H460 (line)]] | wt | 595 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -18.8) |
| [[NCI-H2030 (line)]] | alt | 694 | 0 | 12 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -23.6) |
| [[NCI-H23 (line)]] | alt | 389 | 0 | 12 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.223× (z -18.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.360× (z -18.5) |
| [[SW480 (line)]] | alt | 582 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -20.6) |
| [[LOX-IMVI (line)]] | wt | 396 | 0 | 11 (9 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -19.6) |
| [[HS-578T (line)]] | alt | 356 | 0 | 10 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -17.4) |
| [[LoVo (line)]] | wt | 436 | 1 | 8 (4 ⚠) | [[Auranofin (drug)]] 5 µM 1.82× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.389× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.419× (z -12.8) |
| [[PANC-1 (line)]] | alt | 417 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -31.6) |
| [[SNU-423 (line)]] | alt | 532 | 0 | 9 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -23.1) |
| [[A-427 (line)]] | wt | 855 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -17.3) |
| [[Hs 766T (line)]] | wt | 409 | 2 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 1.58× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -19.1) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 395 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -17.4) |
| [[RKO (line)]] | wt | 502 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -20.2) |
| [[H4 (line)]] | wt | 347 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -13.4) |
| [[HCT15 (line)]] | alt | 450 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -28.0) |
| [[HEC-1-A (line)]] | alt | 250 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.399× (z -11.8) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 427 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -12.1) |
| [[KATO III (line)]] | alt | 460 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.324× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.533× (z -12.5) |
| [[LS 180 (line)]] | wt | 418 | 1 | 5 (4 ⚠) | [[Digitoxin (drug)]] 0.5 µM 2.26× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.353× (z -11.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.567× (z -8.9) |
| [[SK-MEL-2 (line)]] | alt | 182 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.384× (z -11.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 191 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.449× (z -13.9) |
| [[CHP-212 (line)]] | wt | 500 | 0 | 5 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -17.6) |
| [[HT-29 (line)]] | alt | 379 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.506× (z -12.1) |
| [[SW48 (line)]] | wt | 266 | 0 | 5 | — | [[Harringtonine (drug)]] 0.5 µM 0.252× (z -15.0) |
| [[BT-474 (line)]] | alt | 221 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.413× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 299 | 2 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +10.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.592× (z -8.7) |
| [[HOP62 (line)]] | alt | 224 | 1 (1 ⚠) | 2 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.11× (z +12.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.417× (z -9.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H1573 (line)]] | alt | 403 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.292× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.445× (z -11.2) |
| [[SHP-77 (line)]] | alt | 227 | 1 (1 ⚠) | 2 | [[Daptomycin (drug)]] 5 µM 2.59× (z +9.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -20.0) |
| [[SW 900 (line)]] | alt | 307 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -12.4) |
| [[C32 (line)]] | wt | 198 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.302× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[COLO 205 (line)]] | alt | 278 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 4.04× (z +12.3) | — |
| [[AN3 CA (line)]] | alt | 379 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -8.8) |
| [[C-33 A (line)]] | alt | 206 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.438× (z -12.0) |
| [[J82 (line)]] | alt | 265 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -8.5) |
| [[NCI-H596 (line)]] | alt | 419 | 0 | 1 | — | [[Trametinib (drug)]] 5 µM 0.0441× (z -13.9) |
| [[SW 1271 (line)]] | alt | 549 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 330 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 492 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 329 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 428 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 243 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5540), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGK1]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[ZNF281]] | +0.53 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[ZSWIM6]] | +0.52 | +0.37 / +0.53 | both halves | 8e-05 |  |
| [[ERRFI1]] | +0.50 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[MIDN]] | +0.50 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[IRS2]] | +0.50 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[AREG]] | +0.48 | +0.45 / +0.39 | both halves | 5e-05 |  |
| [[MYL12A]] | +0.48 | +0.46 / +0.47 | both halves | 3e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[LINC-PINT]] | +0.48 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DKK1]] | +0.47 | +0.44 / +0.43 | both halves | 3e-05 |  |
| [[SLC16A3]] | +0.47 | +0.43 / +0.48 | both halves | 3e-05 | pathway: SLC-mediated transmembrane transport; STRING 433 |
| [[TBC1D8]] | +0.46 | +0.50 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA5]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[ATPAF1]] | -0.49 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[MIR34AHG]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[NPEPPSP1]] | -0.43 | -0.25 / -0.46 | both halves | 4e-04 |  |
| [[OTUD3]] | -0.42 | -0.31 / -0.51 | both halves | 2e-04 |  |
| [[CDC23]] | -0.42 | -0.43 / -0.36 | both halves | 9e-05 |  |
| [[C12orf4]] | -0.42 | -0.37 / -0.49 | both halves | 8e-05 |  |
| [[RWDD4]] | -0.42 | -0.38 / -0.36 | both halves | 9e-05 |  |
| [[SCP2]] | -0.41 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[UCHL5]] | -0.41 | -0.30 / -0.40 | both halves | 2e-04 |  |
| [[FAM204A]] | -0.41 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TRUB1]] | -0.40 | -0.39 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DUSP4]] | B | DUSP4 activity lowers SLC38A2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without DUSP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[TRIB1]] | B | TRIB1 activity lowers SLC38A2's level | lines that do not express TRIB1 (6) vs lines expressing it (44) | 1.45× higher at baseline in the lines without TRIB1 | 0.031 | ⚠ within organs, on part of the lines; also absent: TGFBR2, VDR, PLSCR2; maybe low, not absent |
| [[TBC1D8]] | B | TBC1D8 activity lowers SLC38A2's level | lines that do not express TBC1D8 (6) vs lines expressing it (44) | 1.57× higher at baseline in the lines without TBC1D8 | 0.032 | ⚠ within organs, on part of the lines; also absent: SSUH2, ARHGAP26, ENSG00000251537; maybe low, not absent |
| [[EFNB2]] | B | EFNB2 activity lowers SLC38A2's level | lines that do not express EFNB2 (15) vs lines expressing it (35) | 1.35× higher at baseline in the lines without EFNB2 | 0.084 | ⚠ within organs, on part of the lines; also absent: FUT2, SATB1, C6orf141 |
| [[RASD1]] | B | RASD1 activity lowers SLC38A2's level | lines that do not express RASD1 (21) vs lines expressing it (29) | 1.14× higher at baseline in the lines without RASD1 | 0.094 | ⚠ within organs, on part of the lines; also absent: MTSS1, TREM1, APOE |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.482). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (34.0, 8.8); signed map (10.4, 26.1). **Vector** length 142, 53.8% of its response variance represented; |z| ≥ 3 in 2,182 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.0 | +3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +8.0 | +3.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | +8.0 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +7.8 | +5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | -2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.5 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +4.3 | +3.7 |
| fall | [[venetoclax (drug)]] 5 µM |  | -7.6 | -8.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.9 | -16.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -6.6 | -6.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.3 | -10.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.1 | -14.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -7.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.2 | -7.2 |
|  | [[EX229 (drug)]] 5 µM |  | -5.2 | -7.5 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 38 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:46,358,188-46,372,773 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SAT2, ATA2, KIAA1382, SNAT2 |
| Gene groups (HGNC) | Solute carrier family 38 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 8 pathways, smallest: Glutamate Neurotransmitter Release Cycle; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96QD8](https://www.uniprot.org/uniprotkb/Q96QD8) (Sodium-coupled neutral amino acid symporter 2):

> Symporter that cotransports neutral amino acids and sodium ions from the extracellular to the intracellular side of the cell membrane. The transport is pH-sensitive, Li(+)-intolerant, electrogenic, driven by the Na(+) electrochemical gradient and cotransports of neutral amino acids and sodium ions with a stoichiometry of 1:1. May function in the transport of amino acids at the blood-brain barrier. May function in the transport of amino acids in the supply of maternal nutrients to the fetus …

**Summary**, from NCBI Gene [54407](https://www.ncbi.nlm.nih.gov/gene/54407):

> Enables neutral L-amino acid:sodium symporter activity. Involved in several processes, including cellular response to arsenite(3-); neutral amino acid transport; and positive regulation of RNA splicing. Located in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13448) · Entrez [54407](https://www.ncbi.nlm.nih.gov/gene/54407) · UniProt [Q96QD8](https://www.uniprot.org/uniprotkb/Q96QD8) · Ensembl [ENSG00000134294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134294)

## Data

Gene col 5540: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5540); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5540, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5540]; `tensor/DDL_lfc|DDL_z.npy` [5540]; `embed/gene_vectors.npy` [5540]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5540 or target_col == 5540). Every well: [[SLC38A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
