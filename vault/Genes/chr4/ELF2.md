---
symbol: "ELF2"
type: "gene"
col: 3047
ensembl_id: "ENSG00000109381"
name: "E74 like ETS transcription factor 2"
location: "4q31.1"
module: 69
arm: "+"
pooled_cpm: 247.85
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 31
n_dd_up_clean: 6
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# ELF2

*E74 like ETS transcription factor 2* — 4q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.29× (z +5.5, q 2e-05, up in 35 of 49 measured lines) ⚠ cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Osimertinib (mesylate) (drug)]] 5 µM: 1.22× (z +4.3, q 0.003, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.358× (z -21.4, q 0e+00, down in 44 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.521× (z -14.1, q 6e-43, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIK3CA]] (+0.75, fdr 7e-06), [[FBXL20]] (+0.74, fdr 7e-06), [[KLHL24]] (+0.73, fdr 7e-06); moves opposite to [[PNO1]] (-0.65, fdr 7e-06), [[NCBP2]] (-0.64, fdr 7e-06), [[ZNF202]] (-0.63, fdr 7e-06).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3047.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.29×** | +5.5 | 2e-05 | 35/49 (SNU-1, LS 180, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.22×** | +4.3 | 0.003 | 25/48 (C-33 A, SNU-1, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.23×** | +4.3 | 0.003 | 27/50 (NCI-H23, LoVo, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.45×** | +4.2 | 0.004 | 29/50 (Hs 766T, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.007 | 22/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.19× | +3.8 | 0.014 | 22/48 (NCI-H460, KATO III, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.39×** | +3.8 | 0.014 | 22/49 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | 1.14× | +3.3 | 0.061 | 11/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.16× | +3.3 | 0.064 | 13/48 (HOP62, AsPC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.066 | 14/49 (NCI-H460, NCI-H23, …) | all doses, flat |  |
| [[RMC-6236 (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.074 | 21/48 (AsPC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.16× | +3.2 | 0.074 | 17/47 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | 1.16× | +3.1 | 0.074 | 11/49 (LoVo, AN3 CA, …) | inconsistent across doses |  |
| [[BI-3406 (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.098 | 21/48 (AsPC-1, NCI-H23, …) | rises with dose | noisy plate (z scaled) |
| [[ULK-101 (drug)]] 0.05 µM |  | 1.16× | +3.0 | 0.098 | 17/49 (Hs 766T, RPMI-7951, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3047.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.358×** | -21.4 | 0e+00 | 44/44 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.385×** | -20.7 | 0e+00 | 47/49 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.499×** | -15.0 | 0e+00 | 48/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.521×** | -14.1 | 6e-43 | 42/48 (NCI-H1792, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.506×** | -13.6 | 3e-40 | 43/45 (NCI-H2347, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.603×** | -10.9 | 1e-25 | 38/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.610×** | -10.7 | 1e-24 | 43/48 (HT-29, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.708×** | -10.5 | 5e-24 | 28/48 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.618×** | -10.4 | 2e-23 | 38/48 (AsPC-1, HT-29, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.422×** | -9.8 | 9e-21 | 48/48 (NCI-H1792, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.644×** | -9.1 | 4e-18 | 46/47 (CFPAC-1, NCI-H2347, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.467×** | -8.6 | 4e-16 | 46/48 (NCI-H1792, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.476×** | -8.4 | 2e-15 | 42/48 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.491×** | -8.0 | 4e-14 | 47/48 (NCI-H1792, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.701×** | -7.7 | 7e-13 | 29/48 (HT-29, HepG2/C3A, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -6.9 | 2e-10 | 27/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.745×** | -6.3 | 8e-09 | 37/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.577×** | -6.2 | 2e-08 | 41/47 (HEC-1-A, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.616×** | -5.5 | 1e-06 | 37/48 (CFPAC-1, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.774×** | -5.3 | 3e-06 | 30/48 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.858× | -4.7 | 8e-05 | 18/48 (A549, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.756×** | -4.0 | 0.001 | 32/49 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.826×** | -3.9 | 0.002 | 23/48 (LoVo, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.884× | -3.7 | 0.004 | 16/49 (C32, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3047. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 325 | 0 | 15 (11 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -21.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.240× (z -21.1) |
| [[HT-29 (line)]] | alt | 408 | 0 | 14 (11 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.305× (z -17.6) |
| [[NCI-H2347 (line)]] | alt | 425 | 0 | 14 (10 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -25.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Belumosudil (drug)]] 5 µM 0.521× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 374 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.290× (z -16.7) |
| [[NCI-H460 (line)]] | wt | 189 | 8 (6 ⚠) | 4 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.63× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.414× (z -14.1) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.530× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 280 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.298× (z -17.1) |
| [[PANC-1 (line)]] | alt | 255 | 3 (2 ⚠) | 6 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.316× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.534× (z -10.7) |
| [[SHP-77 (line)]] | alt | 245 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.549× (z -9.3) |
| [[SW480 (line)]] | alt | 176 | 0 | 9 (7 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.455× (z -12.9) |
| [[A549 (line)]] | wt | 229 | 0 | 8 (8 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HepG2_C3A (line)]] | wt | 333 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.230× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.469× (z -9.6) |
| [[KATO III (line)]] | alt | 235 | 2 (1 ⚠) | 6 (6 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +15.4) | [[Dinaciclib (drug)]] 0.5 µM 0.379× (z -15.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[C32 (line)]] | wt | 291 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.328× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 288 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -18.3) |
| [[HOP62 (line)]] | alt | 266 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.271× (z -17.3) |
| [[Hs 766T (line)]] | wt | 293 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.238× (z -19.9) |
| [[Panc 03.27 (line)]] | alt | 304 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.412× (z -10.2) |
| [[SNU-423 (line)]] | alt | 252 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.239× (z -17.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.296× (z -15.2) |
| [[SW 900 (line)]] | alt | 305 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.335× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.378× (z -12.3) |
| [[BT-474 (line)]] | alt | 247 | 0 | 5 (4 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.160× (z -13.3) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.478× (z -10.2) |
| [[COLO 205 (line)]] | alt | 257 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.327× (z -13.6) |
| [[SK-MEL-2 (line)]] | alt | 317 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.383× (z -12.9) |
| [[A-172 (line)]] | wt | 181 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.286× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.408× (z -11.7) |
| [[AN3 CA (line)]] | alt | 345 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -12.2) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -11.3) |
| [[HCT15 (line)]] | alt | 270 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.557× (z -10.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.511× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 215 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.434× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[hTERT-HPNE (line)]] | wt | 272 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.373× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 148 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.471× (z -12.7) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.465× (z -9.1) |
| [[SW1417 (line)]] | alt | 206 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-427 (line)]] | wt | 258 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.337× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A498 (line)]] | wt | 244 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.303× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[HS-578T (line)]] | alt | 249 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.385× (z -9.9) |
| [[J82 (line)]] | alt | 187 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[LoVo (line)]] | wt | 219 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.471× (z -10.8) |
| [[LS 180 (line)]] | wt | 194 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.44× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.505× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 204 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.282× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[NCI-H661 (line)]] | alt | 420 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.188× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SW48 (line)]] | wt | 189 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[C-33 A (line)]] | alt | 323 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[LOX-IMVI (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.430× (z -10.1) |
| [[MIA PaCa-2 (line)]] | alt | 153 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 2.09× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.377× (z -13.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 162 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.291× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[RPMI-7951 (line)]] | alt | 218 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.319× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 268 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0512× (z -32.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[H4 (line)]] | wt | 283 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 313 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 207 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 289 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3047), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIK3CA]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[FBXL20]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 |  |
| [[KLHL24]] | +0.73 | +0.61 / +0.71 | both halves | 7e-06 |  |
| [[PIAS1]] | +0.69 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[TBC1D12]] | +0.69 | +0.72 / +0.65 | both halves | 7e-06 |  |
| [[TMEM59]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[TXNDC16]] | +0.67 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[PCMTD1]] | +0.67 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[CNNM2]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[RCOR3]] | +0.66 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[YPEL2]] | +0.66 | +0.66 / +0.72 | both halves | 7e-06 |  |
| [[PPM1B]] | +0.65 | +0.69 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNO1]] | -0.65 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[NCBP2]] | -0.64 | -0.63 / -0.59 | both halves | 7e-06 |  |
| [[ZNF202]] | -0.63 | -0.58 / -0.63 | both halves | 7e-06 |  |
| [[MAK16]] | -0.62 | -0.65 / -0.60 | both halves | 7e-06 |  |
| [[ZNF121]] | -0.62 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[GTPBP4]] | -0.62 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[ABCE1]] | -0.61 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[EIF4G1]] | -0.61 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[TMEM185B]] | -0.61 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[MGA]] | -0.60 | -0.68 / -0.54 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.60 | -0.53 / -0.63 | both halves | 1e-05 |  |
| [[ZKSCAN2]] | -0.60 | -0.65 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.4, -41.5); signed map (-15.5, 11.4). **Vector** length 142, 55.4% of its response variance represented; |z| ≥ 3 in 1,755 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +7.1 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.3 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +6.1 | +2.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | -0.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +4.7 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.2 | +1.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +2.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +1.2 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -16.4 | -15.0 |
|  | [[EX229 (drug)]] 5 µM |  | -9.9 | -8.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -9.6 | -8.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -9.4 | -9.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -9.2 | -14.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -9.0 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.2 | -10.7 |

## What is on record

|  |  |
|---|---|
| Name | E74 like ETS transcription factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q31.1 — chr4:139,028,112-139,177,218 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EU32, NERF, NERF-2, NERF-1A, NERF-1B |
| Gene groups (HGNC) | ETS transcription factor family |
| Reactome | 2 pathways, smallest: RUNX1 regulates transcription of genes involved in BCR signaling; Transcriptional regulation by RUNX1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15723](https://www.uniprot.org/uniprotkb/Q15723) (ETS-related transcription factor Elf-2):

> Isoform 1 transcriptionally activates the LYN and BLK promoters and acts synergistically with RUNX1 to transactivate the BLK promoter.; Isoform 2 may function in repression of RUNX1-mediated transactivation.

**Summary**, from NCBI Gene [1998](https://www.ncbi.nlm.nih.gov/gene/1998):

> Enables DNA-binding transcription factor activity, RNA polymerase II-specific and sequence-specific double-stranded DNA binding activity. Involved in negative regulation of DNA-templated transcription; positive regulation of DNA-templated transcription; and regulation of transcription by RNA polymerase II. Located in nuclear body. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:3317](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3317) · Entrez [1998](https://www.ncbi.nlm.nih.gov/gene/1998) · UniProt [Q15723](https://www.uniprot.org/uniprotkb/Q15723) · Ensembl [ENSG00000109381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109381)

## Data

Gene col 3047: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3047); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3047, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3047]; `tensor/DDL_lfc|DDL_z.npy` [3047]; `embed/gene_vectors.npy` [3047]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3047 or target_col == 3047). Every well: [[ELF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
