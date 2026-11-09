---
symbol: "FRMD5"
type: "gene"
col: 10181
ensembl_id: "ENSG00000171877"
name: "FERM domain containing 5"
location: "15q15.3"
module: 34
arm: "+"
pooled_cpm: 230.0
n_lines_expressing: 40
n_dd_up: 28
n_dd_down: 22
n_dd_up_clean: 24
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 7
direction_downstream: 3
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# FRMD5

*FERM domain containing 5* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.31× (z +15.5, q 0e+00, up in 33 of 38 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.78× (z +15.1, q 0e+00, up in 37 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.519× (z -12.2, q 3e-31, down in 32 of 39 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.682× (z -10.0, q 1e-21, down in 28 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDP1]] (+0.62, fdr 1e-05), [[OSBPL3]] (+0.62, fdr 1e-05), [[NHS]] (+0.55, fdr 2e-05); moves opposite to [[TNS2]] (-0.52, fdr 1e-05), [[ISY1]] (-0.50, fdr 2e-05), [[ATG2B]] (-0.50, fdr 3e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GLUL]] → it (grade B ⚠); 3 go from it, the strongest it → [[GLUL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10181.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.31×** | +15.5 | 0e+00 | 33/38 (HT-29, A-172, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.78×** | +15.1 | 0e+00 | 37/38 (HEC-1-A, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.11×** | +13.8 | 4e-41 | 37/38 (HOP62, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +12.3 | 1e-32 | 35/38 (HOP62, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.94×** | +12.2 | 2e-32 | 34/38 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.77×** | +10.6 | 3e-24 | 30/38 (HOP62, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[EX229 (drug)]] 5 µM |  | **2.63×** | +9.4 | 6e-19 | 30/38 (A-172, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +9.3 | 7e-19 | 30/39 (HEC-1-A, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **2.51×** | +8.9 | 3e-17 | 30/38 (A-172, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.30×** | +8.1 | 4e-14 | 29/38 (HT-29, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +7.4 | 5e-12 | 18/38 (HOP62, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Abemaciclib (drug)]] 5 µM |  | **2.08×** | +7.1 | 6e-11 | 25/38 (HT-29, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.01×** | +6.8 | 5e-10 | 26/38 (HT-29, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.86×** | +6.0 | 7e-08 | 25/39 (HOP62, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.32×** | +5.1 | 1e-05 | 20/38 (J82, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.32×** | +5.1 | 1e-05 | 18/38 (HOP62, SHP-77, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 0.5 µM |  | **1.45×** | +4.9 | 3e-05 | 20/39 (NCI-H1792, HT-29, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10181.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.519×** | -12.2 | 3e-31 | 32/39 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.524×** | -11.5 | 2e-28 | 29/34 (C-33 A, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.537×** | -10.7 | 3e-24 | 30/35 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -10.0 | 1e-21 | 28/39 (HepG2/C3A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.383×** | -9.3 | 2e-18 | 31/39 (PANC-1, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.666×** | -7.5 | 4e-12 | 19/38 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.670×** | -7.4 | 9e-12 | 26/38 (KATO III, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **0.770×** | -6.9 | 5e-10 | 17/38 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.692×** | -6.8 | 6e-10 | 17/38 (Hs 766T, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.699×** | -6.6 | 2e-09 | 17/38 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.740×** | -5.6 | 1e-06 | 17/38 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.586×** | -5.2 | 1e-05 | 20/38 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.757×** | -5.2 | 1e-05 | 20/38 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.762×** | -5.0 | 2e-05 | 18/38 (A498, SNU-423, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.767×** | -4.7 | 9e-05 | 19/39 (Hs 766T, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.778×** | -4.6 | 1e-04 | 17/38 (Hs 766T, SNU-423, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **0.803×** | -4.1 | 0.002 | 14/38 (NCI-H1792, A498, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.807×** | -4.0 | 0.002 | 18/38 (Hs 766T, A498, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.797×** | -3.9 | 0.003 | 17/37 (Hs 766T, NCI-H1792, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10181. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 771 | 0 | 27 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -27.2) |
| [[Hs 766T (line)]] | wt | 279 | 6 (4 ⚠) | 21 (5 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.42× (z +13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 2.73× (z +10.7) | [[Clobetasol propionate (drug)]] 5 µM 0.225× (z -16.0) |
| [[HT-29 (line)]] | alt | 204 | 23 (6 ⚠) | 3 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 6.68× (z +22.0) ⚠ unreliable plate only · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.22× (z +19.1) | [[Docetaxel (drug)]] 0.05 µM 0.448× (z -9.4) ⚠ transcription drop |
| [[SNU-423 (line)]] | alt | 399 | 0 | 22 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -18.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -18.4) |
| [[A498 (line)]] | wt | 262 | 1 (1 ⚠) | 19 (2 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.06× (z +12.7) ⚠ unreliable plate only | [[Triamcinolone (drug)]] 5 µM 0.368× (z -12.9) |
| [[NCI-H1792 (line)]] | alt | 195 | 3 (1 ⚠) | 12 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +15.1) | [[Dinaciclib (drug)]] 5 µM 0.140× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Dexamethasone (drug)]] 5 µM 0.376× (z -9.4) |
| [[LoVo (line)]] | wt | 524 | 10 (3 ⚠) | 4 (4 ⚠) | [[Panobinostat (drug)]] 0.5 µM 2.64× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.117× (z -26.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 447 | 2 (2 ⚠) | 12 (4 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.10× (z +9.1) ⚠ unreliable plate only | [[Dinaciclib (drug)]] 0.05 µM 0.203× (z -18.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.366× (z -17.4) |
| [[HEC-1-A (line)]] | alt | 117 | 4 | 9 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.62× (z +16.9) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -17.7) |
| [[hTERT-HPNE (line)]] | wt | 110 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +17.0) | — |
| [[PANC-1 (line)]] | alt | 302 | 2 (1 ⚠) | 8 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.63× (z +12.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 3.36× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.367× (z -18.8) |
| [[HOP62 (line)]] | alt | 78.5 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +22.0) | — |
| [[KATO III (line)]] | alt | 512 | 3 (1 ⚠) | 6 (5 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.98× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -19.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.353× (z -17.2) |
| [[COLO 205 (line)]] | alt | 254 | 8 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +13.4) | — |
| [[C32 (line)]] | wt | 258 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +14.8) | — |
| [[SW1417 (line)]] | alt | 433 | 3 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.19× (z +13.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -22.0) |
| [[SW480 (line)]] | alt | 586 | 0 | 7 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.310× (z -21.9) |
| [[A-172 (line)]] | wt | 214 | 2 (1 ⚠) | 4 (3 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.01× (z +15.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 7.25× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.400× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 226 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +14.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.324× (z -10.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.495× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 81.0 | 6 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.71× (z +12.0) ⚠ unreliable plate only · without an alert: [[Panobinostat (drug)]] 5 µM 4.83× (z +10.8) | — |
| [[SW 900 (line)]] | alt | 210 | 2 (1 ⚠) | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +12.1) | [[Dexamethasone (drug)]] 5 µM 0.440× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 132 | 3 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.46× (z +11.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -10.6) |
| [[SW48 (line)]] | wt | 371 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.487× (z -9.2) |
| [[HS-578T (line)]] | alt | 123 | 1 (1 ⚠) | 3 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.60× (z +12.0) ⚠ unreliable plate only | [[Triamcinolone (drug)]] 5 µM 0.391× (z -9.3) |
| [[J82 (line)]] | alt | 81.4 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.30× (z +12.6) | — |
| [[LS 180 (line)]] | wt | 412 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 1.70× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -19.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 127 | 3 (1 ⚠) | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.05× (z +9.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.169× (z -16.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 134 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.448× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 178 | 1 (1 ⚠) | 2 (1 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.13× (z +9.5) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.8) |
| [[SK-MEL-2 (line)]] | alt | 552 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -12.0) |
| [[C-33 A (line)]] | alt | 195 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0687× (z -27.6) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 325 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.283× (z -11.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 182 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -12.0) |
| [[RPMI-7951 (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 5.27× (z +13.0) ⚠ unreliable plate only | — |
| [[SHP-77 (line)]] | alt | 163 | 1 | 0 | [[Belinostat (drug)]] 5 µM 1.98× (z +8.9) | — |
| [[A549 (line)]] | wt | 49.7 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 47.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 47.1 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 38.3 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 50.7 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 45.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.3 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 234 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 70.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 83.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 83.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10181), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDP1]] | +0.62 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[OSBPL3]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[NHS]] | +0.55 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[CMIP]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CREB5]] | +0.54 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[DOP1B]] | +0.52 | +0.54 / +0.46 | both halves | 3e-05 |  |
| [[PIP4K2A]] | +0.51 | +0.37 / +0.53 | both halves | 9e-05 |  |
| [[TIAM1]] | +0.50 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ARHGAP29]] | +0.50 | +0.41 / +0.46 | both halves | 4e-05 |  |
| [[SH3RF1]] | +0.50 | +0.61 / +0.44 | both halves | 3e-05 |  |
| [[IL1RAPL1]] | +0.49 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[CPA4]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNS2]] | -0.52 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[ISY1]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[ATG2B]] | -0.50 | -0.28 / -0.47 | both halves | 3e-04 |  |
| [[KLF9]] | -0.48 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[MAOA]] | -0.48 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[STXBP5-AS1]] | -0.45 | -0.47 / -0.29 | both halves | 3e-04 |  |
| [[CPD]] | -0.45 | -0.46 / -0.47 | both halves | 2e-05 |  |
| [[HIPK2]] | -0.44 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TSC22D3]] | -0.44 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[TLR2]] | -0.44 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[HIPK3]] | -0.44 | -0.36 / -0.48 | both halves | 1e-04 |  |
| [[VSTM2L]] | -0.43 | -0.38 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLUL]] | B | GLUL activity raises FRMD5's level | lines that do not express GLUL (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without GLUL | 0.032 | ⚠ within organs, on part of the lines |
| [[WNT7A]] | B | WNT7A activity raises FRMD5's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 1.67× lower at baseline in the lines without WNT7A | 0.034 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[NR3C1]] | B | NR3C1 activity lowers FRMD5's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[LINC00973]] | B | LINC00973 activity raises FRMD5's level | lines that do not express LINC00973 (23) vs lines expressing it (27) | 1.36× lower at baseline in the lines without LINC00973 | 0.073 | ⚠ within organs, on part of the lines; also absent: ENSG00000239462, IL11, BICC1 |
| [[WNT7B]] | B | WNT7B activity raises FRMD5's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 1.60× lower at baseline in the lines without WNT7B | 0.096 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[SYNJ2]] | C | SYNJ2 activity raises FRMD5's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 5.53× lower at baseline in the lines without SYNJ2 | 0.025 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |
| [[SH3RF1]] | C | SH3RF1 activity raises FRMD5's level | lines that do not express SH3RF1 (3) vs lines expressing it (47) | 3.88× lower at baseline in the lines without SH3RF1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: LHFPL2, SESTD1, HIPK2; its own permutation p |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GLUL]] | B | FRMD5 activity raises GLUL's level | lines that do not express FRMD5 (10) vs lines expressing it (40) | 3.65× lower at baseline in the lines without FRMD5 | 0.032 | ⚠ within organs, on part of the lines; also absent: ENSG00000291112; maybe low, not absent |
| [[SYNJ2]] | B | FRMD5 activity raises SYNJ2's level | lines that do not express FRMD5 (10) vs lines expressing it (40) | 2.15× lower at baseline in the lines without FRMD5 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000291112; maybe low, not absent |
| [[PDP1]] | B | FRMD5 activity raises PDP1's level | lines that do not express FRMD5 (10) vs lines expressing it (40) | 2.00× lower at baseline in the lines without FRMD5 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000291112; maybe low, not absent |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.348). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.3, 19.3); signed map (2.0, 41.6). **Vector** length 141, 46.5% of its response variance represented; |z| ≥ 3 in 1,777 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +11.8 | +15.5 |
|  | [[EX229 (drug)]] 5 µM |  | +7.2 | +9.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +7.1 | +8.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +15.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +5.6 | +6.8 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.3 | +8.1 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -10.0 | -10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.6 | -10.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.1 | -11.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -7.0 | -6.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.3 | -9.3 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | -5.5 | -4.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -5.5 | -5.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.4 | -2.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | -5.4 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | FERM domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,870,761-44,195,271 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC14161 |
| Gene groups (HGNC) | FERM domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z6J6](https://www.uniprot.org/uniprotkb/Q7Z6J6) (FERM domain-containing protein 5):

> May be involved in regulation of cell migration. May regulate cell-matrix interactions via its interaction with ITGB5 and modifying ITGB5 cytoplasmic tail interactions such as with FERMT2 and TLN1. May regulate ROCK1 kinase activity possibly involved in regulation of actin stress fiber formation.

**Summary**, from NCBI Gene [84978](https://www.ncbi.nlm.nih.gov/gene/84978):

> Enables integrin binding activity and protein kinase binding activity. Involved in negative regulation of cell motility; positive regulation of cell adhesion; and regulation of cell migration. Located in adherens junction. Implicated in neurodevelopmental disorder with eye movement abnormalities and ataxia. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28214](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28214) · Entrez [84978](https://www.ncbi.nlm.nih.gov/gene/84978) · UniProt [Q7Z6J6](https://www.uniprot.org/uniprotkb/Q7Z6J6) · Ensembl [ENSG00000171877](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171877)

## Data

Gene col 10181: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10181); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10181, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10181]; `tensor/DDL_lfc|DDL_z.npy` [10181]; `embed/gene_vectors.npy` [10181]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10181 or target_col == 10181). Every well: [[FRMD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FRMD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
