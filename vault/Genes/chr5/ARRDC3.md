---
symbol: "ARRDC3"
type: "gene"
col: 3456
ensembl_id: "ENSG00000113369"
name: "arrestin domain containing 3"
location: "5q14.3"
module: 14
arm: "+"
pooled_cpm: 200.24
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 48
n_dd_up_clean: 17
n_dd_down_clean: 33
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# ARRDC3

*arrestin domain containing 3* — 5q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 23.0× (z +19.7, q 0e+00, up in 49 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.277× (z -14.9, q 0e+00, down in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Lidocaine (hydrochloride) (drug)]] 5 µM: 0.758× (z -4.8, q 1e-04, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BHLHE40]] (+0.72, fdr 7e-06), [[NR1D1]] (+0.66, fdr 7e-06), [[ZBTB25]] (+0.61, fdr 1e-05); moves opposite to [[VKORC1L1]] (-0.65, fdr 1e-05), [[GATAD2A]] (-0.57, fdr 1e-05), [[TRAPPC10]] (-0.57, fdr 1e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **23.0×** | +19.7 | 0e+00 | 49/49 (NCI-H2347, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.92×** | +11.1 | 5e-26 | 45/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.31×** | +10.0 | 2e-21 | 43/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **4.62×** | +9.6 | 9e-20 | 45/48 (HEC-1-A, C32, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.60×** | +8.0 | 1e-13 | 32/48 (SW1417, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **1.85×** | +7.4 | 1e-11 | 47/48 (SNU-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.80×** | +7.1 | 1e-10 | 44/48 (A549, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.78×** | +6.9 | 3e-10 | 37/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.6 | 3e-09 | 39/48 (KATO III, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.76×** | +6.5 | 5e-09 | 34/48 (AsPC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +5.3 | 5e-06 | 35/48 (SNU-1, H4, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.56×** | +5.3 | 6e-06 | 36/48 (KATO III, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.51×** | +4.9 | 4e-05 | 40/49 (C-33 A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.49×** | +4.8 | 7e-05 | 29/48 (SW1417, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.44×** | +4.4 | 5e-04 | 36/48 (NCI-H2347, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.002 | 30/48 (C-33 A, HT-29, …) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.003 | 29/48 (NCI-H23, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.71×** | +3.4 | 0.023 | 27/48 (SHP-77, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.027 | 28/49 (NCI-H460, COLO 205, …) | top dose only | plate-row cell shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.277×** | -14.9 | 0e+00 | 42/44 (NCI-H2347, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.395×** | -11.2 | 9e-27 | 48/48 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.406×** | -10.9 | 2e-25 | 42/49 (NCI-H2347, SNU-423, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.466×** | -9.2 | 4e-18 | 44/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.507×** | -8.2 | 2e-14 | 40/48 (NCI-H2347, RPMI-7951, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.590×** | -6.1 | 7e-08 | 34/47 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.628×** | -5.4 | 4e-06 | 36/47 (A-172, SW1417, …) | top dose only | cell-cycle shift (explains ~6% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.667×** | -4.9 | 6e-05 | 36/48 (A498, PANC-1, …) | all doses, stronger at high dose |  |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.758×** | -4.8 | 1e-04 | 41/48 (C-33 A, A549, …) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.760×** | -4.7 | 1e-04 | 33/48 (hTERT-HPNE, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.694×** | -4.4 | 5e-04 | 33/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.701×** | -4.3 | 7e-04 | 36/48 (HOP62, J82, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.702×** | -4.3 | 7e-04 | 28/48 (A498, HS-578T, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.705×** | -4.2 | 9e-04 | 32/48 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.797×** | -3.9 | 0.003 | 31/48 (NCI-H1573, NCI-H2347, …) | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.734×** | -3.8 | 0.005 | 32/49 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.740×** | -3.7 | 0.008 | 34/48 (J82, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.741×** | -3.6 | 0.008 | 27/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.010 | 29/48 (C-33 A, SW 900, …) | inconsistent across doses | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.638×** | -3.5 | 0.010 | 26/48 (SW 900, NCI-H23, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.644×** | -3.5 | 0.012 | 28/48 (MIA PaCa-2, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.644×** | -3.5 | 0.012 | 32/49 (SW 900, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 5 µM |  | **0.768×** | -3.2 | 0.027 | 25/48 (NCI-H1573, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 409 | 2 | 15 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 48.2× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.149× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Clobetasol propionate (drug)]] 0.5 µM 0.162× (z -12.0) |
| [[A498 (line)]] | wt | 241 | 2 (1 ⚠) | 8 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 7.44× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.206× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.319× (z -11.6) |
| [[AsPC-1 (line)]] | alt | 253 | 6 (4 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +16.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 5.72× (z +14.9) | [[Panobinostat (drug)]] 5 µM 0.228× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[SW1417 (line)]] | alt | 166 | 5 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +19.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 24.4× (z +17.1) | [[Dinaciclib (drug)]] 0.5 µM 0.346× (z -10.7) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 480 | 3 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 21.7× (z +17.2) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -23.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 344 | 5 (1 ⚠) | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 22.0× (z +14.5) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -16.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 295 | 2 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 13.4× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -17.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 65.6 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.81× (z +18.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 8.92× (z +16.6) | — |
| [[SNU-423 (line)]] | alt | 374 | 1 | 7 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 11.3× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -17.1) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 298 | 3 (2 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +17.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 25.4× (z +14.6) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -13.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 90.9 | 3 | 4 (4 ⚠) | [[PH-797804 (drug)]] 5 µM 15.6× (z +14.5) | [[Panobinostat (drug)]] 0.5 µM 0.317× (z -11.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HS-578T (line)]] | alt | 391 | 2 | 5 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 38.4× (z +15.1) | [[Panobinostat (drug)]] 5 µM 0.284× (z -9.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.324× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 293 | 1 | 6 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 22.7× (z +14.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -12.5) ⚠ cell-cycle shift, explains ~69% of this change |
| [[SNU-1 (line)]] | wt | 139 | 6 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 9.50× (z +22.9) | [[Dinaciclib (drug)]] 0.5 µM 0.299× (z -8.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 90.7 | 7 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 58.1× (z +14.7) | — |
| [[A-172 (line)]] | wt | 220 | 2 (1 ⚠) | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 7.50× (z +8.8) | [[Niclosamide (olamine) (drug)]] 5 µM 0.170× (z -14.1) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 195 | 2 | 4 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 19.0× (z +10.4) | [[Panobinostat (drug)]] 5 µM 0.200× (z -10.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H460 (line)]] | wt | 171 | 6 (3 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 45.6× (z +15.0) | — |
| [[A-427 (line)]] | wt | 138 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 33.1× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.184× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 120 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 30.6× (z +15.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -8.8) ⚠ cell-cycle shift, explains ~69% of this change |
| [[C32 (line)]] | wt | 222 | 2 | 3 (3 ⚠) | [[PH-797804 (drug)]] 5 µM 27.6× (z +14.4) | [[Panobinostat (drug)]] 5 µM 0.265× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[Hs 766T (line)]] | wt | 303 | 3 (1 ⚠) | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 23.4× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.9) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 127 | 4 | 1 (1 ⚠) | [[Selinexor (drug)]] 5 µM 3.80× (z +13.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.267× (z -9.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 269 | 3 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 14.4× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.283× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 174 | 3 (1 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 38.8× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.262× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 63.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.75× (z +12.7) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 23.0× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 76.4 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.25× (z +14.1) | — |
| [[H4 (line)]] | wt | 158 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 37.1× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.4) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 173 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.99× (z +14.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.00× (z +10.3) | — |
| [[LS 180 (line)]] | wt | 85.6 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 20.1× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.295× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 171 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 21.2× (z +12.8) | [[Dinaciclib (drug)]] 5 µM 0.199× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 124 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 23.4× (z +15.5) | [[Dinaciclib (drug)]] 5 µM 0.104× (z -20.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 95.1 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.55× (z +17.5) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 35.9× (z +12.3) | — |
| [[SW 900 (line)]] | alt | 199 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 25.5× (z +14.9) | [[Dinaciclib (drug)]] 5 µM 0.226× (z -12.7) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 168 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +10.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 23.8× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.0513× (z -16.3) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 139 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 17.9× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -11.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 101 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +13.4) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Selinexor (drug)]] 5 µM 3.09× (z +12.5) | — |
| [[LoVo (line)]] | wt | 145 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 32.0× (z +13.4) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -10.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 101 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 26.6× (z +15.6) | — |
| [[SK-MEL-2 (line)]] | alt | 161 | 2 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 16.6× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -10.7) ⚠ toxic; transcription drop |
| [[SW 1088 (line)]] | alt | 577 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0802× (z -12.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 203 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 45.6× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 91.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.1× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.271× (z -9.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 177 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 42.6× (z +13.3) | — |
| [[HCT15 (line)]] | alt | 177 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.249× (z -8.5) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 156 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 145 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 207 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BHLHE40]] | +0.72 | +0.67 / +0.77 | both halves | 7e-06 |  |
| [[NR1D1]] | +0.66 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[ZBTB25]] | +0.61 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[ADM]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[REL]] | +0.58 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[BCOR]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ZNF441]] | +0.57 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[CDKN1B]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[ATP23]] | +0.57 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[ZNF442]] | +0.57 | +0.36 / +0.60 | both halves | 9e-05 |  |
| [[CCNG2]] | +0.56 | +0.49 / +0.56 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.56 | +0.64 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VKORC1L1]] | -0.65 | -0.56 / -0.61 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.57 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TRAPPC10]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[MFSD14CP-1]] | -0.55 | -0.56 / -0.56 | both halves | 1e-05 |  |
| [[PSME4]] | -0.53 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[LMBR1]] | -0.53 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ARIH2]] | -0.53 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[LETM1]] | -0.51 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[TCF3]] | -0.50 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[KIAA0232]] | -0.49 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ACOT7]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[ZNF767P-1]] | -0.49 | -0.40 / -0.51 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.538). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (23.9, -3.3); signed map (-2.2, 12.7). **Vector** length 134, 52.2% of its response variance represented; |z| ≥ 3 in 1,846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +17.7 | +11.1 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +11.6 | +7.4 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +8.4 | +4.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +8.1 | +7.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.9 | +5.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +5.5 | +4.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +4.8 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.3 | +0.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +3.7 | +1.1 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -7.3 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.0 | -5.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -5.8 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | -5.4 | -3.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -5.3 | -3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.5 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -0.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.3 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | arrestin domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.3 — chr5:91,368,631-91,383,317 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1376, TLIMP |
| Gene groups (HGNC) | Alpha arrestins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96B67](https://www.uniprot.org/uniprotkb/Q96B67) (Arrestin domain-containing protein 3):

> Adapter protein that plays a role in regulating cell-surface expression of adrenergic receptors and probably also other G protein-coupled receptors. Plays a role in NEDD4-mediated ubiquitination and endocytosis af activated ADRB2 and subsequent ADRB2 degradation. May recruit NEDD4 to ADRB2. Alternatively, may function as adapter protein that does not play a major role in recruiting NEDD4 to ADRB2, but rather plays a role in a targeting ADRB2 to endosomes.

**Summary**, from NCBI Gene [57561](https://www.ncbi.nlm.nih.gov/gene/57561):

> This gene encodes a member of the arrestin family of proteins, which regulate G protein-mediated signaling. The encoded protein is thought to act as a regulator of breast cancer growth and progression by binding to a phosphorylated form of integrin beta4, a tumor-related antigen, targeting the integrin for internalization and degradation. [provided by RefSeq, Jul 2016]

**Accessions** — [HGNC:29263](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29263) · Entrez [57561](https://www.ncbi.nlm.nih.gov/gene/57561) · UniProt [Q96B67](https://www.uniprot.org/uniprotkb/Q96B67) · Ensembl [ENSG00000113369](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000113369)

## Data

Gene col 3456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3456); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3456]; `tensor/DDL_lfc|DDL_z.npy` [3456]; `embed/gene_vectors.npy` [3456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3456 or target_col == 3456). Every well: [[ARRDC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARRDC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
