---
symbol: "AP1G1"
type: "gene"
col: 9350
ensembl_id: "ENSG00000166747"
name: "adaptor related protein complex 1 subunit gamma 1"
location: "16q22.2"
module: 12
arm: "+"
pooled_cpm: 181.28
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 16
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# AP1G1

*adaptor related protein complex 1 subunit gamma 1* — 16q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 4.29× (z +15.9, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.512× (z -14.0, q 6e-42, down in 46 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.757× (z -8.3, q 2e-14, down in 35 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC39A9]] (+0.66, fdr 7e-06), [[TM9SF4]] (+0.63, fdr 1e-05), [[COQ10B]] (+0.59, fdr 1e-05); moves opposite to [[PALS2]] (-0.58, fdr 1e-05), [[OTUD6B]] (-0.57, fdr 1e-05), [[PPARGC1B]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FER1L4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9350.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **4.29×** | +15.9 | 0e+00 | 48/49 (SW480, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.64×** | +14.6 | 0e+00 | 38/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.98×** | +11.9 | 1e-30 | 48/48 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.69×** | +11.0 | 8e-26 | 48/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.52×** | +8.8 | 2e-16 | 43/48 (HepG2/C3A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.40×** | +7.0 | 2e-10 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +6.7 | 1e-09 | 43/48 (PANC-1, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 7e-08 | 38/48 (A-427, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.32×** | +5.8 | 3e-07 | 37/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +5.0 | 3e-05 | 29/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.2 | 0.002 | 23/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.002 | 25/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9350.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.512×** | -14.0 | 6e-42 | 46/49 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.513×** | -13.5 | 7e-39 | 41/44 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.547×** | -11.7 | 3e-29 | 40/45 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.757×** | -8.3 | 2e-14 | 35/49 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.681×** | -7.8 | 9e-13 | 43/47 (SW 1271, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.810×** | -6.3 | 4e-08 | 31/48 (HT-29, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.747×** | -6.1 | 7e-08 | 31/48 (HT-29, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.766×** | -5.6 | 2e-06 | 34/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.762×** | -5.5 | 3e-06 | 32/48 (NCI-H460, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.779×** | -5.2 | 9e-06 | 36/48 (HepG2/C3A, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.781×** | -5.2 | 1e-05 | 30/48 (HT-29, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.777×** | -5.1 | 2e-05 | 31/50 (H4, RPMI-7951, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.778×** | -5.1 | 2e-05 | 33/48 (NCI-H1573, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.800×** | -4.7 | 1e-04 | 26/48 (COLO 205, HT-29, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 0.863× | -4.4 | 4e-04 | 14/48 (AsPC-1, NCI-H661, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.827×** | -4.0 | 0.002 | 24/49 (HT-29, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.702×** | -3.9 | 0.003 | 32/49 (HS-578T, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 0.852× | -3.4 | 0.020 | 16/48 (SNU-423, PANC-1, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 0.852× | -3.4 | 0.020 | 20/48 (A549, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.894× | -3.3 | 0.022 | 6/48 (A549, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.855× | -3.3 | 0.024 | 20/48 (NCI-H1792, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9350. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 107 | 11 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +21.2) | — |
| [[LOX-IMVI (line)]] | wt | 163 | 6 (2 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +20.5) | [[Dinaciclib (drug)]] 0.05 µM 0.372× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.620× (z -9.2) |
| [[SW480 (line)]] | alt | 294 | 6 (1 ⚠) | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 7.48× (z +16.0) | [[Dinaciclib (drug)]] 0.5 µM 0.380× (z -14.8) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 300 | 6 (3 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.19× (z +14.1) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 122 | 5 (2 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.40× (z +19.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.612× (z -11.0) |
| [[A498 (line)]] | wt | 245 | 2 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.75× (z +13.9) | [[Dinaciclib (drug)]] 5 µM 0.528× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.659× (z -10.5) |
| [[HOP62 (line)]] | alt | 210 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.317× (z -15.0) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 224 | 1 | 6 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 3.77× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.393× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 0.662× (z -8.6) |
| [[LoVo (line)]] | wt | 182 | 4 | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.49× (z +13.2) | [[Dinaciclib (drug)]] 5 µM 0.273× (z -18.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 217 | 3 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 5.56× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.499× (z -13.8) |
| [[RKO (line)]] | wt | 190 | 4 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 6.72× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.170× (z -22.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.583× (z -9.8) |
| [[HS-578T (line)]] | alt | 137 | 3 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.28× (z +15.8) | [[Dinaciclib (drug)]] 5 µM 0.352× (z -13.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 276 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +14.8) | [[Dinaciclib (drug)]] 5 µM 0.368× (z -13.2) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 117 | 1 | 5 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 4.35× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.478× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 143 | 3 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -8.5) |
| [[A549 (line)]] | wt | 176 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.481× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 182 | 2 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.567× (z -10.8) |
| [[A-427 (line)]] | wt | 170 | 3 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.97× (z +11.1) | [[Dinaciclib (drug)]] 0.5 µM 0.528× (z -9.8) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 184 | 1 | 3 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 3.68× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.442× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 215 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -14.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 214 | 2 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 4.30× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.371× (z -13.0) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 167 | 3 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.392× (z -10.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 190 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.54× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -13.6) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 120 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +17.0) | [[Dinaciclib (drug)]] 5 µM 0.291× (z -14.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 167 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.386× (z -12.1) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 136 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 5.43× (z +11.1) | — |
| [[C32 (line)]] | wt | 134 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.407× (z -9.9) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 143 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 4.15× (z +12.1) | — |
| [[NCI-H23 (line)]] | alt | 164 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.454× (z -10.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 139 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +10.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.639× (z -8.5) |
| [[SW 900 (line)]] | alt | 181 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -12.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 174 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.328× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -8.8) |
| [[BT-474 (line)]] | alt | 207 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.81× (z +11.9) | — |
| [[CHP-212 (line)]] | wt | 247 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.321× (z -9.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 231 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 224 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.11× (z +8.7) | [[Dinaciclib (drug)]] 0.05 µM 0.261× (z -12.6) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 186 | 1 | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 2.08× (z +9.2) | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -12.5) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 171 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.95× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.499× (z -9.0) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.90× (z +9.7) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.493× (z -9.3) ⚠ toxic |
| [[SW48 (line)]] | wt | 171 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.289× (z -12.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.573× (z -12.7) |
| [[hTERT-HPNE (line)]] | wt | 178 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.551× (z -8.9) |
| [[J82 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.510× (z -9.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 207 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.205× (z -9.4) ⚠ toxic |
| [[SW1417 (line)]] | alt | 179 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.533× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2122 (line)]] | alt | 190 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 124 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 210 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9350), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC39A9]] | +0.66 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[TM9SF4]] | +0.63 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[COQ10B]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[ARF4]] | +0.58 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[DCP1A]] | +0.58 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[CCNK]] | +0.58 | +0.66 / +0.56 | both halves | 1e-05 | pathway: HIV Infection |
| [[SUPT6H]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[COPE]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_PROTEIN_SECRETION |
| [[GOLGB1]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Golgi Associated Vesicle Biogenesis |
| [[USP8]] | +0.56 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[PSMB1]] | +0.56 | +0.66 / +0.47 | both halves | 2e-05 | pathway: HIV Infection |
| [[CWC25]] | +0.55 | +0.56 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PALS2]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[OTUD6B]] | -0.57 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[PPARGC1B]] | -0.55 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[SINHCAF]] | -0.53 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[LRP5L]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ADAT2]] | -0.53 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[USP31]] | -0.51 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[ABCB10]] | -0.51 | -0.51 / -0.34 | both halves | 1e-04 |  |
| [[ZNRF2P1]] | -0.51 | -0.61 / -0.36 | both halves | 9e-05 |  |
| [[SLC35G1]] | -0.50 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[TMEM64]] | -0.50 | -0.57 / -0.43 | both halves | 3e-05 |  |
| [[GCSH]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FER1L4]] | B | FER1L4 activity raises AP1G1's level | lines that do not express FER1L4 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without FER1L4 | 0.049 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A, STEAP2, OSR2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises AP1G1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity lowers AP1G1's level | compounds that target PSMB5: 2 of 2 raise it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.332). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (8.2, -36.5); signed map (-6.4, -13.2). **Vector** length 90.6, 32.3% of its response variance represented; |z| ≥ 3 in 1,361 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.4 | +14.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +6.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | -14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | -13.5 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.7 | -1.6 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.4 | -1.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | -0.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | -3.3 |
| fall | [[Radotinib (drug)]] 5 µM |  | -3.5 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -6.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.3 | +5.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.0 | -5.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -0.2 |
|  | [[Neratinib (drug)]] 5 µM |  | -2.8 | -2.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.7 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 1 subunit gamma 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q22.2 — chr16:71,729,000-71,809,201 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CLAPG1, ADTG |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 1; Small nucleolar RNA protein coding host genes |
| Hallmark sets | PROTEIN_SECRETION |
| Reactome | 13 pathways, smallest: Nef mediated downregulation of MHC class I complex cell surface expression; Nef-mediates down modulation of cell surface receptors by recruiting them to clathrin adapters; The role of Nef in HIV-1 replication and disease pathogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O43747](https://www.uniprot.org/uniprotkb/O43747) (AP-1 complex subunit gamma-1):

> Subunit of clathrin-associated adaptor protein complex 1 that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules. In association with AFTPH/aftiphilin in the aftiphilin/p200/gamma-synergin complex, involved in the trafficking of transferrin from early to recycling endosomes, and the …

**Summary**, from NCBI Gene [164](https://www.ncbi.nlm.nih.gov/gene/164):

> Adaptins are important components of clathrin-coated vesicles transporting ligand-receptor complexes from the plasma membrane or from the trans-Golgi network to lysosomes. The adaptin family of proteins is composed of four classes of molecules named alpha, beta-, beta prime- and gamma- adaptins. Adaptins, together with medium and small subunits, form a heterotetrameric complex called an adaptor, whose role is to promote the formation of clathrin-coated pits and vesicles. The protein encoded by …

**Accessions** — [HGNC:555](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:555) · Entrez [164](https://www.ncbi.nlm.nih.gov/gene/164) · UniProt [O43747](https://www.uniprot.org/uniprotkb/O43747) · Ensembl [ENSG00000166747](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166747)

## Data

Gene col 9350: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9350); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9350, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9350]; `tensor/DDL_lfc|DDL_z.npy` [9350]; `embed/gene_vectors.npy` [9350]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9350 or target_col == 9350). Every well: [[AP1G1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP1G1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
