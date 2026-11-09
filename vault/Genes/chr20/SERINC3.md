---
symbol: "SERINC3"
type: "gene"
col: 5378
ensembl_id: "ENSG00000132824"
name: "serine incorporator 3"
location: "20q13.12"
module: 69
arm: "+"
pooled_cpm: 191.43
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 21
n_dd_up_clean: 0
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# SERINC3

*serine incorporator 3* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.49× (z +10.5, q 6e-23, up in 39 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 2.44×, HS-578T 2.12×, NCI-H2030 1.95×, HOP62 1.95×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 2.68×, BT-474 2.04×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.00×, BT-474 2.14×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.429× (z -21.9, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[venetoclax (drug)]] 5 µM: 0.411× (z -12.0, q 6e-31, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERINC1]] (+0.68, fdr 1e-05), [[CCDC28A]] (+0.61, fdr 2e-05), [[CRIPT]] (+0.60, fdr 1e-05); moves opposite to [[EIF4E]] (-0.57, fdr 2e-05), [[SNHG15]] (-0.55, fdr 5e-05), [[ZNRF3]] (-0.55, fdr 2e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5378.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 8 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 5 lines (HEC-1-A 2.44×, HS-578T 2.12×, NCI-H2030 1.95×, HOP62 1.95×, …; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (NCI-H1573 2.68×, BT-474 2.04×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H1573 2.00×, BT-474 2.14×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.49×** | +10.5 | 6e-23 | 39/49 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +7.9 | 9e-13 | 31/44 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.24×** | +5.2 | 4e-05 | 24/45 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | 1.14× | +3.4 | 0.094 | 10/48 (KATO III, A-172, …) | two highest doses |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.094 | 18/48 (LS 180, LoVo, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | 1.13× | +3.1 | 0.14 | 13/48 (PANC-1, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.14 | 11/47 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 16 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5378.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.429×** | -21.9 | 0e+00 | 48/48 (HT-29, MIA PaCa-2, …) | all doses, flat |  |
| [[venetoclax (drug)]] 5 µM |  | **0.411×** | -12.0 | 6e-31 | 44/48 (HT-29, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.435×** | -11.3 | 3e-27 | 44/48 (MIA PaCa-2, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.463×** | -10.4 | 3e-23 | 44/48 (SK-MEL-2, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.471×** | -10.2 | 3e-22 | 43/48 (SW1417, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.474×** | -10.1 | 5e-22 | 43/48 (MIA PaCa-2, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.711×** | -8.8 | 1e-16 | 38/48 (NCI-H1792, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.649×** | -8.0 | 1e-13 | 41/48 (Hs 766T, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.730×** | -7.8 | 3e-13 | 38/47 (RKO, SW480, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.577×** | -7.4 | 6e-12 | 37/49 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.753×** | -7.0 | 1e-10 | 36/49 (NCI-H2030, BT-474, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.843× | -6.2 | 3e-08 | 21/49 (SNU-1, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.844× | -6.1 | 3e-08 | 24/48 (CFPAC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 0.5 µM |  | **0.721×** | -6.0 | 8e-08 | 35/49 (SW1417, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.724×** | -5.9 | 1e-07 | 39/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.804×** | -5.3 | 4e-06 | 28/48 (Hs 766T, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.874× | -4.8 | 4e-05 | 13/48 (A-427, LoVo, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.738×** | -4.1 | 0.001 | 27/48 (SW480, SW 900, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.863× | -3.8 | 0.004 | 18/48 (SW 1271, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5378. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 199 | 4 (4 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.68× (z +16.2) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.500× (z -11.3) ⚠ cell-cycle shift, explains ~80% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.582× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 220 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -16.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.584× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 151 | 0 | 7 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -20.4) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.148× (z -14.2) |
| [[HEC-1-A (line)]] | alt | 90.2 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +12.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -16.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.306× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 270 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.407× (z -13.2) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.306× (z -9.1) |
| [[SW1417 (line)]] | alt | 253 | 0 | 5 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.387× (z -17.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.339× (z -10.6) |
| [[SW480 (line)]] | alt | 211 | 0 | 5 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.421× (z -16.3) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.389× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 228 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.281× (z -17.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.188× (z -11.9) |
| [[Hs 766T (line)]] | wt | 393 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.321× (z -18.6) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.328× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 138 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.277× (z -18.2) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.272× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 179 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.364× (z -15.4) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.303× (z -9.5) |
| [[SW 900 (line)]] | alt | 179 | 0 | 4 (3 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -11.3) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.298× (z -8.5) |
| [[A498 (line)]] | wt | 213 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.77× (z +10.0) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.523× (z -11.2) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 179 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.07× (z +10.7) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.461× (z -11.4) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.309× (z -9.0) |
| [[BT-474 (line)]] | alt | 398 | 3 (3 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 2.14× (z +10.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[HOP62 (line)]] | alt | 165 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.95× (z +10.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.466× (z -12.4) ⚠ unreliable plate only |
| [[HS-578T (line)]] | alt | 230 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.12× (z +11.5) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.491× (z -10.7) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 205 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -16.9) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.295× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 196 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.346× (z -16.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.295× (z -9.7) |
| [[NCI-H1792 (line)]] | alt | 206 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.386× (z -13.5) ⚠ unreliable plate only · without an alert: [[Belinostat (drug)]] 0.5 µM 0.512× (z -9.5) |
| [[NCI-H2030 (line)]] | alt | 254 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.01× (z +11.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 148 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.428× (z -12.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.305× (z -9.4) |
| [[SHP-77 (line)]] | alt | 89.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.53× (z +10.0) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.464× (z -8.6) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 158 | 0 | 3 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -12.0) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.215× (z -8.8) |
| [[A-172 (line)]] | wt | 198 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[C-33 A (line)]] | alt | 101 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.55× (z +9.3) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.395× (z -10.0) ⚠ unreliable plate only |
| [[H4 (line)]] | wt | 160 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.379× (z -10.9) ⚠ unreliable plate only · without an alert: [[Belinostat (drug)]] 0.5 µM 0.436× (z -9.4) |
| [[HT-29 (line)]] | alt | 190 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.280× (z -22.0) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.311× (z -10.6) |
| [[hTERT-HPNE (line)]] | wt | 264 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -9.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 242 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -17.2) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.311× (z -9.1) |
| [[NCI-H23 (line)]] | alt | 263 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -15.8) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.293× (z -9.8) |
| [[PANC-1 (line)]] | alt | 173 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.581× (z -10.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.410× (z -8.8) |
| [[RKO (line)]] | wt | 163 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.237× (z -17.2) ⚠ unreliable plate only |
| [[SNU-423 (line)]] | alt | 305 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.489× (z -9.5) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 161 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.562× (z -8.6) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 182 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +9.3) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 201 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.446× (z -11.3) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 158 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -9.3) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 232 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.487× (z -9.4) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 89.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.360× (z -14.6) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 139 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.504× (z -9.5) ⚠ unreliable plate only |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.431× (z -14.4) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 81.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.323× (z -10.1) ⚠ unreliable plate only |
| [[AN3 CA (line)]] | alt | 80.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 171 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 268 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 216 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5378), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 6 of them with an alert (⚠; 6 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERINC1]] | +0.68 | +0.56 / +0.77 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[CCDC28A]] | +0.61 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[CRIPT]] | +0.60 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[BROX]] | +0.59 | +0.38 / +0.73 | both halves | 6e-05 |  |
| [[PAIP2]] | +0.58 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[CALCOCO1]] | +0.56 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SLU7]] | +0.56 | +0.33 / +0.64 | both halves | 1e-04 |  |
| [[PDCD4]] | +0.55 | +0.27 / +0.65 | both halves | 3e-04 |  |
| [[RB1CC1]] | +0.54 | +0.32 / +0.65 | both halves | 2e-04 |  |
| [[TBC1D15]] | +0.53 | +0.27 / +0.70 | both halves | 3e-04 |  |
| [[YPEL5]] | +0.53 | +0.38 / +0.72 | both halves | 6e-05 |  |
| [[CEP44]] | +0.53 | +0.35 / +0.61 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF4E]] | -0.57 | -0.46 / -0.53 | both halves | 2e-05 |  |
| [[SNHG15]] | -0.55 | -0.39 / -0.65 | both halves | 5e-05 |  |
| [[ZNRF3]] | -0.55 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[UCK2]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[NOP2]] | -0.49 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[GPR63]] | -0.48 | -0.36 / -0.55 | both halves | 9e-05 |  |
| [[PA2G4]] | -0.48 | -0.39 / -0.47 | both halves | 5e-05 |  |
| [[SNHG17]] | -0.47 | -0.34 / -0.56 | both halves | 1e-04 |  |
| [[WDR43]] | -0.47 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[PPARGC1B]] | -0.47 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[SCLY]] | -0.47 | -0.42 / -0.54 | both halves | 4e-05 | pathway: Metabolism of amino acids and derivatives |
| [[TBC1D30]] | -0.47 | -0.48 / -0.49 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.519). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (2.9, -45.8); signed map (-16.1, 9.9). **Vector** length 142, 46.8% of its response variance represented; |z| ≥ 3 in 1,405 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | -2.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +10.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.0 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +7.9 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.4 | -3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.6 | +3.3 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +3.5 | +2.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.3 | +2.2 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +3.3 | +2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.2 | +3.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -17.3 | -21.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -11.8 | -12.0 |
|  | [[EX229 (drug)]] 5 µM |  | -11.3 | -10.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -11.0 | -11.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -10.6 | -10.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -8.7 | -10.1 |

## What is on record

|  |  |
|---|---|
| Name | serine incorporator 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:44,496,221-44,522,085 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DIFF33, TDE, SBBI99, TMS-1, AIGP1; previously TDE1 |
| Reactome | 2 pathways, smallest: Serine metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13530](https://www.uniprot.org/uniprotkb/Q13530) (Serine incorporator 3):

> Restriction factor required to restrict infectivity of lentiviruses, such as HIV-1: acts by inhibiting an early step of viral infection. Impairs the penetration of the viral particle into the cytoplasm. Non-ATP-dependent, non-specific lipid transporter for phosphatidylserine, phosphatidylcholine, and phosphatidylethanolamine. Functions as a scramblase that flips lipids in both directions across the membrane. Phospholipid scrambling results in HIV-1 surface exposure of phosphatidylserine and …

**Summary**, from NCBI Gene [10955](https://www.ncbi.nlm.nih.gov/gene/10955):

> Enables phospholipid scramblase activity. Involved in antiviral innate immune response and plasma membrane phospholipid scrambling. Located in plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:11699](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11699) · Entrez [10955](https://www.ncbi.nlm.nih.gov/gene/10955) · UniProt [Q13530](https://www.uniprot.org/uniprotkb/Q13530) · Ensembl [ENSG00000132824](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132824)

## Data

Gene col 5378: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5378); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5378, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5378]; `tensor/DDL_lfc|DDL_z.npy` [5378]; `embed/gene_vectors.npy` [5378]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5378 or target_col == 5378). Every well: [[SERINC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERINC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
