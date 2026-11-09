---
symbol: "POM121C"
type: "gene"
col: 15721
ensembl_id: "ENSG00000272391"
name: "POM121 transmembrane nucleoporin C"
location: "7q11.23"
module: 105
arm: "+"
pooled_cpm: 124.54
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 21
n_dd_up_clean: 11
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/105"]
generated_by: "tahoemap"
---

# POM121C

*POM121 transmembrane nucleoporin C* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.15× (z +13.2, q 7e-37, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.369× (z -17.0, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 0.719× (z -5.9, q 7e-07, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POM121]] (+0.86, fdr 7e-06), [[PRKRIP1]] (+0.82, fdr 7e-06), [[FAM210A]] (+0.72, fdr 7e-06); moves opposite to [[PTPRK]] (-0.53, fdr 1e-05), [[LPP]] (-0.53, fdr 4e-04), [[ITGAV]] (-0.53, fdr 2e-05).
> It is in [[Module 105]], a single-armed module (Late Phase of HIV Life Cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TMEM145]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.15×** | +13.2 | 7e-37 | 46/49 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.92×** | +9.9 | 1e-20 | 45/48 (A-172, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.74×** | +9.8 | 2e-20 | 42/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.50×** | +7.1 | 1e-10 | 36/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +6.6 | 4e-09 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.41×** | +6.0 | 1e-07 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.4 | 1e-03 | 24/38 (HT-29, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.56×** | +4.1 | 0.003 | 31/48 (MIA PaCa-2, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.37×** | +4.0 | 0.005 | 32/48 (LoVo, NCI-H2030, …) | two highest doses | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +3.9 | 0.005 | 27/48 (NCI-H2030, SW1417, …) | inconsistent across doses |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.013 | 25/48 (NCI-H1573, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 0.5 µM |  | **1.20×** | +3.2 | 0.059 | 20/49 (HS-578T, LOX-IMVI, …) | two highest doses |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.2 | 0.064 | 7/48 (H4, SNU-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.075 | 20/48 (MIA PaCa-2, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.40×** | +3.1 | 0.075 | 21/48 (HEC-1-A, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.369×** | -17.0 | 0e+00 | 43/44 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.453×** | -14.0 | 3e-42 | 45/49 (SNU-1, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.702×** | -6.0 | 3e-07 | 36/47 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.719×** | -5.9 | 7e-07 | 37/48 (PANC-1, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.806×** | -5.2 | 2e-05 | 31/48 (A-172, HS-578T, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.812×** | -5.0 | 4e-05 | 25/48 (C32, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.755×** | -5.0 | 5e-05 | 31/48 (NCI-H2347, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.762×** | -4.6 | 2e-04 | 31/48 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.827×** | -4.6 | 2e-04 | 24/48 (A-172, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.779×** | -4.4 | 5e-04 | 29/48 (LOX-IMVI, SW1417, …) | all doses, flat | cell-cycle shift (explains ~3% here) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.789×** | -4.2 | 0.001 | 31/48 (RPMI-7951, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.793×** | -4.0 | 0.004 | 25/50 (RPMI-7951, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.804×** | -3.9 | 0.005 | 29/48 (RPMI-7951, LOX-IMVI, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.812×** | -3.7 | 0.009 | 25/49 (HOP62, LOX-IMVI, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.009 | 27/48 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.814×** | -3.6 | 0.009 | 21/48 (H4, A-172, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.010 | 27/48 (C32, MIA PaCa-2, …) | rises with dose |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.819×** | -3.5 | 0.013 | 27/49 (A-172, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 138 | 7 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.80× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.508× (z -9.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 137 | 2 | 5 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 5.60× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.282× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.581× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 110 | 6 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.77× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.60× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.333× (z -11.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 144 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.08× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.300× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -11.1) |
| [[LoVo (line)]] | wt | 106 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.18× (z +15.6) | — |
| [[LS 180 (line)]] | wt | 83.3 | 5 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.64× (z +10.8) | [[Dinaciclib (drug)]] 0.5 µM 0.437× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 93.0 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.15× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.585× (z -9.6) |
| [[C32 (line)]] | wt | 332 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.387× (z -13.7) |
| [[NCI-H1792 (line)]] | alt | 196 | 3 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.81× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.209× (z -16.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 103 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.35× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.334× (z -11.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 111 | 3 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.33× (z +9.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.48× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -10.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 106 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.331× (z -13.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 130 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.55× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.417× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 129 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.67× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.355× (z -14.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 124 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.45× (z +8.6) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -13.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 142 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 230 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.98× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.424× (z -10.9) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 98.9 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.08× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -10.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 142 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.156× (z -17.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 124 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.287× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.0) |
| [[A549 (line)]] | wt | 95.6 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.07× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.306× (z -10.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 194 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.416× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 123 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +12.0) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -11.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 149 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.139× (z -16.1) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.338× (z -12.0) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 57.6 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.23× (z +9.6) | — |
| [[H4 (line)]] | wt | 212 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0917× (z -17.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 152 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -12.0) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 103 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.323× (z -8.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 96.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.356× (z -12.0) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 152 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.70× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.345× (z -9.5) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 123 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.398× (z -10.3) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -17.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.433× (z -8.7) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 109 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.324× (z -13.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -16.7) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 95.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 6.13× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 76.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.443× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 147 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.199× (z -16.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0419× (z -14.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.310× (z -11.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 123 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 72.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 144 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 89.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POM121]] | +0.86 | +0.90 / +0.83 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 931 |
| [[PRKRIP1]] | +0.82 | +0.91 / +0.74 | both halves | 7e-06 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[FAM210A]] | +0.72 | +0.81 / +0.64 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.72 | +0.80 / +0.65 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.71 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[FUT11]] | +0.69 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[FNTB]] | +0.68 | +0.75 / +0.64 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[UBE2O]] | +0.68 | +0.80 / +0.60 | both halves | 7e-06 |  |
| [[PMS2CL]] | +0.67 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[RNMT]] | +0.67 | +0.80 / +0.55 | both halves | 1e-05 | pathway: HIV Infection |
| [[CRYBB2P1-1]] | +0.67 | +0.71 / +0.60 | both halves | 7e-06 |  |
| [[SFXN1]] | +0.66 | +0.77 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRK]] | -0.53 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[LPP]] | -0.53 | -0.26 / -0.45 | both halves | 4e-04 |  |
| [[ITGAV]] | -0.53 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[TJP1]] | -0.52 | -0.39 / -0.51 | both halves | 6e-05 | pathway: SARS-CoV-2 Infection |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TMEM145]] | B | TMEM145 activity raises POM121C's level | lines that do not express TMEM145 (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without TMEM145 | 0.083 | ⚠ within organs, on part of the lines; also absent: GXYLT2, KCNK13, DLX1 |
| [[IKBIP]] | C | IKBIP activity raises POM121C's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without IKBIP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 105]] — Late Phase of HIV Life Cycle; 44 genes; every member is in the + arm (projection on the module's main direction 0.872). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.5, -20.1); signed map (-40.7, 22.1). **Vector** length 109, 37.1% of its response variance represented; |z| ≥ 3 in 1,111 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +8.9 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +7.0 | -1.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +13.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.9 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +4.0 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +1.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.2 | +3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +4.1 |
|  | [[EX229 (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +3.0 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -4.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.9 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.9 | -2.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.3 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.4 | -3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.0 | -1.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.9 | -3.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.6 | -3.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.4 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | POM121 transmembrane nucleoporin C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:75,416,786-75,486,299 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 69 pathways, smallest: IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus; IPs transport between nucleus and cytosol |
| Matched by | ensembl_id |

**Function**, from UniProt [A8CG34](https://www.uniprot.org/uniprotkb/A8CG34) (Nuclear envelope pore membrane protein POM 121C):

> Essential component of the nuclear pore complex (NPC). The repeat-containing domain may be involved in anchoring components of the pore complex to the pore membrane. When overexpressed in cells induces the formation of cytoplasmic annulate lamellae (AL).

**Summary**, from NCBI Gene [100101267](https://www.ncbi.nlm.nih.gov/gene/100101267):

> Predicted to enable nuclear localization sequence binding activity. Predicted to be a structural constituent of nuclear pore. Predicted to be involved in RNA export from nucleus and protein import into nucleus. Predicted to be located in nuclear envelope. Predicted to be part of nuclear pore. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:34005](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:34005) · Entrez [100101267](https://www.ncbi.nlm.nih.gov/gene/100101267) · UniProt [A8CG34](https://www.uniprot.org/uniprotkb/A8CG34) · Ensembl [ENSG00000272391](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000272391)

## Data

Gene col 15721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15721); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15721]; `tensor/DDL_lfc|DDL_z.npy` [15721]; `embed/gene_vectors.npy` [15721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15721 or target_col == 15721). Every well: [[POM121C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POM121C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
