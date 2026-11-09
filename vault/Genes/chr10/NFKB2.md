---
symbol: "NFKB2"
type: "gene"
col: 1175
ensembl_id: "ENSG00000077150"
name: "nuclear factor kappa B subunit 2"
location: "10q24.32"
module: 14
arm: "+"
pooled_cpm: 70.01
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 18
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# NFKB2

*nuclear factor kappa B subunit 2* — 10q24.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 7.94× (z +45.8, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.566× (z -8.9, q 3e-16, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NR1D1]] (+0.71, fdr 7e-06), [[BCL3]] (+0.71, fdr 7e-06), [[HCP5]] (+0.68, fdr 1e-05); moves opposite to [[CDC123]] (-0.63, fdr 1e-05), [[COP1]] (-0.62, fdr 1e-05), [[ZFYVE9]] (-0.61, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HLA-F]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1175.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **7.94×** | +45.8 | 0e+00 | 48/48 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **7.01×** | +29.3 | 0e+00 | 48/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **4.07×** | +22.0 | 0e+00 | 48/48 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.34×** | +13.3 | 3e-38 | 42/48 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.29×** | +13.0 | 2e-36 | 41/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.84×** | +9.5 | 2e-19 | 36/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.59×** | +7.3 | 3e-11 | 34/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.49×** | +6.2 | 4e-08 | 34/48 (NCI-H460, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.29×** | +5.6 | 2e-06 | 30/48 (NCI-H2347, RKO, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **1.95×** | +5.5 | 3e-06 | 30/49 (PANC-1, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.1 | 2e-05 | 26/47 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 0.05 µM |  | **1.26×** | +3.7 | 0.012 | 21/49 (SW1417, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.017 | 19/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM |  | **1.28×** | +3.5 | 0.018 | 23/48 (SW48, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | **1.24×** | +3.4 | 0.024 | 22/48 (A-172, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.063 | 17/48 (NCI-H2347, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.084 | 18/48 (NCI-H2347, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1175.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.566×** | -8.9 | 3e-16 | 37/48 (HOP62, SW48, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.471×** | -6.2 | 2e-07 | 31/45 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Bisoprolol (hemifumarate) (drug)]] 5 µM |  | **0.666×** | -6.1 | 2e-07 | 45/47 (A549, NCI-H1792, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.715×** | -5.1 | 6e-05 | 26/42 (Hs 766T, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.728×** | -4.7 | 3e-04 | 27/48 (SW 900, PANC-1, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.583×** | -4.4 | 9e-04 | 31/47 (SW48, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.769×** | -4.1 | 0.003 | 22/48 (NCI-H460, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Ivabradine (hydrochloride) (drug)]] 5 µM | ⚠ unreliable plate only | **0.781×** | -3.9 | 0.007 | 30/48 (C-33 A, RPMI-7951, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.782×** | -3.9 | 0.007 | 23/48 (NCI-H460, A549, …) | all doses, flat | position effect removed |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.787×** | -3.8 | 0.009 | 22/48 (SW 900, A-172, …) | inconsistent across doses | position effect removed |
| [[Allantoin (drug)]] 5 µM |  | 0.846× | -3.7 | 0.011 | 16/48 (BT-474, RPMI-7951, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.791×** | -3.7 | 0.011 | 22/48 (PANC-1, H4, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.808×** | -3.3 | 0.035 | 24/48 (NCI-H23, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.809×** | -3.3 | 0.035 | 10/48 (NCI-H460, SW1417, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.940× | -3.3 | 0.038 | 1/49 (SW 1271) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.815×** | -3.2 | 0.047 | 21/48 (H4, PANC-1, …) | rises with dose |  |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.817×** | -3.2 | 0.048 | 17/47 (SNU-423, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.817×** | -3.2 | 0.048 | 22/48 (LOX-IMVI, SNU-1, …) | top dose only |  |
| [[Loperamide (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -3.1 | 0.048 | 16/48 (NCI-H2347, NCI-H1792, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.813×** | -3.1 | 0.048 | 15/48 (NCI-H1573, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1175. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 77.7 | 11 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +33.8) | — |
| [[SW 900 (line)]] | alt | 68.7 | 8 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.57× (z +28.1) | [[Bortezomib (drug)]] 0.05 µM 0.294× (z -10.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[HOP62 (line)]] | alt | 72.2 | 7 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 16.1× (z +38.3) | [[Auranofin (drug)]] 5 µM 0.339× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 66.0 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +22.3) | — |
| [[PANC-1 (line)]] | alt | 84.5 | 6 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 13.8× (z +41.3) | [[Bortezomib (drug)]] 0.05 µM 0.401× (z -9.7) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.433× (z -9.4) |
| [[A-172 (line)]] | wt | 96.9 | 6 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +33.8) | [[Dinaciclib (drug)]] 5 µM 0.364× (z -9.9) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 50.0 | 5 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.58× (z +28.7) | [[Dinaciclib (drug)]] 5 µM 0.335× (z -9.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.359× (z -9.2) |
| [[KATO III (line)]] | alt | 33.7 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.32× (z +22.6) | — |
| [[LoVo (line)]] | wt | 59.2 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.49× (z +30.4) | [[Dinaciclib (drug)]] 5 µM 0.396× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 152 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.39× (z +22.8) | [[Dinaciclib (drug)]] 5 µM 0.403× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 153 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.24× (z +18.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -8.8) ⚠ cell-cycle shift, explains <1% of this change |
| [[BT-474 (line)]] | alt | 43.6 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +21.3) | — |
| [[J82 (line)]] | alt | 55.1 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.1× (z +36.7) | — |
| [[NCI-H2347 (line)]] | alt | 44.3 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +28.2) | — |
| [[SW48 (line)]] | wt | 92.3 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.35× (z +20.1) | [[Auranofin (drug)]] 5 µM 0.283× (z -9.8) |
| [[A498 (line)]] | wt | 79.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.55× (z +35.2) | — |
| [[HS-578T (line)]] | alt | 58.2 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.99× (z +25.2) | — |
| [[hTERT-HPNE (line)]] | wt | 86.4 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +24.8) | — |
| [[LS 180 (line)]] | wt | 32.1 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.3× (z +26.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 70.6 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +23.8) | — |
| [[SNU-423 (line)]] | alt | 95.7 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 12.5× (z +32.2) | [[Auranofin (drug)]] 5 µM 0.372× (z -8.9) |
| [[A-427 (line)]] | wt | 82.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +15.6) | — |
| [[A549 (line)]] | wt | 113 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +34.2) | — |
| [[AsPC-1 (line)]] | alt | 62.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +33.5) | — |
| [[C32 (line)]] | wt | 33.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +18.7) | — |
| [[H4 (line)]] | wt | 81.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.17× (z +19.4) | — |
| [[HCT15 (line)]] | alt | 80.1 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +15.4) | [[Auranofin (drug)]] 5 µM 0.310× (z -9.0) |
| [[HEC-1-A (line)]] | alt | 66.9 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +33.7) | — |
| [[HepG2_C3A (line)]] | wt | 55.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +24.1) | — |
| [[Hs 766T (line)]] | wt | 84.9 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +29.8) | [[Dinaciclib (drug)]] 5 µM 0.292× (z -10.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 64.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.79× (z +23.5) | — |
| [[SW1417 (line)]] | alt | 56.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.55× (z +28.6) | — |
| [[CFPAC-1 (line)]] | alt | 97.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +33.3) | — |
| [[LOX-IMVI (line)]] | wt | 45.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.89× (z +25.1) | — |
| [[NCI-H2030 (line)]] | alt | 97.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +23.1) | — |
| [[Panc 03.27 (line)]] | alt | 64.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.07× (z +28.2) | — |
| [[RKO (line)]] | wt | 57.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +19.5) | — |
| [[SW480 (line)]] | alt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +19.9) | — |
| [[AN3 CA (line)]] | alt | 119 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.33× (z +11.9) | — |
| [[C-33 A (line)]] | alt | 48.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.246× (z -10.3) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 26.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +17.8) | — |
| [[SK-MEL-2 (line)]] | alt | 97.2 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 5.00× (z +14.4) | — |
| [[SW 1271 (line)]] | alt | 85.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.83× (z +10.6) | [[Temsirolimus (drug)]] 0.5 µM 0.0806× (z -9.7) |
| [[CHP-212 (line)]] | wt | 45.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.89× (z +10.9) | — |
| [[NCI-H23 (line)]] | alt | 90.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.347× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +14.7) | — |
| [[SW 1088 (line)]] | alt | 57.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.16× (z +9.3) | — |
| [[NCI-H2122 (line)]] | alt | 61.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1175), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NR1D1]] | +0.71 | +0.65 / +0.71 | both halves | 7e-06 |  |
| [[BCL3]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[HCP5]] | +0.68 | +0.56 / +0.76 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.67 | +0.65 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 901 |
| [[TNFAIP2]] | +0.65 | +0.58 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 400 |
| [[AGRN]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 |  |
| [[RELB]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[KDM6B]] | +0.63 | +0.74 / +0.53 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[RELA]] | +0.62 | +0.59 / +0.66 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |
| [[SDC4]] | +0.62 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[HIVEP2]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[REL]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 | same gene group; pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 999 |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDC123]] | -0.63 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[COP1]] | -0.62 | -0.68 / -0.57 | both halves | 1e-05 |  |
| [[ZFYVE9]] | -0.61 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[FBXW11]] | -0.58 | -0.54 / -0.60 | both halves | 1e-05 | pathway: C-type lectin receptors (CLRs); STRING 898 |
| [[CACYBP]] | -0.57 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[RAP1GDS1]] | -0.57 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.56 | -0.64 / -0.47 | both halves | 2e-05 | same gene group; pathway: C-type lectin receptors (CLRs) |
| [[POP1]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[TNPO3]] | -0.55 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[OPA1]] | -0.54 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ATP2C1]] | -0.54 | -0.53 / -0.47 | both halves | 2e-05 |  |
| [[HSPE1]] | -0.53 | -0.50 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-F]] | B | HLA-F activity raises NFKB2's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 1.45× lower at baseline in the lines without HLA-F | 0.019 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[SOCS2]] | B | SOCS2 activity raises NFKB2's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.49× lower at baseline in the lines without SOCS2 | 0.039 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[EBI3]] | B | EBI3 activity raises NFKB2's level | lines that do not express EBI3 (12) vs lines expressing it (38) | 1.48× lower at baseline in the lines without EBI3 | 0.067 | ⚠ within organs, on part of the lines; also absent: ENSG00000258272, CTSL, DNAAF9; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.727). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.4, 5.5); signed map (43.2, 6.5). **Vector** length 126, 39.2% of its response variance represented; |z| ≥ 3 in 1,248 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +9.4 | +29.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.5 | +13.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~41% of this change | +7.3 | +3.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +45.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.7 | +5.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | -0.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.2 | -0.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +2.6 | +0.9 |
| fall | [[Auranofin (drug)]] 5 µM |  | -10.6 | -8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~22% of this change | -9.5 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | -9.0 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.9 | -3.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -6.4 | -6.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.4 | -1.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | +1.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | nuclear factor kappa B subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.32 — chr10:102,394,110-102,402,524 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LYT-10, p52, p105, NF-kB2, p49/p100 |
| Gene groups (HGNC) | Ankyrin repeat domain containing; NF-kappa B complex subunits; IPT domain containing; NFKB inhibitor family |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 58 pathways, smallest: DEx/H-box helicases activate type I IFN and inflammatory cytokines production; IkBA variant leads to EDA-ID; Interleukin-1 processing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00653](https://www.uniprot.org/uniprotkb/Q00653) (Nuclear factor NF-kappa-B p100 subunit):

> NF-kappa-B is a pleiotropic transcription factor present in almost all cell types and is the endpoint of a series of signal transduction events that are initiated by a vast array of stimuli related to many biological processes such as inflammation, immunity, differentiation, cell growth, tumorigenesis and apoptosis. NF-kappa-B is a homo- or heterodimeric complex formed by the Rel-like domain-containing proteins RELA/p65, RELB, NFKB1/p105, NFKB1/p50, REL and NFKB2/p52. The dimers bind at kappa-B …

**Summary**, from NCBI Gene [4791](https://www.ncbi.nlm.nih.gov/gene/4791):

> This gene encodes a subunit of the transcription factor complex nuclear factor-kappa-B (NFkB). The NFkB complex is expressed in numerous cell types and functions as a central activator of genes involved in inflammation and immune function. The protein encoded by this gene can function as both a transcriptional activator or repressor depending on its dimerization partner. The p100 full-length protein is co-translationally processed into a p52 active form. Chromosomal rearrangements and …

**Accessions** — [HGNC:7795](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7795) · Entrez [4791](https://www.ncbi.nlm.nih.gov/gene/4791) · UniProt [Q00653](https://www.uniprot.org/uniprotkb/Q00653) · Ensembl [ENSG00000077150](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000077150)

## Data

Gene col 1175: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1175); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1175, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1175]; `tensor/DDL_lfc|DDL_z.npy` [1175]; `embed/gene_vectors.npy` [1175]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1175 or target_col == 1175). Every well: [[NFKB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NFKB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
