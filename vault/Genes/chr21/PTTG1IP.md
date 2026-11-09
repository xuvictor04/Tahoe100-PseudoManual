---
symbol: "PTTG1IP"
type: "gene"
col: 11385
ensembl_id: "ENSG00000183255"
name: "PTTG1 interacting protein"
location: "21q22.3"
module: 76
arm: "+"
pooled_cpm: 190.33
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# PTTG1IP

*PTTG1 interacting protein* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.48× (z +9.8, q 7e-20, up in 35 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 1.36× (z +7.7, q 3e-12, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.730× (z -7.8, q 3e-12, down in 35 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.644× (z -5.7, q 1e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSB]] (+0.55, fdr 1e-05), [[IDS]] (+0.54, fdr 1e-05), [[SUN1]] (+0.53, fdr 3e-05); moves opposite to [[ZNF254]] (-0.49, fdr 3e-05), [[GABPB1]] (-0.49, fdr 4e-04), [[MTHFS]] (-0.49, fdr 2e-04).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11385.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.48×** | +9.8 | 7e-20 | 35/49 (HEC-1-A, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +8.1 | 1e-13 | 30/44 (A498, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.36×** | +7.7 | 3e-12 | 26/48 (SW1417, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.29×** | +6.4 | 2e-08 | 27/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.26×** | +5.8 | 7e-07 | 29/48 (SW1417, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +5.7 | 1e-06 | 29/49 (NCI-H2030, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.27×** | +5.6 | 2e-06 | 23/45 (SW1417, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | 1.19× | +4.3 | 0.001 | 21/48 (SHP-77, A-427, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.001 | 27/49 (HS-578T, NCI-H460, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.7 | 0.014 | 18/48 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Sinomenine (drug)]] 0.5 µM |  | 1.16× | +3.6 | 0.014 | 11/48 (LS 180, SW 900, …) | inconsistent across doses |  |
| [[Fumaric acid (drug)]] 5 µM |  | 1.16× | +3.5 | 0.018 | 14/49 (NCI-H2030, Hs 766T, …) | top dose only | plate-row cell shift; position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.027 | 15/48 (HT-29, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 1.14× | +3.2 | 0.052 | 13/49 (PANC-1, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | 1.19× | +3.1 | 0.071 | 14/48 (HOP62, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 1.13× | +3.1 | 0.071 | 10/48 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Relugolix (drug)]] 0.5 µM |  | 1.13× | +3.0 | 0.073 | 7/48 (NCI-H2347, SW 900, …) | inconsistent across doses | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.26×** | +3.0 | 0.073 | 16/48 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.073 | 12/47 (A-427, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11385.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.730×** | -7.8 | 3e-12 | 35/48 (AsPC-1, SW480, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.733×** | -7.4 | 3e-11 | 32/47 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.827×** | -6.7 | 4e-09 | 26/48 (C32, NCI-H2347, …) | rises with dose | low cells (technical?) |
| [[TAK-733 (drug)]] 5 µM |  | **0.644×** | -5.7 | 1e-06 | 31/48 (SW480, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.796×** | -5.4 | 1e-05 | 26/48 (HepG2/C3A, C32, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.810×** | -5.3 | 1e-05 | 25/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.866× | -5.1 | 4e-05 | 22/48 (C-33 A, Hs 766T, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.693×** | -4.8 | 1e-04 | 27/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.829×** | -4.7 | 2e-04 | 23/48 (SNU-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.820×** | -4.7 | 2e-04 | 25/48 (LoVo, PANC-1, …) | inconsistent across doses | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.829×** | -4.7 | 2e-04 | 25/48 (SW 1088, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.714×** | -4.4 | 5e-04 | 25/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.842× | -4.3 | 8e-04 | 22/48 (HepG2/C3A, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.837× | -4.3 | 8e-04 | 24/48 (C-33 A, C32, …) | top dose only | composition shift |
| [[Verteporfin (drug)]] 5 µM |  | 0.843× | -4.1 | 0.002 | 19/49 (SK-MEL-2, A498, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.744×** | -3.9 | 0.004 | 24/48 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.815×** | -3.6 | 0.010 | 19/48 (SW480, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.818×** | -3.6 | 0.011 | 21/48 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.820×** | -3.5 | 0.013 | 17/49 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.769×** | -3.4 | 0.017 | 18/48 (SW480, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.872× | -3.4 | 0.017 | 14/48 (C32, BT-474, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 0.910× | -3.1 | 0.043 | 4/48 (C32, NCI-H1792, …) | inconsistent across doses |  |
| [[Everolimus (drug)]] 5 µM |  | 0.853× | -2.9 | 0.080 | 11/50 (MIA PaCa-2, SK-MEL-2, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11385. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 632 | 0 | 13 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -15.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.439× (z -10.1) |
| [[C-33 A (line)]] | alt | 248 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.338× (z -9.7) |
| [[HepG2_C3A (line)]] | wt | 765 | 0 | 8 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.311× (z -14.7) ⚠ toxic; cell-cycle shift, explains ~24% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.394× (z -12.2) |
| [[SW480 (line)]] | alt | 244 | 0 | 8 (6 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.444× (z -13.6) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.368× (z -8.7) |
| [[SW1417 (line)]] | alt | 108 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.14× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 257 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.473× (z -10.2) |
| [[A498 (line)]] | wt | 198 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +12.2) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.546× (z -9.5) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 368 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.582× (z -8.8) |
| [[A-427 (line)]] | wt | 88.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.17× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 1.95× (z +8.7) | [[Selinexor (drug)]] 5 µM 0.619× (z -8.8) ⚠ cell-cycle shift, explains ~35% of this change |
| [[HEC-1-A (line)]] | alt | 223 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.10× (z +12.4) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.557× (z -9.9) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 123 | 1 (1 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.11× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 216 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.22× (z +11.7) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.561× (z -8.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 221 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.00× (z +9.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 182 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.365× (z -15.0) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.327× (z -8.7) |
| [[HCT15 (line)]] | alt | 141 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.50× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 214 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.32× (z +11.5) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 88.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.19× (z +9.5) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 243 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.426× (z -11.6) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 189 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.507× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.427× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 199 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.77× (z +8.9) ⚠ toxic; transcription drop | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.538× (z -10.1) ⚠ unreliable plate only |
| [[Panc 03.27 (line)]] | alt | 190 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +11.9) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 213 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.143× (z -16.6) |
| [[AN3 CA (line)]] | alt | 192 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.213× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 79.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +10.9) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 134 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.458× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~24% of this change |
| [[LoVo (line)]] | wt | 93.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.17× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 172 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.79× (z +9.5) | — |
| [[RKO (line)]] | wt | 126 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +8.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[RPMI-7951 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.499× (z -8.5) |
| [[SHP-77 (line)]] | alt | 94.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.64× (z +11.0) | — |
| [[A549 (line)]] | wt | 97.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 411 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 189 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 152 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 215 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 143 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 173 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 158 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 94.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 174 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 250 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 94.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11385), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSB]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[IDS]] | +0.54 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SUN1]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[IGF1R]] | +0.52 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[RETREG2]] | +0.52 | +0.55 / +0.39 | both halves | 5e-05 |  |
| [[SPTBN1]] | +0.52 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[FKBP8]] | +0.51 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[SLC25A23]] | +0.51 | +0.46 / +0.39 | both halves | 5e-05 |  |
| [[CNN2]] | +0.51 | +0.41 / +0.45 | both halves | 4e-05 |  |
| [[PJA2]] | +0.51 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[HMG20B]] | +0.51 | +0.38 / +0.44 | both halves | 7e-05 |  |
| [[USP9X]] | +0.50 | +0.47 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF254]] | -0.49 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[GABPB1]] | -0.49 | -0.49 / -0.24 | both halves | 4e-04 |  |
| [[MTHFS]] | -0.49 | -0.30 / -0.46 | both halves | 2e-04 |  |
| [[ZC3HC1]] | -0.49 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[MRM1]] | -0.49 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[NOP56]] | -0.48 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[TOE1]] | -0.47 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[COA6]] | -0.47 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[PTPN9]] | -0.47 | -0.32 / -0.34 | both halves | 2e-04 |  |
| [[NSUN4]] | -0.46 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[SHLD1]] | -0.46 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[ANKAR]] | -0.46 | -0.38 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers PTTG1IP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.449). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -44.0); signed map (-28.1, 25.8). **Vector** length 138, 41.5% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.6 | +5.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +7.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.9 | +6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.7 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +4.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.8 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | -9.0 | -7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.4 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -7.8 | -6.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -6.8 | -5.3 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.9 | -4.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.5 | -5.7 |
|  | [[EX229 (drug)]] 5 µM |  | -5.4 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.3 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | PTTG1 interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:44,849,585-44,873,903 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PBF, PTTG1IP1; previously C21orf3, C21orf1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P53801](https://www.uniprot.org/uniprotkb/P53801) (Pituitary tumor-transforming gene 1 protein-interacting protein):

> May facilitate PTTG1 nuclear translocation.

**Summary**, from NCBI Gene [754](https://www.ncbi.nlm.nih.gov/gene/754):

> This gene encodes a single-pass type I integral membrane protein, which binds to pituitary tumor-transforming 1 protein (PTTG1), and facilitates translocation of PTTG1 into the nucleus. Coexpression of this protein and PTTG1 induces transcriptional activation of basic fibroblast growth factor. Alternatively spliced transcript variants have been found for this gene. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:13524](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13524) · Entrez [754](https://www.ncbi.nlm.nih.gov/gene/754) · UniProt [P53801](https://www.uniprot.org/uniprotkb/P53801) · Ensembl [ENSG00000183255](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183255)

## Data

Gene col 11385: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11385); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11385, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11385]; `tensor/DDL_lfc|DDL_z.npy` [11385]; `embed/gene_vectors.npy` [11385]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11385 or target_col == 11385). Every well: [[PTTG1IP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTTG1IP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
