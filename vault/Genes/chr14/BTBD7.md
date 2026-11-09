---
symbol: "BTBD7"
type: "gene"
col: 224
ensembl_id: "ENSG00000011114"
name: "BTB domain containing 7"
location: "14q32.12"
module: 24
arm: "+"
pooled_cpm: 140.83
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# BTBD7

*BTB domain containing 7* — 14q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.85× (z +17.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.577× (z -15.3, q 0e+00, down in 36 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.720× (z -9.5, q 3e-19, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (89 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 16 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC24B]] (+0.61, fdr 7e-06), [[PGLS]] (+0.61, fdr 1e-05), [[KLHDC10]] (+0.58, fdr 1e-05); moves opposite to [[RLIM]] (-0.55, fdr 7e-05), [[PFKP]] (-0.54, fdr 1e-04), [[CYP27B1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 224.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.85×** | +17.8 | 0e+00 | 43/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +16.1 | 0e+00 | 44/48 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.58×** | +13.2 | 2e-37 | 38/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.57×** | +13.1 | 9e-37 | 42/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +12.3 | 7e-33 | 43/49 (SW480, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~3% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.90×** | +9.7 | 2e-20 | 41/48 (SW480, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +8.5 | 2e-15 | 34/48 (LS 180, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +7.6 | 2e-12 | 30/47 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +6.9 | 3e-10 | 30/48 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +6.9 | 3e-10 | 28/48 (LS 180, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.25×** | +6.3 | 1e-08 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.24×** | +5.8 | 3e-07 | 23/48 (HT-29, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.11× | +4.2 | 0.001 | 10/49 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.012 | 13/49 (PANC-1, C-33 A, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.11× | +3.1 | 0.071 | 18/47 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 10 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 224.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.577×** | -15.3 | 0e+00 | 36/44 (A-427, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.664×** | -10.3 | 1e-22 | 37/49 (HCT15, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.720×** | -9.5 | 3e-19 | 38/48 (KATO III, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.736×** | -8.9 | 1e-16 | 33/48 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.828×** | -7.7 | 1e-12 | 25/48 (HEC-1-A, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.832×** | -7.5 | 5e-12 | 25/49 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.831×** | -5.3 | 7e-06 | 25/49 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 0.841× | -5.0 | 4e-05 | 20/48 (HEC-1-A, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~22% of this change | 0.842× | -4.6 | 3e-04 | 22/45 (NCI-H2030, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | 0.859× | -4.4 | 6e-04 | 20/48 (HOP62, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~9% of this change | 0.859× | -4.4 | 6e-04 | 17/48 (HOP62, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.899× | -4.4 | 6e-04 | 12/48 (HEC-1-A, AsPC-1, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.879× | -3.6 | 0.014 | 19/48 (A-172, SW480, …) | top dose only |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.893× | -3.3 | 0.040 | 6/48 (NCI-H1573, SW1417, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.895× | -3.2 | 0.050 | 11/48 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | 0.902× | -3.0 | 0.093 | 7/48 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | 0.903× | -3.0 | 0.098 | 6/48 (C-33 A, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 224. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 294 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.318× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.487× (z -11.4) |
| [[LS 180 (line)]] | wt | 161 | 8 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.51× (z +16.8) | [[Dinaciclib (drug)]] 5 µM 0.426× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 201 | 9 (2 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.96× (z +15.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.85× (z +14.7) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -19.1) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 120 | 7 (2 ⚠) | 3 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.86× (z +18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +18.0) | [[Panobinostat (drug)]] 5 µM 0.473× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 190 | 7 (4 ⚠) | 3 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.10× (z +20.1) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 2.82× (z +19.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.520× (z -17.0) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.513× (z -12.3) |
| [[PANC-1 (line)]] | alt | 102 | 7 (3 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.29× (z +20.5) | [[Dinaciclib (drug)]] 5 µM 0.534× (z -10.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 143 | 6 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.43× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.25× (z +17.4) | [[Panobinostat (drug)]] 0.5 µM 0.604× (z -10.7) ⚠ cell-cycle shift, explains ~20% of this change |
| [[BT-474 (line)]] | alt | 179 | 4 (1 ⚠) | 2 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +11.3) | [[Lonafarnib (drug)]] 5 µM 0.194× (z -12.4) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 204 | 5 (2 ⚠) | 1 (1 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 1.70× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.503× (z -9.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 135 | 4 (1 ⚠) | 2 (2 ⚠) | [[Digitoxin (drug)]] 5 µM 2.00× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.627× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 106 | 5 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.68× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +16.7) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 211 | 3 (1 ⚠) | 3 (3 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.468× (z -11.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 92.7 | 4 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +15.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.89× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.103× (z -29.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 102 | 4 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 4.86× (z +11.0) | [[Dinaciclib (drug)]] 5 µM 0.305× (z -15.1) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 152 | 5 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.65× (z +14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +12.7) | — |
| [[AsPC-1 (line)]] | alt | 154 | 3 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.25× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.494× (z -9.9) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 131 | 4 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +12.9) | — |
| [[SW 900 (line)]] | alt | 181 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.41× (z +11.9) | — |
| [[A-172 (line)]] | wt | 92.2 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.625× (z -9.5) ⚠ cell-cycle shift, explains ~21% of this change |
| [[A549 (line)]] | wt | 144 | 1 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.65× (z +10.6) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.505× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 267 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -14.7) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 143 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.234× (z -15.1) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.413× (z -9.9) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 95.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.09× (z +9.4) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.163× (z -22.3) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.55× (z +11.3) | — |
| [[SW 1088 (line)]] | alt | 110 | 0 | 2 | — | [[Talc (drug)]] 0.05 µM 0.0764× (z -11.1) |
| [[SW1417 (line)]] | alt | 135 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.21× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +11.7) | — |
| [[SW48 (line)]] | wt | 120 | 2 | 0 | [[TAK-901 (drug)]] 0.05 µM 2.85× (z +9.7) | — |
| [[A498 (line)]] | wt | 89.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.78× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C32 (line)]] | wt | 89.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.07× (z +9.0) | — |
| [[H4 (line)]] | wt | 133 | 1 | 0 | [[Digitoxin (drug)]] 0.5 µM 2.21× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 169 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.413× (z -13.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 89.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.377× (z -11.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 135 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 74.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 162 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 122 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 86.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 88.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 140 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 178 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 159 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 106 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 126 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 162 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 224), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 14 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC24B]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[PGLS]] | +0.61 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[KLHDC10]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[MARCHF5]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[WDR83OS]] ⚠ | +0.56 | +0.31 / +0.60 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TRIM52-AS1]] | +0.54 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[ADGRL3-AS1]] | +0.54 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[PIAS1]] | +0.53 | +0.54 / +0.49 | both halves | 2e-05 |  |
| [[GATD1-DT]] | +0.52 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[MZT2B]] | +0.51 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[ZNF358]] | +0.51 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[USP42]] | +0.51 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ATP6V0D1-DT]] | +0.51 | +0.30 / +0.50 | both halves | 2e-04 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RLIM]] | -0.55 | -0.38 / -0.41 | both halves | 7e-05 |  |
| [[PFKP]] | -0.54 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[CYP27B1]] | -0.54 | -0.51 / -0.49 | both halves | 1e-05 |  |
| [[MIR30DHG]] | -0.53 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SHC1]] | -0.50 | -0.26 / -0.49 | both halves | 3e-04 |  |
| [[LINC03009]] | -0.48 | -0.06 / -0.48 | ⚠ not reproduced | 0.004 |  |
| [[ELK4]] | -0.48 | -0.43 / -0.40 | both halves | 5e-05 |  |
| [[LIN7C]] | -0.48 | -0.40 / -0.42 | both halves | 4e-05 |  |
| [[ATP13A1]] | -0.47 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[NUP188]] | -0.46 | -0.44 / -0.39 | both halves | 6e-05 |  |
| [[RSC1A1]] | -0.46 | -0.38 / -0.40 | both halves | 6e-05 |  |
| [[SPTLC1]] | -0.46 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[RELT]] | -0.45 | -0.23 / -0.47 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises BTBD7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.498). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-44.6, -15.8); signed map (-22.4, -2.0). **Vector** length 80.9, 21.4% of its response variance represented; |z| ≥ 3 in 1,218 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.3 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | -2.1 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | +2.4 | +1.8 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.4 | +1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.2 | -0.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.3 | +0.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.8 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.8 | -15.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.7 | -7.7 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -2.1 | -1.6 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -2.0 | +0.4 |
|  | [[Fluvoxamine (drug)]] 0.5 µM |  | -1.9 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | BTB domain containing 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.12 — chr14:93,237,550-93,333,092 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10648, FUP1 |
| Gene groups (HGNC) | BTB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P203](https://www.uniprot.org/uniprotkb/Q9P203) (BTB/POZ domain-containing protein 7):

> Acts as a mediator of epithelial dynamics and organ branching by promoting cleft progression. Induced following accumulation of fibronectin in forming clefts, leading to local expression of the cell-scattering SNAIL2 and suppression of E-cadherin levels, thereby altering cell morphology and reducing cell-cell adhesion. This stimulates cell separation at the base of forming clefts by local, dynamic intercellular gap formation and promotes cleft progression (By similarity).

**Summary**, from NCBI Gene [55727](https://www.ncbi.nlm.nih.gov/gene/55727):

> Predicted to be involved in regulation of branching involved in salivary gland morphogenesis. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18269](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18269) · Entrez [55727](https://www.ncbi.nlm.nih.gov/gene/55727) · UniProt [Q9P203](https://www.uniprot.org/uniprotkb/Q9P203) · Ensembl [ENSG00000011114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000011114)

## Data

Gene col 224: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 224); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 224, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 224]; `tensor/DDL_lfc|DDL_z.npy` [224]; `embed/gene_vectors.npy` [224]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 224 or target_col == 224). Every well: [[BTBD7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTBD7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
