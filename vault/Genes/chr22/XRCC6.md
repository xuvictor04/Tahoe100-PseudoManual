---
symbol: "XRCC6"
type: "gene"
col: 12202
ensembl_id: "ENSG00000196419"
name: "X-ray repair cross complementing 6"
location: "22q13.2"
module: 25
arm: "+"
pooled_cpm: 131.56
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# XRCC6

*X-ray repair cross complementing 6* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.88× (z +26.1, q 0e+00, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 5.58× (z +17.3, q 0e+00, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.734× (z -5.9, q 2e-06, down in 35 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Altretamine (drug)]] 0.5 µM in 1 line (SW 1088 0.150×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAPRIN1]] (+0.69, fdr 7e-06), [[COPS6]] (+0.68, fdr 7e-06), [[CCT7]] (+0.68, fdr 7e-06); moves opposite to [[ARID3A]] (-0.68, fdr 7e-06), [[CDKN1C]] (-0.67, fdr 7e-06), [[INAFM1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 22 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.88×** | +26.1 | 0e+00 | 49/49 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.41×** | +22.7 | 0e+00 | 43/44 (HS-578T, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.17×** | +20.5 | 0e+00 | 45/45 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **5.58×** | +17.3 | 0e+00 | 48/49 (COLO 205, LoVo, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.22×** | +11.8 | 7e-30 | 45/48 (HEC-1-A, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +8.8 | 2e-16 | 44/48 (NCI-H1792, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.57×** | +8.7 | 4e-16 | 45/48 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +8.7 | 4e-16 | 46/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.47×** | +7.1 | 6e-11 | 38/50 (MIA PaCa-2, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~47% of this change | **1.43×** | +6.7 | 2e-09 | 40/47 (C32, NCI-H1573, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.41×** | +6.4 | 7e-09 | 32/48 (NCI-H1792, NCI-H1573, …) | two highest doses | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.7 | 5e-07 | 25/48 (A-172, SW1417, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.34×** | +5.7 | 6e-07 | 37/48 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.23×** | +5.6 | 7e-07 | 29/49 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.43×** | +5.5 | 1e-06 | 37/48 (NCI-H1792, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.006 | 24/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Sulfatinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.028 | 15/49 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.17× | +3.1 | 0.038 | 19/48 (HS-578T, Panc 03.27, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | 1.18× | +3.0 | 0.042 | 17/48 (HS-578T, A549, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | 1.17× | +3.0 | 0.042 | 14/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12202.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Altretamine (drug)]] 0.5 µM in 1 line (SW 1088 0.150×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.734×** | -5.9 | 2e-06 | 35/49 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -5.3 | 4e-05 | 23/48 (SK-MEL-2, SW1417, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.839× | -3.2 | 0.22 | 22/48 (A-427, LOX-IMVI, …) | top dose only |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | 0.894× | -3.0 | 0.26 | 2/48 (LS 180, SW48) | rises with dose |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.854× | -3.0 | 0.26 | 17/48 (HepG2/C3A, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.25 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 121 | 13 (8 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +17.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 10.2× (z +14.9) | — |
| [[HOP62 (line)]] | alt | 139 | 9 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.47× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 70.1 | 9 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.54× (z +22.4) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.07× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 108 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.79× (z +23.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.96× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 122 | 8 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.58× (z +20.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.95× (z +9.8) | — |
| [[C32 (line)]] | wt | 151 | 7 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.17× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 152 | 7 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.77× (z +21.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.06× (z +12.7) | — |
| [[A549 (line)]] | wt | 112 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +19.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.96× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 95.4 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.13× (z +11.3) | — |
| [[LoVo (line)]] | wt | 99.5 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +21.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 9.98× (z +15.1) | — |
| [[LOX-IMVI (line)]] | wt | 78.3 | 6 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.77× (z +18.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.68× (z +10.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 121 | 6 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.48× (z +19.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.67× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 85.1 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +18.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.52× (z +11.4) | — |
| [[COLO 205 (line)]] | alt | 90.2 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 24.5× (z +16.0) | — |
| [[HEC-1-A (line)]] | alt | 146 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.60× (z +13.4) | — |
| [[KATO III (line)]] | alt | 165 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.01× (z +21.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.79× (z +12.0) | — |
| [[LS 180 (line)]] | wt | 113 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +17.5) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 8.30× (z +12.3) | — |
| [[NCI-H2030 (line)]] | alt | 204 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +17.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.34× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 135 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +14.6) ⚠ cell-cycle shift, explains ~23% of this change | — |
| [[NCI-H460 (line)]] | wt | 102 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +23.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.22× (z +12.6) | — |
| [[SK-MEL-2 (line)]] | alt | 509 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.50× (z +19.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.44× (z +11.8) | — |
| [[SW 900 (line)]] | alt | 114 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +13.2) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.02× (z +10.4) | — |
| [[SW480 (line)]] | alt | 160 | 5 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.62× (z +20.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.73× (z +13.6) | — |
| [[A-172 (line)]] | wt | 83.2 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.54× (z +17.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.54× (z +9.3) | — |
| [[A498 (line)]] | wt | 175 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.83× (z +21.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.30× (z +9.8) | — |
| [[Hs 766T (line)]] | wt | 127 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.22× (z +16.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.67× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 80.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.54× (z +9.5) | — |
| [[hTERT-HPNE (line)]] | wt | 106 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +14.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.40× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 167 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +16.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.09× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 100 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.88× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.48× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 89.0 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +16.7) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.07× (z +9.4) | — |
| [[A-427 (line)]] | wt | 126 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +13.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 93.4 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 4.78× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 112 | 3 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 6.12× (z +10.5) | — |
| [[C-33 A (line)]] | alt | 169 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.25× (z +10.3) | — |
| [[H4 (line)]] | wt | 145 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.43× (z +10.1) | — |
| [[HCT15 (line)]] | alt | 175 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.11× (z +9.0) | — |
| [[J82 (line)]] | alt | 101 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +15.8) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 148 | 3 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +14.0) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 6.81× (z +11.8) | — |
| [[HepG2_C3A (line)]] | wt | 109 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +11.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 184 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +14.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 122 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 7.66× (z +10.1) | — |
| [[SW48 (line)]] | wt | 138 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.02× (z +12.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 175 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW 1088 (line)]] | alt | 142 | 0 | 1 | — | [[Altretamine (drug)]] 0.5 µM 0.150× (z -9.0) |
| [[CHP-212 (line)]] | wt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 180 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 97.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPRIN1]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[COPS6]] | +0.68 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[CCT7]] | +0.68 | +0.70 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 423 |
| [[API5]] | +0.68 | +0.76 / +0.63 | both halves | 7e-06 |  |
| [[NUP155]] | +0.68 | +0.70 / +0.64 | both halves | 7e-06 | pathway: HIV Infection |
| [[KARS1]] | +0.66 | +0.59 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[USP5]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[ERH]] | +0.66 | +0.65 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1 |
| [[SF3B4]] | +0.66 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[EIF2S1]] | +0.65 | +0.67 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[XRCC5]] | +0.64 | +0.67 / +0.62 | both halves | 7e-06 | same gene group; pathway: HALLMARK_ANDROGEN_RESPONSE; STRING 999 |
| [[COPS3]] | +0.64 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID3A]] | -0.68 | -0.58 / -0.68 | both halves | 7e-06 |  |
| [[CDKN1C]] | -0.67 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.67 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[CSKMT]] | -0.66 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[SNHG19]] | -0.65 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[ZFAND2B]] | -0.65 | -0.51 / -0.64 | both halves | 1e-05 |  |
| [[SNHG7]] | -0.64 | -0.47 / -0.70 | both halves | 2e-05 |  |
| [[HOTAIRM1]] | -0.63 | -0.57 / -0.66 | both halves | 9e-06 |  |
| [[EIF1B]] | -0.63 | -0.57 / -0.64 | both halves | 1e-05 |  |
| [[SNHG12]] | -0.63 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[SNHG9]] | -0.63 | -0.57 / -0.64 | both halves | 8e-06 |  |
| [[CDKN2D]] | -0.62 | -0.67 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers XRCC6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.653). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-32.4, -31.7); signed map (-14.0, -43.6). **Vector** length 105, 37.0% of its response variance represented; |z| ≥ 3 in 1,155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +9.2 | +17.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.4 | +11.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +5.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.0 | +8.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +5.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.9 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +1.7 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.7 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -4.2 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.7 | -5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.5 | -0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +3.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -3.0 | +0.8 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -2.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | X-ray repair cross complementing 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:41,621,163-41,664,048 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D22S731, D22S671, KU70, ML8; previously G22P1 |
| Gene groups (HGNC) | Helicases; DNA-(apurinic or apyrimidinic site) lyases |
| Hallmark sets | ANDROGEN_RESPONSE, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 14 pathways, smallest: 2-LTR circle formation; Integration of provirus; IRF3-mediated induction of type I IFN |
| Matched by | ensembl_id |

**Function**, from UniProt [P12956](https://www.uniprot.org/uniprotkb/P12956) (DNA repair protein Ku70):

> DNA-binding protein critical for the DNA damage response, specifically in repairing double-strand breaks (DSBs) via the classical non-homologous end joining (NHEJ) pathway. It forms a heterodimer with XRCC5 (Ku80), creating the Ku70:Ku80 heterodimer (Ku complex), which serves as a DNA end-binding complex. It primarily binds DSBs and recruits essential repair factors, assembling the core long-range NHEJ complex to facilitate the alignment and ligation of broken DNA ends. This pathway ensures the …

**Summary**, from NCBI Gene [2547](https://www.ncbi.nlm.nih.gov/gene/2547):

> The p70/p80 autoantigen is a nuclear complex consisting of two subunits with molecular masses of approximately 70 and 80 kDa. The complex functions as a single-stranded DNA-dependent ATP-dependent helicase. The complex may be involved in the repair of nonhomologous DNA ends such as that required for double-strand break repair, transposition, and V(D)J recombination. High levels of autoantibodies to p70 and p80 have been found in some patients with systemic lupus erythematosus. [provided by …

**Accessions** — [HGNC:4055](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4055) · Entrez [2547](https://www.ncbi.nlm.nih.gov/gene/2547) · UniProt [P12956](https://www.uniprot.org/uniprotkb/P12956) · Ensembl [ENSG00000196419](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196419)

## Data

Gene col 12202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12202); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12202]; `tensor/DDL_lfc|DDL_z.npy` [12202]; `embed/gene_vectors.npy` [12202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12202 or target_col == 12202). Every well: [[XRCC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/XRCC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
