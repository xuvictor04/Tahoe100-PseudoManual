---
symbol: "CREBRF"
type: "gene"
col: 8950
ensembl_id: "ENSG00000164463"
name: "CREB3 regulatory factor"
location: "5q35.1"
module: 69
arm: "+"
pooled_cpm: 123.54
n_lines_expressing: 50
n_dd_up: 29
n_dd_down: 34
n_dd_up_clean: 24
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# CREBRF

*CREB3 regulatory factor* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.06× (z +24.7, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (13 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.132× (z -31.6, q 0e+00, down in 48 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 0.169× (z -14.5, q 3e-45, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL24]] (+0.85, fdr 7e-06), [[HBP1]] (+0.82, fdr 8e-06), [[PIK3CA]] (+0.77, fdr 7e-06); moves opposite to [[RNGTT]] (-0.66, fdr 7e-06), [[EIPR1]] (-0.64, fdr 7e-06), [[PDSS1]] (-0.60, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[MTOR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8950.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.06×** | +24.7 | 0e+00 | 47/48 (NCI-H2347, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.93×** | +16.8 | 0e+00 | 47/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +15.9 | 0e+00 | 46/49 (LoVo, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.68×** | +15.4 | 0e+00 | 47/48 (NCI-H460, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.16×** | +12.1 | 2e-31 | 45/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.93×** | +10.3 | 7e-23 | 43/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.95×** | +10.1 | 7e-22 | 37/48 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +8.6 | 5e-16 | 35/48 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.67×** | +8.0 | 6e-14 | 45/49 (NCI-H2347, HT-29, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.12×** | +6.1 | 5e-08 | 32/48 (NCI-H2347, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +5.7 | 8e-07 | 32/47 (NCI-H460, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +5.1 | 1e-05 | 31/48 (HS-578T, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 2e-04 | 28/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.3 | 6e-04 | 31/50 (RKO, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 9e-04 | 26/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 5 µM |  | **1.20×** | +4.1 | 0.001 | 25/49 (PANC-1, Hs 766T, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.30×** | +4.1 | 0.001 | 26/48 (RPMI-7951, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8950.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.132×** | -31.6 | 0e+00 | 48/48 (HT-29, NCI-H2347, …) | all doses, flat |  |
| [[EX229 (drug)]] 5 µM |  | **0.169×** | -14.5 | 3e-45 | 47/48 (NCI-H2347, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.173×** | -14.3 | 4e-44 | 48/48 (SW1417, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.186×** | -13.7 | 1e-40 | 48/48 (AsPC-1, SW1417, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.229×** | -12.0 | 4e-31 | 48/48 (HT-29, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.230×** | -12.0 | 5e-31 | 48/48 (SW1417, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.409×** | -9.9 | 3e-21 | 47/48 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.552×** | -8.7 | 2e-16 | 45/48 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.576×** | -8.6 | 6e-16 | 40/48 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.623×** | -7.3 | 1e-11 | 39/48 (AsPC-1, LOX-IMVI, …) | all doses, stronger at high dose | position effect removed |
| [[EX229 (drug)]] 0.5 µM |  | **0.566×** | -6.3 | 1e-08 | 44/49 (SW1417, MIA PaCa-2, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.667×** | -6.3 | 2e-08 | 37/48 (SNU-423, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.668×** | -6.3 | 2e-08 | 38/48 (COLO 205, AsPC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Abemaciclib (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.678×** | -6.0 | 7e-08 | 40/48 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.483×** | -5.9 | 1e-07 | 40/47 (AsPC-1, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.789×** | -5.2 | 8e-06 | 34/48 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.711×** | -5.0 | 2e-05 | 35/48 (LoVo, SW48, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.672×** | -4.4 | 3e-04 | 32/48 (SW 1271, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | **0.785×** | -3.8 | 0.004 | 29/49 (HEC-1-A, A498, …) | inconsistent across doses | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.786×** | -3.7 | 0.005 | 24/48 (Panc 03.27, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.64 per unit of S-phase module lfc, +0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8950. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 192 | 10 (1 ⚠) | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.57× (z +33.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.102× (z -31.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.106× (z -16.3) |
| [[NCI-H460 (line)]] | wt | 67.7 | 13 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.57× (z +27.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -17.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.150× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 134 | 3 (1 ⚠) | 11 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +14.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.108× (z -26.4) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0680× (z -16.7) |
| [[HT-29 (line)]] | alt | 182 | 5 (1 ⚠) | 9 (4 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +11.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0625× (z -32.7) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0826× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 127 | 5 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0780× (z -26.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0901× (z -13.2) |
| [[NCI-H1792 (line)]] | alt | 86.4 | 6 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.59× (z +22.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0640× (z -28.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.133× (z -10.8) |
| [[SW 900 (line)]] | alt | 259 | 6 (1 ⚠) | 7 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.95× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -20.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0894× (z -12.9) |
| [[HS-578T (line)]] | alt | 128 | 7 (1 ⚠) | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +21.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.131× (z -21.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.154× (z -10.4) |
| [[SNU-423 (line)]] | alt | 243 | 4 (1 ⚠) | 8 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +21.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -22.7) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.137× (z -12.1) |
| [[SW1417 (line)]] | alt | 202 | 5 (1 ⚠) | 7 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +16.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0989× (z -30.3) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.0838× (z -17.0) |
| [[BT-474 (line)]] | alt | 90.5 | 9 (2 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.09× (z +14.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.173× (z -13.7) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.123× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 143 | 2 | 9 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +11.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.127× (z -22.8) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.117× (z -12.4) |
| [[COLO 205 (line)]] | alt | 176 | 6 (2 ⚠) | 5 (2 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 6.12× (z +18.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.133× (z -20.8) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.103× (z -12.3) |
| [[LoVo (line)]] | wt | 89.6 | 7 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.31× (z +17.4) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.116× (z -22.1) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.248× (z -13.5) |
| [[PANC-1 (line)]] | alt | 99.0 | 5 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +17.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.159× (z -20.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.168× (z -10.6) |
| [[A-172 (line)]] | wt | 129 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +27.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -14.6) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.168× (z -9.7) |
| [[KATO III (line)]] | alt | 108 | 6 (1 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +17.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0723× (z -22.9) ⚠ unreliable plate only · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.154× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 162 | 2 | 7 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.32× (z +13.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0823× (z -27.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.109× (z -12.8) |
| [[hTERT-HPNE (line)]] | wt | 116 | 7 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +15.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.150× (z -16.5) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 101 | 3 (1 ⚠) | 5 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.70× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.116× (z -22.5) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.149× (z -10.4) |
| [[A549 (line)]] | wt | 135 | 1 | 6 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.50× (z +14.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.104× (z -25.5) ⚠ unreliable plate only · without an alert: [[TAK-733 (drug)]] 5 µM 0.119× (z -12.5) |
| [[H4 (line)]] | wt | 94.4 | 6 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +15.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.129× (z -13.9) ⚠ unreliable plate only |
| [[HOP62 (line)]] | alt | 106 | 6 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +14.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.127× (z -16.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 157 | 2 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.29× (z +12.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0662× (z -27.8) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.0948× (z -12.6) |
| [[RKO (line)]] | wt | 126 | 3 (1 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.33× (z +12.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.105× (z -18.5) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.299× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 186 | 4 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +25.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.130× (z -23.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.197× (z -9.7) |
| [[HEC-1-A (line)]] | alt | 135 | 2 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.125× (z -20.8) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.180× (z -9.0) |
| [[Hs 766T (line)]] | wt | 128 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +20.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.144× (z -18.3) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.138× (z -9.8) |
| [[J82 (line)]] | alt | 98.3 | 5 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.70× (z +18.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.136× (z -13.6) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 84.3 | 3 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.96× (z +15.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.175× (z -14.1) ⚠ unreliable plate only · without an alert: [[Abemaciclib (drug)]] 5 µM 0.114× (z -9.2) |
| [[CHP-212 (line)]] | wt | 145 | 3 | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.43× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.114× (z -14.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.0427× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 114 | 3 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +11.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.190× (z -14.9) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 0.05 µM 0.343× (z -9.1) |
| [[LS 180 (line)]] | wt | 75.3 | 4 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 5.21× (z +13.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 4.85× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.156× (z -15.2) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 68.5 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 4.64× (z +12.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.230× (z -12.2) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 103 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.154× (z -15.5) ⚠ unreliable plate only |
| [[NCI-H2030 (line)]] | alt | 134 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +15.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.142× (z -16.5) ⚠ unreliable plate only |
| [[SHP-77 (line)]] | alt | 92.0 | 0 | 4 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.103× (z -19.7) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.142× (z -8.8) |
| [[C-33 A (line)]] | alt | 34.0 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.71× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.165× (z -9.8) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 84.8 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +13.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.183× (z -14.3) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 175 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +15.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.182× (z -15.6) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.145× (z -9.2) |
| [[SW48 (line)]] | wt | 54.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.55× (z +10.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.124× (z -11.9) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 108 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +11.9) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.140× (z -14.4) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 134 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.45× (z +15.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.187× (z -12.1) ⚠ unreliable plate only |
| [[SNU-1 (line)]] | wt | 115 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0774× (z -18.2) ⚠ unreliable plate only · without an alert: [[EX229 (drug)]] 5 µM 0.0916× (z -8.9) |
| [[SW 1088 (line)]] | alt | 112 | 0 | 2 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0489× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Thymol (drug)]] 0.5 µM 0.0951× (z -8.7) |
| [[AN3 CA (line)]] | alt | 202 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.107× (z -13.3) ⚠ unreliable plate only |
| [[NCI-H661 (line)]] | alt | 88.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.137× (z -9.1) ⚠ unreliable plate only |
| [[SW 1271 (line)]] | alt | 224 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.135× (z -11.8) ⚠ unreliable plate only |
| [[NCI-H2122 (line)]] | alt | 168 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 139 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8950), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL24]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | STRING 759 |
| [[HBP1]] | +0.82 | +0.57 / +0.86 | both halves | 8e-06 |  |
| [[PIK3CA]] | +0.77 | +0.59 / +0.84 | both halves | 7e-06 |  |
| [[SLU7]] | +0.76 | +0.60 / +0.80 | both halves | 7e-06 |  |
| [[UBXN7]] | +0.76 | +0.62 / +0.85 | both halves | 7e-06 |  |
| [[ATOSA]] | +0.75 | +0.63 / +0.74 | both halves | 7e-06 |  |
| [[WDR48]] | +0.74 | +0.62 / +0.87 | both halves | 7e-06 |  |
| [[JMY]] | +0.73 | +0.55 / +0.80 | both halves | 1e-05 |  |
| [[RB1CC1]] | +0.73 | +0.60 / +0.81 | both halves | 7e-06 |  |
| [[UBN2]] | +0.72 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[NBR1]] | +0.71 | +0.54 / +0.77 | both halves | 1e-05 |  |
| [[YPEL5]] | +0.71 | +0.49 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNGTT]] | -0.66 | -0.72 / -0.62 | both halves | 7e-06 |  |
| [[EIPR1]] | -0.64 | -0.72 / -0.60 | both halves | 7e-06 |  |
| [[PDSS1]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[POLR3G]] | -0.59 | -0.46 / -0.56 | both halves | 2e-05 |  |
| [[PGAM5]] | -0.58 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[AGK]] | -0.58 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[POP1]] | -0.58 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[EIF2B3]] | -0.58 | -0.37 / -0.55 | both halves | 8e-05 |  |
| [[POLR3H]] | -0.57 | -0.56 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTOR]] | B | MTOR activity lowers CREBRF's level | compounds that target MTOR: 5 of 8 raise it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 5.3% of all compounds | 0.026 | ⚠ off-target possible; 5 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.904). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-0.8, -44.3); signed map (-13.6, 9.7). **Vector** length 164, 67.8% of its response variance represented; |z| ≥ 3 in 1,949 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +14.3 | +15.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.0 | +5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +4.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.2 | +4.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.8 | +2.4 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +5.7 | +4.1 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +5.5 | +4.1 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.9 | +3.4 |
|  | [[AZD-8055 (drug)]] 5 µM |  | +4.8 | +3.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -26.6 | -31.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -15.6 | -14.3 |
|  | [[EX229 (drug)]] 5 µM |  | -14.8 | -14.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -14.8 | -13.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -14.2 | -12.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -12.9 | -12.0 |

## What is on record

|  |  |
|---|---|
| Name | CREB3 regulatory factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:173,056,352-173,139,284 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRF; previously C5orf41 |
| Gene groups (HGNC) | Basic leucine zipper proteins |
| Reactome | 4 pathways, smallest: CREB3 factors activate genes; Unfolded Protein Response (UPR); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUR6](https://www.uniprot.org/uniprotkb/Q8IUR6) (CREB3 regulatory factor):

> Acts as a negative regulator of the endoplasmic reticulum stress response or unfolded protein response (UPR). Represses the transcriptional activity of CREB3 during the UPR. Recruits CREB3 into nuclear foci.

**Summary**, from NCBI Gene [153222](https://www.ncbi.nlm.nih.gov/gene/153222):

> Enables DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II transcription regulatory region sequence-specific DNA binding activity. Involved in several processes, including negative regulation of endoplasmic reticulum unfolded protein response; positive regulation of protein catabolic process; and regulation of transcription by RNA polymerase II. Located in cytoplasm and nuclear body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24050](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24050) · Entrez [153222](https://www.ncbi.nlm.nih.gov/gene/153222) · UniProt [Q8IUR6](https://www.uniprot.org/uniprotkb/Q8IUR6) · Ensembl [ENSG00000164463](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164463)

## Data

Gene col 8950: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8950); `tables/drug_effects.parquet` (70 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8950, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8950]; `tensor/DDL_lfc|DDL_z.npy` [8950]; `embed/gene_vectors.npy` [8950]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8950 or target_col == 8950). Every well: [[CREBRF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CREBRF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
