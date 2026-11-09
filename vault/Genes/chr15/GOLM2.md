---
symbol: "GOLM2"
type: "gene"
col: 9348
ensembl_id: "ENSG00000166734"
name: "golgi membrane protein 2"
location: "15q15.3"
module: 12
arm: "-"
pooled_cpm: 180.26
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# GOLM2

*golgi membrane protein 2* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.94× (z +21.2, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.743× (z -9.5, q 1e-18, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GDE1]] (+0.59, fdr 3e-05), [[TMEM30A]] (+0.59, fdr 1e-05), [[EXT2]] (+0.58, fdr 2e-05); moves opposite to [[ZNF330]] (-0.62, fdr 1e-05), [[ZCCHC3]] (-0.57, fdr 4e-05), [[MED18]] (-0.57, fdr 5e-05).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRPM2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 7 with an alert ⚠; shown: the 15 strongest. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9348.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.94×** | +21.2 | 0e+00 | 47/48 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.83×** | +19.3 | 0e+00 | 46/48 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.81×** | +19.0 | 0e+00 | 45/48 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +17.8 | 0e+00 | 44/49 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +15.5 | 0e+00 | 38/44 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +10.8 | 2e-25 | 39/48 (NCI-H1792, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +9.9 | 3e-21 | 39/48 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.46×** | +9.8 | 7e-21 | 36/45 (A-427, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.72×** | +9.2 | 4e-18 | 41/49 (LoVo, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +6.9 | 3e-10 | 28/48 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +6.9 | 4e-10 | 28/48 (COLO 205, HepG2/C3A, …) | two highest doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.23×** | +6.6 | 2e-09 | 31/49 (RKO, SW480, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | 1.20× | +5.9 | 2e-07 | 23/48 (COLO 205, SW48, …) | two highest doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.41×** | +5.8 | 3e-07 | 28/49 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.09× | +4.1 | 0.002 | 4/48 (HEC-1-A, LoVo, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9348.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.743×** | -9.5 | 1e-18 | 28/48 (COLO 205, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **0.826×** | -8.6 | 2e-15 | 26/48 (COLO 205, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.931× | -7.6 | 6e-12 | 0/50 | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.820×** | -6.1 | 2e-07 | 25/47 (HT-29, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~1% of this change | 0.854× | -5.0 | 6e-05 | 17/48 (A498, LoVo, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.899× | -4.8 | 1e-04 | 6/49 (SK-MEL-2, NCI-H1573, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | 0.866× | -4.6 | 4e-04 | 14/48 (SW480, BT-474, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.828×** | -4.3 | 0.001 | 20/48 (SW 900, LoVo, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.879× | -4.1 | 0.002 | 10/48 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.881× | -4.0 | 0.003 | 7/48 (hTERT-HPNE, SNU-1, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 5 µM |  | **0.791×** | -3.9 | 0.005 | 22/46 (RKO, hTERT-HPNE, …) | rises with dose | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | 0.882× | -3.8 | 0.006 | 15/49 (A498, HOP62, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 0.846× | -3.8 | 0.006 | 17/48 (A-172, HS-578T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.894× | -3.6 | 0.015 | 8/48 (NCI-H1573, SK-MEL-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.895× | -3.5 | 0.016 | 13/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[venetoclax (drug)]] 5 µM |  | **0.813×** | -3.5 | 0.019 | 16/48 (NCI-H23, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.907× | -3.1 | 0.061 | 10/47 (NCI-H1573, SK-MEL-2, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.904× | -3.0 | 0.074 | 10/47 (LS 180, SW 900, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.910× | -3.0 | 0.075 | 8/48 (A498, LoVo, …) | all doses, stronger at high dose |  |
| [[Thymol (drug)]] 0.5 µM |  | 0.910× | -3.0 | 0.075 | 9/48 (RKO, NCI-H23, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9348. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 180 | 8 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.09× (z +16.3) | — |
| [[NCI-H1792 (line)]] | alt | 171 | 6 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +16.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.62× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.599× (z -11.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[A549 (line)]] | wt | 143 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.45× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.01× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 211 | 4 (1 ⚠) | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.17× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.3) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.505× (z -9.5) |
| [[HOP62 (line)]] | alt | 156 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.17× (z +12.0) | — |
| [[SNU-423 (line)]] | alt | 104 | 6 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.52× (z +12.2) | — |
| [[A-172 (line)]] | wt | 238 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.11× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 1.95× (z +12.1) | — |
| [[AsPC-1 (line)]] | alt | 120 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +13.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.26× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 169 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.25× (z +14.3) | — |
| [[LS 180 (line)]] | wt | 179 | 4 (1 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.93× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -13.4) ⚠ cell-cycle shift, explains ~14% of this change |
| [[MIA PaCa-2 (line)]] | alt | 123 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.21× (z +17.3) | — |
| [[NCI-H460 (line)]] | wt | 141 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.47× (z +15.9) | — |
| [[SW1417 (line)]] | alt | 174 | 4 (1 ⚠) | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 2.01× (z +12.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.597× (z -8.7) ⚠ toxic |
| [[SW480 (line)]] | alt | 155 | 4 (1 ⚠) | 1 | [[Panobinostat (drug)]] 5 µM 2.08× (z +14.9) | [[Auranofin (drug)]] 5 µM 0.581× (z -11.0) |
| [[COLO 205 (line)]] | alt | 260 | 1 | 3 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 1.91× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -23.2) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -17.5) |
| [[Hs 766T (line)]] | wt | 113 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.39× (z +11.4) | — |
| [[KATO III (line)]] | alt | 230 | 3 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.91× (z +9.9) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 1.84× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.560× (z -12.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[LoVo (line)]] | wt | 287 | 2 (1 ⚠) | 2 (1 ⚠) | [[Belinostat (drug)]] 5 µM 1.59× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -22.4) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.567× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 146 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.41× (z +14.6) | — |
| [[NCI-H1573 (line)]] | alt | 212 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +16.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.581× (z -11.8) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H2030 (line)]] | alt | 247 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 1.96× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.575× (z -12.6) ⚠ cell-cycle shift, explains ~14% of this change |
| [[RPMI-7951 (line)]] | alt | 219 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 1.92× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.615× (z -9.9) ⚠ cell-cycle shift, explains ~14% of this change |
| [[SK-MEL-2 (line)]] | alt | 177 | 4 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.16× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 2.05× (z +11.0) | — |
| [[A-427 (line)]] | wt | 157 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 2.65× (z +13.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -12.6) |
| [[A498 (line)]] | wt | 258 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 1.74× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.586× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 168 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.19× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.504× (z -12.5) ⚠ cell-cycle shift, explains ~14% of this change |
| [[J82 (line)]] | alt | 126 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 1.89× (z +10.2) | — |
| [[Panc 03.27 (line)]] | alt | 158 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 1.94× (z +9.2) | [[Homoharringtonine (drug)]] 0.5 µM 0.495× (z -9.8) |
| [[RKO (line)]] | wt | 198 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.23× (z +12.4) | — |
| [[BT-474 (line)]] | alt | 129 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.617× (z -9.1) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.525× (z -8.6) |
| [[C-33 A (line)]] | alt | 231 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 1.87× (z +9.9) | — |
| [[C32 (line)]] | wt | 151 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +10.4) | — |
| [[HS-578T (line)]] | alt | 189 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.87× (z +9.8) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 268 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.576× (z -12.2) ⚠ cell-cycle shift, explains ~14% of this change |
| [[NCI-H2347 (line)]] | alt | 108 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.99× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 171 | 2 | 0 | [[Belinostat (drug)]] 5 µM 1.86× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 268 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -13.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[HCT15 (line)]] | alt | 262 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 1.91× (z +9.2) | — |
| [[hTERT-HPNE (line)]] | wt | 194 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.04× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 161 | 1 | 0 | [[Belinostat (drug)]] 5 µM 1.78× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 206 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.35× (z +10.6) | — |
| [[SW 1088 (line)]] | alt | 186 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0956× (z -12.0) |
| [[SW 900 (line)]] | alt | 173 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.05× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 173 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 206 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 161 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9348), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*51 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GDE1]] | +0.59 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[TMEM30A]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[EXT2]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[UGGT1]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[TGOLN2]] | +0.58 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[ERP44]] | +0.58 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CAPZB]] | +0.57 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[CETN2]] | +0.56 | +0.51 / +0.31 | both halves | 2e-04 |  |
| [[MAPK9]] | +0.56 | +0.41 / +0.52 | both halves | 4e-05 |  |
| [[DNM1]] | +0.55 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[ABI2]] | +0.55 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ADAM10]] | +0.54 | +0.52 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*49 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF330]] | -0.62 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[ZCCHC3]] | -0.57 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[MED18]] | -0.57 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[MTG2]] | -0.56 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[ZNF525]] | -0.54 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[PBDC1]] | -0.54 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RRP8]] | -0.54 | -0.41 / -0.39 | both halves | 6e-05 |  |
| [[ZNF397]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[RPAP1]] | -0.53 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[WASHC1]] | -0.53 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[POLR1H]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[C11orf68]] | -0.53 | -0.38 / -0.53 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPM2]] | B | TRPM2 activity raises GOLM2's level | lines that do not express TRPM2 (11) vs lines expressing it (39) | 1.19× lower at baseline in the lines without TRPM2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000229195; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.363). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-27.5, 19.0); signed map (-29.9, -35.5). **Vector** length 134, 42.0% of its response variance represented; |z| ≥ 3 in 1,229 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.5 | +6.9 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.5 | +10.8 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +5.3 | +9.9 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.1 | +19.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.7 | +9.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +3.4 | +1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.0 | +0.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.6 | +6.6 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | -11.9 | -8.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -11.1 | -9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.6 | -6.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.8 | -4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -8.1 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.8 | -3.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -3.8 |
|  | [[vincristine (drug)]] 0.5 µM |  | -4.3 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | golgi membrane protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:44,288,719-44,415,758 (+) |
| Ensembl biotype | protein_coding |
| Also known as | H63, DKFZp459F1927; previously CASC4 |
| Matched by | ensembl_id |

UniProt [Q6P4E1](https://www.uniprot.org/uniprotkb/Q6P4E1) carries no function annotation.

**Summary**, from NCBI Gene [113201](https://www.ncbi.nlm.nih.gov/gene/113201):

> The increased expression level of this gene is associated with HER-2/neu proto-oncogene overexpression. Amplification and resulting overexpression of this proto-oncogene are found in approximately 30% of human breast and 20% of human ovarian cancers. Alternatively spliced variants encoding different isoforms have been identified for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:24892](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24892) · Entrez [113201](https://www.ncbi.nlm.nih.gov/gene/113201) · UniProt [Q6P4E1](https://www.uniprot.org/uniprotkb/Q6P4E1) · Ensembl [ENSG00000166734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166734)

## Data

Gene col 9348: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9348); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9348, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9348]; `tensor/DDL_lfc|DDL_z.npy` [9348]; `embed/gene_vectors.npy` [9348]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9348 or target_col == 9348). Every well: [[GOLM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
