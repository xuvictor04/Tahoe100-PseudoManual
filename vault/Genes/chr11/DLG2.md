---
symbol: "DLG2"
type: "gene"
col: 7452
ensembl_id: "ENSG00000150672"
name: "discs large MAGUK scaffold protein 2"
location: "11q14.1"
module: 26
arm: "+"
pooled_cpm: 95.03
n_lines_expressing: 48
n_dd_up: 34
n_dd_down: 32
n_dd_up_clean: 32
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# DLG2

*discs large MAGUK scaffold protein 2* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.78× (z +18.6, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 32 drug-doses (6 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.384× (z -11.9, q 8e-30, down in 41 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.444× (z -10.5, q 3e-23, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00907]] (+0.69, fdr 7e-06), [[LIX1-AS1]] (+0.63, fdr 7e-06), [[CXCL13]] (+0.62, fdr 7e-06); moves opposite to [[BRAT1]] (-0.60, fdr 5e-05), [[ACTR5]] (-0.58, fdr 5e-05), [[TRIM35]] (-0.57, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7452.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.78×** | +18.6 | 0e+00 | 42/47 (HepG2/C3A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.91×** | +11.8 | 2e-29 | 34/46 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.40×** | +11.3 | 4e-27 | 41/46 (A-172, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.53×** | +7.8 | 1e-12 | 32/46 (A-172, BT-474, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.78×** | +7.1 | 2e-10 | 39/45 (SW480, NCI-H23, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.7 | 2e-09 | 30/46 (A-172, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.72×** | +5.7 | 8e-07 | 37/46 (SW1417, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.37×** | +5.6 | 1e-06 | 28/46 (A-427, NCI-H23, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +4.9 | 6e-05 | 28/48 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.56×** | +4.7 | 1e-04 | 34/46 (SNU-423, A-172, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.44×** | +4.7 | 2e-04 | 25/46 (A-172, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.3 | 9e-04 | 23/46 (SK-MEL-2, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.88×** | +4.3 | 9e-04 | 30/47 (NCI-H23, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.1 | 0.002 | 24/46 (LoVo, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.44×** | +3.9 | 0.004 | 26/47 (HOP62, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +3.8 | 0.006 | 23/46 (SW1417, HT-29, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7452.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.384×** | -11.9 | 8e-30 | 41/45 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.444×** | -10.5 | 3e-23 | 42/46 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.445×** | -10.4 | 3e-23 | 41/46 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.462×** | -10.0 | 3e-21 | 44/46 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.484×** | -9.4 | 7e-19 | 41/46 (HepG2/C3A, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.529×** | -6.6 | 5e-09 | 35/46 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.608×** | -6.4 | 1e-08 | 34/46 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.668×** | -5.0 | 3e-05 | 31/46 (NCI-H460, SW 900, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.479×** | -5.0 | 4e-05 | 32/47 (RKO, CHP-212, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.638×** | -4.8 | 9e-05 | 27/46 (H4, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.682×** | -4.8 | 1e-04 | 31/46 (hTERT-HPNE, H4, …) | top dose only | plate-row cell shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.690×** | -4.6 | 2e-04 | 27/45 (HepG2/C3A, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.525×** | -4.3 | 6e-04 | 27/46 (SW48, AN3 CA, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.681×** | -4.1 | 0.002 | 26/45 (SW480, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **0.710×** | -4.1 | 0.002 | 27/45 (HepG2/C3A, SW480, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.801×** | -4.1 | 0.002 | 27/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.548×** | -4.1 | 0.002 | 26/46 (NCI-H460, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.004 | 25/46 (NCI-H460, LOX-IMVI, …) | rises with dose |  |
| [[Vilanterol (drug)]] 5 µM |  | **0.819×** | -3.7 | 0.007 | 26/47 (C32, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7452. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 161 | 4 | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.46× (z +27.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.159× (z -18.2) ⚠ toxic · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.372× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 118 | 1 | 7 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.18× (z +19.0) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.128× (z -14.6) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -12.7) |
| [[SW480 (line)]] | alt | 72.4 | 5 | 3 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +14.0) | [[Digitoxin (drug)]] 0.5 µM 0.395× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 75.3 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.228× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.267× (z -10.4) |
| [[PANC-1 (line)]] | alt | 70.2 | 2 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +12.4) | [[Digitoxin (drug)]] 5 µM 0.207× (z -14.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -12.6) |
| [[A-172 (line)]] | wt | 57.3 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.06× (z +18.0) | — |
| [[A-427 (line)]] | wt | 65.7 | 1 (1 ⚠) | 3 (2 ⚠) | [[Selinexor (drug)]] 5 µM 3.35× (z +14.7) ⚠ cell-cycle shift, explains ~47% of this change | [[Digitoxin (drug)]] 5 µM 0.331× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.344× (z -9.2) |
| [[C32 (line)]] | wt | 199 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +14.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -10.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 57.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.27× (z +15.0) | — |
| [[HOP62 (line)]] | alt | 50.0 | 4 | 0 | [[Auranofin (drug)]] 5 µM 4.86× (z +11.9) | — |
| [[hTERT-HPNE (line)]] | wt | 74.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +16.3) | [[Digitoxin (drug)]] 5 µM 0.178× (z -12.3) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 133 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +13.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.234× (z -11.3) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.345× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.213× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 429 | 0 | 4 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.186× (z -10.0) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.241× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 51.4 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.36× (z +16.1) | [[Digitoxin (drug)]] 5 µM 0.182× (z -11.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 110 | 2 | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.94× (z +10.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.210× (z -11.3) ⚠ toxic |
| [[BT-474 (line)]] | alt | 39.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.92× (z +13.0) | — |
| [[COLO 205 (line)]] | alt | 82.8 | 2 | 1 | [[Auranofin (drug)]] 5 µM 4.47× (z +11.6) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.326× (z -8.7) |
| [[HCT15 (line)]] | alt | 51.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.22× (z +18.8) | — |
| [[J82 (line)]] | alt | 31.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.95× (z +18.2) | — |
| [[LS 180 (line)]] | wt | 42.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 116 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.201× (z -11.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 113 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -9.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -8.7) |
| [[HS-578T (line)]] | alt | 61.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.23× (z +13.1) | — |
| [[HT-29 (line)]] | alt | 39.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.08× (z +15.7) | — |
| [[KATO III (line)]] | alt | 51.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.5) | — |
| [[RKO (line)]] | wt | 107 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +13.2) | [[Digitoxin (drug)]] 5 µM 0.282× (z -10.1) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 38.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.4) | — |
| [[SNU-1 (line)]] | wt | 111 | 2 | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.82× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 41.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.75× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 36.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +14.7) | — |
| [[A498 (line)]] | wt | 116 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -12.1) ⚠ toxic |
| [[A549 (line)]] | wt | 42.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 52.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.69× (z +12.4) | — |
| [[CHP-212 (line)]] | wt | 142 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0842× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 50.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.61× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +10.5) | — |
| [[NCI-H1792 (line)]] | alt | 64.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +17.3) | — |
| [[NCI-H2030 (line)]] | alt | 118 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 49.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.57× (z +12.7) | — |
| [[SHP-77 (line)]] | alt | 229 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.260× (z -12.7) ⚠ toxic |
| [[SW 1271 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0637× (z -10.8) ⚠ toxic |
| [[SW48 (line)]] | wt | 230 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.170× (z -10.6) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.1 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 64.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7452), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00907]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[LIX1-AS1]] | +0.63 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CXCL13]] | +0.62 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[NQO1-DT]] | +0.62 | +0.79 / +0.41 | both halves | 4e-05 |  |
| [[LINC01340]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[CAPS2]] | +0.60 | +0.76 / +0.42 | both halves | 4e-05 |  |
| [[TPRG1]] | +0.60 | +0.68 / +0.48 | both halves | 2e-05 |  |
| [[DAB1]] | +0.60 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.60 | +0.67 / +0.57 | both halves | 1e-05 | ⚠ same locus (31.5 kb: neighbours can correlate without regulation) |
| [[CFAP418-AS1]] | +0.59 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[FBXO38-DT]] | +0.59 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[DRAIC]] | +0.59 | +0.66 / +0.46 | both halves | 3e-05 |  |
| [[ARHGAP15]] | +0.58 | +0.71 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRAT1]] | -0.60 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[ACTR5]] | -0.58 | -0.66 / -0.40 | both halves | 5e-05 |  |
| [[TRIM35]] | -0.57 | -0.57 / -0.34 | both halves | 1e-04 |  |
| [[GALNT11]] | -0.56 | -0.61 / -0.42 | both halves | 4e-05 |  |
| [[TTLL4]] | -0.56 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[TMEM242]] | -0.55 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[ZNF341]] | -0.55 | -0.64 / -0.41 | both halves | 4e-05 |  |
| [[ANKS6]] | -0.54 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[ZNF30]] | -0.54 | -0.19 / -0.42 | ⚠ not reproduced | 8e-04 |  |
| [[SMYD4]] | -0.54 | -0.58 / -0.35 | both halves | 1e-04 |  |
| [[MINK1]] | -0.54 | -0.66 / -0.39 | both halves | 5e-05 |  |
| [[COPG2]] | -0.53 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[TXNL4A]] | -0.53 | -0.62 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises DLG2's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 2.47× lower at baseline in the lines without FSIP2-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DLG2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TPRG1]] | B | TPRG1 activity raises DLG2's level | lines that do not express TPRG1 (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without TPRG1 | 0.060 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SYCP2L; maybe low, not absent |
| [[LINC02112]] | B | LINC02112 activity raises DLG2's level | lines that do not express LINC02112 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without LINC02112 | 0.069 | ⚠ within organs, on part of the lines; also absent: DNAH6, IQCM, LINC02932; maybe low, not absent |
| [[COP1-DT]] | B | COP1-DT activity raises DLG2's level | lines that do not express COP1-DT (13) vs lines expressing it (37) | 1.81× lower at baseline in the lines without COP1-DT | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC01234, CNTNAP2, ENSG00000231772; maybe low, not absent |
| [[GUCY1A2]] | B | GUCY1A2 activity raises DLG2's level | lines that do not express GUCY1A2 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without GUCY1A2 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZNF559, ENSG00000229195, LINC02456; maybe low, not absent |
| [[LINC02398]] | B | LINC02398 activity raises DLG2's level | lines that do not express LINC02398 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without LINC02398 | 0.089 | ⚠ within organs, on part of the lines; also absent: ANKRD7, KCNMB2, IGSF11; maybe low, not absent |
| [[FBXO38-DT]] | C | FBXO38-DT activity raises DLG2's level | lines that do not express FBXO38-DT (4) vs lines expressing it (46) | 2.50× lower at baseline in the lines without FBXO38-DT | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FBXL13, MIAT; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.639). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (11.2, 15.4); signed map (24.2, -2.8). **Vector** length 102, 31.7% of its response variance represented; |z| ≥ 3 in 1,430 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.3 | +11.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.8 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.3 | +18.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +7.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +0.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.5 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -10.8 | -11.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -9.9 | -6.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.6 | +3.5 |
|  | [[Panobinostat (drug)]] 5 µM |  | -5.0 | +4.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.9 | -6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.8 | -4.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -3.2 | -4.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | -2.7 | -0.2 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -2.4 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | discs large MAGUK scaffold protein 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:83,455,012-85,628,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PSD-93, PSD93, chapsyn-110, PPP1R58 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Membrane associated guanylate kinases; PDZ domain containing; SH3 domain containing |
| Reactome | 16 pathways, smallest: Ras activation upon Ca2+ influx through NMDA receptor; Unblocking of NMDA receptors, glutamate binding and activation; Negative regulation of NMDA receptor-mediated neuronal transmission |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15700](https://www.uniprot.org/uniprotkb/Q15700) (MAGUK scaffold protein DLG2):

> Required for perception of chronic pain through NMDA receptor signaling. Regulates surface expression of NMDA receptors in dorsal horn neurons of the spinal cord. Interacts with the cytoplasmic tail of NMDA receptor subunits as well as inward rectifying potassium channels. Involved in regulation of synaptic stability at cholinergic synapses. Part of the postsynaptic protein scaffold of excitatory synapses (By similarity).

**Summary**, from NCBI Gene [1740](https://www.ncbi.nlm.nih.gov/gene/1740):

> This gene encodes a member of the membrane-associated guanylate kinase (MAGUK) family. The encoded protein forms a heterodimer with a related family member that may interact at postsynaptic sites to form a multimeric scaffold for the clustering of receptors, ion channels, and associated signaling proteins. Multiple transcript variants encoding different isoforms have been found for this gene. Additional transcript variants have been described, but their full-length nature is not known. …

**Accessions** — [HGNC:2901](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2901) · Entrez [1740](https://www.ncbi.nlm.nih.gov/gene/1740) · UniProt [Q15700](https://www.uniprot.org/uniprotkb/Q15700) · Ensembl [ENSG00000150672](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000150672)

## Data

Gene col 7452: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7452); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7452, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7452]; `tensor/DDL_lfc|DDL_z.npy` [7452]; `embed/gene_vectors.npy` [7452]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7452 or target_col == 7452). Every well: [[DLG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DLG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
