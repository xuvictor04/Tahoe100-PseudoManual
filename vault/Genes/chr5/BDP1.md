---
symbol: "BDP1"
type: "gene"
col: 7019
ensembl_id: "ENSG00000145734"
name: "BDP1 general transcription factor IIIB subunit"
location: "5q13.2"
module: 12
arm: "+"
pooled_cpm: 265.99
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 13
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# BDP1

*BDP1 general transcription factor IIIB subunit* — 5q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.42× (z +37.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.779× (z -10.5, q 5e-23, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESF1]] (+0.71, fdr 7e-06), [[PPIG]] (+0.70, fdr 7e-06), [[SNW1]] (+0.69, fdr 7e-06); moves opposite to [[TECR]] (-0.58, fdr 1e-05), [[FKBP1A]] (-0.56, fdr 3e-05), [[ITM2C]] (-0.55, fdr 2e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TPTE]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7019.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.42×** | +37.2 | 0e+00 | 48/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.25×** | +24.2 | 0e+00 | 48/48 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.12×** | +21.6 | 0e+00 | 47/48 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.70×** | +15.9 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.61×** | +14.2 | 9e-44 | 47/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.46×** | +11.4 | 6e-28 | 44/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~17% of this change | **1.28×** | +7.5 | 7e-12 | 31/48 (SW480, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +6.6 | 2e-09 | 33/48 (NCI-H2347, SW 900, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.22×** | +6.0 | 1e-07 | 25/48 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +5.8 | 3e-07 | 29/48 (SW480, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +5.0 | 2e-05 | 23/48 (LOX-IMVI, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.19× | +4.9 | 4e-05 | 21/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[EX229 (drug)]] 5 µM |  | **1.37×** | +4.9 | 4e-05 | 35/48 (AsPC-1, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.17× | +4.6 | 1e-04 | 20/48 (SW480, LoVo, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 27/48 (NCI-H1792, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.003 | 29/48 (Hs 766T, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.14× | +3.9 | 0.003 | 9/48 (SW480, HCT15, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 23/48 (AsPC-1, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.26×** | +3.6 | 0.010 | 20/48 (AsPC-1, SW 900, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | 1.18× | +3.5 | 0.016 | 14/48 (NCI-H460, SW 900, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7019.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.779×** | -10.5 | 5e-23 | 35/48 (SW480, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.741×** | -8.9 | 1e-16 | 39/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.746×** | -8.7 | 6e-16 | 38/49 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.818×** | -8.4 | 5e-15 | 24/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **0.761×** | -8.1 | 6e-14 | 32/48 (MIA PaCa-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.773×** | -7.6 | 2e-12 | 34/48 (A498, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -7.4 | 2e-11 | 1/50 (SW 1271) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.803×** | -6.5 | 6e-09 | 24/48 (A-172, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.837× | -5.3 | 9e-06 | 22/49 (A-172, A498, …) | all doses, stronger at high dose | composition shift |
| [[Thymol (drug)]] 0.5 µM |  | 0.861× | -4.4 | 5e-04 | 19/48 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | 0.858× | -4.4 | 7e-04 | 18/47 (MIA PaCa-2, CHP-212, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.864× | -4.1 | 0.002 | 21/44 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | composition shift |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.877× | -3.9 | 0.005 | 9/48 (CHP-212, SW480, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.781×** | -3.8 | 0.005 | 22/49 (A498, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **0.786×** | -3.7 | 0.007 | 23/45 (PANC-1, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | 0.883× | -3.7 | 0.008 | 16/48 (A-172, SNU-423, …) | top dose only |  |
| [[Decitabine (drug)]] 0.05 µM |  | 0.888× | -3.2 | 0.039 | 9/47 (HEC-1-A, CHP-212, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7019. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 257 | 4 | 8 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +20.9) | [[Niclosamide (olamine) (drug)]] 5 µM 0.538× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~62% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.555× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 380 | 5 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +14.8) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.497× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~25% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.538× (z -11.2) |
| [[SW480 (line)]] | alt | 329 | 9 (3 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +32.5) | [[Tucidinostat (drug)]] 0.5 µM 0.666× (z -9.0) |
| [[A498 (line)]] | wt | 289 | 5 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +27.9) | [[Panobinostat (drug)]] 0.5 µM 0.527× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 303 | 5 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +21.6) | [[Panobinostat (drug)]] 0.5 µM 0.569× (z -11.5) |
| [[LoVo (line)]] | wt | 302 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +23.9) | — |
| [[NCI-H2347 (line)]] | alt | 334 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +25.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.636× (z -12.8) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Tucidinostat (drug)]] 0.5 µM 0.631× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 268 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +28.2) | — |
| [[SW48 (line)]] | wt | 307 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +19.9) | — |
| [[A549 (line)]] | wt | 296 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +27.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.652× (z -10.0) ⚠ cell-cycle shift, explains ~8% of this change |
| [[CFPAC-1 (line)]] | alt | 291 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +22.7) | [[Panobinostat (drug)]] 5 µM 0.596× (z -9.6) |
| [[COLO 205 (line)]] | alt | 194 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +25.5) | — |
| [[HOP62 (line)]] | alt | 264 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.539× (z -10.7) |
| [[LS 180 (line)]] | wt | 239 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +25.1) | — |
| [[NCI-H1573 (line)]] | alt | 273 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +34.5) | [[Dinaciclib (drug)]] 5 µM 0.580× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 254 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +22.0) | [[Dinaciclib (drug)]] 5 µM 0.296× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 270 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +28.9) | — |
| [[SNU-423 (line)]] | alt | 233 | 3 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.12× (z +18.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.657× (z -10.3) ⚠ cell-cycle shift, explains ~8% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.662× (z -10.1) |
| [[A-427 (line)]] | wt | 298 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +14.6) | — |
| [[AsPC-1 (line)]] | alt | 260 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +26.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -15.1) ⚠ cell-cycle shift, explains ~8% of this change |
| [[C-33 A (line)]] | alt | 286 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +14.9) | — |
| [[C32 (line)]] | wt | 213 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +23.4) | — |
| [[HepG2_C3A (line)]] | wt | 169 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +15.8) | — |
| [[HS-578T (line)]] | alt | 185 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +16.4) | [[Tucidinostat (drug)]] 5 µM 0.646× (z -9.8) |
| [[LOX-IMVI (line)]] | wt | 238 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +22.1) | — |
| [[NCI-H1792 (line)]] | alt | 224 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +23.9) | — |
| [[Panc 03.27 (line)]] | alt | 320 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +13.9) | [[Panobinostat (drug)]] 0.5 µM 0.596× (z -9.5) |
| [[RKO (line)]] | wt | 260 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +23.5) | — |
| [[SW 900 (line)]] | alt | 296 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +23.0) | — |
| [[HCT15 (line)]] | alt | 344 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +16.9) | — |
| [[HT-29 (line)]] | alt | 178 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +32.4) | — |
| [[hTERT-HPNE (line)]] | wt | 202 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +18.0) | — |
| [[J82 (line)]] | alt | 235 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +16.3) | [[Dinaciclib (drug)]] 5 µM 0.593× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 181 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +21.9) | — |
| [[SK-MEL-2 (line)]] | alt | 201 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +22.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -9.9) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SNU-1 (line)]] | wt | 289 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 221 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +20.3) | — |
| [[CHP-212 (line)]] | wt | 264 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.99× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 296 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +23.4) | — |
| [[RPMI-7951 (line)]] | alt | 216 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.93× (z +14.0) | — |
| [[SW1417 (line)]] | alt | 175 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +18.2) | — |
| [[AN3 CA (line)]] | alt | 330 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +8.9) | — |
| [[H4 (line)]] | wt | 269 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +17.4) | — |
| [[Hs 766T (line)]] | wt | 179 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +11.5) | — |
| [[SHP-77 (line)]] | alt | 308 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +12.4) | — |
| [[NCI-H2122 (line)]] | alt | 247 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 257 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 356 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 442 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7019), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESF1]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[PPIG]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |
| [[SNW1]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[CCAR1]] | +0.69 | +0.65 / +0.77 | both halves | 7e-06 |  |
| [[UPF3B]] | +0.68 | +0.76 / +0.54 | both halves | 1e-05 |  |
| [[NSRP1]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[TRIP11]] | +0.68 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[C1orf131]] | +0.66 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.66 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[ZC3H13]] | +0.66 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[CCDC137]] | +0.66 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CCDC43]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TECR]] | -0.58 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[FKBP1A]] | -0.56 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[ITM2C]] | -0.55 | -0.59 / -0.46 | both halves | 2e-05 |  |
| [[LAPTM4A]] | -0.55 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[BRK1]] | -0.55 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[TMEM248]] | -0.54 | -0.66 / -0.42 | both halves | 4e-05 |  |
| [[ILRUN]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[PGAM1]] | -0.54 | -0.59 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TPTE]] | B | TPTE activity lowers BDP1's level | lines that do not express TPTE (35) vs lines expressing it (15) | 1.13× higher at baseline in the lines without TPTE | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: BAGE2, ENSG00000291025, ANKRD20A8P |
| [[TP53I11]] | B | TP53I11 activity raises BDP1's level | lines that do not express TP53I11 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without TP53I11 | 0.060 | ⚠ within organs, on part of the lines |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BDP1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises BDP1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GPX3]] | B | GPX3 activity lowers BDP1's level | lines that do not express GPX3 (26) vs lines expressing it (24) | 1.05× higher at baseline in the lines without GPX3 | 0.097 | ⚠ within organs, on part of the lines; also absent: LINC02057, KYNU, C3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.583). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-36.5, 2.0); signed map (1.9, -15.8). **Vector** length 137, 48.0% of its response variance represented; |z| ≥ 3 in 1,282 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.6 | +24.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +9.7 | +14.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +9.3 | +15.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.9 | +37.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +21.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +5.5 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.6 | +4.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.8 | +1.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.6 | +3.9 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.8 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.4 | -3.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -7.0 | -0.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.6 | -8.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -5.7 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.6 | -0.6 |
|  | [[Lopinavir (drug)]] 5 µM |  | -3.1 | -2.5 |
|  | [[Clonidine (hydrochloride) (drug)]] 5 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | BDP1 general transcription factor IIIB subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q13.2 — chr5:71,455,651-71,567,820 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TFC5, KIAA1241, KIAA1689, HSA238520, TFIIIB150; previously TFNR, TAF3B1 |
| Gene groups (HGNC) | Myb/SANT domain containing; General transcription factor IIIB complex subunits |
| Reactome | 6 pathways, smallest: RNA Polymerase III Transcription Initiation From Type 2 Promoter; RNA Polymerase III Transcription Initiation From Type 1 Promoter; RNA Polymerase III Transcription Initiation From Type 3 Promoter |
| Matched by | ensembl_id |

**Function**, from UniProt [A6H8Y1](https://www.uniprot.org/uniprotkb/A6H8Y1) (Transcription factor TFIIIB component B'' homolog):

> General activator of RNA polymerase III transcription. Requires for transcription from all three types of polymerase III promoters. Requires for transcription of genes with internal promoter elements and with promoter elements upstream of the initiation site.

**Summary**, from NCBI Gene [55814](https://www.ncbi.nlm.nih.gov/gene/55814):

> The product of this gene is a subunit of the TFIIIB transcription initiation complex, which recruits RNA polymerase III to target promoters in order to initiate transcription. The encoded protein localizes to concentrated aggregates in the nucleus, and is required for transcription from all three types of polymerase III promoters. It is phosphorylated by casein kinase II during mitosis, resulting in its release from chromatin and suppression of polymerase III transcription. [provided by RefSeq, …

**Accessions** — [HGNC:13652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13652) · Entrez [55814](https://www.ncbi.nlm.nih.gov/gene/55814) · UniProt [A6H8Y1](https://www.uniprot.org/uniprotkb/A6H8Y1) · Ensembl [ENSG00000145734](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145734)

## Data

Gene col 7019: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7019); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7019, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7019]; `tensor/DDL_lfc|DDL_z.npy` [7019]; `embed/gene_vectors.npy` [7019]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7019 or target_col == 7019). Every well: [[BDP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BDP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
