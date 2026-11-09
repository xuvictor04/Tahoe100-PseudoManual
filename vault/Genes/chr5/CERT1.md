---
symbol: "CERT1"
type: "gene"
col: 3436
ensembl_id: "ENSG00000113163"
name: "ceramide transporter 1"
location: "5q13.3"
module: 69
arm: "+"
pooled_cpm: 216.01
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CERT1

*ceramide transporter 1* — 5q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.26× (z +20.0, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.489× (z -16.8, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.677× (z -5.0, q 6e-05, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[OGA]] (+0.72, fdr 7e-06), [[ZNF654]] (+0.70, fdr 7e-06), [[AAMDC]] (+0.70, fdr 7e-06); moves opposite to [[MIER2]] (-0.68, fdr 3e-05), [[NAA15]] (-0.67, fdr 7e-06), [[GCN1]] (-0.67, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → cells under [[Posaconazole (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3436.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.26×** | +20.0 | 0e+00 | 48/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +14.2 | 2e-43 | 42/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.55×** | +11.9 | 1e-30 | 47/49 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.63×** | +11.9 | 1e-30 | 37/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.61×** | +11.6 | 6e-29 | 37/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +11.0 | 4e-26 | 32/48 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +6.5 | 6e-09 | 32/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.29×** | +6.0 | 1e-07 | 27/50 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.49×** | +5.1 | 2e-05 | 31/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.1 | 2e-05 | 25/48 (RKO, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +5.0 | 3e-05 | 22/49 (AsPC-1, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~2% of this change | 1.20× | +4.4 | 6e-04 | 24/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.19× | +4.3 | 7e-04 | 22/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~1% of this change | 1.18× | +4.1 | 0.002 | 19/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.9 | 0.004 | 20/48 (HS-578T, A498, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.10× | +3.2 | 0.043 | 7/49 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.27×** | +3.1 | 0.064 | 14/48 (CFPAC-1, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 13 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3436.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.489×** | -16.8 | 0e+00 | 42/44 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.509×** | -16.5 | 0e+00 | 45/49 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.695×** | -8.2 | 4e-14 | 32/45 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.776×** | -6.2 | 8e-08 | 26/48 (SNU-423, CFPAC-1, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.792×** | -5.7 | 1e-06 | 28/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.677×** | -5.0 | 6e-05 | 31/48 (PANC-1, NCI-H23, …) | top dose only | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.948× | -4.7 | 2e-04 | 0/50 | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -4.7 | 2e-04 | 29/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.880× | -4.4 | 6e-04 | 17/48 (NCI-H2347, C32, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.882× | -4.3 | 8e-04 | 6/48 (SNU-423, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.843× | -4.2 | 0.002 | 22/48 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.847× | -4.1 | 0.002 | 22/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.849× | -4.0 | 0.003 | 21/48 (PANC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.855× | -3.8 | 0.005 | 20/48 (HOP62, AsPC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.741×** | -3.8 | 0.005 | 25/48 (PANC-1, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.750×** | -3.7 | 0.008 | 28/48 (MIA PaCa-2, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Carbamazepine (drug)]] 5 µM |  | 0.868× | -3.5 | 0.017 | 9/47 (NCI-H460, J82, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 0.869× | -3.4 | 0.017 | 9/48 (A498, AsPC-1, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.875× | -3.3 | 0.030 | 4/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.778×** | -3.2 | 0.033 | 17/48 (PANC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | 0.882× | -3.1 | 0.050 | 5/49 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.883× | -3.1 | 0.050 | 9/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.057 | 9/48 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.891× | -2.8 | 0.098 | 8/48 (NCI-H460, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3436. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 186 | 13 (6 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.76× (z +25.2) | [[Dinaciclib (drug)]] 5 µM 0.218× (z -23.6) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 192 | 7 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +18.4) | [[Dinaciclib (drug)]] 0.5 µM 0.600× (z -8.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 211 | 6 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.45× (z +16.9) | [[Dinaciclib (drug)]] 0.5 µM 0.508× (z -12.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 317 | 5 (2 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.477× (z -10.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 203 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.04× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.347× (z -12.0) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 185 | 6 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -19.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 160 | 5 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.97× (z +21.8) | [[Dinaciclib (drug)]] 0.5 µM 0.600× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 274 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.306× (z -15.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 176 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.561× (z -8.6) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 198 | 4 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.433× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 170 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.09× (z +17.2) | — |
| [[NCI-H1792 (line)]] | alt | 241 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.16× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.323× (z -15.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 469 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +12.6) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -16.6) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 234 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.460× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 323 | 1 | 5 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.91× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.373× (z -14.0) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 228 | 5 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.12× (z +15.2) | [[Dinaciclib (drug)]] 0.5 µM 0.448× (z -10.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 156 | 5 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.26× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 208 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +14.5) | [[Dinaciclib (drug)]] 0.5 µM 0.415× (z -14.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 274 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.04× (z +13.7) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -14.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 223 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -15.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 225 | 2 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.52× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.435× (z -10.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 187 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -9.9) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 246 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.52× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 275 | 1 | 3 (3 ⚠) | [[AZD-7648 (drug)]] 5 µM 3.33× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.459× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 333 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.193× (z -23.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 238 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.42× (z +13.5) | [[Dinaciclib (drug)]] 0.5 µM 0.364× (z -15.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 175 | 3 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.80× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.241× (z -15.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 231 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.301× (z -16.4) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 258 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +10.9) | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -13.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 221 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.16× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 174 | 2 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 203 | 1 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.420× (z -12.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 154 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.54× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 167 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.31× (z +11.6) | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -13.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 133 | 2 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +14.8) | [[Dinaciclib (drug)]] 0.05 µM 0.533× (z -8.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 260 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -15.8) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.518× (z -10.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 169 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.74× (z +12.5) | — |
| [[SK-MEL-2 (line)]] | alt | 163 | 2 | 0 | [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +8.9) | — |
| [[A-427 (line)]] | wt | 160 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.629× (z -9.9) |
| [[AN3 CA (line)]] | alt | 263 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.309× (z -10.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 113 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.98× (z +8.7) | — |
| [[C-33 A (line)]] | alt | 144 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 192 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 214 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 222 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 157 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3436), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OGA]] | +0.72 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[ZNF654]] | +0.70 | +0.78 / +0.60 | both halves | 7e-06 |  |
| [[AAMDC]] | +0.70 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[CDK19]] | +0.69 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PIK3CA]] | +0.68 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[UBXN7]] | +0.68 | +0.59 / +0.70 | both halves | 7e-06 |  |
| [[CCNG2]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[MICU1]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[CREBRF]] | +0.67 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.66 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ATOSA]] | +0.66 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[NPC2]] | +0.64 | +0.57 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIER2]] | -0.68 | -0.46 / -0.65 | both halves | 3e-05 |  |
| [[NAA15]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[GCN1]] | -0.67 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[DCAF1]] | -0.65 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[CLPB]] | -0.65 | -0.51 / -0.68 | both halves | 1e-05 |  |
| [[E2F4]] | -0.63 | -0.60 / -0.58 | both halves | 7e-06 |  |
| [[TXLNA]] | -0.63 | -0.53 / -0.64 | both halves | 1e-05 |  |
| [[WDR4]] | -0.63 | -0.64 / -0.63 | both halves | 7e-06 |  |
| [[CTPS1]] | -0.62 | -0.62 / -0.62 | both halves | 7e-06 |  |
| [[MYBBP1A]] | -0.61 | -0.54 / -0.55 | both halves | 1e-05 |  |
| [[PUS1]] | -0.61 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[PGAM5]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Posaconazole (drug)]] 5 µM | C | CERT1's natural level lowers the cells' numbers under Posaconazole 5 µM (makes them more sensitive) | CERT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.69 | 0.268 over the table, 0.023 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Hesperidin (drug)]] 0.05 µM | C | CERT1's natural level lowers the cells' numbers under Hesperidin 0.05 µM (makes them more sensitive) | CERT1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.68 | 0.285 over the table, 0.079 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.713). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-3.3, -42.3); signed map (-12.2, 9.0). **Vector** length 101, 34.5% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +6.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +5.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.4 | +3.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.2 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.4 | +0.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +0.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.0 | +0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.0 | +0.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.0 | +0.7 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.6 | -5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -3.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.0 | -5.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.9 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.8 | -3.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.3 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | ceramide transporter 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.3 — chr5:75,356,345-75,512,138 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPBP, STARD11, CERT; previously COL4A3BP |
| Gene groups (HGNC) | Pleckstrin homology domain containing; StAR related lipid transfer domain containing |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y5P4](https://www.uniprot.org/uniprotkb/Q9Y5P4) (Ceramide transfer protein):

> Shelters ceramides inside its steroidogenic acute regulatory lipid transfer (START) domain and mediates their intracellular trafficking in a non-vesicular manner from the endoplasmic reticulum to the Golgi apparatus for conversion to sphingomyelin. Efficiently transfers ceramide molecules having long-chain fatty chains, but not those with very long acyl chains. Capable of transferring diacylglycerol, although with very low efficiency.

**Summary**, from NCBI Gene [10087](https://www.ncbi.nlm.nih.gov/gene/10087):

> This gene encodes a kinase that specifically phosphorylates the N-terminal region of the non-collagenous domain of the alpha 3 chain of type IV collagen, known as the Goodpasture antigen. Goodpasture disease is the result of an autoimmune response directed at this antigen. One isoform of this protein is also involved in ceramide intracellular transport. Three transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2205](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2205) · Entrez [10087](https://www.ncbi.nlm.nih.gov/gene/10087) · UniProt [Q9Y5P4](https://www.uniprot.org/uniprotkb/Q9Y5P4) · Ensembl [ENSG00000113163](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113163)

## Data

Gene col 3436: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3436); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3436, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3436]; `tensor/DDL_lfc|DDL_z.npy` [3436]; `embed/gene_vectors.npy` [3436]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3436 or target_col == 3436). Every well: [[CERT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
