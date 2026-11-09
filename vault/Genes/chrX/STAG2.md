---
symbol: "STAG2"
type: "gene"
col: 2196
ensembl_id: "ENSG00000101972"
name: "STAG2 cohesin complex component"
location: "Xq25"
module: 3
arm: "-"
pooled_cpm: 271.11
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 24
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# STAG2

*STAG2 cohesin complex component* — Xq25

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.49× (z +11.0, q 1e-25, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.241× (z -39.3, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BROX]] (+0.74, fdr 7e-06), [[HMGN2]] (+0.70, fdr 1e-05), [[PCM1]] (+0.69, fdr 7e-06); moves opposite to [[HMOX2]] (-0.70, fdr 7e-06), [[ANKS6]] (-0.62, fdr 3e-05), [[MPP3]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 003]] (mRNA 3'-end processing).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 8 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2196.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.49×** | +11.0 | 1e-25 | 41/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.26×** | +6.1 | 3e-07 | 27/48 (A498, A549, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | 1.17× | +6.0 | 3e-07 | 24/48 (A498, A549, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.24×** | +5.8 | 8e-07 | 28/47 (LoVo, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.22×** | +5.6 | 2e-06 | 26/48 (LoVo, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.21×** | +5.3 | 1e-05 | 24/49 (HS-578T, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.6 | 3e-04 | 22/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 1.15× | +3.7 | 0.014 | 19/44 (HS-578T, HEC-1-A, …) | two highest doses | composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.09× | +3.5 | 0.026 | 6/48 (PANC-1, HS-578T, …) | all doses, stronger at high dose | low cells (technical?) |
| [[TAK-901 (drug)]] 5 µM |  | **1.46×** | +3.2 | 0.066 | 20/49 (SK-MEL-2, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.08× | +3.2 | 0.069 | 0/48 | all doses, flat | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.16× | +3.2 | 0.069 | 9/48 (SW480, Hs 766T, …) | all doses, flat | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2196.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.241×** | -39.3 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.242×** | -39.1 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.288×** | -34.4 | 0e+00 | 48/48 (SW480, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.532×** | -17.4 | 0e+00 | 48/48 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.544×** | -16.2 | 0e+00 | 45/47 (NCI-H1573, KATO III, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.615×** | -13.4 | 4e-39 | 44/48 (CFPAC-1, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.728×** | -12.4 | 3e-33 | 44/48 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.663×** | -11.3 | 6e-28 | 43/48 (SNU-1, NCI-H2347, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.755×** | -7.7 | 7e-13 | 37/48 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.484×** | -6.2 | 4e-08 | 41/49 (SW480, SW 900, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **0.797×** | -6.0 | 1e-07 | 27/48 (NCI-H460, hTERT-HPNE, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.736×** | -5.9 | 1e-07 | 36/48 (HT-29, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | 0.861× | -5.8 | 3e-07 | 22/49 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.787×** | -5.0 | 2e-05 | 32/48 (BT-474, A549, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.778×** | -4.9 | 4e-05 | 29/48 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.799×** | -4.7 | 8e-05 | 31/49 (SK-MEL-2, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.576×** | -4.7 | 8e-05 | 30/48 (Hs 766T, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **0.789×** | -4.6 | 1e-04 | 35/49 (NCI-H460, A498, …) | two highest doses | plate-row cell shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.597×** | -4.4 | 3e-04 | 32/48 (Hs 766T, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **0.813×** | -4.3 | 4e-04 | 26/48 (HT-29, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.866× | -3.9 | 0.002 | 11/49 (NCI-H2347, SW 900, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.44 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2196. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 142 | 5 (5 ⚠) | 5 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.84× (z +18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.293× (z -17.7) |
| [[NCI-H460 (line)]] | wt | 336 | 1 | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.80× (z +9.2) | [[Panobinostat (drug)]] 5 µM 0.206× (z -24.9) |
| [[PANC-1 (line)]] | alt | 317 | 4 (3 ⚠) | 5 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.30× (z +16.2) | [[Panobinostat (drug)]] 5 µM 0.223× (z -29.1) |
| [[SW1417 (line)]] | alt | 307 | 1 | 8 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.60× (z +8.6) | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -27.6) |
| [[A498 (line)]] | wt | 271 | 2 (2 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +18.5) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -22.1) |
| [[CFPAC-1 (line)]] | alt | 264 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.183× (z -30.2) |
| [[HEC-1-A (line)]] | alt | 231 | 2 (2 ⚠) | 6 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 1.81× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Belinostat (drug)]] 5 µM 0.287× (z -23.6) |
| [[LoVo (line)]] | wt | 189 | 5 (3 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.51× (z +17.0) | [[Panobinostat (drug)]] 5 µM 0.343× (z -19.7) |
| [[NCI-H2347 (line)]] | alt | 333 | 1 (1 ⚠) | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.61× (z +12.8) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 0.5 µM 0.250× (z -26.4) |
| [[SW480 (line)]] | alt | 400 | 1 | 7 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.53× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.141× (z -40.6) |
| [[AsPC-1 (line)]] | alt | 373 | 0 | 7 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -28.0) |
| [[HOP62 (line)]] | alt | 270 | 1 | 6 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.70× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -28.8) |
| [[NCI-H1573 (line)]] | alt | 243 | 1 | 6 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.82× (z +10.2) | [[Panobinostat (drug)]] 5 µM 0.157× (z -31.6) |
| [[NCI-H1792 (line)]] | alt | 240 | 1 (1 ⚠) | 6 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 1.81× (z +8.6) ⚠ cell-cycle shift, explains ~20% of this change | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -28.2) |
| [[NCI-H2030 (line)]] | alt | 264 | 1 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.67× (z +12.0) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 5 µM 0.258× (z -22.5) |
| [[SW 900 (line)]] | alt | 195 | 0 | 7 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -27.9) |
| [[A549 (line)]] | wt | 218 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +18.1) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 5 µM 0.232× (z -24.6) |
| [[BT-474 (line)]] | alt | 155 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.196× (z -23.9) |
| [[COLO 205 (line)]] | alt | 276 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -26.6) |
| [[HepG2_C3A (line)]] | wt | 172 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -21.4) |
| [[HT-29 (line)]] | alt | 258 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.253× (z -24.9) |
| [[hTERT-HPNE (line)]] | wt | 182 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -21.5) |
| [[J82 (line)]] | alt | 294 | 2 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +15.5) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.93× (z +10.5) | [[Panobinostat (drug)]] 5 µM 0.285× (z -19.8) |
| [[NCI-H23 (line)]] | alt | 345 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -28.7) |
| [[Panc 03.27 (line)]] | alt | 294 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -35.5) |
| [[SK-MEL-2 (line)]] | alt | 305 | 1 (1 ⚠) | 5 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +14.7) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 0.5 µM 0.212× (z -28.1) |
| [[SNU-423 (line)]] | alt | 506 | 0 | 6 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.175× (z -25.6) |
| [[A-172 (line)]] | wt | 111 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +12.5) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 5 µM 0.225× (z -22.2) |
| [[A-427 (line)]] | wt | 311 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -26.4) |
| [[KATO III (line)]] | alt | 291 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.06× (z +12.4) | [[Panobinostat (drug)]] 5 µM 0.253× (z -23.5) |
| [[LS 180 (line)]] | wt | 224 | 1 | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.87× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.302× (z -17.4) |
| [[MIA PaCa-2 (line)]] | alt | 403 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -26.8) |
| [[SNU-1 (line)]] | wt | 273 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -17.7) |
| [[C32 (line)]] | wt | 191 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -21.8) |
| [[CHP-212 (line)]] | wt | 210 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.201× (z -15.0) |
| [[H4 (line)]] | wt | 162 | 1 | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.62× (z +9.0) | [[Panobinostat (drug)]] 5 µM 0.200× (z -14.9) |
| [[Hs 766T (line)]] | wt | 304 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.251× (z -20.7) |
| [[RKO (line)]] | wt | 272 | 1 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.0) ⚠ cell-cycle shift, explains ~62% of this change | [[Panobinostat (drug)]] 0.5 µM 0.353× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 208 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.220× (z -21.6) |
| [[SHP-77 (line)]] | alt | 159 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.283× (z -17.7) |
| [[SW48 (line)]] | wt | 227 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.266× (z -16.5) |
| [[AN3 CA (line)]] | alt | 313 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.309× (z -12.3) |
| [[C-33 A (line)]] | alt | 199 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.215× (z -21.2) |
| [[HCT15 (line)]] | alt | 256 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.281× (z -17.0) |
| [[LOX-IMVI (line)]] | wt | 80.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.301× (z -12.5) |
| [[SW 1088 (line)]] | alt | 239 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.154× (z -10.0) |
| [[NCI-H661 (line)]] | alt | 598 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.319× (z -9.7) |
| [[SW 1271 (line)]] | alt | 183 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -8.7) |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 253 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2196), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*54 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BROX]] | +0.74 | +0.59 / +0.77 | both halves | 7e-06 |  |
| [[HMGN2]] | +0.70 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[PCM1]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 | pathway: Mitotic Prometaphase |
| [[FMR1]] | +0.66 | +0.50 / +0.66 | both halves | 1e-05 |  |
| [[SF3B1]] | +0.63 | +0.46 / +0.73 | both halves | 2e-05 | same gene group; STRING 469 |
| [[CUL4B]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[HSD17B11]] | +0.61 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[PRKAR1A]] | +0.61 | +0.39 / +0.63 | both halves | 5e-05 |  |
| [[CHD3]] | +0.60 | +0.44 / +0.57 | both halves | 3e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[MATR3]] | +0.60 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[SUCLG2-DT]] | +0.59 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[ATRX]] | +0.59 | +0.37 / +0.58 | both halves | 8e-05 | STRING 730 |

## Genes that move opposite

*46 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMOX2]] | -0.70 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[ANKS6]] | -0.62 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[MPP3]] | -0.60 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[RABGEF1P1]] | -0.60 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[CSNK1E]] | -0.60 | -0.38 / -0.48 | both halves | 7e-05 | pathway: Mitotic Prometaphase |
| [[LPCAT1]] | -0.59 | -0.34 / -0.53 | both halves | 1e-04 |  |
| [[RBAK-RBAKDN]] | -0.59 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[ZNF544]] | -0.58 | -0.43 / -0.60 | both halves | 3e-05 |  |
| [[ABCC10]] | -0.58 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[NLK]] | -0.57 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[TMEM184B]] | -0.57 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[POLR3A]] | -0.57 | -0.42 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **-** arm (projection on the module's main direction -0.502). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-2.9, 0.8); signed map (16.2, -35.3). **Vector** length 130, 47.9% of its response variance represented; |z| ≥ 3 in 1,313 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.3 | +5.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +10.2 | +3.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | +7.8 | +6.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +7.6 | +0.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.6 | +3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +4.5 | +2.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.2 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | -0.1 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +3.3 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.1 | +1.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.8 | -11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | -7.0 | -16.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -13.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -12.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -5.4 | -17.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.0 | -2.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -5.0 | -4.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -4.6 | -5.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.5 | -4.7 |

## What is on record

|  |  |
|---|---|
| Name | STAG2 cohesin complex component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq25 — chrX:123,960,212-124,422,664 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SA-2, SCC3B, SA2 |
| Gene groups (HGNC) | Cohesin complex; Armadillo like helical domain containing; STAG family |
| Reactome | 21 pathways, smallest: Cohesin Loading onto Chromatin; Establishment of Sister Chromatid Cohesion; Mitotic Telophase/Cytokinesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N3U4](https://www.uniprot.org/uniprotkb/Q8N3U4) (Cohesin subunit SA-2):

> Component of cohesin complex, a complex required for the cohesion of sister chromatids after DNA replication. The cohesin complex apparently forms a large proteinaceous ring within which sister chromatids can be trapped. At anaphase, the complex is cleaved and dissociates from chromatin, allowing sister chromatids to segregate. The cohesin complex may also play a role in spindle pole assembly during mitosis.

**Summary**, from NCBI Gene [10735](https://www.ncbi.nlm.nih.gov/gene/10735):

> The protein encoded by this gene is a subunit of the cohesin complex, which regulates the separation of sister chromatids during cell division. Targeted inactivation of this gene results in chromatid cohesion defects and aneuploidy, suggesting that genetic disruption of cohesin is a cause of aneuploidy in human cancer. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2013]

**Accessions** — [HGNC:11355](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11355) · Entrez [10735](https://www.ncbi.nlm.nih.gov/gene/10735) · UniProt [Q8N3U4](https://www.uniprot.org/uniprotkb/Q8N3U4) · Ensembl [ENSG00000101972](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101972)

## Data

Gene col 2196: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2196); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2196, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2196]; `tensor/DDL_lfc|DDL_z.npy` [2196]; `embed/gene_vectors.npy` [2196]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2196 or target_col == 2196). Every well: [[STAG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/STAG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
