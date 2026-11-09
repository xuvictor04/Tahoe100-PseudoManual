---
symbol: "GSK3B"
type: "gene"
col: 1354
ensembl_id: "ENSG00000082701"
name: "glycogen synthase kinase 3 beta"
location: "3q13.33"
module: 86
arm: "+"
pooled_cpm: 364.36
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# GSK3B

*glycogen synthase kinase 3 beta* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.12× (z +14.7, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.394× (z -17.8, q 0e+00, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.726× (z -9.0, q 3e-17, down in 37 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAND3]] (+0.60, fdr 7e-06), [[LDLR]] (+0.52, fdr 5e-05), [[GDF11]] (+0.52, fdr 2e-04); moves opposite to [[TXNL4B]] (-0.55, fdr 3e-05), [[ZNF550]] (-0.52, fdr 4e-05), [[POLE3]] (-0.45, fdr 4e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1354.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.12×** | +14.7 | 0e+00 | 49/49 (Hs 766T, C32, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +8.7 | 8e-16 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.3 | 4e-11 | 41/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +6.7 | 2e-09 | 37/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.86×** | +6.4 | 2e-08 | 44/48 (C32, SW48, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +5.9 | 4e-07 | 35/47 (HOP62, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +5.7 | 8e-07 | 26/48 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +4.6 | 3e-04 | 30/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.24×** | +4.3 | 0.001 | 29/48 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.25×** | +4.2 | 0.002 | 30/48 (SW480, HOP62, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.42×** | +3.7 | 0.013 | 29/48 (C32, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.5 | 0.025 | 21/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 1.19× | +3.4 | 0.025 | 23/48 (SNU-1, LoVo, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.19× | +3.2 | 0.048 | 21/47 (C32, HOP62, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.063 | 17/48 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.11× | +3.0 | 0.089 | 7/48 (NCI-H23, HT-29, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.089 | 21/47 (SNU-423, H4, …) | rises with dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1354.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -17.8 | 0e+00 | 43/44 (HCT15, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.420×** | -17.2 | 0e+00 | 48/49 (HCT15, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.459×** | -14.3 | 8e-44 | 42/45 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -9.3 | 1e-18 | 41/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.726×** | -9.0 | 3e-17 | 37/49 (A549, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.690×** | -7.3 | 2e-11 | 44/48 (H4, SW 1271, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -7.3 | 3e-11 | 39/48 (NCI-H2030, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.685×** | -7.2 | 4e-11 | 39/50 (NCI-H2347, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.726×** | -6.4 | 1e-08 | 40/48 (NCI-H23, SK-MEL-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.769×** | -5.2 | 1e-05 | 30/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.783×** | -4.8 | 7e-05 | 29/48 (HEC-1-A, NCI-H1792, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.789×** | -4.7 | 1e-04 | 29/48 (NCI-H2030, NCI-H1573, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.796×** | -4.5 | 3e-04 | 28/48 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.804×** | -4.2 | 0.001 | 29/48 (NCI-H1792, LS 180, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.707×** | -3.6 | 0.013 | 29/49 (LOX-IMVI, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **0.833×** | -3.5 | 0.017 | 24/49 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.760×** | -3.5 | 0.017 | 28/48 (HS-578T, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.776×** | -3.2 | 0.040 | 28/47 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.785×** | -3.1 | 0.060 | 25/48 (C32, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.860× | -3.0 | 0.071 | 22/48 (C32, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1354. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 339 | 8 (4 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.13× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -12.2) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 183 | 7 (2 ⚠) | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.71× (z +13.1) | [[Dinaciclib (drug)]] 0.5 µM 0.504× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.661× (z -9.5) |
| [[SW480 (line)]] | alt | 282 | 7 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.20× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.372× (z -17.6) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 367 | 0 | 9 (6 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.291× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.453× (z -13.8) |
| [[HEC-1-A (line)]] | alt | 389 | 2 | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.443× (z -13.1) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 271 | 5 (1 ⚠) | 3 (3 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.12× (z +12.1) ⚠ toxic · without an alert: [[TAK-901 (drug)]] 5 µM 3.30× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.427× (z -13.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 410 | 1 | 7 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.13× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.242× (z -21.2) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.509× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 827 | 1 | 7 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 5.51× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -15.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.455× (z -11.4) |
| [[J82 (line)]] | alt | 501 | 2 (1 ⚠) | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.08× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -16.3) |
| [[KATO III (line)]] | alt | 347 | 0 | 7 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.266× (z -18.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.536× (z -8.9) |
| [[NCI-H2347 (line)]] | alt | 405 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.92× (z +13.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.376× (z -14.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -13.3) |
| [[SNU-423 (line)]] | alt | 321 | 4 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.33× (z +14.2) | [[Dinaciclib (drug)]] 5 µM 0.380× (z -13.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 243 | 3 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.55× (z +19.0) | [[Dinaciclib (drug)]] 5 µM 0.425× (z -11.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 518 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 13.0× (z +17.5) | [[Dinaciclib (drug)]] 0.5 µM 0.268× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.539× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 469 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.54× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -17.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -10.8) |
| [[HS-578T (line)]] | alt | 481 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.55× (z +9.5) | [[Dinaciclib (drug)]] 0.5 µM 0.359× (z -14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.576× (z -11.2) |
| [[HT-29 (line)]] | alt | 535 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.614× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 467 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 7.31× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.461× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 259 | 1 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 3.79× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.541× (z -12.7) |
| [[RKO (line)]] | wt | 339 | 3 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.07× (z +10.4) | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -18.2) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 218 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 11.4× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.520× (z -8.7) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 324 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.97× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.381× (z -14.6) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 435 | 1 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 5.21× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.318× (z -15.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 316 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.27× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -21.1) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 578 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.25× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.260× (z -19.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 330 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 5.44× (z +12.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 282 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.97× (z +11.2) | [[Dinaciclib (drug)]] 0.5 µM 0.416× (z -10.5) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 288 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 4.39× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.339× (z -13.0) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 416 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.51× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.230× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.422× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 402 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.68× (z +9.0) | [[Dinaciclib (drug)]] 0.5 µM 0.387× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 212 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.04× (z +11.2) | — |
| [[SW48 (line)]] | wt | 418 | 3 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 9.23× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -18.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 474 | 2 | 1 | [[TAK-901 (drug)]] 5 µM 5.38× (z +11.6) | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.421× (z -11.4) |
| [[COLO 205 (line)]] | alt | 364 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.48× (z +9.9) | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -12.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 356 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -12.7) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 252 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.63× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.427× (z -10.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 426 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -15.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 205 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.354× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.561× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 311 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 5.89× (z +13.6) | [[Auranofin (drug)]] 5 µM 0.506× (z -10.0) |
| [[SW1417 (line)]] | alt | 403 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.407× (z -14.0) ⚠ toxic |
| [[C-33 A (line)]] | alt | 320 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.327× (z -14.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 370 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -23.2) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 422 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.94× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.155× (z -20.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 423 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.154× (z -14.0) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 273 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -11.2) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 293 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 378 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 382 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 277 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 259 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1354), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND3]] | +0.60 | +0.59 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[LDLR]] | +0.52 | +0.55 / +0.39 | both halves | 5e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GDF11]] | +0.52 | +0.30 / +0.39 | both halves | 2e-04 |  |
| [[LIPG]] | +0.51 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[NR6A1]] | +0.51 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[STK3]] | +0.51 | +0.43 / +0.42 | both halves | 4e-05 |  |
| [[ACSL3]] | +0.50 | +0.47 / +0.42 | both halves | 4e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[DHCR7]] | +0.50 | +0.44 / +0.50 | both halves | 3e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[STAU2]] | +0.50 | +0.30 / +0.43 | both halves | 2e-04 |  |
| [[PTK2]] | +0.48 | +0.56 / +0.45 | both halves | 3e-05 | STRING 656 |
| [[DHCR24]] | +0.47 | +0.48 / +0.40 | both halves | 5e-05 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[LRBA]] | +0.47 | +0.48 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNL4B]] | -0.55 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[ZNF550]] | -0.52 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[POLE3]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 | pathway: S Phase |
| [[TGDS]] | -0.44 | -0.45 / -0.37 | both halves | 8e-05 |  |
| [[C8orf33]] | -0.44 | -0.56 / -0.27 | both halves | 3e-04 |  |
| [[PPP1R8]] | -0.43 | -0.59 / -0.28 | both halves | 3e-04 |  |
| [[SMYD5]] | -0.43 | -0.54 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[BLOC1S5-TXNDC5]] | -0.42 | -0.31 / -0.21 | both halves | 7e-04 |  |
| [[NUP133]] | -0.41 | -0.40 / -0.36 | both halves | 1e-04 | pathway: Cell Cycle Checkpoints |
| [[ZNF25]] | -0.41 | -0.35 / -0.32 | both halves | 2e-04 |  |
| [[CEP44]] | -0.41 | -0.33 / -0.41 | both halves | 1e-04 |  |
| [[RBM48]] | -0.41 | -0.47 / -0.39 | both halves | 5e-05 |  |
| [[AARSD1]] | -0.41 | -0.45 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.492). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.7, -47.6); signed map (-17.1, 31.1). **Vector** length 90.8, 35.1% of its response variance represented; |z| ≥ 3 in 1,492 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.0 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +1.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.3 | +14.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +4.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.1 | -17.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.8 | +3.0 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.6 | +2.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[EX229 (drug)]] 5 µM |  | +3.2 | +2.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -5.0 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.7 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.3 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -2.4 | -9.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.9 | -1.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | glycogen synthase kinase 3 beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:119,821,321-120,094,994 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Glycogen synthase kinase 3 family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING, MTORC1_SIGNALING |
| Reactome | 70 pathways, smallest: Maturation of nucleoprotein_9683610; AKT phosphorylates targets in the cytosol; APC truncation mutants have impaired AXIN binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P49841](https://www.uniprot.org/uniprotkb/P49841) (Glycogen synthase kinase-3 beta):

> Constitutively active protein kinase that acts as a negative regulator in the hormonal control of glucose homeostasis, Wnt signaling and regulation of transcription factors and microtubules, by phosphorylating and inactivating glycogen synthase (GYS1 or GYS2), EIF2B, CTNNB1/beta-catenin, APC, AXIN1, DPYSL2/CRMP2, JUN, NFATC1/NFATC, MAPT/TAU and MACF1. Requires primed phosphorylation of the majority of its substrates. In skeletal muscle, contributes to insulin regulation of glycogen synthesis by …

**Summary**, from NCBI Gene [2932](https://www.ncbi.nlm.nih.gov/gene/2932):

> The protein encoded by this gene is a serine-threonine kinase belonging to the glycogen synthase kinase subfamily. It is a negative regulator of glucose homeostasis and is involved in energy metabolism, inflammation, ER-stress, mitochondrial dysfunction, and apoptotic pathways. Defects in this gene have been associated with Parkinson disease and Alzheimer disease. [provided by RefSeq, Aug 2017]

**Accessions** — [HGNC:4617](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4617) · Entrez [2932](https://www.ncbi.nlm.nih.gov/gene/2932) · UniProt [P49841](https://www.uniprot.org/uniprotkb/P49841) · Ensembl [ENSG00000082701](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000082701)

## Data

Gene col 1354: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1354); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1354, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1354]; `tensor/DDL_lfc|DDL_z.npy` [1354]; `embed/gene_vectors.npy` [1354]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1354 or target_col == 1354). Every well: [[GSK3B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GSK3B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
