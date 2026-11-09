---
symbol: "OSBPL9"
type: "gene"
col: 3951
ensembl_id: "ENSG00000117859"
name: "oxysterol binding protein like 9"
location: "1p32.3"
module: 45
arm: "+"
pooled_cpm: 198.42
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 14
n_dd_up_clean: 17
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# OSBPL9

*oxysterol binding protein like 9* — 1p32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.19× (z +17.2, q 0e+00, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.692× (z -11.3, q 4e-27, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO3]] (+0.72, fdr 7e-06), [[MED30]] (+0.67, fdr 1e-05), [[LMBRD1]] (+0.64, fdr 7e-06); moves opposite to [[PIGW]] (-0.64, fdr 1e-05), [[CYREN]] (-0.63, fdr 3e-05), [[PCBP1-AS1]] (-0.62, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3951.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.19×** | +17.2 | 0e+00 | 44/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.15×** | +16.8 | 0e+00 | 48/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.93×** | +14.4 | 1e-44 | 47/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.74×** | +12.1 | 1e-31 | 47/48 (SW480, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +11.6 | 3e-29 | 37/48 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +11.1 | 9e-27 | 42/48 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.60×** | +10.3 | 4e-23 | 42/48 (HT-29, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.58×** | +10.0 | 1e-21 | 33/48 (NCI-H460, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.55×** | +9.7 | 3e-20 | 33/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +9.5 | 1e-19 | 39/47 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.22×** | +9.2 | 3e-18 | 38/49 (SW480, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.50×** | +8.4 | 2e-15 | 39/48 (HT-29, COLO 205, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +8.3 | 5e-15 | 29/48 (RKO, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +7.6 | 1e-12 | 39/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +6.3 | 2e-08 | 29/48 (KATO III, Panc 03.27, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.32×** | +5.9 | 2e-07 | 30/48 (MIA PaCa-2, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.40×** | +5.2 | 7e-06 | 40/49 (COLO 205, PANC-1, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3951.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.692×** | -11.3 | 4e-27 | 40/49 (A549, HS-578T, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.627×** | -10.2 | 6e-22 | 40/49 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.620×** | -10.1 | 2e-21 | 37/44 (CFPAC-1, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.645×** | -9.6 | 1e-19 | 48/48 (HS-578T, NCI-H2347, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.742×** | -6.5 | 9e-09 | 26/48 (SNU-423, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.773×** | -5.4 | 6e-06 | 31/50 (HS-578T, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.639×** | -5.1 | 2e-05 | 37/48 (HS-578T, C32, …) | rises with dose | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.785×** | -5.1 | 3e-05 | 30/48 (SNU-423, A-172, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~12% of this change | **0.799×** | -4.9 | 7e-05 | 29/48 (HS-578T, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.667×** | -4.6 | 2e-04 | 31/48 (HS-578T, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.672×** | -4.5 | 3e-04 | 34/48 (HS-578T, A549, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.865× | -4.5 | 4e-04 | 15/48 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.678×** | -4.4 | 4e-04 | 26/48 (HS-578T, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.687×** | -4.3 | 7e-04 | 32/48 (HS-578T, A549, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.784×** | -3.7 | 0.008 | 25/49 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 0.861× | -3.3 | 0.035 | 15/48 (C32, RPMI-7951, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.865× | -3.1 | 0.049 | 14/48 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.868× | -3.1 | 0.060 | 13/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.869× | -3.0 | 0.063 | 17/48 (NCI-H2030, AsPC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3951. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 148 | 12 (4 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 8.40× (z +35.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.607× (z -11.8) |
| [[KATO III (line)]] | alt | 130 | 12 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.50× (z +24.8) | — |
| [[SW480 (line)]] | alt | 175 | 12 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.49× (z +17.0) | — |
| [[PANC-1 (line)]] | alt | 181 | 11 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.38× (z +24.1) | — |
| [[LOX-IMVI (line)]] | wt | 197 | 5 (1 ⚠) | 5 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.94× (z +12.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.419× (z -10.4) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.565× (z -9.6) |
| [[HT-29 (line)]] | alt | 185 | 9 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 2.50× (z +13.8) | — |
| [[NCI-H1573 (line)]] | alt | 145 | 9 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.67× (z +22.6) | — |
| [[SW1417 (line)]] | alt | 171 | 8 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.37× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -9.3) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 189 | 8 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.69× (z +19.3) | — |
| [[SHP-77 (line)]] | alt | 195 | 5 (2 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.73× (z +14.9) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 2.84× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.438× (z -9.7) ⚠ unreliable plate only |
| [[BT-474 (line)]] | alt | 179 | 7 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.43× (z +15.0) | — |
| [[C32 (line)]] | wt | 167 | 5 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 9.14× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.447× (z -8.9) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 351 | 2 (1 ⚠) | 5 (4 ⚠) | [[Daptomycin (drug)]] 5 µM 1.99× (z +9.0) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 1.62× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.297× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.473× (z -13.8) |
| [[HS-578T (line)]] | alt | 285 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.416× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 228 | 6 (2 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +14.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -13.1) |
| [[SNU-423 (line)]] | alt | 225 | 2 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.98× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.534× (z -14.3) |
| [[LS 180 (line)]] | wt | 224 | 6 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +13.9) | — |
| [[NCI-H2347 (line)]] | alt | 234 | 3 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.27× (z +12.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -11.6) |
| [[SW48 (line)]] | wt | 161 | 5 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.19× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.350× (z -8.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 231 | 5 | 0 | [[Panobinostat (drug)]] 5 µM 2.22× (z +10.9) | — |
| [[AsPC-1 (line)]] | alt | 235 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.51× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.450× (z -8.8) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 283 | 3 | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.285× (z -13.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 247 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.14× (z +13.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[Hs 766T (line)]] | wt | 216 | 2 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.484× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.624× (z -9.1) |
| [[J82 (line)]] | alt | 186 | 4 | 1 | [[Panobinostat (drug)]] 5 µM 2.12× (z +11.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.640× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 169 | 4 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +11.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.618× (z -9.5) |
| [[A549 (line)]] | wt | 175 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.17× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -15.4) |
| [[C-33 A (line)]] | alt | 141 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.73× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 223 | 1 | 3 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.589× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 254 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 2.48× (z +12.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.603× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 232 | 1 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.79× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -11.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 188 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.33× (z +14.1) | — |
| [[SK-MEL-2 (line)]] | alt | 179 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.29× (z +10.2) | — |
| [[SW 900 (line)]] | alt | 176 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.35× (z +15.3) | — |
| [[A-172 (line)]] | wt | 154 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.13× (z +10.6) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -10.8) ⚠ cell-cycle shift, explains ~19% of this change |
| [[A-427 (line)]] | wt | 150 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 2.76× (z +14.5) | — |
| [[COLO 205 (line)]] | alt | 150 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 2.75× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 212 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.07× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.459× (z -11.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 169 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.358× (z -11.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 220 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.43× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.9) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 239 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.38× (z +10.0) | — |
| [[HEC-1-A (line)]] | alt | 191 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.63× (z +11.3) | — |
| [[SNU-1 (line)]] | wt | 172 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.6) | — |
| [[AN3 CA (line)]] | alt | 197 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3951), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO3]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[MED30]] | +0.67 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[PLEKHM3]] | +0.63 | +0.47 / +0.61 | both halves | 2e-05 | same gene group |
| [[CYB5R4]] | +0.62 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[STX7]] | +0.62 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[ABI1]] | +0.62 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[CAT]] | +0.62 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[STRN]] | +0.61 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[YPEL2]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[HACL1]] | +0.61 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[HDAC5]] | +0.61 | +0.44 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGW]] | -0.64 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[CYREN]] | -0.63 | -0.63 / -0.44 | both halves | 3e-05 |  |
| [[PCBP1-AS1]] | -0.62 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[CSTF3]] | -0.61 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[PYCR2]] | -0.60 | -0.64 / -0.33 | both halves | 1e-04 |  |
| [[KIAA0753]] | -0.60 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[TRNT1]] | -0.59 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[MPDU1]] | -0.59 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.58 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[IDI2-AS1]] | -0.58 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[MSANTD2]] | -0.57 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[CENPL]] | -0.57 | -0.55 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises OSBPL9's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.646). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-1.7, -4.2); signed map (-29.9, -8.1). **Vector** length 117, 45.1% of its response variance represented; |z| ≥ 3 in 1,545 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +7.8 | +16.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +7.8 | +14.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.7 | +12.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +6.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.5 | +10.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.7 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.1 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -11.1 | -9.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.7 | -11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.5 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.4 | -6.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.3 | -5.1 |
|  | [[EX229 (drug)]] 5 µM |  | -6.1 | -4.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -5.8 | -4.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -5.8 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | oxysterol binding protein like 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p32.3 — chr1:51,577,179-51,798,427 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Oxysterol binding proteins; Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of bile acids and bile salts; Bile acid and bile salt metabolism; Metabolism of steroids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96SU4](https://www.uniprot.org/uniprotkb/Q96SU4) (Oxysterol-binding protein-related protein 9):

> Interacts with OSBPL11 to function as lipid transfer proteins. Together they form a heterodimer that localizes at the ER-trans-Golgi membrane contact sites, and exchanges phosphatidylserine (1,2-diacyl-sn-glycero-3-phospho-L-serine, PS) for phosphatidylinositol-4-phosphate (1,2-diacyl-sn-glycero-3-phospho-(1D-myo-inositol 4-phosphate), PI(4)P) between the two organelles, a step that is critical for sphingomyelin synthesis in the Golgi complex. Interacts with OSBPL10 to function as lipid …

**Summary**, from NCBI Gene [114883](https://www.ncbi.nlm.nih.gov/gene/114883):

> This gene encodes a member of the oxysterol-binding protein (OSBP) family, a group of intracellular lipid receptors. Most members contain an N-terminal pleckstrin homology domain and a highly conserved C-terminal OSBP-like sterol-binding domain, although some members contain only the sterol-binding domain. This family member functions as a cholesterol transfer protein that regulates Golgi structure and function. Multiple transcript variants, most of which encode distinct isoforms, have been …

**Accessions** — [HGNC:16386](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16386) · Entrez [114883](https://www.ncbi.nlm.nih.gov/gene/114883) · UniProt [Q96SU4](https://www.uniprot.org/uniprotkb/Q96SU4) · Ensembl [ENSG00000117859](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117859)

## Data

Gene col 3951: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3951); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3951, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3951]; `tensor/DDL_lfc|DDL_z.npy` [3951]; `embed/gene_vectors.npy` [3951]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3951 or target_col == 3951). Every well: [[OSBPL9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OSBPL9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
