---
symbol: "MTHFD2"
type: "gene"
col: 809
ensembl_id: "ENSG00000065911"
name: "methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2, methenyltetrahydrofolate cyclohydrolase"
location: "2p13.1"
module: 63
arm: "+"
pooled_cpm: 144.87
n_lines_expressing: 50
n_dd_up: 41
n_dd_down: 19
n_dd_up_clean: 30
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# MTHFD2

*methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2, methenyltetrahydrofolate cyclohydrolase* — 2p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.89× (z +15.5, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Neratinib (maleate) (drug)]] 0.5 µM: 1.88× (z +9.2, q 4e-18, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.392× (z -19.4, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSAT1]] (+0.90, fdr 7e-06), [[ASNS]] (+0.89, fdr 7e-06), [[IARS1]] (+0.87, fdr 7e-06); moves opposite to [[EID2]] (-0.59, fdr 1e-05), [[PLPP3]] (-0.58, fdr 1e-05), [[GPATCH8]] (-0.56, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[RPS6KA2]] → it (grade B ⚠); 2 go from it, the strongest it → [[IARS1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 809.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.89×** | +15.5 | 0e+00 | 49/49 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +14.7 | 0e+00 | 42/44 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.20×** | +10.7 | 2e-24 | 42/45 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.88×** | +9.2 | 4e-18 | 48/48 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.56×** | +9.2 | 4e-18 | 44/48 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.79×** | +8.5 | 2e-15 | 45/48 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.75×** | +7.9 | 3e-13 | 37/47 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +6.8 | 6e-10 | 42/48 (MIA PaCa-2, BT-474, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.56×** | +6.5 | 4e-09 | 40/48 (SNU-1, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.37×** | +6.5 | 6e-09 | 36/48 (NCI-H2030, SHP-77, …) | all doses, stronger at high dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.48×** | +5.7 | 5e-07 | 37/48 (C-33 A, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.48×** | +5.7 | 6e-07 | 38/48 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.07×** | +5.6 | 1e-06 | 40/48 (LOX-IMVI, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.30×** | +5.4 | 3e-06 | 29/49 (SNU-1, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.38×** | +4.6 | 2e-04 | 28/50 (LOX-IMVI, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 29/48 (NCI-H2030, CFPAC-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.79×** | +4.5 | 3e-04 | 38/48 (CFPAC-1, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.71×** | +4.1 | 0.001 | 34/48 (AsPC-1, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +4.1 | 0.001 | 25/49 (COLO 205, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.29×** | +3.8 | 0.005 | 30/48 (HCT15, HepG2/C3A, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.60×** | +3.6 | 0.009 | 27/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 809.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.392×** | -19.4 | 0e+00 | 46/48 (A-427, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -13.1 | 1e-36 | 46/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -8.9 | 1e-16 | 36/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.573×** | -8.1 | 5e-14 | 37/48 (A-427, SW48, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.580×** | -8.0 | 2e-13 | 32/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.711×** | -7.1 | 2e-10 | 36/48 (A-427, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.488×** | -5.5 | 3e-06 | 37/49 (A-427, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.792×** | -4.8 | 1e-04 | 27/48 (A-427, PANC-1, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.719×** | -4.5 | 5e-04 | 27/47 (LoVo, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.753×** | -4.2 | 0.002 | 33/49 (SK-MEL-2, NCI-H23, …) | all doses, flat |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.831×** | -3.8 | 0.006 | 26/48 (H4, KATO III, …) | all doses, stronger at high dose |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.773×** | -3.8 | 0.008 | 25/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.615×** | -3.7 | 0.009 | 24/48 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[AZD-8055 (drug)]] 5 µM |  | **0.625×** | -3.6 | 0.013 | 23/49 (H4, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.803×** | -3.2 | 0.048 | 22/48 (NCI-H23, HCT15, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 809. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 280 | 0 | 16 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -26.8) |
| [[A-427 (line)]] | wt | 303 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0589× (z -55.2) |
| [[LoVo (line)]] | wt | 209 | 3 (1 ⚠) | 6 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.10× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.106× (z -26.3) |
| [[MIA PaCa-2 (line)]] | alt | 148 | 7 (4 ⚠) | 1 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.42× (z +11.2) | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.9) |
| [[SNU-1 (line)]] | wt | 191 | 3 | 5 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.73× (z +13.9) | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -18.9) |
| [[H4 (line)]] | wt | 239 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.0682× (z -35.3) |
| [[HT-29 (line)]] | alt | 229 | 1 (1 ⚠) | 6 | [[Dinaciclib (drug)]] 0.5 µM 2.08× (z +8.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -27.7) |
| [[KATO III (line)]] | alt | 263 | 0 | 7 | — | [[Harringtonine (drug)]] 5 µM 0.0860× (z -23.5) |
| [[NCI-H2030 (line)]] | alt | 185 | 6 (3 ⚠) | 1 | [[Neratinib (maleate) (drug)]] 0.5 µM 3.03× (z +11.4) | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -10.2) |
| [[SW1417 (line)]] | alt | 165 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -22.1) |
| [[SW480 (line)]] | alt | 151 | 4 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.06× (z +14.1) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 1.64× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -22.8) |
| [[A-172 (line)]] | wt | 108 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.40× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -15.3) |
| [[SW48 (line)]] | wt | 207 | 1 (1 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 2.72× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -20.5) |
| [[A549 (line)]] | wt | 136 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.35× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 76.5 | 4 (4 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.40× (z +10.7) ⚠ toxic | [[Harringtonine (drug)]] 5 µM 0.348× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 104 | 3 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +11.8) ⚠ toxic; transcription drop · without an alert: [[Artesunate (drug)]] 5 µM 2.34× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -10.5) |
| [[HepG2_C3A (line)]] | wt | 105 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -18.0) |
| [[HS-578T (line)]] | alt | 136 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.61× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -14.7) |
| [[LS 180 (line)]] | wt | 180 | 1 | 4 | [[Artesunate (drug)]] 5 µM 1.95× (z +9.0) | [[Harringtonine (drug)]] 5 µM 0.194× (z -15.2) |
| [[HCT15 (line)]] | alt | 232 | 2 | 2 | [[Artesunate (drug)]] 5 µM 2.25× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -12.9) |
| [[Hs 766T (line)]] | wt | 67.3 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.39× (z +9.7) | — |
| [[NCI-H23 (line)]] | alt | 157 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -24.1) |
| [[NCI-H460 (line)]] | wt | 135 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +11.9) ⚠ toxic; transcription drop · without an alert: [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.05× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.394× (z -11.7) |
| [[RKO (line)]] | wt | 144 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -25.2) |
| [[A498 (line)]] | wt | 251 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -19.3) |
| [[J82 (line)]] | alt | 59.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.12× (z +11.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -10.1) |
| [[LOX-IMVI (line)]] | wt | 88.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.21× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 92.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.10× (z +10.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.257× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 82.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.04× (z +9.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 64.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -9.9) |
| [[SHP-77 (line)]] | alt | 103 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.48× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -11.9) |
| [[SW 900 (line)]] | alt | 83.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.46× (z +12.1) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 97.6 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.72× (z +9.6) | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.7) |
| [[C-33 A (line)]] | alt | 115 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.81× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -11.0) |
| [[C32 (line)]] | wt | 48.3 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.90× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 128 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -12.8) |
| [[COLO 205 (line)]] | alt | 106 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +11.8) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.342× (z -8.6) |
| [[HOP62 (line)]] | alt | 96.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 85.4 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +11.9) ⚠ cell-cycle shift, explains ~74% of this change | [[Homoharringtonine (drug)]] 5 µM 0.431× (z -11.7) |
| [[SK-MEL-2 (line)]] | alt | 80.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 99.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.66× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 87.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.39× (z +9.1) ⚠ toxic; transcription drop | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.9) |
| [[SNU-423 (line)]] | alt | 71.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +9.0) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 66.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 101 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 809), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSAT1]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 763 |
| [[ASNS]] | +0.89 | +0.89 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 717 |
| [[IARS1]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[XPOT]] | +0.86 | +0.86 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_UNFOLDED_PROTEIN_RESPONSE |
| [[AARS1]] | +0.86 | +0.84 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[PHGDH]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 722 |
| [[GARS1]] | +0.84 | +0.85 / +0.83 | both halves | 7e-06 |  |
| [[CARS1]] | +0.83 | +0.84 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[SLC1A4]] | +0.81 | +0.77 / +0.80 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[MARS1]] | +0.80 | +0.79 / +0.79 | both halves | 7e-06 |  |
| [[NARS1]] | +0.80 | +0.72 / +0.80 | both halves | 7e-06 |  |
| [[SARS1]] | +0.80 | +0.79 / +0.78 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EID2]] | -0.59 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PLPP3]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH8]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[TGIF2]] | -0.55 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[HNRNPH2]] | -0.55 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[TBCC]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[MRFAP1L1]] | -0.53 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.52 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[CSTF2T]] | -0.52 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ZNF776]] | -0.52 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[NFAT5]] | -0.52 | -0.38 / -0.51 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RPS6KA2]] | B | RPS6KA2 activity lowers MTHFD2's level | lines that do not express RPS6KA2 (6) vs lines expressing it (44) | 1.09× higher at baseline in the lines without RPS6KA2 | 0.036 | ⚠ within organs, on part of the lines; also absent: RAB20, FAM102A, LINC02100 |
| [[MTOR]] | B | MTOR activity raises MTHFD2's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Temsirolimus) | 50% of the class's compounds vs 3.1% of all compounds | 0.040 | ⚠ off-target possible; 4 compounds |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IARS1]] | C | MTHFD2's natural level weakens IARS1's drug response | MTHFD2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.68, reverse -0.05; direction clear | 0.015 | ⚠ tissue can mimic it; precision caveat |
| [[HSPA9]] | C | MTHFD2's natural level weakens HSPA9's drug response | MTHFD2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse +0.07; direction not clear | 0.062 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.891). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.7, 47.8); signed map (-13.8, 24.4). **Vector** length 153, 59.1% of its response variance represented; |z| ≥ 3 in 1,692 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.81 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.81 to 9); *Metabolism of amino acids and derivatives* (reactome, mean cos +0.72 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +10.2 | +8.5 |
|  | [[Artesunate (drug)]] 5 µM |  | +9.5 | +9.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.8 | +5.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +7.6 | +6.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +7.6 | +6.5 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | +6.2 | +3.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +5.9 | +5.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -12.3 | -13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -10.2 | -19.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -10.2 | -8.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.5 | -7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -8.0 | -8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -7.5 | -4.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.0 | -4.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.7 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | methylenetetrahydrofolate dehydrogenase (NADP+ dependent) 2, methenyltetrahydrofolate cyclohydrolase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p13.1 — chr2:74,186,172-74,217,565 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MTHFD family; Methylenetetrahydrofolate dehydrogenases |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, INTERFERON_GAMMA_RESPONSE, MTORC1_SIGNALING, E2F_TARGETS |
| Reactome | 3 pathways, smallest: Metabolism of folate and pterines; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [P13995](https://www.uniprot.org/uniprotkb/P13995) (Bifunctional methylenetetrahydrofolate dehydrogenase/cyclohydrolase, mitochondrial):

> Although its dehydrogenase activity is NAD-specific, it can also utilize NADP at a reduced efficiency.

**Summary**, from NCBI Gene [10797](https://www.ncbi.nlm.nih.gov/gene/10797):

> This gene encodes a nuclear-encoded mitochondrial bifunctional enzyme with methylenetetrahydrofolate dehydrogenase and methenyltetrahydrofolate cyclohydrolase activities. The enzyme functions as a homodimer and is unique in its absolute requirement for magnesium and inorganic phosphate. Formation of the enzyme-magnesium complex allows binding of NAD. Alternative splicing results in two different transcripts, one protein-coding and the other not protein-coding. This gene has a pseudogene on …

**Accessions** — [HGNC:7434](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7434) · Entrez [10797](https://www.ncbi.nlm.nih.gov/gene/10797) · UniProt [P13995](https://www.uniprot.org/uniprotkb/P13995) · Ensembl [ENSG00000065911](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000065911)

## Data

Gene col 809: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 809); `tables/drug_effects.parquet` (62 rows, flagged included); `relations/gene_relations.parquet` (col_a == 809, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 809]; `tensor/DDL_lfc|DDL_z.npy` [809]; `embed/gene_vectors.npy` [809]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 809 or target_col == 809). Every well: [[MTHFD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTHFD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
