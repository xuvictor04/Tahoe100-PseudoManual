---
symbol: "CERS2"
type: "gene"
col: 6739
ensembl_id: "ENSG00000143418"
name: "ceramide synthase 2"
location: "1q21.3"
module: 126
arm: "+"
pooled_cpm: 38.09
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# CERS2

*ceramide synthase 2* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.09× (z +26.0, q 0e+00, up in 37 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 1.50× (z +7.8, q 5e-13, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.355× (z -19.9, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LY6G5B]] (+0.72, fdr 1e-05), [[MOB1A]] (+0.71, fdr 1e-05), [[HCFC1]] (+0.71, fdr 7e-06); moves opposite to [[PITPNA-AS1]] (-0.70, fdr 7e-06), [[SNAPIN]] (-0.66, fdr 1e-05), [[KBTBD7]] (-0.66, fdr 7e-06).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[KCTD15]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6739.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.09×** | +26.0 | 0e+00 | 37/38 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.83×** | +25.8 | 0e+00 | 45/45 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.87×** | +18.7 | 0e+00 | 43/43 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +8.9 | 1e-16 | 40/46 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.50×** | +7.8 | 5e-13 | 38/48 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +7.6 | 2e-12 | 37/46 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.45×** | +7.2 | 6e-11 | 30/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.35×** | +5.8 | 5e-07 | 28/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +4.9 | 7e-05 | 24/47 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +4.6 | 3e-04 | 18/48 (PANC-1, NCI-H1792, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.002 | 25/48 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.0 | 0.003 | 16/48 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.014 | 16/48 (A-172, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +3.2 | 0.051 | 10/40 (SHP-77, C32, …) | top dose only | noisy plate (z scaled) |
| [[Erlotinib (drug)]] 5 µM |  | 1.19× | +3.2 | 0.062 | 9/47 (SW48, SW480, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.12× | +3.1 | 0.068 | 14/48 (A-172, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.36×** | +3.1 | 0.069 | 6/48 (NCI-H460, NCI-H1792, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6739.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.355×** | -19.9 | 0e+00 | 47/48 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.369×** | -19.2 | 0e+00 | 46/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.546×** | -16.4 | 0e+00 | 43/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.452×** | -15.2 | 0e+00 | 44/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.553×** | -11.4 | 8e-28 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.686×** | -10.2 | 2e-22 | 39/48 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.492×** | -7.1 | 9e-11 | 38/48 (PANC-1, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.698×** | -6.3 | 2e-08 | 24/48 (A-172, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.722×** | -6.0 | 1e-07 | 29/48 (SNU-1, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.727×** | -5.6 | 1e-06 | 27/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.793×** | -4.4 | 5e-04 | 22/47 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.793×** | -4.3 | 9e-04 | 20/47 (A-172, SHP-77, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.802×** | -4.1 | 0.002 | 18/47 (NCI-H23, A549, …) | inconsistent across doses |  |
| [[Penfluridol (drug)]] 5 µM |  | 0.834× | -3.3 | 0.034 | 10/47 (A-172, HepG2/C3A, …) | top dose only | position effect removed |
| [[Demeclocycline (drug)]] 5 µM |  | 0.887× | -3.3 | 0.043 | 4/48 (SNU-1, SW1417, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6739. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 81.8 | 4 (3 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +12.9) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.303× (z -13.8) |
| [[NCI-H460 (line)]] | wt | 50.4 | 3 (3 ⚠) | 6 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +16.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.263× (z -16.5) |
| [[PANC-1 (line)]] | alt | 43.5 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +22.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -16.6) |
| [[SW480 (line)]] | alt | 29.1 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +15.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.286× (z -15.3) |
| [[A-427 (line)]] | wt | 37.0 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 6.99× (z +16.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.0) |
| [[HOP62 (line)]] | alt | 35.4 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +16.7) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.283× (z -12.6) |
| [[J82 (line)]] | alt | 33.9 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.39× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -11.5) |
| [[MIA PaCa-2 (line)]] | alt | 47.6 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.219× (z -13.2) |
| [[A498 (line)]] | wt | 50.1 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.90× (z +18.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.474× (z -8.7) |
| [[Hs 766T (line)]] | wt | 45.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +12.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.330× (z -9.4) |
| [[KATO III (line)]] | alt | 26.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.85× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.278× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 53.6 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.163× (z -17.5) |
| [[RKO (line)]] | wt | 44.7 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +9.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -12.3) |
| [[A549 (line)]] | wt | 46.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.39× (z +13.3) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.240× (z -12.8) |
| [[HepG2_C3A (line)]] | wt | 43.9 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -11.0) |
| [[HT-29 (line)]] | alt | 40.4 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.84× (z +15.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.342× (z -9.6) |
| [[LoVo (line)]] | wt | 28.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.43× (z +16.0) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.380× (z -8.5) |
| [[LOX-IMVI (line)]] | wt | 36.8 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.43× (z +12.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.262× (z -11.7) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.52× (z +11.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.294× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 47.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.38× (z +11.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.361× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 31.3 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.05× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -9.0) |
| [[Panc 03.27 (line)]] | alt | 27.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.09× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.4) |
| [[SHP-77 (line)]] | alt | 44.3 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +11.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.273× (z -10.8) |
| [[SW 900 (line)]] | alt | 39.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.74× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.5) |
| [[AsPC-1 (line)]] | alt | 49.8 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.10× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.219× (z -13.6) |
| [[CFPAC-1 (line)]] | alt | 29.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.22× (z +10.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 28.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.49× (z +9.0) ⚠ toxic; transcription drop | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.107× (z -11.2) |
| [[HS-578T (line)]] | alt | 24.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.24× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 31.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -8.9) |
| [[LS 180 (line)]] | wt | 29.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.65× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 33.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.50× (z +16.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.19× (z +10.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 38.1 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +9.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.247× (z -11.2) |
| [[SW48 (line)]] | wt | 36.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -9.9) |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.154× (z -12.1) |
| [[C-33 A (line)]] | alt | 32.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.177× (z -11.4) |
| [[C32 (line)]] | wt | 25.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.83× (z +10.2) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 31.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.87× (z +12.0) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 34.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.0) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 30.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.49× (z +11.4) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 35.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.9) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 49.3 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0704× (z -12.9) ⚠ toxic; unreliable plate only |
| [[SNU-1 (line)]] | wt | 46.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.270× (z -8.6) |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6739), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LY6G5B]] | +0.72 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[MOB1A]] | +0.71 | +0.54 / +0.67 | both halves | 1e-05 |  |
| [[HCFC1]] | +0.71 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[CTSZ]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[UBQLN4]] | +0.70 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[KLC2]] | +0.70 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[U2AF2]] | +0.69 | +0.39 / +0.72 | both halves | 5e-05 |  |
| [[MSL3]] | +0.68 | +0.58 / +0.58 | both halves | 7e-06 |  |
| [[SELENON]] | +0.67 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[DVL3]] | +0.66 | +0.40 / +0.67 | both halves | 5e-05 |  |
| [[WASH8P]] ⚠ | +0.66 | +0.54 / +0.63 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[SNHG22]] | +0.66 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[MTA2]] | +0.66 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 6 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PITPNA-AS1]] | -0.70 | -0.62 / -0.60 | both halves | 7e-06 |  |
| [[SNAPIN]] | -0.66 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[KBTBD7]] | -0.66 | -0.65 / -0.63 | both halves | 7e-06 |  |
| [[MTLN]] ⚠ | -0.65 | -0.40 / -0.63 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RP9]] | -0.64 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[ATP5PO]] ⚠ | -0.64 | -0.54 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNF10]] | -0.64 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[SUMO4]] | -0.64 | -0.54 / -0.68 | both halves | 1e-05 |  |
| [[TCEAL8]] | -0.63 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[CTR9]] | -0.63 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[NTHL1]] | -0.63 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[NDUFA7]] | -0.63 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[MED19]] | -0.63 | -0.61 / -0.67 | both halves | 7e-06 |  |
| [[MPHOSPH10]] | -0.62 | -0.46 / -0.56 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCTD15]] | B | KCTD15 activity raises CERS2's level | lines that do not express KCTD15 (7) vs lines expressing it (43) | 1.28× lower at baseline in the lines without KCTD15 | 0.067 | ⚠ within organs, on part of the lines; also absent: EGFL7, SEPTIN3, EEF1A2 |
| [[CCDC110]] | B | CCDC110 activity lowers CERS2's level | lines that do not express CCDC110 (5) vs lines expressing it (45) | 1.35× higher at baseline in the lines without CCDC110 | 0.072 | ⚠ within organs, on part of the lines; also absent: MLF1, CDC42EP3, C1orf216; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.851). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.5, -23.9); signed map (-12.7, -35.9). **Vector** length 97.4, 25.7% of its response variance represented; |z| ≥ 3 in 1,076 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +26.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +18.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +6.7 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +25.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | +1.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.8 | +2.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Budesonide (drug)]] 5 µM |  | +2.8 | +1.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.4 | -16.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -10.2 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.2 | -15.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -19.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.6 | -0.2 |
|  | [[Azithromycin (hydrate) (drug)]] 5 µM |  | -2.3 | -0.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -4.3 |
|  | [[Silodosin (drug)]] 5 µM |  | -2.1 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ceramide synthase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,960,583-150,975,003 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SP260, FLJ10243; previously LASS2 |
| Gene groups (HGNC) | CERS class homeoboxes; Ceramide synthases |
| Reactome | 3 pathways, smallest: Sphingolipid de novo biosynthesis; Sphingolipid metabolism; Metabolism of lipids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G23](https://www.uniprot.org/uniprotkb/Q96G23) (Ceramide synthase 2):

> Ceramide synthase that catalyzes the transfer of the acyl chain from acyl-CoA to a sphingoid base, with high selectivity toward very-long-chain fatty acyl-CoA (chain length C22-C27). N-acylates sphinganine and sphingosine bases to form dihydroceramides and ceramides in de novo synthesis and salvage pathways, respectively (By similarity). Plays a non-redundant role in the synthesis of ceramides with very-long-chain fatty acids in kidney, liver and brain. Regulates the abundance of …

**Summary**, from NCBI Gene [29956](https://www.ncbi.nlm.nih.gov/gene/29956):

> This gene encodes a protein that has sequence similarity to yeast longevity assurance gene 1. Mutation or overexpression of the related gene in yeast has been shown to alter yeast lifespan. The human protein may play a role in the regulation of cell growth. Alternatively spliced transcript variants encoding the same protein have been described. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14076](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14076) · Entrez [29956](https://www.ncbi.nlm.nih.gov/gene/29956) · UniProt [Q96G23](https://www.uniprot.org/uniprotkb/Q96G23) · Ensembl [ENSG00000143418](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143418)

## Data

Gene col 6739: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6739); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6739, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6739]; `tensor/DDL_lfc|DDL_z.npy` [6739]; `embed/gene_vectors.npy` [6739]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6739 or target_col == 6739). Every well: [[CERS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CERS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
