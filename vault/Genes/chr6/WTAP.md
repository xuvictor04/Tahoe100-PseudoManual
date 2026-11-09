---
symbol: "WTAP"
type: "gene"
col: 7097
ensembl_id: "ENSG00000146457"
name: "WT1 associated protein"
location: "6q25.3"
module: 14
arm: "+"
pooled_cpm: 154.54
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# WTAP

*WT1 associated protein* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 9.41× (z +24.4, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.467× (z -15.8, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NFKBIA]] (+0.70, fdr 7e-06), [[CEBPD]] (+0.70, fdr 7e-06), [[SOD2]] (+0.69, fdr 7e-06, ⚠ same locus), [[RAF1]] (+0.68, fdr 7e-06); moves opposite to [[PPM1F]] (-0.58, fdr 3e-05), [[DPP9]] (-0.57, fdr 1e-04), [[EP400]] (-0.56, fdr 6e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7097.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **9.41×** | +24.4 | 0e+00 | 48/49 (LoVo, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +20.5 | 0e+00 | 45/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +15.2 | 0e+00 | 44/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.45×** | +13.5 | 4e-39 | 46/48 (HEC-1-A, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +10.9 | 2e-25 | 43/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.58×** | +9.5 | 2e-19 | 45/48 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +8.0 | 8e-14 | 45/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.45×** | +7.7 | 1e-12 | 38/48 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +7.1 | 6e-11 | 29/38 (HT-29, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.40×** | +7.0 | 2e-10 | 32/48 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +6.7 | 1e-09 | 34/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +6.2 | 2e-08 | 29/47 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.27×** | +4.9 | 3e-05 | 27/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.07× | +4.5 | 3e-04 | 3/50 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 22/48 (HEC-1-A, BT-474, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7097.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.467×** | -15.8 | 0e+00 | 47/48 (AsPC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.465×** | -15.3 | 0e+00 | 42/44 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.487×** | -15.0 | 0e+00 | 48/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.530×** | -13.2 | 7e-38 | 40/49 (NCI-H2347, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.566×** | -11.9 | 2e-30 | 45/48 (PANC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -9.6 | 8e-20 | 43/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.667×** | -8.4 | 3e-15 | 43/48 (SW480, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.644×** | -4.8 | 1e-04 | 30/49 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.799×** | -4.7 | 2e-04 | 26/48 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.877× | -3.9 | 0.006 | 15/48 (SW480, SW1417, …) | top dose only |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.842× | -3.6 | 0.016 | 20/48 (HEC-1-A, NCI-H2030, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.847× | -3.5 | 0.024 | 20/48 (NCI-H1792, A549, …) | rises with dose |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.849× | -3.4 | 0.026 | 19/48 (RPMI-7951, AsPC-1, …) | inconsistent across doses |  |
| [[Apalutamide (drug)]] 0.5 µM |  | 0.854× | -3.3 | 0.036 | 20/48 (J82, SW 900, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.854× | -3.3 | 0.036 | 17/49 (SNU-423, NCI-H2347, …) | top dose only | position effect removed |
| [[Ranolazine (drug)]] 0.05 µM |  | 0.857× | -3.2 | 0.041 | 13/48 (HT-29, Hs 766T, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 5 µM |  | 0.901× | -3.1 | 0.060 | 9/49 (MIA PaCa-2, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7097. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 136 | 11 (2 ⚠) | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +23.9) | [[Panobinostat (drug)]] 5 µM 0.453× (z -12.6) |
| [[NCI-H460 (line)]] | wt | 186 | 12 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +19.4) | [[Panobinostat (drug)]] 0.5 µM 0.341× (z -12.9) |
| [[LoVo (line)]] | wt | 128 | 10 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 15.9× (z +23.0) | [[Dinaciclib (drug)]] 5 µM 0.200× (z -24.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 163 | 6 | 4 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.18× (z +28.0) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -14.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.252× (z -13.0) |
| [[A549 (line)]] | wt | 166 | 4 | 5 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +16.0) | [[Panobinostat (drug)]] 5 µM 0.382× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 123 | 6 (1 ⚠) | 3 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.20× (z +15.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.08× (z +13.5) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.299× (z -11.6) |
| [[SNU-423 (line)]] | alt | 415 | 3 | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.161× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.235× (z -14.1) |
| [[A498 (line)]] | wt | 149 | 5 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +17.6) | [[Dinaciclib (drug)]] 5 µM 0.374× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.411× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 132 | 6 | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 10.8× (z +16.1) | [[Dinaciclib (drug)]] 5 µM 0.314× (z -14.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 123 | 3 (1 ⚠) | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.5× (z +17.3) | [[Dinaciclib (drug)]] 5 µM 0.395× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.469× (z -10.7) |
| [[KATO III (line)]] | alt | 115 | 5 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.65× (z +13.6) | [[Panobinostat (drug)]] 0.5 µM 0.483× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 171 | 5 (1 ⚠) | 3 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.50× (z +16.1) ⚠ position not correctable · without an alert: [[TAK-901 (drug)]] 5 µM 8.19× (z +12.4) | [[Dinaciclib (drug)]] 0.5 µM 0.410× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.424× (z -9.7) |
| [[SW480 (line)]] | alt | 159 | 3 | 5 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.42× (z +18.1) | [[Dinaciclib (drug)]] 0.5 µM 0.462× (z -13.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.488× (z -12.4) |
| [[HepG2_C3A (line)]] | wt | 212 | 3 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +13.9) | [[Panobinostat (drug)]] 5 µM 0.376× (z -10.3) |
| [[hTERT-HPNE (line)]] | wt | 206 | 5 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.21× (z +21.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.311× (z -9.0) |
| [[AsPC-1 (line)]] | alt | 158 | 2 | 4 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.9× (z +16.2) | [[Dinaciclib (drug)]] 5 µM 0.294× (z -15.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.335× (z -14.3) |
| [[CFPAC-1 (line)]] | alt | 124 | 2 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 10.7× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.407× (z -11.0) |
| [[HOP62 (line)]] | alt | 123 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.89× (z +22.0) | [[Panobinostat (drug)]] 0.5 µM 0.368× (z -9.9) |
| [[HS-578T (line)]] | alt | 161 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +14.3) | — |
| [[J82 (line)]] | alt | 200 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.95× (z +20.7) | [[Panobinostat (drug)]] 0.5 µM 0.308× (z -10.8) |
| [[LOX-IMVI (line)]] | wt | 126 | 3 | 3 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 7.33× (z +12.3) | [[Dinaciclib (drug)]] 5 µM 0.346× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.424× (z -10.2) |
| [[NCI-H2347 (line)]] | alt | 184 | 2 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.0× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -18.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.454× (z -9.4) |
| [[RPMI-7951 (line)]] | alt | 196 | 4 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 17.1× (z +12.3) | [[Panobinostat (drug)]] 0.5 µM 0.346× (z -8.9) |
| [[BT-474 (line)]] | alt | 124 | 4 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 37.3× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.285× (z -12.3) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 136 | 4 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 20.9× (z +12.6) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -9.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 89.2 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.356× (z -8.5) |
| [[LS 180 (line)]] | wt | 128 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 9.71× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.2) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 210 | 3 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 3.78× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -10.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 159 | 3 | 2 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 6.75× (z +13.1) | [[Panobinostat (drug)]] 0.5 µM 0.497× (z -9.2) |
| [[NCI-H1792 (line)]] | alt | 227 | 1 | 3 | [[TAK-901 (drug)]] 5 µM 4.65× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.353× (z -13.3) |
| [[Panc 03.27 (line)]] | alt | 113 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.1) | — |
| [[SW 900 (line)]] | alt | 187 | 3 | 1 | [[TAK-901 (drug)]] 5 µM 11.6× (z +10.7) | [[Panobinostat (drug)]] 0.5 µM 0.334× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 109 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 9.41× (z +13.2) | — |
| [[SW48 (line)]] | wt | 145 | 3 | 0 | [[TAK-901 (drug)]] 0.05 µM 4.87× (z +13.9) | — |
| [[C-33 A (line)]] | alt | 136 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.36× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.453× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 94.1 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 4.57× (z +10.3) | — |
| [[RKO (line)]] | wt | 124 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.30× (z +13.9) | — |
| [[A-427 (line)]] | wt | 103 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.64× (z +13.1) | — |
| [[AN3 CA (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.5) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 142 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.5× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 101 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 15.9× (z +12.6) | — |
| [[HCT15 (line)]] | alt | 145 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.46× (z +9.3) | — |
| [[Hs 766T (line)]] | wt | 130 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.8× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -12.9) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 118 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.37× (z +11.2) | — |
| [[SW 1271 (line)]] | alt | 160 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +11.1) | — |
| [[NCI-H2122 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 165 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 230 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7097), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NFKBIA]] | +0.70 | +0.66 / +0.76 | both halves | 7e-06 |  |
| [[CEBPD]] | +0.70 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[SOD2]] | +0.69 | +0.66 / +0.67 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[RAF1]] | +0.68 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[CHASERR]] | +0.62 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[C1RL]] | +0.62 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[DENND2B]] | +0.62 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[CHKB-DT]] | +0.62 | +0.51 / +0.39 | both halves | 5e-05 |  |
| [[TP53]] | +0.61 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[RBM7]] | +0.61 | +0.54 / +0.58 | both halves | 1e-05 | pathway: Processing of Capped Intron-Containing Pre-mRNA |
| [[C1QTNF1-AS1]] | +0.61 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[SIAH1]] | +0.60 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[PIGP]] | +0.60 | +0.50 / +0.40 | both halves | 4e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPM1F]] | -0.58 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[DPP9]] | -0.57 | -0.36 / -0.50 | both halves | 1e-04 |  |
| [[EP400]] | -0.56 | -0.38 / -0.52 | both halves | 6e-05 |  |
| [[PRKCZ]] | -0.55 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[FXYD5]] | -0.55 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[LINC02693]] | -0.54 | -0.30 / -0.60 | both halves | 2e-04 |  |
| [[BCAP31]] | -0.54 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[AP3M2]] | -0.54 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[ERCC2]] | -0.54 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[PWWP3A]] | -0.53 | -0.37 / -0.53 | both halves | 8e-05 |  |
| [[CAP1]] | -0.52 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[MCFD2]] | -0.52 | -0.54 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises WTAP's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SOD2]] | C | SOD2 activity raises WTAP's level | lines that do not express SOD2 (3) vs lines expressing it (47) | 1.46× lower at baseline in the lines without SOD2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SLC9A3, SMOX, NDRG1; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.8, 16.0); signed map (41.7, 5.4). **Vector** length 114, 42.1% of its response variance represented; |z| ≥ 3 in 1,460 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.2 | +20.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.8 | +2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +6.0 | +1.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.9 | +24.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.6 | +15.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.5 | +1.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.0 | +0.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.0 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +3.7 | +1.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | +3.7 | +0.0 |
| fall | [[Auranofin (drug)]] 5 µM |  | -9.6 | -9.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.2 | -0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.2 | -15.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.9 | -11.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.8 | +2.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.6 | -2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.9 | +0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.9 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | WT1 associated protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:159,725,585-159,756,319 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0105, MGC3925, Mum2 |
| Gene groups (HGNC) | m6A methyltransferase complex; WTAP complex |
| Reactome | 2 pathways, smallest: Processing of Capped Intron-Containing Pre-mRNA; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15007](https://www.uniprot.org/uniprotkb/Q15007) (Pre-mRNA-splicing regulator WTAP):

> Associated component of the WMM complex, a complex that mediates N6-methyladenosine (m6A) methylation of RNAs, a modification that plays a role in the efficiency of mRNA splicing and RNA processing. Required for accumulation of METTL3 and METTL14 to nuclear speckle. Acts as a mRNA splicing regulator. Regulates G2/M cell-cycle transition by binding to the 3' UTR of CCNA2, which enhances its stability. Impairs WT1 DNA-binding ability and inhibits expression of WT1 target genes.

**Summary**, from NCBI Gene [9589](https://www.ncbi.nlm.nih.gov/gene/9589):

> The Wilms tumor suppressor gene WT1 appears to play a role in both transcriptional and posttranscriptional regulation of certain cellular genes. This gene encodes a WT1-associating protein, which is a ubiquitously expressed nuclear protein. Like WT1 protein, this protein is localized throughout the nucleoplasm as well as in speckles and partially colocalizes with splicing factors. Alternative splicing of this gene results in several transcript variants encoding three different isoforms. …

**Accessions** — [HGNC:16846](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16846) · Entrez [9589](https://www.ncbi.nlm.nih.gov/gene/9589) · UniProt [Q15007](https://www.uniprot.org/uniprotkb/Q15007) · Ensembl [ENSG00000146457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000146457)

## Data

Gene col 7097: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7097); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7097, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7097]; `tensor/DDL_lfc|DDL_z.npy` [7097]; `embed/gene_vectors.npy` [7097]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7097 or target_col == 7097). Every well: [[WTAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WTAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
