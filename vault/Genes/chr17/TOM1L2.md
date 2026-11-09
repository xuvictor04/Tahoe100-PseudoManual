---
symbol: "TOM1L2"
type: "gene"
col: 10636
ensembl_id: "ENSG00000175662"
name: "target of myb1 like 2 membrane trafficking protein"
location: "17p11.2"
module: 69
arm: "+"
pooled_cpm: 109.75
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 23
n_dd_up_clean: 11
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/069"]
generated_by: "tahoemap"
---

# TOM1L2

*target of myb1 like 2 membrane trafficking protein* — 17p11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.52× (z +24.1, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (9 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.413× (z -23.2, q 0e+00, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.609× (z -13.0, q 1e-36, down in 43 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZER1]] (+0.60, fdr 7e-05), [[GCC2]] (+0.60, fdr 9e-06), [[OSBPL2]] (+0.59, fdr 7e-05); moves opposite to [[ZNF300]] (-0.66, fdr 1e-05), [[AADAT]] (-0.59, fdr 1e-05), [[B3GALNT1]] (-0.58, fdr 1e-05).
> It is in [[Module 069]], a single-armed module (FOXO-mediated transcription).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10636.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.52×** | +24.1 | 0e+00 | 47/48 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.19×** | +20.6 | 0e+00 | 48/48 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.04×** | +18.6 | 0e+00 | 45/48 (SNU-423, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +12.4 | 2e-33 | 28/48 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +12.3 | 1e-32 | 29/49 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +7.5 | 4e-12 | 33/48 (A-172, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.0 | 2e-10 | 30/48 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +6.5 | 4e-09 | 37/49 (HEC-1-A, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.0 | 4e-05 | 24/50 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +4.9 | 5e-05 | 22/48 (A-427, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 1.16× | +3.9 | 0.005 | 13/49 (RKO, C32, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.034 | 13/48 (RKO, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.15× | +3.3 | 0.035 | 14/47 (NCI-H2030, A-172, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.09× | +3.3 | 0.035 | 7/49 (BT-474, LoVo, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.09× | +3.2 | 0.048 | 9/48 (PANC-1, C32, …) | all doses, flat |  |
| [[Bergenin (drug)]] 5 µM |  | 1.09× | +3.2 | 0.057 | 1/49 (SW 1271) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 42 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10636.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.413×** | -23.2 | 0e+00 | 47/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.444×** | -21.3 | 0e+00 | 43/49 (SHP-77, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.545×** | -14.5 | 1e-45 | 37/43 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.578×** | -13.3 | 5e-38 | 33/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -13.0 | 1e-36 | 43/48 (SW480, C-33 A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.395×** | -12.7 | 4e-35 | 47/48 (NCI-H460, SHP-77, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.415×** | -12.0 | 2e-31 | 44/48 (SW1417, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.470×** | -10.3 | 3e-23 | 37/48 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -9.8 | 8e-21 | 37/49 (RPMI-7951, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.496×** | -9.6 | 5e-20 | 39/48 (NCI-H460, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.504×** | -9.4 | 4e-19 | 38/48 (NCI-H1792, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.715×** | -8.8 | 8e-17 | 32/48 (hTERT-HPNE, SW 900, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.805×** | -8.0 | 4e-14 | 26/48 (A549, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.632×** | -6.3 | 1e-08 | 27/48 (RPMI-7951, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.798×** | -5.9 | 1e-07 | 27/48 (HS-578T, LOX-IMVI, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.829×** | -4.9 | 3e-05 | 22/48 (SW1417, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.749×** | -4.8 | 5e-05 | 27/48 (SW1417, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.825×** | -4.8 | 5e-05 | 21/48 (LoVo, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.836× | -4.7 | 8e-05 | 23/48 (LoVo, J82, …) | two highest doses |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.887× | -4.4 | 2e-04 | 6/48 (A498, COLO 205, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.771×** | -4.3 | 4e-04 | 17/49 (SW48, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10636. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 87.6 | 6 | 11 (8 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +18.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.234× (z -20.5) ⚠ unreliable plate only · without an alert: [[venetoclax (drug)]] 5 µM 0.283× (z -9.3) |
| [[HS-578T (line)]] | alt | 117 | 3 | 9 (6 ⚠) | [[Panobinostat (drug)]] 5 µM 2.52× (z +11.2) | [[Dinaciclib (drug)]] 5 µM 0.313× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.479× (z -12.6) |
| [[HOP62 (line)]] | alt | 165 | 3 | 8 (7 ⚠) | [[Panobinostat (drug)]] 5 µM 2.18× (z +10.2) | [[Dinaciclib (drug)]] 5 µM 0.261× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.480× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 68.3 | 6 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +17.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -11.7) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.398× (z -9.3) |
| [[SW480 (line)]] | alt | 168 | 4 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.57× (z +14.6) | [[Dinaciclib (drug)]] 0.05 µM 0.296× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.413× (z -13.6) |
| [[A-172 (line)]] | wt | 117 | 4 | 4 (4 ⚠) | [[Belinostat (drug)]] 5 µM 3.24× (z +15.9) | [[Dinaciclib (drug)]] 5 µM 0.235× (z -18.0) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 164 | 3 | 5 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 2.31× (z +11.4) | [[Dinaciclib (drug)]] 5 µM 0.332× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.459× (z -10.6) |
| [[KATO III (line)]] | alt | 214 | 2 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.33× (z +10.4) | [[Dinaciclib (drug)]] 0.5 µM 0.251× (z -17.0) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.263× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 67.4 | 4 | 4 (4 ⚠) | [[Panobinostat (drug)]] 5 µM 3.31× (z +13.3) | [[Dinaciclib (drug)]] 5 µM 0.299× (z -12.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 119 | 4 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.54× (z +15.6) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -23.3) ⚠ toxic; transcription drop · without an alert: [[c-Kit-IN-1 (drug)]] 5 µM 0.242× (z -9.1) |
| [[A549 (line)]] | wt | 118 | 4 | 3 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.75× (z +13.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.298× (z -15.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.286× (z -8.5) |
| [[HT-29 (line)]] | alt | 83.7 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +12.2) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.239× (z -16.8) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 166 | 2 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.03× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.264× (z -17.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.560× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 72.1 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.06× (z +14.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.483× (z -9.4) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.514× (z -8.6) |
| [[J82 (line)]] | alt | 81.1 | 3 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.04× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.367× (z -12.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 131 | 1 | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +14.1) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.245× (z -17.5) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.403× (z -11.3) |
| [[PANC-1 (line)]] | alt | 68.9 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.93× (z +15.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.334× (z -15.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 47.8 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +17.7) | — |
| [[AsPC-1 (line)]] | alt | 121 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.11× (z +8.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.337× (z -12.8) ⚠ unreliable plate only · without an alert: [[TAK-901 (drug)]] 5 µM 0.241× (z -8.7) |
| [[C32 (line)]] | wt | 101 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.49× (z +14.2) | [[Dinaciclib (drug)]] 0.5 µM 0.402× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.426× (z -8.7) |
| [[LS 180 (line)]] | wt | 181 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -17.2) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 106 | 1 | 4 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.29× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.308× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.135× (z -12.2) |
| [[SNU-423 (line)]] | alt | 75.3 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.34× (z +16.5) | [[Dinaciclib (drug)]] 0.5 µM 0.425× (z -9.7) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 165 | 1 | 4 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 1.95× (z +8.5) | [[Docetaxel (drug)]] 0.05 µM 0.413× (z -11.2) ⚠ transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.210× (z -10.4) |
| [[C-33 A (line)]] | alt | 176 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.289× (z -11.3) |
| [[COLO 205 (line)]] | alt | 116 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.87× (z +10.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.368× (z -10.0) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 99.5 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.71× (z +10.0) | [[Docetaxel (drug)]] 0.05 µM 0.263× (z -13.4) ⚠ transcription drop |
| [[LOX-IMVI (line)]] | wt | 86.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.81× (z +12.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.442× (z -9.7) ⚠ unreliable plate only |
| [[NCI-H23 (line)]] | alt | 65.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 3.75× (z +11.6) | — |
| [[RKO (line)]] | wt | 69.3 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.40× (z +10.8) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.274× (z -11.2) ⚠ unreliable plate only |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.51× (z +10.5) | — |
| [[SW1417 (line)]] | alt | 185 | 0 | 4 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.316× (z -14.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.446× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 46.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.81× (z +13.9) | — |
| [[NCI-H1573 (line)]] | alt | 109 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.32× (z +9.7) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.354× (z -12.0) ⚠ unreliable plate only |
| [[NCI-H1792 (line)]] | alt | 73.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.351× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[EX229 (drug)]] 5 µM 0.241× (z -8.5) |
| [[BT-474 (line)]] | alt | 156 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +13.5) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.428× (z -8.8) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 134 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -12.1) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.164× (z -15.0) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.308× (z -9.8) |
| [[AN3 CA (line)]] | alt | 83.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.128× (z -11.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 112 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -14.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 37.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.71× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 79.3 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.303× (z -9.1) ⚠ unreliable plate only |
| [[SW 1088 (line)]] | alt | 162 | 0 | 1 | — | [[Orlistat (drug)]] 0.5 µM 0.153× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 63.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 118 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 219 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10636), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZER1]] | +0.60 | +0.38 / +0.64 | both halves | 7e-05 | STRING 455 |
| [[GCC2]] | +0.60 | +0.57 / +0.61 | both halves | 9e-06 |  |
| [[OSBPL2]] | +0.59 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[ARID4A]] | +0.59 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[WBP1]] | +0.59 | +0.42 / +0.70 | both halves | 4e-05 |  |
| [[TESK2]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[MAP3K3]] | +0.58 | +0.29 / +0.64 | both halves | 3e-04 |  |
| [[CDK2AP2]] | +0.57 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[DDT]] | +0.57 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[TULP3]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[CCDC186]] | +0.57 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[INAFM1]] | +0.57 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF300]] | -0.66 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[AADAT]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[B3GALNT1]] | -0.58 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[PFKM]] | -0.56 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[BTBD1]] | -0.56 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[RABGGTB]] | -0.55 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[DARS2]] | -0.55 | -0.46 / -0.47 | both halves | 3e-05 |  |
| [[TMEM33]] | -0.54 | -0.46 / -0.57 | both halves | 3e-05 |  |
| [[CCT5]] | -0.54 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[HDDC2]] | -0.54 | -0.27 / -0.56 | both halves | 3e-04 |  |
| [[SLC35B4]] | -0.54 | -0.41 / -0.55 | both halves | 4e-05 |  |
| [[PSPH]] | -0.53 | -0.47 / -0.53 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TOM1L2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 069]] — FOXO-mediated transcription; 71 genes; every member is in the + arm (projection on the module's main direction 0.461). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.6, -44.8); signed map (-15.2, 14.2). **Vector** length 126, 41.1% of its response variance represented; |z| ≥ 3 in 1,550 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.8 | +3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.8 | +18.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +3.7 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.6 | +20.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.9 | +3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | +2.9 | +2.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | +2.7 | +1.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -12.8 | -23.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -10.0 | -8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -8.5 | -13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -8.2 | -13.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -7.7 | -14.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -7.5 | -12.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -6.9 | -12.0 |
|  | [[EX229 (drug)]] 5 µM |  | -6.9 | -9.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -6.7 | -10.3 |

## What is on record

|  |  |
|---|---|
| Name | target of myb1 like 2 membrane trafficking protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p11.2 — chr17:17,843,511-17,972,422 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZVM7](https://www.uniprot.org/uniprotkb/Q6ZVM7) (TOM1-like protein 2):

> Acts as a MYO6/Myosin VI adapter protein that targets myosin VI to endocytic structures. May also play a role in recruiting clathrin to endosomes. May regulate growth factor-induced mitogenic signaling.

**Summary**, from NCBI Gene [146691](https://www.ncbi.nlm.nih.gov/gene/146691):

> This gene belongs to a small gene family whose members have an N-terminal VHS domain followed by a GAT domain; domains which typically participate in vesicular trafficking. The canonical protein encoded by this gene also has a C-terminal clathrin binding motif. This protein has been shown to interact with Tollip, clathrin and ubiquitin and is thought to play a role in endosomal sorting. This gene resides in the 3.7 Mb deletion of chromosome region 17p11.2 that is associated with Smith-Magenis …

**Accessions** — [HGNC:11984](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11984) · Entrez [146691](https://www.ncbi.nlm.nih.gov/gene/146691) · UniProt [Q6ZVM7](https://www.uniprot.org/uniprotkb/Q6ZVM7) · Ensembl [ENSG00000175662](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175662)

## Data

Gene col 10636: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10636); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10636, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10636]; `tensor/DDL_lfc|DDL_z.npy` [10636]; `embed/gene_vectors.npy` [10636]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10636 or target_col == 10636). Every well: [[TOM1L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TOM1L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
