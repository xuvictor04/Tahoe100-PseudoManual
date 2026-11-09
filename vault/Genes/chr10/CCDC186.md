---
symbol: "CCDC186"
type: "gene"
col: 9193
ensembl_id: "ENSG00000165813"
name: "coiled-coil domain containing 186"
location: "10q25.3"
module: 74
arm: "+"
pooled_cpm: 110.32
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/074"]
generated_by: "tahoemap"
---

# CCDC186

*coiled-coil domain containing 186* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.11× (z +18.3, q 0e+00, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.468× (z -13.9, q 3e-41, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-733 (drug)]] 5 µM: 0.477× (z -7.1, q 4e-10, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AKAP9]] (+0.77, fdr 7e-06), [[SELENOK]] (+0.76, fdr 7e-06), [[TMF1]] (+0.75, fdr 7e-06); moves opposite to [[VMA21]] (-0.65, fdr 7e-06), [[EFTUD2]] (-0.64, fdr 7e-06), [[CAD]] (-0.61, fdr 1e-05).
> It is in [[Module 074]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Belzutifan (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9193.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.11×** | +18.3 | 0e+00 | 45/48 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.33×** | +15.4 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.67×** | +9.4 | 1e-18 | 41/48 (HepG2/C3A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.61×** | +8.4 | 6e-15 | 38/48 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.7 | 1e-12 | 31/49 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.38×** | +5.8 | 5e-07 | 29/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.35×** | +5.1 | 2e-05 | 29/48 (PANC-1, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.8 | 1e-04 | 28/48 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.28×** | +4.5 | 5e-04 | 28/48 (BT-474, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.26×** | +4.2 | 0.002 | 25/48 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.020 | 20/48 (SW48, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.022 | 22/48 (A-427, HEC-1-A, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | 1.15× | +3.4 | 0.025 | 10/48 (HT-29, A-427, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.13× | +3.4 | 0.025 | 20/48 (SW1417, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.42×** | +3.4 | 0.030 | 21/45 (SNU-423, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.031 | 17/49 (PANC-1, C32, …) | all doses, flat | noisy plate (z scaled) |
| [[Silodosin (drug)]] 5 µM |  | 1.19× | +3.1 | 0.064 | 14/47 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +3.0 | 0.074 | 15/49 (CFPAC-1, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9193.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.468×** | -13.9 | 3e-41 | 48/48 (NCI-H2347, HT-29, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.477×** | -7.1 | 4e-10 | 43/48 (AsPC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.690×** | -6.8 | 2e-09 | 34/49 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.503×** | -6.6 | 7e-09 | 37/48 (AsPC-1, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.508×** | -6.5 | 1e-08 | 34/48 (AsPC-1, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.551×** | -5.7 | 1e-06 | 33/48 (AsPC-1, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.604×** | -4.8 | 1e-04 | 31/48 (NCI-H2347, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.604×** | -4.8 | 1e-04 | 34/47 (SW 900, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.779×** | -4.4 | 6e-04 | 21/42 (NCI-H1573, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.780×** | -4.4 | 6e-04 | 28/48 (LoVo, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.773×** | -4.4 | 6e-04 | 25/45 (A498, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.832×** | -4.3 | 9e-04 | 24/48 (AsPC-1, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.783×** | -4.3 | 9e-04 | 28/48 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.843× | -4.2 | 0.001 | 19/48 (CFPAC-1, LS 180, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.806×** | -3.8 | 0.007 | 20/49 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.811×** | -3.6 | 0.010 | 25/48 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.816×** | -3.5 | 0.014 | 17/48 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Adenine (drug)]] 5 µM |  | 0.869× | -3.4 | 0.023 | 11/48 (PANC-1, HT-29, …) | top dose only |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.835× | -3.1 | 0.052 | 17/49 (NCI-H2122, LS 180, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.837× | -3.1 | 0.057 | 14/49 (LS 180, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9193. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 154 | 1 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.330× (z -14.1) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.216× (z -10.2) |
| [[HT-29 (line)]] | alt | 256 | 2 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -18.3) ⚠ unreliable plate only |
| [[NCI-H460 (line)]] | wt | 49.7 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.12× (z +16.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.400× (z -9.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 64.6 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.96× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.142× (z -18.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 187 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.383× (z -14.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.622× (z -9.5) |
| [[PANC-1 (line)]] | alt | 89.3 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.41× (z +19.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.422× (z -10.3) ⚠ unreliable plate only |
| [[CFPAC-1 (line)]] | alt | 129 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.439× (z -10.5) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 110 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.419× (z -9.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 159 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -11.7) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 57.2 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.69× (z +14.1) | — |
| [[NCI-H1573 (line)]] | alt | 151 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +15.0) | [[Dinaciclib (drug)]] 5 µM 0.0507× (z -32.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 191 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.28× (z +12.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.284× (z -18.9) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 170 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +11.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.285× (z -16.8) ⚠ unreliable plate only |
| [[SW48 (line)]] | wt | 99.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.03× (z +11.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.267× (z -9.3) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 79.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +18.2) | — |
| [[LOX-IMVI (line)]] | wt | 67.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.79× (z +16.5) | — |
| [[LS 180 (line)]] | wt | 176 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 62.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.80× (z +9.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.305× (z -11.2) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 109 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -8.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 146 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.94× (z +11.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.405× (z -11.2) ⚠ unreliable plate only |
| [[RKO (line)]] | wt | 89.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.95× (z +12.2) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -9.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 60.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +14.4) | — |
| [[SNU-423 (line)]] | alt | 98.7 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +14.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.424× (z -10.1) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 141 | 1 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.86× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.301× (z -18.0) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.303× (z -9.4) |
| [[A-172 (line)]] | wt | 59.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 154 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.311× (z -9.5) ⚠ unreliable plate only |
| [[HepG2_C3A (line)]] | wt | 123 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 68.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +16.6) | — |
| [[HS-578T (line)]] | alt | 69.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.1) | — |
| [[LoVo (line)]] | wt | 165 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.383× (z -9.4) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 73.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.68× (z +14.2) | — |
| [[SNU-1 (line)]] | wt | 49.9 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.31× (z +10.4) | — |
| [[SW 1088 (line)]] | alt | 103 | 0 | 2 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.0815× (z -9.5) |
| [[SW 900 (line)]] | alt | 158 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.428× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Belzutifan (drug)]] 5 µM 0.238× (z -8.7) |
| [[AN3 CA (line)]] | alt | 71.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +8.9) | — |
| [[BT-474 (line)]] | alt | 40.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +8.6) | — |
| [[C-33 A (line)]] | alt | 43.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 263 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +8.9) | — |
| [[Hs 766T (line)]] | wt | 82.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.371× (z -9.0) ⚠ unreliable plate only |
| [[J82 (line)]] | alt | 50.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +10.2) | — |
| [[NCI-H661 (line)]] | alt | 63.7 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0911× (z -9.8) |
| [[SHP-77 (line)]] | alt | 54.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.355× (z -9.1) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 105 | 0 | 1 | — | [[Folic acid (drug)]] 5 µM 0.220× (z -8.9) |
| [[C32 (line)]] | wt | 65.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 105 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9193), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AKAP9]] | +0.77 | +0.79 / +0.76 | both halves | 7e-06 |  |
| [[SELENOK]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[TMF1]] | +0.75 | +0.77 / +0.67 | both halves | 7e-06 | same gene group; STRING 564 |
| [[GCC2]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 | STRING 458 |
| [[DNAJB9]] | +0.72 | +0.56 / +0.71 | both halves | 1e-05 |  |
| [[SMIM14]] | +0.72 | +0.58 / +0.78 | both halves | 7e-06 |  |
| [[IFT20]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[SLU7]] | +0.69 | +0.63 / +0.70 | both halves | 7e-06 |  |
| [[ZRSR2]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[SAFB2]] | +0.68 | +0.77 / +0.58 | both halves | 7e-06 |  |
| [[NKAP]] | +0.67 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[CIR1]] | +0.67 | +0.60 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VMA21]] | -0.65 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.64 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[CAD]] | -0.61 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[NUP155]] | -0.60 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[PFAS]] | -0.60 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[PHB1]] | -0.59 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[TATDN2]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[RPSA]] | -0.58 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[UTP4]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[TBRG4]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[RPE]] | -0.56 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[DHX15]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises CCDC186's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.58× lower at baseline in the lines without AGR2 | 0.022 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[PSMB5]] | B | PSMB5 activity lowers CCDC186's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Belzutifan (drug)]] 5 µM | C | CCDC186's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | CCDC186's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.478 over the table, 0.080 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 074]]; 63 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.8, -38.7); signed map (-49.2, 15.2). **Vector** length 129, 42.8% of its response variance represented; |z| ≥ 3 in 1,178 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.9 | +15.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +7.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.6 | +0.8 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.6 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +1.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.2 | +1.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -14.6 | -13.9 |
|  | [[EX229 (drug)]] 5 µM |  | -8.7 | -6.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -8.2 | -7.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.8 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -7.2 | -4.8 |
|  | [[venetoclax (drug)]] 5 µM |  | -6.9 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 186 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:114,120,862-114,174,232 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10188, FLJ35301, CCCP-1, golgin104; previously C10orf118 |
| Gene groups (HGNC) | MicroRNA protein coding host genes |
| Matched by | ensembl_id |

UniProt [Q7Z3E2](https://www.uniprot.org/uniprotkb/Q7Z3E2) carries no function annotation.

**Summary**, from NCBI Gene [55088](https://www.ncbi.nlm.nih.gov/gene/55088):

> Predicted to enable small GTPase binding activity. Predicted to be involved in vesicle cytoskeletal trafficking. Predicted to act upstream of or within insulin secretion involved in cellular response to glucose stimulus and response to bacterium. Predicted to be located in Golgi apparatus. Predicted to be active in trans-Golgi network. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24349](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24349) · Entrez [55088](https://www.ncbi.nlm.nih.gov/gene/55088) · UniProt [Q7Z3E2](https://www.uniprot.org/uniprotkb/Q7Z3E2) · Ensembl [ENSG00000165813](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165813)

## Data

Gene col 9193: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9193); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9193, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9193]; `tensor/DDL_lfc|DDL_z.npy` [9193]; `embed/gene_vectors.npy` [9193]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9193 or target_col == 9193). Every well: [[CCDC186 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC186.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
